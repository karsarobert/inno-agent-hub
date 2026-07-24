# Inno Agent Hub — részletes projektáttekintés

Vizsgálat dátuma: 2026-07-24  
Helyi klón: `/home/karsa-robert/hermes/inno-agent`  
Forrás: `https://github.com/Chloris-Blaxk/inno-agent-hub`  
Vizsgált commit: `933909d3e752a934d060ef11d90882523a5a3e71` (main)

## 1. Rövid vezetői összefoglaló

Az **inno-agent-hub nem az Inno Agent futtatókódja**, hanem egy 87,7 MB-os, főként kínai nyelvű **tartalom- és erőforrás-elosztó tár**. Célja, hogy az Inno Agent tanulási asszisztenshez három építőelemet adjon:

1. használati útmutatókat (`how-to/`),
2. önállóan telepíthető Skill-csomagokat (`skill-library/`),
3. előre összeállított tanulási/oktatási munkatér-sablonokat (`workspace-templates/`).

A tároló erőssége a széles és strukturált Skill-választék: **46 Skill**, kötelező kategóriacímkékkel, valamint **19 munkatér-sablon**. A tartalom erősen oktatási fókuszú, de dokumentumkezelési, kutatási, frontend-, MCP- és LLM-fejlesztési elemeket is tartalmaz.

A projekt jelen állapotában **nem telepítendő alkalmazás**, ezért nincs gyökérszintű `package.json`, `pyproject.toml`, Dockerfile vagy CI. A vizsgálat ebből következően nem build- és tesztfuttatás, hanem tartalomstruktúra-, metaadat-, futtatható-segédscript- és ellátásilánc-áttekintés volt.

## 2. A projekt tényleges szerepe és kapcsolata az Inno Agenttel

A gyökér README egyértelműen kimondja, hogy a futtatókód a másik repóban található: `hhyqhh/inno-agent`; ez a tároló kizárólag külső dokumentumokat és erőforrásokat tartalmaz (`README.md:13-21`).

A működési modell:

```text
Inno Agent workspace
├── agent.md       munkatér-kontekstus: persona, folyamat, szabályok
├── .skills/       munkatérhez kötött képességek
│   └── <skill>/SKILL.md
└── files/         tananyagok és felhasználói fájlok

Hub-forrás
├── how-to/                útmutatók
├── skill-library/         külön letölthető Skill-csomagok
└── workspace-templates/   agent.md + .skills + preset.json sablonok
```

Az Inno Agent kliens a sablonokat egyszerű módban előre beállított kártyákként kezeli; ezt a `workspace-templates/README.md:3-20, 76-91` írja le. A `preset.json`-nak `id`, `name` és `category` mezőt kell tartalmaznia, az `id`-nak pedig meg kell egyeznie a könyvtár nevével.

## 3. Inventár és technológiai kép

### 3.1 Mennyiségi kép

| Mutató | Eredmény |
|---|---:|
| Verziózott fájlok száma (git metadata nélkül) | 1188 |
| Teljes méret | 87 746 029 byte / kb. 87,7 MB |
| Markdown fájlok | 523 |
| Python fájlok | 142 |
| TypeScript fájlok | 57 |
| XSD fájlok | 195 |
| HTML fájlok | 25 |
| Bash script | 8 |
| Skill-csomag | 46 |
| Publikus munkatér-sablon | 19 |
| GitHub Actions workflow | 0 |

A méret jelentős része nem futtatókód: PDF-ek, bemutató GIF-ek, képek és betűkészletek. A három legnagyobb fájl:

- `how-to/教学助手快速上手.pdf` — 13,16 MiB;
- `skill-library/assets/edu-solid-geometry/demo.gif` — 10,86 MiB;
- `skill-library/assets/edu-analytic-geometry/demo.gif` — 3,50 MiB.

Ez egy dokumentációs/asset-repónál érthető, de lassíthatja a teljes klónozást és az Inno Agent tartalomforrásának frissítését.

### 3.2 Fő komponensek

| Könyvtár | Funkció | Megjegyzés |
|---|---|---|
| `how-to/` | Felhasználói útmutatók | Elsősorban kínai nyelvű, a v0.4.1 körüli Inno Agent használathoz. |
| `skill-library/` | Feltölthető, önálló képességcsomagok | 46 `SKILL.md`, önálló script-, referencia-, template- és asset-könyvtárakkal. |
| `workspace-templates/` | Teljes, helyzethez kötött agent-konfiguráció | Munkatér-kontextus, opcionális lokális Skill-ek, tipikusan `preset.json`. |
| `dokumentumok/`, `scripts/`, `otletek/` | Helyi projektmunkához létrehozott könyvtárak | Nem upstream tartalom; jelenleg üresek. |

