# Teljes magyar Content Hub-, Skill- és dokumentációlokalizáció — architektúra és végrehajtási terv

> Ez a dokumentum a `02_magyar_nyelvek_megvalositasi_terv.md` V1 UI-tervét egészíti ki a jóváhagyott, teljes Content Hub hatókörrel. Nem írja felül a korábbi tervet.

Készítés: 2026-07-24  
Hub repository: `/home/karsa-robert/hermes/inno-agent`  
Runtime repository: `/home/karsa-robert/hermes/inno-agent/app`  
Vizsgált runtime commit: `a1573de7dcc6513b9e49d26426c80eb24d386009`

## 1. Jóváhagyott cél és ajánlás

**Cél:** a kínai és angol mellett magyarul elérhetővé tenni az Inno Agent teljes használati élményét:

1. a futó alkalmazás UI-ját;
2. a Content Hub preset- és Skill-katalógusának címkéit;
3. a ténylegesen telepített Skill-ek és preset-munkaterületek agent-utasításait;
4. a Skill-ek referenciafájljait, sablonjait és felhasználói dokumentációját;
5. a Hub `README.md` és `how-to/` anyagait.

**Ajánlott megvalósítás:** ne másoljuk át vagy írjuk felül a jelenlegi kínai/angol fákat. Minden tartalmi csomaghoz adjunk **azonosítóra épülő, külön magyar locale-fát**, és a futtatókód az import/instanciálás pillanatában a választott tartalomnyelv fáit materializálja az aktív munkatérbe.

Ez megőrzi:

- a stabil Skill-/preset-azonosítókat és URL-eket;
- a jelenlegi angol/kínai csomagokat;
- a folyamatban hivatkozott fájlneveket és relatív útvonalakat;
- a Content Hub jelenlegi GitHub- és bundle-service kompatibilitását;
- a felhasználó már létrehozott munkaterületeit és telepített Skill-jeit.

## 2. Leltár: a lokalizáció tényleges mérete

A repositoryból kizártuk az `app/`, `.git` és `node_modules` könyvtárakat. Az eredmény:

| Terület | Fájlok | Szöveges fájlok | Kínai karaktert tartalmazó szöveges fájlok | Lokalizációs szerep |
|---|---:|---:|---:|---|
| `skill-library/` | 859 | 639 | 167 | 46 importálható globális Skill + referenciák, sablonok, scriptek |
| `workspace-templates/` | 281 | 196 | 67 | 19 használható preset + 1 `_template` váz |
| `how-to/` | 46 | 3 | 3 | felhasználói útmutatók |
| gyökér README | 1 | 1 | 1 | Hub belépődokumentáció |

További szerkezeti tények:

- 46 root-szintű `skill-library/<id>/SKILL.md` csomag van.
- 20 `workspace-templates/<id>/agent.md` létezik; ebből 19 mellett van `preset.json`, a `_template` nem publikált minta.
- A jelenlegi Hub-szolgáltatás a root marker alapján azonosítja a Skill-et (`SKILL.md`) és a presetet (`preset.json`): `app/scripts/content-hub-server/server.mjs:45-49,104-145`.
- A GitHub source a root marker jelenlétét keresi: `app/apps/inno-agent/src/content-source/github-source.ts:139-157`.
- A Skill katalógus jelenleg a root `SKILL.md` frontmatteréből olvassa a `description` és `category` értéket: `app/apps/inno-agent/src/server.ts:1127-1163`.
- A preset katalógus a root `preset.json` egyetlen `name`, `description`, `category` értékét adja a UI-nak: `app/apps/inno-agent/src/presets/preset-store.ts:28-34,117-143`.

Ezért az egész Hub nem lokalizálható kizárólag az alkalmazás `hu.json` UI-katalógusával.

## 3. Nem javasolt megoldások

### 3.1 A jelenlegi kínai/angol fájlok helyben magyarra fordítása

Elvetendő. Elveszne az upstream nyelvű eredeti, a merge-ek nehezülnének, és nem maradna többnyelvű termék.

### 3.2 Minden magyar Skill/preset külön `-hu` azonosítóval

Elvetendő. A `tutor` és `tutor-hu` két külön Skill-ként jelenne meg, dupla importot és párhuzamos karbantartást okozna. Az ID a technikai identitás, nem a nyelv neve.

### 3.3 Csak metadata-fordítás

Elvetendő teljes lokalizációként. A kártya címe magyar lenne, de az import után az agent továbbra is angol/kínai viselkedési promptot kapna.

