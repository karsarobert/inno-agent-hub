# C irány szakaszos port — állapot (2026-09-27)

Cél: az upstream v0.6.x-re átállni **külön ágon, szakaszosan**, miközben a tanteremben
bizonyított állapot változatlan marad.

## Hol tartunk (mentés: 2026-09-27 este) — folytatáshoz

| Mi | Állapot |
|---|---|
| A port ága | `feat/v0.6.2-port` @ **`9b8456d`** (a forkra felpusholva), az upstream v0.6.2 csúcsa fölött **11 saját commit** |
| 1. szakasz (backend) | **kész és igazolva** (lásd lentebb a tételeket és a méréseket) |
| Következő | **2. szakasz**: szerepkör-szűrés (diák/tanár) + Practice Lab az új felületen |
| Utána | **3. szakasz**: magyar felület/i18n + a hozzá tartozó UI-elemek (mentés panel, leállítás gomb), és a parkolva tartott hub-lokalizációs tétel |
| Érintetlen | tag `pte-2026.09.27` / `stable` / `3e08cdf`; helyi `main` = `2026011` (szándékosan helyben); futó éles példány `~/.local/opt/inno-agent` → `:3000` |

**Teszt-környezet (élő, külön az éles példánytól):** http://localhost:3100
(a `~/inno-test/home` config + adat, `~/inno-test/workspace` munkatér; a hub a fork
`stable` kiadásáról, 24 kártyával). Indítás a `feat/v0.6.2-port` buildből:

    cd /home/karsa-robert/hermes/inno-agent/app && npm run build
    node apps/inno-agent/dist/server.js --home /home/karsa-robert/inno-test/home \
      --workspace /home/karsa-robert/inno-test/workspace --port 3100 &

Leállítás: `kill $(ss -lptnH 'sport = :3100' | grep -oP 'pid=\K[0-9]+' | head -1)`
(Figyelem: a Vite fejlesztői mód **fixen a `:3000`-re** proxyzza az API-t, ezért HMR-es
fejlesztéshez előbb az éles példányt kell leállítani, vagy átírni a proxy célportját.)

## Rögzített, érintetlen állapot

| Mi | Ref | Commit |
|---|---|---|
| Kiadott, bizonyított app | tag `pte-2026.09.27` + `stable` | `3e08cdf` |
| Helyi fejlesztői vonal | `main` | `2026011` |
| Élesben futó példány | `~/.local/opt/inno-agent` | `3e08cdf` |

## A port ága

`feat/v0.6.2-port` a fork main-jén kívül, az upstream csúcsáról indítva
(`fc74cd6` = v0.6.2 + 8 commit). Az ág a forkon is fent van, a `main`-t nem érinti.

## A 38 saját commit felosztása

- **34 a miénk** (Karsa Róbert) → átemelendő.
- **4 upstream szerzőtől** származó korai átvétel, aminek a megfelelője már benne van a
  v0.6.2-ben → **kihagyva, nulla munka**:
  `0a11b09` és `3ad2136` (yonghenguo — SSE újracsatlakozás + esemény-visszajátszás, 19 fájl!),
  `d0233c1` és `5c8a10f` (haohao — ask_user_question felszabadítás, Tavily web_search).
  A Tavily a v0.6.2-ben már tovább is fejlődött (web-access + beállítás UI).

Ez az egyetlen mérés 19 fájllal csökkentette a konfliktusfelületet.

## Szakaszok és állapot

### 1. szakasz — backend, felülettől független (részben kész)

Kész, tesztelve:
- `fix(config)`: UTF-8 BOM tolerancia a `config.json`-ban (PowerShell 5.1 ír BOM-ot;
  nélküle minden `/api/*` 500-at adott, a `/health` viszont 200-at). + `config.bom.test.ts`.
- `feat(config)`: a beépített alapértelmezett hub `karsarobert/inno-agent-hub`, `ref: stable`.
- `feat(config)`: hub típus `none` (üzemi backend rész: config-union/normalizer, content-source
  factory, `PUT /api/settings/content-hub`).
- `fix(presets)`: kikapcsolt hubnál a `/api/presets` és a `/api/preset-library` üres lista —
  a beépített tartalék presetek (ppt-creation, lesson-plan, scenario-explain) sem jelennek meg.
  + `server/routes/presets.test.ts`.
- `feat(backup)`: a teljes hallgatói állapot export/import egy zipben, **üzemi backend**
  (3 commit): zip író/olvasó, állapotgyűjtő és -visszaállító a saját tesztjeikkel, L2 füzet
  (wiki oldalak, manifest, nyers/kinyert források) a mentésben, L3 store-ok felszabadítása
  visszaállítás előtt, stream-registry védelem (futó feladat alatt nincs visszaállítás).
  Az végpontok az új felosztás szerint a `server/routes/backup.ts`-ben:
  `GET /api/backup/export`, `POST /api/backup/import`. + `server/routes/backup.test.ts`.
  A beállítás-panel UI (BackupPanel, oldalsáv gombok, nyelvi kulcsok) a 3. szakaszra marad.
  Megjegyzés: a commit, amiből portoltunk, véletlenül magával hozta a PTE-portál WIP-et is —
  az szándékosan NEM került át.

- `feat(settings)`: `POST /api/shutdown` — leállítás, kérésre **mentéssel**
  (`{ saveBeforeExit: true }` → a teljes állapot a `<dataDir>/exports/`-ba, ugyanaz az
  archívum, mint a letöltés; ha a mentés nem sikerül, a leállás akkor is megtörténik).
  A végpont a `server/routes/backup.ts`-ben van (ott van az archívum-összeállítás),
  a szerver a saját listener-ét adja hozzá callbackként. A gomb + nyelvi kulcsok a 3. szakaszra.