## 4. Skill-könyvtár áttekintése

A repó minden 46 felsőszintű Skill-csomagján végzett metaadat-ellenőrzés alapján mindegyikben van YAML frontmatter, `name`, `category` és `description`. A kategóriaeloszlás:

| Kategória | Darab | Jellemző példák |
|---|---:|---|
| 教学辅导 / oktatási támogatás | 16 | `tutor`, `math-tutor`, `homework-grader`, K12 tervezés, geometriák |
| 内容创作 / tartalomalkotás | 11 | `smart-illustrator`, `baoyu-comic`, `frontend-slides`, `theme-factory` |
| 文档处理 / dokumentumkezelés | 8 | `docx`, `pptx`, `xlsx`, `pdf`, `markitdown` |
| 开发工具 / fejlesztői eszköz | 7 | `mcp-builder`, `skill-creator`, `webapp-testing`, `prompt-engineer` |
| 研究检索 / kutatás és keresés | 4 | `paper-lookup`, `citation-management`, `storm-research`, `tavily-search` |

A katalogizálás konzisztens: a kategóriamező kötelező a kliensben történő csoportosítás miatt (`README.md:95-146`; `skill-library/README.md:29-33`). Ez jó, gyakorlati governance-mechanizmus.

### 4.1 Kiemelten érdekes csoportok

**Oktatás és tanulás**
- `k12-lesson-planning`, `k12-lesson-differentiation`, `backwards-design-unit-planner`, `scope-and-sequence-designer`, `explicit-instruction-sequence-builder`, `differentiation-adapter`, `formative-assessment-technique-selector`.
- Kifejezetten K–12-központúak; magyar felsőoktatási felhasználás előtt tantervi, nyelvi és szabályozási lokalizáció kell.
- A `tutor`, `math-tutor`, `socratic-tutor` általánosabb, ezért adaptálhatóságuk jobb.

**Dokumentum- és prezentációs feldolgozás**
- `docx`, `pptx`, `xlsx`, `pdf`, `markitdown` működési mintái értékesek, de erős átfedésben vannak a Hermes meglévő produktivitási képességeivel.
- Több Skill LibreOffice/`soffice`, Poppler és Python-könyvtár függőségeit használja; ezek hostonként ellenőrzendők.

**Kutatás**
- `paper-lookup`, `citation-management`, `storm-research`, `tavily-search` jó szerkezeti kiindulópontot jelenthetnek.
- Külső API-k és nem determinisztikus webes források miatt a forrás-ellenőrzés, kulcskezelés és használati feltételek kötelezőek.

**Fejlesztői meta-Skill-ek**
- `mcp-builder`, `prompt-engineer`, `skill-creator`, `understand`, `webapp-testing` technikai értéket adnak.
- A `skill-creator` különösen érett: értékelési hurok, benchmark-összesítés, gyors validáció és csomagolás a `skill-library/skill-creator/` alatt.

### 4.2 Átvételi javaslat Hermeshez

| Komponens | Döntés | Indok |
|---|---|---|
| `skill-creator` | adaptálható | Hasznos benchmark- és minőségbiztosítási szemlélet, de Hermes saját Skill-sémájához kell igazítani. |
| `storm-research` | adaptálható | Többnézőpontú kutatási munkafolyamat; a Hermes saját kutatási és böngészőeszközeire kell átírni. |
| `paper-lookup`, `citation-management` | adaptálható | Tudományos keresési minták; API-kulcsok, rate limit, megbízhatóság és helyi forráskezelés átvilágítandó. |
| `docx`, `pptx`, `xlsx`, `pdf` | csak szelektíven | A Hermesben már vannak megfelelő, karbantartott Skills; tartalomként összevethetők, vakon nem másolandók. |
| K–12 pedagógiai Skill-ek | csak lokalizálás után | Angolszász K–12 oktatási háttér, nem magyar felsőoktatási vagy intézményi kontextus. |
| `claude-api` | nem közvetlenül átveendő | Anthropic SDK- és Managed Agents-specifikus; a jelenlegi Hermes modell- és szolgáltatófüggetlen architektúrától eltér. |
| `frontend-slides` | szelektíven, hardening után | Jó asset- és designkészlet, de a publikáló script külső csomagtelepítést és publikus Vercel-deployt végez. |

## 5. Munkatér-sablonok áttekintése

