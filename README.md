<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/banner-dark.png">
    <img src=".github/assets/banner.png" alt="TrueNAS apps: one paste, one app" width="100%">
  </picture>
</p>

<p align="center">
  <a href="https://github.com/junkerderprovinz/truenas-apps/actions/workflows/generate.yml"><img src="https://img.shields.io/github/actions/workflow/status/junkerderprovinz/truenas-apps/generate.yml?branch=main&label=Generate&style=for-the-badge&logo=githubactions&logoColor=white" alt="Generate" height="36"></a>&nbsp;
  <a href="#apps"><img src="https://img.shields.io/badge/Apps-39-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Apps" height="36"></a>&nbsp;
  <a href="https://github.com/junkerderprovinz/truenas-apps/commits/main"><img src="https://img.shields.io/github/last-commit/junkerderprovinz/truenas-apps?branch=main&style=for-the-badge&logo=git&logoColor=white&label=Updated" alt="Last commit" height="36"></a>&nbsp;
  <a href="https://www.truenas.com/truenas-community-edition/"><img src="https://img.shields.io/badge/TrueNAS-Install%20via%20YAML-0095d5?style=for-the-badge&logo=truenas&logoColor=white" alt="TrueNAS Install via YAML" height="36"></a>&nbsp;
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge&logo=opensourceinitiative&logoColor=white" alt="License" height="36"></a>
</p>

<p align="center">
Ready-made app files for <a href="https://www.truenas.com/truenas-community-edition/">TrueNAS</a> with junkerderprovinz's containers, grouped like the profile: <b>Apps</b> (my own software), <b>Images</b> (my own image builds of third-party apps) and <b>Wrappers</b> (thin templates over an upstream image). TrueNAS installs apps from its own catalog only, so each app here is one file to paste under <b>Install via YAML</b>.
</p>


<!-- apps:start -->
## Apps

*My own software, built and published by junkerderprovinz. Full docs live in each app's own repository.*

<a id="arrowloop"></a>
<img src=".github/readme-icons/arrowloop.png" width="84" align="left" alt="ArrowLoop">