- `feat(terminal)`: C források futtatása `gcc -std=c17 -Wall -Wextra -Wpedantic`-kel, és
  ezzel együtt a **C++ is** (`g++ -std=c++20 -Wall -Wextra -pedantic`) — az upstream Run gombja
  ugyanis csak python/node/ts/sh-t ismert, a C/C++ teljesen hiányzott az új felületen.
  A parancs-összeállító külön modulba került (`web/src/react/terminal/run-command.ts`,
  a `RunButton` ezt importálja), ezért önállóan tesztelhető. A `&&` lánc miatt fordítási hiba
  esetén nem fut le egy korábbi, elavult bináris.

Az 1. szakasz ezzel **kész**; ami maradt, az a 3. szakaszhoz tartozó lokalizációs tétel:

- **Parkolva**: hub lokalizált skill-metaadatok (`88e77ac`) — az upstream közben
  `content-source/catalog-service.ts`-be szervezte a katalógust, és a
  `content-source/localized-metadata.ts` segédmodulunk náluk nincs meg, ezért ez nem
  szöveg-merge, hanem beépítés az új modulba (a 3. szakasz lokalizációs munkájával együtt).

### 2. szakasz — szerepkör-szűrés és Practice Lab

`2092be0`, `364c20f`, `68a1b36`, `21ef03c`. **Figyelem:** az upstream a Simple Mode-ot
beolvasztotta a normál módba, a mi diák/tanár szűrésünk viszont a Simple Mode-ra épül —
ezért itt új horgonyokat kell keresni, nem elég a szöveget átemelni.

### 3. szakasz — magyar felület, i18n, dokumentáció, arculat

A legnagyobb blokk: `52bd98e`, `4a732c9`, `2f06b7f`, `becb996`, `0487293`, `380cbb1`,
`e31e1f4`, `c5420a3`, `1758ba0`, `9549c27`, `79e2fd2`, `e2ad604`, `7d089cf`, `417b869`,
`2026011`. Az upstream átstrukturálta az i18n kulcskészletet (en/zh-CN +728 sor) és újratervezte
a felületet, ezért a magyar szövegeket az új kulcsokon kell újra megadni. Ide tartozik a
`localized-metadata.ts` és a `hu.json` visszahozatala, valamint a beállítás-panelek
(amiket az upstream teljes képernyős overlay-be szervezett át).

## Ellenőrzés

| Mérés | Eredmény |
|---|---|
| Tesztsor az upstream bázison (kiindulás) | 96 fájl, 721 teszt — zöld |
| Tesztsor a portolt ágon (most) | 103 fájl, 759 teszt — zöld |
| `tsc --noEmit` (build) | rc=0 |
| BOM-os config élőben | `/api/settings` HTTP 200 (előtte 500) |
| Hub `none` élőben | `/api/presets` = `[]`, `/api/preset-library` = `[]` |
| Hub github élőben | `/api/presets` = 3 beépített preset (a normál út nem tört el) |
| Mentés/visszaállítás élőben (teljes kör) | export: 10 bejegyzéses zip + manifest (formatVersion 1, appVersion 0.6.2); a szimulált veszteség (törölt beszélgetés, átírt munkatér-fájl, törölt L2 oldal) után az import `{"status":"restored"}` és minden fájl visszaállt; a régi állapot a `data/.restore-trash/restore-<ts>/`-be került (nem törlődött) |
| Leállítás mentéssel élőben | `POST /api/shutdown {"saveBeforeExit":true}` → 200 `{status:"stopping", savedBackup:"…/data/exports/inno-agent-mentes-2026-09-27-20-34-37.zip"}`; a folyamat 3 mp-en belül leállt (a `/health` nem válaszolt), az archívumban 8 bejegyzés (config, sessions, workspace, l2, l3, jobs, workspaces, manifest) |
| C/C++ futtatás valódi fordítóval | a generált parancsok a gépi `gcc`/`g++` 13.3.0-val lefordultak és lefutottak (`C17 rendben`, `C++20 rendben`); szándékos szintaktikai hibánál a `&&` miatt **nem** indult futtatás (kilépési kód 1, nem keletkezett bináris) |

Élő ellenőrzés eldobható példányból történt (3097–3102 portok), a `:3000`-es éles példány
végig érintetlen maradt.

## Következő lépés

A 2. szakasz (szerepkör-szűrés + Practice Lab az új felületen), majd a 3. szakasz
(magyar felület/i18n + a hozzá tartozó UI-elemek: mentés/visszaállítás panel, leállítás gomb).

## Tapasztalatok a következő szakaszokhoz

- **Az LSP elavult típushibát jelezhet** a cherry-pick után (a fájlt nem a szerkesztő írta):
  a `tsc --noEmit` az irányadó.
- Az upstream **route-modulokra bontotta a `server.ts`-t** (P2 route split), ezért a port nem
  szöveg-összefésülés: a változtatást az új helyre kell beépíteni
  (`server/routes/presets.ts`, `server/routes/settings.ts`, `server/routes/practice.ts`, …).
- A szerver a configot **`<home>/config/config.json`** útvonalon keresi (nem `<home>/config.json`).
- Az eldobható példány indítása forrásból:
  `node --import tsx apps/inno-agent/src/server.ts --home <tmp>/home --data-dir <tmp>/home/data --workspace <tmp>/ws --port <p>`.
