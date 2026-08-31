# Inno Agent — telepítési parancsok

## Előfeltételek

A telepítőnek **Git** és **Node.js 20.6+** kell. Ha nincs meg, itt vannak a
telepítési parancsok.

---

## 1. Git telepítése

A telepítő ellenőrzi a gitet, és hiány esetén megáll — ezért előbb telepítsd.

**Ellenőrzés:** `git --version`

**Linux (Debian/Ubuntu):**
```bash
sudo apt update && sudo apt install -y git
```

**Linux (Fedora/RHEL):**
```bash
sudo dnf install -y git
```

**Linux (Arch):**
```bash
sudo pacman -S git
```

**macOS:** a Git az Apple parancssori eszközeivel érkezik:
```bash
xcode-select --install
```
(vagy Homebrew-val: `brew install git`)

**Windows:** `winget install Git.Git`, vagy töltsd le innen:
https://git-scm.com/downloads (a telepítőjében mindent hagyhatsz alapértelmezetten).

---

## 2. Node.js 20.6+ telepítése (ajánlott: 22 LTS)

**Ellenőrzés:** `node --version` → legalább `v20.6.0` kell.

### nvm — Linux/macOS, admin-jog nélkül (ajánlott)

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
# zárd be és nyisd újra a terminált, vagy:
export NVM_DIR="$HOME/.nvm"
. "$NVM_DIR/nvm.sh"
nvm install 22
nvm alias default 22
node --version   # v22.x.x
```

> A telepítő magától is megpróbálja az `~/.nvm/nvm.sh`-t használni, ha a
> rendszerszintű node hiányzik.

### NodeSource — Linux (Debian/Ubuntu), rendszerszinten

```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt install -y nodejs
```

### macOS

```bash
brew install node@22
```
(vagy a hivatalos telepítő: https://nodejs.org — a „LTS" verzió.)

### Windows

```powershell
winget install OpenJS.NodeJS.LTS
```
(vagy a hivatalos `.msi`: https://nodejs.org — a „LTS" verzió. Telepítés után
nyiss új PowerShellt, hogy a PATH frissüljön.)

### Ha a node fent van, de a telepítő nem találja

Ha a `node --version` jó, de a telepítő mégis hibát dob (pl. az nvm nincs
betöltve), átugorhatod az ellenőrzést:

```bash
curl -fsSL https://cdn.jsdelivr.net/gh/karsarobert/inno-agent-hub/install.sh | INNO_SKIP_NODE_CHECK=1 sh
```

---

## 3. Linux / macOS — egysoros telepítés (CDN)

```bash
curl -fsSL https://cdn.jsdelivr.net/gh/karsarobert/inno-agent-hub/install.sh | sh
```

A telepítő:
- klónozza az alkalmazást (`karsarobert/inno-agent`) a `~/.local/opt/inno-agent`-be,
- futtatja az `npm ci`-t és a buildet,
- tiszta configot ír (placeholder provider — a valódit a Beállításokban állítod be),
- alapból bekapcsolja a GitHub-tartalomhubot (`karsarobert/inno-agent-hub`),
  így a készségek és a preset-kártyák rögtön elérhetők,
- létrehoz menü-ikont, elindítja a szervert és megnyitja a Web UI-t
  (http://localhost:3000).

> **Újrafuttatás meglévő API-beállítással:** ha a `runtime/config/config.json`
> már tartalmaz valós provider/API-kulcsot, a telepítő megkérdezi, hogy
> megtartsa-e vagy törölje. Nem interaktív futtatásnál (CI, csővezeték) az
> alapértelmezés a **megtartás** — `INNO_CONFIG_MODE=reset` a törléshez,
> `INNO_CONFIG_MODE=keep` a kérdés kihagyásához.

## 4. Windows — egysoros telepítés (GitHub)

```powershell
irm https://cdn.jsdelivr.net/gh/karsarobert/inno-agent-hub/install.ps1 | iex
```

---

## 5. Tartalomhub beállítása

A telepítő alapértelmezésben a **GitHub-tartalomhubot** használja
(`karsarobert/inno-agent-hub`, `main` ág) — nem kell semmit megadnod.

**Offline telepítés (nincs hub, nincs készség/kártya):**
```bash
curl -fsSL https://cdn.jsdelivr.net/gh/karsarobert/inno-agent-hub/install.sh | INNO_HUB_TYPE=none sh
```

**Saját (saját üzemeltetésű) hub:**
```bash
curl -fsSL https://cdn.jsdelivr.net/gh/karsarobert/inno-agent-hub/install.sh | INNO_HUB_URL="http://sajat-hub:8787" sh
```
(Az `INNO_HUB_URL` megadása automatikusan `bundle` típusra állít.)

---

## 6. Telepítés opciókkal (provider előre megadva)

```bash
curl -fsSL https://cdn.jsdelivr.net/gh/karsarobert/inno-agent-hub/install.sh \
  | INNO_HOME="$HOME/inno-agent" \
    INNO_PORT=3000 \
    INNO_PROVIDER_BASE_URL="http://10.0.64.2:8000/v1" \
    INNO_PROVIDER_API_KEY="kulcs" \
    INNO_PROVIDER_MODEL="Qwen3.8-27B-nvfp4" sh