### 3.4 Nyelvváltáskor a meglévő munkaterületek automatikus felülírása

Elvetendő. Egy preset-munkatér létrejötte után a felhasználó szerkesztheti az `agent.md`-t, a Skill-eket és a fájlokat; automatikus nyelvi felülírás adatvesztést okozna.

## 4. Cél Hub-csomagséma

A root marker-ek maradnak visszafelé kompatibilis kanonikus fájlként, a magyar változatok külön locale-könyvtárba kerülnek.

### 4.1 Skill csomag

```text
skill-library/
  tutor/
    SKILL.md                       # kanonikus / régi kliensekhez kompatibilis
    i18n.json                      # kijelzett metadata nyelvenként
    locales/
      en/
        SKILL.md
        references/
          pedagogy.md
          obstacles.md
      zh-CN/
        SKILL.md
        references/...
      hu/
        SKILL.md
        references/
          pedagogy.md
          obstacles.md
    scripts/                        # fordításfüggetlen, közös végrehajtható fájlok
    assets/                         # fordításfüggetlen, közös képek/adatok
```

Kötelező invariánsok:

- a Skill technikai ID-je és frontmatter `name` mezője minden nyelven azonos, például `tutor`;
- a frontmatter `description` adott locale szerinti magyar/angol/kínai rövid leírás;
- csak a megjelenített természetes nyelv, példák, promptok és referenciák fordíthatók;
- változatlan: fájlnév, relatív import/link, parancsnév, API-kulcs-környezeti változó, JSON-kulcs, placeholder (`{{value}}`), reguláris kifejezés, URL, licence- és forráshivatkozás;
- a `locales/hu/` fában a `SKILL.md`-ből hivatkozott lokalizált referencia relatív útvonalának ténylegesen léteznie kell.

### 4.2 Preset csomag

```text
workspace-templates/
  ielts-prep/
    preset.json                    # kanonikus kompatibilis metadata
    i18n.json                      # kijelzett metadata nyelvenként
    agent.md                        # kanonikus / régi kliensekhez
    locales/
      en/
        agent.md
        .skills/
          vocabulary-cards/
            SKILL.md
      zh-CN/
        agent.md
        .skills/...
      hu/
        agent.md
        .skills/
          vocabulary-cards/
            SKILL.md
    assets/                         # közös eszközök, képek, mintaadatok
```

A `locales/<nyelv>/` könyvtár a munkatérbe másolható nyelvi tartalom. A nem lokalizált, közös fájlok ugyanúgy másolódnak. Ha egy nyelvi fa hiányzik, a megengedett fallback a kanonikus fája; az alkalmazás ezt a felületen jelezze, ne csendben keverje a nyelveket.

### 4.3 Lokalizált metadata

Javasolt közös `i18n.json` séma minden importálható elemen:

```json
{
  "schemaVersion": 1,
  "locales": {
    "en": {
      "name": "IELTS Preparation",
      "description": "Academic English preparation workspace.",
      "category": "teaching"
    },
    "zh-CN": {
      "name": "雅思备考",
      "description": "学术英语备考工作区。",
      "category": "教学"
    },
    "hu": {
      "name": "IELTS-felkészítő",
      "description": "Akadémiai angol nyelvvizsga-felkészítő munkatér.",
      "category": "oktatás"
    }
  }
}
```

A `preset.json` meglévő, egyértékű `id/name/description/category/icon` mezői maradnak. A `i18n.json` felülírhatja kizárólag a megjelenítési metadata három mezőjét. Az `id` és az `icon` nem lokalizált.

A Skill-eknél az `i18n.json` a lista UI metadata forrása; a runtime Skill fájl saját frontmattere továbbra is érvényes a materializált nyelvi példányban.

## 5. Runtime architektúra: tartalomnyelv ≠ UI-nyelv

A **kezelőfelület nyelve** és a **tartalomnyelv** összefüggő, de nem azonos beállítás:

- UI-nyelv: gombok, beállítások, panelcímkék, dátumformátum.
- Tartalomnyelv: a telepítéskor kiválasztott Skill/preset természetes nyelve, a `SKILL.md`, `agent.md`, referenciák és sablonok nyelve.

Ajánlott UX:

1. a Content language alapértéke kövesse az UI-nyelvet (`hu`);
2. a Beállításokban külön „Tartalom nyelve” legördülő legyen: `Magyar`, `English`, `中文`;
3. Skill vagy preset importáláskor az elemhez elérhető nyelvek látszanak;
4. ha `hu` nem elérhető, az UI egyértelműen jelzi a fallback nyelvét, és import előtt választást kér;
5. már materializált munkatér/Skill nyelve nem változik UI-váltásra; ehhez későbbi, explicit „Nyelvi változat létrehozása/frissítése” művelet kell, biztonsági mentéssel.