A 19 nyilvános sablon két domináns csoportba rendeződik:

1. **Oktatási előbeállítások:** `ielts-prep`, `ielts-coach`, `lesson-plan`, `classroom-quiz`, `knowledge-explain`, `teaching-webpage`, `math-interactive`, `ppt-creation`, `scenario-explain`.
2. **VeryMath AI4Math lánc:** `ai4math-paper-reading`, `ai4math-paper-writing`, `ai4math-lean-agents`, `ai4math-computational-mathematics`, `ai4math-optimization`, `ai4math-auto-research`, `ai4math-evolving`.

A VeryMath-sorozat upstream forrásait a gyökér README nevesíti (`README.md:153-161`), ami jó provenance-gyakorlat. A `workspace-templates/README.md:34-50` a használati területeket és upstream repókat táblázatban is leírja.

### 5.1 Részletes példa: instructional-design

`workspace-templates/instructional-design/agent.md` egy jól kidolgozott, ötlépcsős alsó-középiskolai matematikaoktatási demonstráció:

1. tanulói adatok elemzése és HTML-vizualizáció;
2. mérhető oktatási célok;
3. PPTX óratartalom;
4. tanórai tevékenységek;
5. értékelési rubrika.

Erősségei:
- fázisonkénti emberi megerősítés;
- tanulói preferenciákra építő személyre szabás;
- fokozatos, hivatkozott forrásgyűjtés;
- tantervi/kompetencia-alapú cél, tevékenység és értékelés összekapcsolása.

Korlát: erősen egy konkrét kínai alsó-középiskolai matematikai curriculumra és Inno Agent-specifikus eszközökre épül (`get_learner_context`, `ask_user_question`, Tavily). Magyar adaptációhoz a NAT, érettségi, intézményi tanterv vagy felsőoktatási tanulási kimenetek alapján újra kell írni.

## 6. Minőség- és karbantarthatósági megállapítások

### Magas prioritás

1. **Gyökérszintű licenc hiánya**
   - Bizonyíték: a GitHub API a repó licencét `null` értékkel adta; a gyökérben nincs `LICENSE` fájl.
   - A `README.md:165-167` azt állítja, hogy az egyes almappák saját licencét kell követni, egyébként a főprojekt licence érvényes. Ez azonban nem ad egyértelmű újrafelhasználási jogot a Hub egészére, különösen az eltérő upstream eredetű Skill-eknél.
   - Teendő: gyökér `LICENSE`, harmadik fél eredet/provenance lista és géppel olvasható licencjegyzék (`THIRD_PARTY_NOTICES.md` vagy SPDX-tábla).

2. **Kiadási/CI validáció hiánya**
   - Bizonyíték: `.github/workflows/` alatt nincs fájl; nincs gyökér build- vagy tesztmanifest.
   - A kézi ellenőrzés lefuttatható, de új PR bevihet hibás YAML-t, `preset.json`-t vagy törött katalogizációt.
   - Teendő: CI-ben frontmatter-, JSON-schema-, `id == directory`, belső link- és Skill-index-ellenőrzés.

### Közepes prioritás

3. **Egy publikált sablon metaadata hiányzik**
   - Az `workspace-templates/instructional-design/` valódi sablon: `agent.md`, `.skills/`, CSV, PPTX-minta és build script található benne, de nincs `preset.json`.
   - Következmény: nem jelenhet meg a „simple mode" előbeállított kártyái között, noha a többi sablonhoz hasonló tartalom.
   - Teendő: döntés szükséges: vagy adjunk hozzá valid `preset.json`-t és a README-katalógusban jelenjen meg, vagy jelöljük demo/internal mintaként, például `_instructional-design` néven.

4. **Dokumentációs katalógus és tényleges készlet eltérése**
   - A gyökér README „jelenleg" csak két Skillt emel ki (`README.md:41-45`) és a sablonok felsorolása sem teljes, miközben 46 Skill és 19 sablon van.
   - A `workspace-templates/README.md:56-72` szintén kihagy több könyvtárat (például `instructional-design`, `classroom-quiz`, `knowledge-explain`, egyes kínai nyelvű változatok).
   - Teendő: generált index a fájlrendszerből és frontmatterből; a kézzel írt rövidlista legyen „példák", ne teljes állítás.

5. **Nagy bináris bemutató assetek a normál klónban**
   - 87,7 MB összméret, ebből a 10,86 MB-os GIF és 13,16 MB-os PDF domináns.
   - Teendő: Git LFS vagy külső release/CDN assetek; dokumentációban előnézeti thumbnail és opcionális letöltés.

