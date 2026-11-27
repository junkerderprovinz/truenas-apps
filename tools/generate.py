"""Builds the TrueNAS compose files in apps/ from the templates in unraid-apps.

unraid-apps stays the only place an app's container settings are edited. This
script takes the compose file that unraid-apps generates for each app listed in
apps.json and moves its folders onto a TrueNAS pool. TrueNAS takes them as they
are under Install via YAML.

    python tools/generate.py ../unraid-apps          write apps/
    python tools/generate.py ../unraid-apps --check  fail if apps/ is stale
"""

import argparse
import importlib.util
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
FEED_URL = "https://github.com/junkerderprovinz/unraid-apps"
POOL = "/mnt/tank"

# TrueNAS runs its own apps as the apps user and group.
SYSTEM_VALUES = {"PUID": "568", "PGID": "568"}

HEADER = """\
# {name} for TrueNAS, from junkerderprovinz/truenas-apps.
# Paste it under Apps, Discover Apps, then Install via YAML in the menu beside
# Custom App, and name the app {app}.
#
# Replace tank with the name of your pool and fill in every value marked
# "required". Docker creates the folders on the first start. Create datasets
# for them first if you want snapshots of each one.
#
# Built from the Unraid template in junkerderprovinz/unraid-apps. Change the
# template there, not this file.

"""

BADGE = '<a href="apps/{app}.yaml"><img src="https://img.shields.io/badge/TrueNAS%20YAML-0095d5?style=for-the-badge&logo=truenas&logoColor=white" align="right" alt="TrueNAS YAML"></a>'


class Dumper(yaml.SafeDumper):
    """Indents list items under their key, as the compose files in the app repositories do."""

    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)


# Docker's own docs quote port mappings, since YAML 1.1 reads 22:22 as a number.
Dumper.add_representer(str, lambda dumper, value: dumper.represent_scalar(
    "tag:yaml.org,2002:str", value, style='"' if re.fullmatch(r"[\d.:]+(/\w+)?", value) else None))