Ez a modell a meglévő munkaterületeket változatlanul hagyja, és lehetővé teszi, hogy egy magyar UI-ban angol szakmai Skill legyen szándékosan telepítve.

## 6. Kötelező runtime módosítások

### 6.1 Közös content-locale típus és fallback

Új modul a runtime-ban, például:

`app/apps/inno-agent/src/content-source/content-locale.ts`

Feladata:

- `ContentLocale = "zh-CN" | "en" | "hu"`;
- egyetlen validátor és fallback sorrend (`requested → en → canonical`);
- locale-specifikus fájlok feloldása;
- kizárólag előre definiált, path-traversal-mentes locale azonosító elfogadása.

A jelenlegi `RemoteContentSource` továbbra is teljes csomagot tölt le (`downloadItem`), ezért a GitHub és bundle transport változatlan maradhat. A nyelvi kiválasztás a letöltött csomag ellenőrzött materializálásakor történjen.

### 6.2 Lokalizált metadata olvasása

Módosítandó érintett útvonalak:

- `app/apps/inno-agent/src/presets/preset-store.ts:57-82,117-143`
- `app/apps/inno-agent/src/server.ts:1127-1163`
- `app/apps/inno-agent/src/content-source/types.ts:15-47`
- `app/apps/inno-agent/scripts/content-hub-server/server.mjs:62-145`

Viselkedés:

- a listázási API a kérés `contentLocale` paraméteréhez választ `i18n.json` metadata-t;
- a remote bundle index tartalmazhatja a teljes `locales` metadata-t, a kliens/backend abból szűr;
- GitHub source esetén `i18n.json` olvasás történik a már meglévő, korlátozott párhuzamosságú raw fetch mechanizmussal;
- hiányzó `i18n.json` esetén az eredeti root `SKILL.md` / `preset.json` metadata marad azonnali, kompatibilis fallback.

### 6.3 Skill import lokalizált materializálása

Módosítandó útvonalak:

- backend: `app/apps/inno-agent/src/server.ts:1171-1181,2593-2601`
- frontend API: `app/apps/inno-agent/web/src/api/skills.ts:13-18`
- frontend típus/UI: `web/src/types/skills.ts`, `web/src/react/SkillsPanel.tsx`

Új kérésforma:

```json
POST /api/skill-library/import
{ "name": "tutor", "contentLocale": "hu" }
```

Import után a szerver:

1. letölti és integritásellenőrzi a teljes csomagot;
2. kiválasztja a `locales/hu/` fát vagy dokumentált fallbacket;
3. a kiválasztott tartalmi fákat másolja az aktív Skill gyökerébe;
4. a közös `scripts/`, `assets/` és szükséges nem nyelvi fájlokat másolja;
5. az aktív root `SKILL.md` a ténylegesen választott nyelvi változat;
6. a Skill telepített metadata-jába rögzíti a forrás ID-t, a kiválasztott `contentLocale`-t, az upstream content revisiont és a fordítás revisiont.

A provenance ne a meglévő SKILL frontmatter egyszerű mezőibe kerüljön, mert a jelenlegi parser csak egyszerű string/boolean sorokat kezel (`server.ts:844-856`). Javasolt külön, gépi fájl:

```json
// .inno-content.json
{
  "sourceId": "tutor",
  "contentLocale": "hu",
  "fallbackFrom": null,
  "hubRevision": "<git SHA vagy bundle verzió>",
  "translationRevision": "2026-07-24"
}
```

### 6.4 Preset instanciálás lokalizált materializálása

Módosítandó útvonalak:

- `app/apps/inno-agent/src/presets/preset-store.ts:150-249`
- `app/apps/inno-agent/src/server.ts` presetnyitó route-ja (a jelenlegi hivatkozás szerint körülbelül `2973`)
- `app/apps/inno-agent/web/src/api/presets.ts`
- `app/apps/inno-agent/web/src/react/ChatCenter.tsx`

Új kérésforma:

```json
POST /api/presets/:id/open
{ "contentLocale": "hu" }
```

A szerver csak az első instanciáláskor választ és másol nyelvet. Ha ugyanaz a preset már létezik más tartalomnyelven, az API ne írja felül: jelezze a nyelvet és kínáljon új munkatér létrehozását, illetve explicit klónozást.