```

Windows (PowerShellben előre beállítva):
```powershell
$env:INNO_HOME = "$env:USERPROFILE\inno-agent"
$env:INNO_PORT = "3000"
$env:INNO_PROVIDER_BASE_URL = "http://10.0.64.2:8000/v1"
$env:INNO_PROVIDER_API_KEY = "kulcs"
$env:INNO_PROVIDER_MODEL = "Qwen3.8-27B-nvfp4"
irm https://cdn.jsdelivr.net/gh/karsarobert/inno-agent-hub/install.ps1 | iex
```

---

## 7. Telepítő opciók (env változók)

| Változó | Alapértelmezés | Mit csinál |
|---|---|---|
| `INNO_HOME` | `~/.local/opt/inno-agent` | Telepítési könyvtár |
| `INNO_REPO_URL` | `https://github.com/karsarobert/inno-agent.git` | Forrás repo (az alkalmazás) |
| `INNO_BRANCH` | `main` | Branch |
| `INNO_PORT` | `3000` | Web UI portja |
| `INNO_NODE_VER` | `22` | nvm-mel telepített Node verzió |
| `INNO_SKIP_NODE_CHECK` | üres | `1` = Node-ellenőrzés átugrása |
| `INNO_HUB_TYPE` | `github` | `none` / `bundle` / `github` |
| `INNO_HUB_URL` | üres | Saját hub baseUrl — megadása `bundle` típusra állít |
| `INNO_PROVIDER_BASE_URL` | üres (placeholder) | Alapértelmezett provider baseUrl |
| `INNO_PROVIDER_API_KEY` | üres | Provider API kulcs (opcionális) |
| `INNO_PROVIDER_MODEL` | üres (placeholder) | Alapértelmezett modell |
| `INNO_CONFIG_MODE` | üres (kérdez) | Meglévő config kezelése: `keep` / `reset` |
| `INNO_SKIP_BUILD` | `0` | `1` = build kihagyása (gyors teszt) |
| `INNO_SKIP_START` | `0` | `1` = indítás kihagyása |

---

## 8. Indítás újraindítás után

A menüből (Beállítások → „Alkalmazás leállítása" is innen érhető el), vagy parancsban:

```bash
~/.local/opt/inno-agent/inno-agent.sh
```

## 9. Frissítés (meglévő telepítés)

```bash
cd ~/.local/opt/inno-agent && git pull && npm ci && npm run build
```

(a config, beszélgetések és munkaterületek megmaradnak)

## 10. Leállítás

- Az appban: Beállítások → „Alkalmazás leállítása" gomb
- Parancsban: `pkill -f "dist/server.js.*--port 3000"` (vagy a megfelelő port)

---

## GitHub források

| Mi | Cím |
|---|---|
| Telepítő (Linux/macOS) | https://cdn.jsdelivr.net/gh/karsarobert/inno-agent-hub/install.sh |
| Telepítő (Windows) | https://cdn.jsdelivr.net/gh/karsarobert/inno-agent-hub/install.ps1 |
| Alkalmazás repo | https://github.com/karsarobert/inno-agent |
| Tartalomhub repo (készségek + presetek) | https://github.com/karsarobert/inno-agent-hub |