### Alacsony–közepes prioritás: scriptbiztonság és supply chain

6. **`webapp-testing` tetszőleges shell-parancsot futtat**
   - `skill-library/webapp-testing/scripts/with_server.py:68-74` a `--server` értékét `shell=True` mellett indítja.
   - Ez a Script deklarált funkciója (több szerver, `cd ... && ...`), ezért nem a repó távoli RCE hibája. Viszont az agentnek vagy felhasználónak adott bemenet parancsinjekciós felület.
   - Teendő: csak megbízható, explicit felhasználói inputtal; lehetőleg argv-lista + `cwd` opció, shell mód kizárólag explicit `--allow-shell` kapcsolóval.

7. **`frontend-slides` publikus Vercel-deployt és nem pinelt telepítést végez**
   - `skill-library/frontend-slides/scripts/deploy.sh:113-120` `npx --yes vercel` ellenőrzést, majd szükség esetén `npm install -g vercel` futtat.
   - `deploy.sh:188` a megadott tartalmat `--prod` módban publikálja Vercelre.
   - Teendő: minden deploy előtt explicit felhasználói jóváhagyás; verziópin; előzetes érzékenyadat-szkennelés; defaultként preview mód vagy lokális export.

8. **Külső szolgáltatók és API-k**
   - Tavily, Vercel, Anthropic/Claude, Google Scholar, PubMed és számos upstream Skill bevonásra kerül.
   - A Skill-ek importálása előtt kulcskezelés, adatátadási határ, rate limit és licenc vizsgálat kell.

## 7. Végrehajtott ellenőrzések

| Ellenőrzés | Eredmény |
|---|---|
| `git ls-remote --symref ... HEAD` | Sikeres; alapág: `main`, HEAD: `933909d...` |
| GitHub repo-metaadat | Publikus, nem archivált, Python-domináns, licenc API-ban nincs |
| Skill frontmatter validáció | 46/46 Skill: `name`, `category`, `description` jelen van; kategória és könyvtárnév konzisztens |
| Sablon metadata validáció | 19 sablonból 18-nak érvényes `preset.json`; 1 hiány: `instructional-design` |
| Kategóriaeloszlás | 16 oktatás, 11 alkotás, 8 dokumentum, 7 fejlesztés, 4 kutatás |
| CI vizsgálat | GitHub Actions workflow nincs |
| Script mintavétel | `with_server.py` és `deploy.sh` funkcionálisan érthető, de a fent leírt biztonsági/supply-chain korlátokkal |
| Futtatókód teszt/build | Nem alkalmazható gyökérszinten: a repó nem futtató alkalmazás és nincs gyökérmanifest |

## 8. Javasolt következő sprint

1. **Tartalom-minőségkapu (1–2 nap)**
   - `scripts/validate_content.py` vagy GitHub Action: frontmatter, `preset.json`, directory-ID, `category`, belső hivatkozások, indexek.
   - Az `instructional-design` státuszának rendezése.

2. **Licenc és provenance audit (1–2 nap)**
   - Gyökérlicenc döntés.
   - Minden Skillhez upstream URL, eredeti licenc, módosítási státusz és kompatibilitás táblázata.

3. **Katalógus automatikus generálása (1 nap)**
   - A Skill- és Template-README táblázatokat YAML/frontmatter/preset JSON alapján generálni.
   - Megszünteti a dokumentáció és fájlrendszer driftjét.

4. **Biztonságos telepítési/publikálási policy (1 nap)**
   - `npx`/globális install verziópin; publikáló Skill-ek felhasználói megerősítése; publikus deploy előtti titokszkennelés.

5. **Magyar pilot workspace (2–4 nap)**
   - Nem a teljes könyvtár átemelése, hanem 1 minta: magyar felsőoktatási tananyagfejlesztő munkatér.
   - Javasolt alap: `instructional-design` szerkezete + Hermes oktatási/dokumentum Skills + magyar tantervi/egyetemi kimenetek.

## 9. Végső értékelés

Az Inno Agent Hub értékes **Skill- és pedagógiai workflow-tár**, nem kész, önálló szoftvertermék. Legerősebb elemei a katalogizált Skill-ek, a munkatér-alapú gondolkodás és az oktatási folyamatok strukturálása. A közvetlen, teljes átvétel helyett a megfelelő stratégia: **szelektív adaptáció, licencek tisztázása, saját környezetre átírás és CI-vel ellenőrzött tartalomimport**.