### 6.5 UI nyelv és tartalomnyelv kapcsolata

A V1 UI-i18n tervben szereplő `SupportedLocale` típusból ne következtessünk automatikusan minden runtime kérésben. Külön `contentLocale` állapotot kell kezelni és helyben perzisztálni, például `inno.contentLocale` kulcson.

A default csak első indításkor örököljön a UI locale-ból; utána független felhasználói választás.

## 7. Tartalmi fordítási gyártósor

A fordítás minősége itt egyben agent-viselkedési és pedagógiai minőség. A teljes Hubhoz minden csomagnál azonos, auditalható folyam kell.

### 7.1 Előkészítés és forrásbefagyasztás

1. Hozzunk létre `content-manifest.json` fájlt a Hub gyökerében a csomag-ID, forrásnyelv, upstream revision, licenc és fordítási állapot rögzítésére.
2. Rögzítsük a pontos forráscommitot minden fordítási batchhez.
3. A source textet ne szerkesszük fordítás közben.
4. Minden lokalizált fájlban vagy manifestben legyen `sourcePath`, `sourceSha256`, `translator/reviewer`, `translatedAt` provenance.

### 7.2 Géppel ellenőrizhető transzformációs szabályok

Nem fordítható elemek:

- YAML frontmatter technikai `name` azonosító;
- linkcél, relatív fájlnév, URL, Markdown anchor, API endpoint;
- shell/parancssori kód, JSON/YAML kulcs, környezeti változó;
- i18n interpoláció (`{{…}}`), template placeholder, regex;
- hivatkozás, DOI, szerzőnév, licencszöveg jogi része;
- skill triggerhez szükséges angol/kínai kulcsszavak: a magyar kulcsszavakat hozzá kell adni, nem a régieket lecserélni.

Fordítandó elemek:

- címek, szövegtörzs, felhasználónak adott instruktív promptok;
- példák és pedagógiai forgatókönyvek, ha magyar kontextusra vannak adaptálva;
- metadata `name/description/category` megjelenített értékei;
- felhasználói dokumentáció és képernyőképfeliratok.

### 7.3 Fordítási és felülvizsgálati szerepek

Minden csomag legalább négy ellenőrzési ponton megy át:

1. **Terminológiai ellenőrzés:** a központi magyar termszótár szerint.
2. **Technikai diff:** fájlútvonalak, parancsok, placeholderek, linkek, kódrészletek változatlanok.
3. **Pedagógiai/domain review:** az oktatási példák és értékelési logika magyar környezetben értelmes és nem félrevezető.
4. **Funkcionális agent-eval:** az adott locale Skill tényleg aktiválódik, a magyar inputra magyarul, a szakmai elvárás szerint viselkedik.

Az automatikus első fordítás lehet gépi/LLM-támogatott, de nem publikálható humán review nélkül olyan csomagnál, amely értékelési, hallgatói profil- vagy oktatási döntést befolyásol.

### 7.4 Javasolt fordítási sorrend

| Hullám | Tartalom | Indok |
|---|---|---|
| 0 | termszótár, metadata-séma, validator, 3 referencia pilot | Előbb a folyamat bizonyítása. |
| 1 | Hub README + 3 how-to + V1 UI | Magyar belépési út és használhatóság. |
| 2 | 19 publikált preset + `agent.md` + privát `.skills` | A Simple Mode által közvetlenül használt tartalom. |
| 3 | 46 globális Skill `SKILL.md` és metadata | A teljes katalogizált képességkészlet. |
| 4 | 639 szöveges Skill referencia/sablon és 196 template-szöveg | Teljes mélység, domain review-val. |
| 5 | magyar feature/behavior evalok, release audit, üzemeltetési átadás | Csak validált tartalom kerül élesbe. |

A „teljes” cél minden hullámot tartalmaz, de a release-ek lehetnek fokozatosak: az 1–2. hullám ad azonnali magyar belépési élményt, a 3–4. hullám teljesíti a Content Hub teljességét.

## 8. Minőségkapuk és automatizált ellenőrzés

A Hubhoz új, CI-ben futó validátor kell. Javasolt fájl:

`/home/karsa-robert/hermes/inno-agent/scripts/validate_locales.py`

Ellenőrizze minden publikált Skill/preset esetén:

1. a root marker megmaradt;
2. a `i18n.json` JSON-sémája és a `hu/en/zh-CN` metadata jelen van;
3. a szükséges `locales/hu/SKILL.md` vagy `locales/hu/agent.md` létezik;
4. a magyar változatban a technikai frontmatter `name` azonos a kanonikussal;
5. a forrás és a fordítás relatív linkjei célba érnek;
6. a kódfence-ek, shell parancsok, URL-ek, interpolációk és környezeti változók változatlanok;
7. nincs hiányzó lokalizált belső hivatkozás;
8. a magyar metadata üres vagy többsoros hiba nélkül parse-olható;
9. az installálható root item ID-k ütközésmentesek;
10. provenance mezők és forrás-hash jelen vannak.

Runtime tesztek a `app/` repositoryban:

- `content-locale.test.ts`: validáció és fallback sorrend;
- `localized-metadata.test.ts`: `hu` metadata választása, hiány esetén kanonikus fallback;
- `localized-skill-install.test.ts`: teljes Skill-csomagból a `hu` root `SKILL.md` materializálódik, a referenciák működnek;
- `localized-preset-instantiation.test.ts`: a magyar `agent.md` és `.skills` kerül az új munkatérbe;
- regressziós tesztek: `en`, `zh-CN`, régi `i18n.json` nélküli csomag és korábbi GitHub Hub továbbra is működik;
- e2e: magyar UI → magyar content locale → magyar kártyanév → import → agent magyar Skill-promptot kap.

Az implementáció TDD szerint történjen: minden fenti viselkedéshez előbb bukó teszt, utána minimális implementáció, végül teljes build és e2e ellenőrzés.

## 9. Release- és migrációs stratégia

### 9.1 SemVer / kompatibilitás

- A Hub-séma opcionális `i18n.json` fájllal indul: régi csomagok változatlanul listázhatók és telepíthetők.
- A runtime csak akkor támaszkodhat a `locales/` fára, ha a Hub feature flag/séma verzió ezt jelzi.
- A bundle service indexének új lokalizációs mezői additívak; korábbi kliensek figyelmen kívül hagyják őket.

### 9.2 Meglévő telepítések

- A már importált globális Skill-eket tilos átírni.
- A már létrehozott preset-munkaterületeket tilos automatikusan átírni.
- Később külön „magyar változat klónozása” funkció hozhat létre új példányt, egyedi azonosítóval és migration loggal.
- A `runtime/data/preset-cache/` cache verziózást igényel: új, nyelvi anyag telepítése cache-érvénytelenítés után frissüljön, felhasználói munkatér megőrzése mellett.

### 9.3 Fordításfrissítés

Ha a forrás Skill/preset változik:

1. a CI összehasonlítja a `sourceSha256` vagy Git revision értékét;
2. a magyar fordítás státusza `outdated` lesz;
3. a katalógus jelezheti ezt, de nem szabad részben friss, részben régi csomagot csendben telepíteni;
4. fordítás + review + validátor után új `translationRevision` készül.

## 10. Elfogadási kritériumok a teljes célhoz

A projekt akkor tekinthető teljesítettnek, ha:

- a kínai, angol és magyar UI választható és tartós;
- mind a 19 publikált presetnek van magyar katalógusadata, `agent.md`-je és publikus privát Skill-je;
- mind a 46 globális Skill-nek van magyar metadata- és `SKILL.md`-változata;
- minden hivatkozott, a magyar Skill működéséhez szükséges referencia/sablon magyarul elérhető;
- a 3 how-to dokumentum és a Hub README magyar változata megvan;
- a kiválasztott `hu` content locale valóban magyar fákat materializál, nem csak magyar címkét;
- a `hu` locale hiányának fallbackje látható, determinisztikus és tesztelt;
- a régi, nem lokalizált Hubok és az angol/kínai csomagok regresszió nélkül működnek;
- minden automatizált Hub-validator, runtime unit/integrációs teszt, `npm run build` és magyar e2e zöld;
- minden magyarított csomaghoz revision és forrásprovenance rögzített.

## 11. Következő végrehajtási lépés

A közvetlen következő fejlesztési sprint ne a 900+ fájl vak fordításával induljon. Elsőként a következőket kell megvalósítani és tesztelni:

1. runtime content-locale modell és metadata-fallback;
2. Hub `i18n.json` séma + validator;
3. egy kis, reprezentatív pilot: `tutor` Skill, `ielts-prep` preset és a hozzájuk tartozó referenciafák;
4. magyar UI-váltó + Content language beállítás;
5. teljes importálási/instanciálási e2e.

Csak a pilot elfogadása után szabad a 19 preset és 46 Skill tömeges fordítását megkezdeni. Ez a módszer biztosítja, hogy a fordítások nem egy később módosítandó, hibás csomagsémába készülnek el.