**[ArrowLoop](https://github.com/junkerderprovinz/arrowloop#readme)** · [TrueNAS YAML](apps/arrowloop.yaml)<br>
Two-way file sync that shows you the plan before it touches a file, sends deletions to a trash and stops a run that would delete too much.

<br clear="all">

<a id="cannoncommander"></a>
<img src=".github/readme-icons/cannoncommander.png" width="84" align="left" alt="CannonCommander">

**[CannonCommander](https://github.com/junkerderprovinz/cannoncommander#readme)** · [TrueNAS YAML](apps/cannoncommander.yaml)<br>
The most beautiful file manager you will ever run, and the only one you need: two panels, F5 to copy, jobs in the background and a trash for second thoughts.

<br clear="all">

<a id="castleparcel"></a>
<img src=".github/readme-icons/castleparcel.png" width="84" align="left" alt="CastleParcel">

**[CastleParcel](https://github.com/junkerderprovinz/castleparcel#readme)** · [TrueNAS YAML](apps/castleparcel.yaml)<br>
The big-file transfer site you know, on your own server and sealed: encrypted in your browser, with an optional owner sign-in, self-expiring share links, file requests and notes.

<br clear="all">

<a id="knightloader"></a>
<img src=".github/readme-icons/knightloader.png" width="84" align="left" alt="KnightLoader">

**[KnightLoader](https://github.com/junkerderprovinz/knightloader#readme)** · [TrueNAS YAML](apps/knightloader.yaml)<br>
Self-hosted download manager for hosters, debrid, torrents, Usenet and video, with an Android app and a browser extension.

<br clear="all">

<a id="trickwork"></a>
<img src=".github/readme-icons/trickwork.png" width="84" align="left" alt="TrickWork">

**[TrickWork](https://github.com/junkerderprovinz/trickwork#readme)** · [TrueNAS YAML](apps/trickwork.yaml)<br>
Turns images into proportional-font-aware ASCII art - a rebuild of ASCII Gen 2, picking characters by real ink coverage, not brightness.

<br clear="all">


## Images

*My own custom image builds of third-party apps. Full docs in each app's own repository.*

<a id="cadcraft"></a>
<img src=".github/readme-icons/cadcraft.png" width="84" align="left" alt="CADCraft">

**[CADCraft](https://github.com/junkerderprovinz/artcraft-apps#cadcraft)** · [TrueNAS YAML](apps/cadcraft.yaml)<br>
CADCraft on a Selkies web desktop: 2D drafting with layers, blocks and dimensions, and DXF and DWG files, all in the browser.

<br clear="all">

<a id="deckcraft"></a>
<img src=".github/readme-icons/deckcraft.png" width="84" align="left" alt="DeckCraft">

**[DeckCraft](https://github.com/junkerderprovinz/artcraft-apps#deckcraft)** · [TrueNAS YAML](apps/deckcraft.yaml)<br>
DeckCraft on a Selkies web desktop, for building and presenting PowerPoint decks from any browser.

<br clear="all">

<a id="designcraft"></a>
<img src=".github/readme-icons/designcraft.png" width="84" align="left" alt="DesignCraft">

**[DesignCraft](https://github.com/junkerderprovinz/artcraft-apps#designcraft)** · [TrueNAS YAML](apps/designcraft.yaml)<br>
DesignCraft on a Selkies web desktop: lay out magazines and flyers in the browser and export print-ready PDFs.

<br clear="all">

<a id="effectcraft"></a>
<img src=".github/readme-icons/effectcraft.png" width="84" align="left" alt="EffectCraft">

**[EffectCraft](https://github.com/junkerderprovinz/artcraft-apps#effectcraft)** · [TrueNAS YAML](apps/effectcraft.yaml)<br>
EffectCraft on a Selkies web desktop, for motion graphics with compositions, keyframes and effects in the browser.

<br clear="all">

<a id="euro-office"></a>
<img src=".github/readme-icons/euro-office.png" width="84" align="left" alt="Euro Office">

**[Euro Office](https://github.com/junkerderprovinz/euro-office#readme)** · [TrueNAS YAML](apps/euro-office.yaml)<br>
Sovereign, OnlyOffice-compatible document server for browser editing of Office and OpenDocument files, wired into OpenCloud over WOPI.

<br clear="all">

<a id="excalidraw"></a>
<img src=".github/readme-icons/excalidraw.png" width="84" align="left" alt="Excalidraw">

**[Excalidraw](https://github.com/junkerderprovinz/excalidraw#readme)** · [TrueNAS YAML](apps/excalidraw.yaml)<br>
The hand-drawn whiteboard, built so it keeps to itself: shared links, live collaboration, the session scene and even the fonts all come from your own server.

<br clear="all">

<a id="figcraft"></a>
<img src=".github/readme-icons/figcraft.png" width="84" align="left" alt="FigCraft">

**[FigCraft](https://github.com/junkerderprovinz/artcraft-apps#figcraft)** · [TrueNAS YAML](apps/figcraft.yaml)<br>
FigCraft on a Selkies web desktop: design interfaces with frames and components and click through prototypes in the browser.

<br clear="all">

<a id="filebot"></a>
<img src=".github/readme-icons/filebot.png" width="84" align="left" alt="FileBot">

**[FileBot](https://github.com/junkerderprovinz/filebot#readme)** · [TrueNAS YAML](apps/filebot.yaml)<br>
The FileBot media renamer in your browser on a fast Selkies web desktop, dark from the first start. Bring your own FileBot license.

<br clear="all">

<a id="filmcraft"></a>
<img src=".github/readme-icons/filmcraft.png" width="84" align="left" alt="FilmCraft">

**[FilmCraft](https://github.com/junkerderprovinz/artcraft-apps#filmcraft)** · [TrueNAS YAML](apps/filmcraft.yaml)<br>
FilmCraft on a Selkies web desktop, a nonlinear video editor that cuts the footage on your array from any browser.

<br clear="all">

<a id="garage"></a>
<img src=".github/readme-icons/garage.png" width="84" align="left" alt="Garage">

**[Garage](https://github.com/junkerderprovinz/garage#readme)** · [TrueNAS YAML](apps/garage.yaml)<br>
Garage's S3-compatible object store and its web admin panel in one container, with the single-node layout and S3 keys created automatically.

<br clear="all">

<a id="gridcraft"></a>
<img src=".github/readme-icons/gridcraft.png" width="84" align="left" alt="GridCraft">

**[GridCraft](https://github.com/junkerderprovinz/artcraft-apps#gridcraft)** · [TrueNAS YAML](apps/gridcraft.yaml)<br>
GridCraft on a Selkies web desktop: a spreadsheet with formulas and charts that opens and saves Excel workbooks.

<br clear="all">

<a id="handbrake"></a>
<img src=".github/readme-icons/handbrake.png" width="84" align="left" alt="HandBrake">

**[HandBrake](https://github.com/junkerderprovinz/handbrake#readme)** · [TrueNAS YAML](apps/handbrake.yaml)<br>
HandBrake's full GUI on a fast Selkies web desktop, GPU-accelerated on NVIDIA, Intel and AMD, with a watch folder that converts on its own.

<br clear="all">

<a id="jdownloader"></a>
<img src=".github/readme-icons/jdownloader.png" width="84" align="left" alt="JDownloader">

**[JDownloader](https://github.com/junkerderprovinz/jdownloader#readme)** · [TrueNAS YAML](apps/jdownloader.yaml)<br>
JDownloader 2 with a complete, sleek dark UI out of the box, on a fast Selkies web desktop in your browser. No VNC client, no install.

<br clear="all">

<a id="krusader"></a>
<img src=".github/readme-icons/krusader.png" width="84" align="left" alt="Krusader">

**[Krusader](https://github.com/junkerderprovinz/krusader#readme)** · [TrueNAS YAML](apps/krusader.yaml)<br>
Twin-pane KDE file manager with a native dark theme on a fast Selkies web desktop, with Kate, krename and RAR built in.

<br clear="all">

<a id="lightcraft"></a>
<img src=".github/readme-icons/lightcraft.png" width="84" align="left" alt="LightCraft">

**[LightCraft](https://github.com/junkerderprovinz/artcraft-apps#lightcraft)** · [TrueNAS YAML](apps/lightcraft.yaml)<br>
LightCraft on a Selkies web desktop, a photo library and raw developer that sits right next to the photos on your array.

<br clear="all">

<a id="opencloud"></a>
<img src=".github/readme-icons/opencloud.png" width="84" align="left" alt="OpenCloud">

**[OpenCloud](https://github.com/junkerderprovinz/opencloud#readme)** · [TrueNAS YAML](apps/opencloud.yaml)<br>
One-click OpenCloud file sync &amp; share: auto-runs init, heals appdata permissions and honours PUID/PGID.

<br clear="all">

<a id="pdfcraft"></a>
<img src=".github/readme-icons/pdfcraft.png" width="84" align="left" alt="PdfCraft">

**[PdfCraft](https://github.com/junkerderprovinz/artcraft-apps#pdfcraft)** · [TrueNAS YAML](apps/pdfcraft.yaml)<br>
PdfCraft on a Selkies web desktop, for reading, editing, signing and running OCR on PDFs in the browser.

<br clear="all">

<a id="photocraft"></a>
<img src=".github/readme-icons/photocraft.png" width="84" align="left" alt="PhotoCraft">

**[PhotoCraft](https://github.com/junkerderprovinz/artcraft-apps#photocraft)** · [TrueNAS YAML](apps/photocraft.yaml)<br>
PhotoCraft on a Selkies web desktop: a layered photo editor in the browser that opens PSD, Krita and Affinity files.

<br clear="all">

<a id="prusaslicer"></a>
<img src=".github/readme-icons/prusaslicer.png" width="84" align="left" alt="PrusaSlicer">

**[PrusaSlicer](https://github.com/junkerderprovinz/prusaslicer#readme)** · [TrueNAS YAML](apps/prusaslicer.yaml)<br>
The PrusaSlicer 3D-printing slicer in your browser on a fast Selkies web desktop: slice and export G-code, no VNC client (amd64 + arm64).

<br clear="all">

<a id="rustdesk"></a>
<img src=".github/readme-icons/rustdesk.png" width="84" align="left" alt="RustDesk">

**[RustDesk](https://github.com/junkerderprovinz/rustdesk#readme)** · [TrueNAS YAML](apps/rustdesk.yaml)<br>
Your own RustDesk server with a web console, accounts, an address book on every client and devices that can change their ID.

<br clear="all">

<a id="seafile"></a>
<img src=".github/readme-icons/seafile.png" width="84" align="left" alt="Seafile">

**[Seafile](https://github.com/junkerderprovinz/seafile#readme)** · [TrueNAS YAML](apps/seafile.yaml)<br>
The official Seafile server from one template, with its secrets generated on first start and MariaDB, Redis and the notification server built in on request.

<br clear="all">

<a id="securo"></a>
<img src=".github/readme-icons/securo.png" width="84" align="left" alt="Securo">

**[Securo](https://github.com/junkerderprovinz/securo#readme)** · [TrueNAS YAML](apps/securo.yaml)<br>
The Securo finance manager with its worker and scheduler in one container, on your own PostgreSQL and Redis or on built-in ones.

<br clear="all">

<a id="soundcraft"></a>
<img src=".github/readme-icons/soundcraft.png" width="84" align="left" alt="SoundCraft">

**[SoundCraft](https://github.com/junkerderprovinz/artcraft-apps#soundcraft)** · [TrueNAS YAML](apps/soundcraft.yaml)<br>
SoundCraft on a Selkies web desktop, a multitrack audio workstation whose sound plays in the browser.

<br clear="all">

<a id="stellarium"></a>
<img src=".github/readme-icons/stellarium.png" width="84" align="left" alt="Stellarium">

**[Stellarium](https://github.com/junkerderprovinz/stellarium#readme)** · [TrueNAS YAML](apps/stellarium.yaml)<br>
The Stellarium planetarium in your browser on a fast Selkies web desktop: pan the sky, zoom a nebula, scrub through time, no VNC client.

<br clear="all">

<a id="vectorcraft"></a>
<img src=".github/readme-icons/vectorcraft.png" width="84" align="left" alt="VectorCraft">

**[VectorCraft](https://github.com/junkerderprovinz/artcraft-apps#vectorcraft)** · [TrueNAS YAML](apps/vectorcraft.yaml)<br>
VectorCraft on a Selkies web desktop: vector illustration with paths and type, SVG and PDF in and out.

<br clear="all">

<a id="wordcraft"></a>
<img src=".github/readme-icons/wordcraft.png" width="84" align="left" alt="WordCraft">

**[WordCraft](https://github.com/junkerderprovinz/artcraft-apps#wordcraft)** · [TrueNAS YAML](apps/wordcraft.yaml)<br>
WordCraft on a Selkies web desktop, a word processor in the browser that opens and saves Word documents.

<br clear="all">


## Wrappers

*Thin templates over a third-party upstream image (no custom build). Full docs in each app's folder below.*

<a id="couchdb"></a>
<img src=".github/readme-icons/couchdb.png" width="84" align="left" alt="CouchDB">

**[CouchDB](https://github.com/junkerderprovinz/unraid-apps/blob/main/couchdb/README.md)** · [TrueNAS YAML](apps/couchdb.yaml)<br>
The HTTP/JSON document database behind Obsidian LiveSync, on the official 3.x image with data, config and CORS mapped so they survive a recreate or update.

<br clear="all">

<a id="github-runner"></a>
<img src=".github/readme-icons/github-runner.png" width="84" align="left" alt="GitHub-Runner">

**[GitHub-Runner](https://github.com/junkerderprovinz/github-runner#readme)** · [TrueNAS YAML](apps/github-runner.yaml)<br>
Self-hosted GitHub Actions runners for several repositories of a personal account in one container, removed from GitHub again when it stops.

<br clear="all">

<a id="pocket-id"></a>
<img src=".github/readme-icons/pocket-id.png" width="84" align="left" alt="Pocket ID">

**[Pocket ID](https://github.com/junkerderprovinz/unraid-apps/blob/main/pocket-id/README.md)** · [TrueNAS YAML](apps/pocket-id.yaml)<br>
Passkey login for every app on your server that speaks OpenID Connect, with users, groups and an audit log, on SQLite or PostgreSQL.

<br clear="all">

<a id="rustfs"></a>
<img src=".github/readme-icons/rustfs.png" width="84" align="left" alt="RustFS">

**[RustFS](https://github.com/junkerderprovinz/unraid-apps/blob/main/rustfs/README.md)** · [TrueNAS YAML](apps/rustfs.yaml)<br>
An S3 object store in Rust, with the two fixes it needs to run on Unraid at all. Pre-release: every version so far is a release candidate.

<br clear="all">

<a id="seaweedfs"></a>
<img src=".github/readme-icons/seaweedfs.png" width="84" align="left" alt="SeaweedFS">

**[SeaweedFS](https://github.com/junkerderprovinz/unraid-apps/blob/main/seaweedfs/README.md)** · [TrueNAS YAML](apps/seaweedfs.yaml)<br>
Fast, S3-API-compatible object store on the official image, the actively-maintained alternative now that MinIO's open edition is done.

<br clear="all">

<a id="silo"></a>
<img src=".github/readme-icons/silo.png" width="84" align="left" alt="Silo">

**[Silo](https://github.com/junkerderprovinz/unraid-apps/blob/main/silo/README.md)** · [TrueNAS YAML](apps/silo.yaml)<br>
MinIO, still maintained: PGSTY's fork of the open-source server, with the full web console. It reads an existing MinIO data folder as it is.

<br clear="all">

<a id="standardnotes-webui"></a>
<img src=".github/readme-icons/standardnotes-webui.png" width="84" align="left" alt="Standard Notes Web UI">

**[Standard Notes Web UI](https://github.com/junkerderprovinz/unraid-apps/blob/main/standardnotes-webui/README.md)** · [TrueNAS YAML](apps/standardnotes-webui.yaml)<br>
The official Standard Notes web client, self-hosted next to your own sync server for end-to-end encrypted notes in the browser.

<br clear="all">

<a id="versitygw"></a>
<img src=".github/readme-icons/versitygw.png" width="84" align="left" alt="VersityGW">

**[VersityGW](https://github.com/junkerderprovinz/unraid-apps/blob/main/versitygw/README.md)** · [TrueNAS YAML](apps/versitygw.yaml)<br>
An S3 API in front of a share you already have: top-level folders become buckets, and every file stays readable over SMB and NFS at the same time.

<br clear="all">
<!-- apps:end -->


## Install

1. Open the app's file with the **TrueNAS YAML** button on its card and copy it.
2. In TrueNAS, open **Apps**, then **Discover Apps**, and choose **Install via YAML** in the menu beside **Custom App**.
3. Give the app the name the file's first lines suggest and paste the file. Replace `tank` with the name of your pool, fill in every value marked `required` and save.

TrueNAS pulls the image and starts the app. The file lists the ports its web page and services listen on.

A few apps share a port: CastleParcel and Securo use 3000, Excalidraw and GitHub Runner 8080, RustFS and Silo 9000 and 9001. To run both of a pair, change the number left of the colon for one of them.

Questions and bugs go to the issue tracker of the app's own repository, linked from **Repository & ReadMe** on its card.


## How these differ from the Unraid templates

The apps are built from the Unraid templates in [unraid-apps](https://github.com/junkerderprovinz/unraid-apps), through the same compose files the app repositories offer for other Docker hosts, with the changes TrueNAS needs:

- Appdata goes to `/mnt/tank/apps/<app>`. File managers, slicers and the web desktops see the whole pool, and downloads land in `/mnt/tank/downloads`.
- `PUID` and `PGID` are `568`, the user and group TrueNAS runs its own apps as.
- Each Selkies web desktop gets its own pair of ports, 32000 and up, so several of them fit on one TrueNAS.
- CannonCommander sees `/mnt` where it looks for Unraid's user shares, `/mnt/user`, and keeps the capabilities and `/dev/fuse` it needs for rclone's mounts. It runs without Docker's AppArmor profile, which would refuse those mounts. The Unraid state and flash folders are left out.
- A password or key that the Unraid template asks for at install time stays empty and is marked `required`.
- JuiceFS, ParleyPort and the apps that need a database next to them (Matrix, n8n, Claper) are not here yet.

To change an app, edit its template in unraid-apps, not the files in `apps/`, `.github/readme-icons/` or the app list in this README. A workflow here rebuilds them every night. To build them by hand:

```sh
python3 tools/generate.py ../unraid-apps
```

`apps.json` lists the apps. Per app it can set where a folder goes on the pool (`paths`) and where it shows up in the container (`targets`), give ports another host port (`ports`), leave a path out (`drop_paths`), set Docker's `security_opt` (`security_opt`), set variables (`env`), or read a template file with another name (`xml`).


## How AI is used here

One knight builds this, and AI is one of the tools I work with, the same way I work with an editor or a compiler. It helps me write code and documentation and it checks my work, and that saves me a good many evenings. It does not make the decisions, though. I read and understand everything before it ships, and if something here breaks, that is on me and not on the tool.

You do not have to take my word for it. The code is open and every release note is written by hand. The issue tracker shows how problems actually get handled, including the ones I got wrong the first time. If you find something that is not right, open an issue and I will look at it.

## Support

A one-knight job: I build them, keep them running, work through the issues and add what people ask for, until nothing is missing. They are free, with no accounts, no telemetry, no ads and no paid tier. No asterisk anywhere. Nothing readable ever leaves your own walls. Forged on evenings and weekends, with heart and stubbornness.

If one of these has earned a place on your server or computer, toss a coin to your knight: it helps cover the costs and keeps the project alive. It also makes this knight's heart beat a little faster. Three ways below, whichever suits you.

<p align="center">
  <a href="https://buymeacoffee.com/junkerderprovinz"><img src="https://raw.githubusercontent.com/junkerderprovinz/junkerderprovinz/main/donate/buttons/give.svg#svgView(viewBox(-23.082,-20.153,888.064,285.606))" alt="Buy me a coffee" width="168.773" height="54.278"></a>
  <a href="https://www.paypal.com/donate/?hosted_button_id=76FVV52TKXTUS"><img src="https://raw.githubusercontent.com/junkerderprovinz/junkerderprovinz/main/donate/buttons/give.svg#svgView(viewBox(890.818,-20.153,888.064,285.606))" alt="PayPal" width="168.773" height="54.278"></a>
  <a href="https://junkerderprovinz.github.io/junkerderprovinz/"><img src="https://raw.githubusercontent.com/junkerderprovinz/junkerderprovinz/main/donate/buttons/give.svg#svgView(viewBox(1804.718,-20.153,888.064,285.606))" alt="Donate with crypto" width="168.773" height="54.278"></a>
</p>