def load_gen_compose(feed):
    spec = importlib.util.spec_from_file_location("gen_compose", feed / ".github" / "gen-compose.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def host_path(volume, app, overrides):
    host, target, *mode = volume.split(":")
    if host.startswith("./appdata"):
        host = f"{POOL}/apps/{app}" + host[len("./appdata"):]
    elif host.startswith("./"):
        host = overrides.get("paths", {}).get(target, f"{POOL}/apps/{app}/{host[2:]}")
    return ":".join([host, overrides.get("targets", {}).get(target, target), *mode])


def host_port(mapping, ports):
    host, target = mapping.split(":", 1)
    return f"{ports.get(target.split('/')[0], host)}:{target}"


def build(feed, gen_compose, app, overrides):
    xml = overrides.get("xml", f"{app}.xml")
    name = (ET.parse(feed / app / xml).getroot().findtext("Name") or app).strip()
    text, unknown = gen_compose.compose(app, xml)
    required = re.findall(r"^\s+(\w+):.*# required$", text, re.M)
    doc = yaml.safe_load(text)
    service = doc["services"][app]
    caps = [arg.split("=", 1)[1] for arg in unknown if arg.startswith("--cap-add=")]
    if caps:
        service["cap_add"] = caps
    if "security_opt" in overrides:
        service["security_opt"] = overrides["security_opt"]
    # The Selkies desktops all listen on 3000 and 3001, so each gets its own
    # pair and several of them fit on one TrueNAS.
    if "ports" in overrides:
        service["ports"] = [host_port(p, overrides["ports"]) for p in service["ports"]]

    drop = overrides.get("drop_paths", [])
    service["volumes"] = [host_path(v, app, overrides) for v in service.get("volumes", []) if v.split(":")[1] not in drop]
    if not service["volumes"]:
        del service["volumes"]
    env = service.get("environment") or {}
    for key, value in SYSTEM_VALUES.items():
        if key in env:
            env[key] = value
    env.update(overrides.get("env", {}))

    body = yaml.dump(doc, Dumper=Dumper, sort_keys=False, allow_unicode=True, width=1000)
    for key in required:
        if not env.get(key) or key in gen_compose.PLACEHOLDERS.get(app, ()):
            body = re.sub(rf"^(\s+{key}: .*)$", r"\1  # required", body, count=1, flags=re.M)
    return HEADER.format(name=name, app=app) + body


def readme_cards(feed, apps):
    """Return the README's app section, built from the cards in the feed README.

    Each app keeps the card, description and group (Apps, Images, Wrappers) it
    has in unraid-apps, so the two READMEs cannot drift apart. The compose
    button gives way to the TrueNAS one.
    """
    source = (feed / "README.md").read_text(encoding="utf-8")
    groups = {}
    for app in apps:
        start = source.index(f'<img src=".github/readme-icons/{app}.png"')
        end = source.index('<br clear="all">', start) + len('<br clear="all">')
        heading = list(re.finditer(r"^## (\w+)\n\n(\*.+\*)$", source[:start], re.M))[-1]
        card = re.sub(r'href="([\w-]+/README\.md)"', rf'href="{FEED_URL}/blob/main/\1"', source[start:end])
        lines = [line for line in card.split("\n") if 'alt="Docker compose file"' not in line]
        repo = next(i for i, line in enumerate(lines) if 'alt="Repository &amp; ReadMe"' in line)
        lines.insert(repo + 1, BADGE.format(app=app))
        groups.setdefault(heading.group(1), (heading.group(2), []))[1].append(f'<a id="{app}"></a>\n' + "\n".join(lines))
    order = [h for h in ("Apps", "Images", "Wrappers") if h in groups]
    parts = [f"## {h}\n\n{groups[h][0]}\n\n" + "\n\n".join(groups[h][1]) for h in order]
    return "\n\n\n".join(parts)


def readme(current, feed, apps):
    body = readme_cards(feed, apps)
    current = re.sub(
        r"(<!-- apps:start -->\n).*?(<!-- apps:end -->)",
        lambda m: m.group(1) + body + "\n" + m.group(2),
        current,
        flags=re.S,
    )
    return re.sub(r"badge/Apps-\d+-", f"badge/Apps-{len(apps)}-", current)


def main():
    parser = argparse.ArgumentParser(description="Write the TrueNAS compose files from the Unraid templates.")
    parser.add_argument("feed", type=Path, help="checkout of junkerderprovinz/unraid-apps")
    parser.add_argument("--check", action="store_true", help="report stale files instead of writing")
    args = parser.parse_args()

    gen_compose = load_gen_compose(args.feed)
    apps = json.loads((ROOT / "apps.json").read_text(encoding="utf-8"))

    wanted = {}
    for app, overrides in apps.items():
        wanted[f"apps/{app}.yaml"] = build(args.feed, gen_compose, app, overrides).encode("utf-8")
        wanted[f".github/readme-icons/{app}.png"] = (
            args.feed / ".github" / "readme-icons" / f"{app}.png"
        ).read_bytes()
    wanted["README.md"] = readme(
        (ROOT / "README.md").read_text(encoding="utf-8"), args.feed, apps
    ).encode("utf-8")

    stale = []
    for name, content in wanted.items():
        target = ROOT / name
        if not target.exists() or target.read_bytes() != content:
            stale.append(name)
            if not args.check:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(content)
    present = [p for d in ("apps", ".github/readme-icons") for p in (ROOT / d).glob("*") if p.is_file()]
    removed = [p for p in sorted(p.relative_to(ROOT).as_posix() for p in present) if p not in wanted]
    stale += removed
    if not args.check:
        for leftover in removed:
            (ROOT / leftover).unlink()

    if args.check and stale:
        print("out of date: " + ", ".join(stale), file=sys.stderr)
        print("run: python tools/generate.py <unraid-apps checkout>", file=sys.stderr)
        return 1
    for name in stale:
        print(f"{'removed' if name in removed else 'updated'} {name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
