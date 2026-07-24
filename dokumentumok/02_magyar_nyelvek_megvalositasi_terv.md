# Inno Agent magyar felület — megvalósítási javaslat

> **Fejlesztési dokumentum.** A következő javaslat a magyar **kezelőfelület** hozzáadására vonatkozik. Nem fordítja le automatikusan az LLM-válaszokat, a felhasználói munkatérfájlokat vagy a Content Hub egyedi Skill-/preset-tartalmát.

Készítés: 2026-07-24  
Vizsgált futtatókód: `app/`  
Vizsgált commit: `a1573de7dcc6513b9e49d26426c80eb24d386009`

## 1. Döntési javaslat

A magyar nyelvet **harmadik, teljes értékű UI-lokálként** kell felvenni a jelenlegi `zh-CN` és `en` mellé, a már bevezetett `i18next` + `react-i18next` mechanizmust használva. Új i18n-keretrendszer vagy szerveroldali locale-tárolás nem szükséges.

**Javasolt azonosító:** `hu`  
**Megjelenített név:** `Magyar`  
**Dátum-/időformátum locale:** `hu-HU`

Ez a legkisebb kockázatú és legjobban karbantartható út, mert:

- a kliensben már működik a locale-váltó és a `localStorage`-perzisztencia;
- a két jelenlegi fordítás 530/530 kulccsal teljesen szinkronban van;
- a webes felület szövegeinek túlnyomó többsége már `t("…")` hívásból érkezik;
- a változtatás tisztán frontendoldali: a backend API, a memória, a munkaterek és a provider-konfiguráció változatlan marad.

A bevezetést két fázisra kell bontani:

1. **V1 – magyar UI:** navigáció, beállítások, párbeszédablakok, ütemező, munkatér, Skills, preset-rács címkéi, dátum/idő és akadálymentesítési metaadatok.
2. **V2 – magyar tartalom:** a Content Hub Skill- és preset-metaadatainak, `agent.md`-inek és dokumentációinak lokalizálása. Ez külön termék- és fordítási projekt, nem egyszerű UI-fordítás.

## 2. Tényleges kiinduló architektúra

### 2.1 Ami már kész

`app/apps/inno-agent/web/src/i18n/index.ts` jelenleg:

- betölti a `zh-CN.json` és `en.json` katalógust;
- az `inno.locale` localStorage-kulcsban őrzi a választást;
- indításkor `zh-CN`-t használ, ha nincs mentett választás;
- `i18n.changeLanguage()` segítségével vált;
- az alkalmazás belépési pontja már importálja (`web/src/main.tsx:2`).

A fordítási fájlok:

- `app/apps/inno-agent/web/src/i18n/locales/zh-CN.json`
- `app/apps/inno-agent/web/src/i18n/locales/en.json`

Mindkettőben **530 levélkulcs** van; a statikus összehasonlítás eredménye: `zh_only=0`, `en_only=0`.

A Settings panelben működő UI-választó van:

- `app/apps/inno-agent/web/src/react/SettingsPanel.tsx:1172-1213`
- jelenlegi opciók: `zh-CN`, `en`.

### 2.2 Külön választandó nyelvi rétegek

| Réteg | V1 magyar UI része? | Magyarázat |
|---|---|---|
| Gombok, címek, űrlapok, hibák, tabok | Igen | `i18next`-kulcsokból jönnek. |
| Dátum és idő | Igen | Jelenleg több helyen `zh-CN` van beégetve. |
| Böngésző `<html lang>` attribútum | Igen | Képernyőolvasó, helyesírás, kereső és nyelvi eszközök miatt. |
| Chat stream állapotszövegei | Igen | Jelenleg több kínai szöveg közvetlenül a store-ban szerepel. |
| Modell válasza | Nem közvetlenül | Ezt a választott LLM / system prompt nyelve határozza meg. |
| Skill/preset neve és leírása | Nem V1-ben | A Hub metaadataiból érkezik; képernyőképen is kínai és angol vegyesen látszik. |
| `agent.md`, Skill-ek, tutorialok | Nem V1-ben | Tartalmi fordítás és pedagógiai lokalizáció szükséges. |
| Felhasználó által létrehozott adatok | Nem | Nem szabad automatikusan fordítani vagy módosítani. |

## 3. Feltárt hiányok, amelyeket a V1-nek kezelnie kell

### 3.1 Beégetett `zh-CN` dátumformátumok

A nyelvváltó megléte ellenére legalább öt megjelenítési útvonal rögzíti a kínai locale-t:

- `web/src/react/JobsPanel.tsx:46-58`
- `web/src/react/LearnerProfilePanel.tsx:21-33`
- `web/src/react/SessionSidebar.tsx:67-79`
- `web/src/components/sidebar/session-sidebar.ts:41-52`
- részben a `web/src/i18n/index.ts` kezdeti logikája.

Ezeket az aktív UI-locale-ból kell képezni, például `Intl.DateTimeFormat(locale, options)` vagy `date.toLocaleString(locale, options)` használatával. Magyar esetben a javasolt érték `hu-HU`; a platformnyelvnek megfelelő `currentLocale()` azonban a jövőbeni új nyelveket is kezeli.

### 3.2 Közvetlen kínai UI-szövegek

A lokalizációs fájlokon kívül 621 kínai karakter van kilenc TypeScript/TSX fájlban. A kommentek nem igényelnek fordítást, de az alábbi felhasználói felületet érintő szövegek igen:

- `web/src/stores/chat-store.ts:77,116,229,296,399,428,430,475,485,634-647,828-846` — stream- és fájlműveleti állapotok, rövidített tool output jelzések;
- `web/src/react/WorkspaceBrowser.tsx:477-553` — `t()` fallbackek jelenleg kínaiak;
- `web/src/react/ChatCenter.tsx:130,147,1159` — hosszú üzenet/stream állapot fallbackek;
- `web/src/react/SettingsPanel.tsx:836-1029` — Content Hub és OCR fallbackek;
- `web/src/react/SessionSidebar.tsx:452` — export fallback.

Különösen a `chat-store.ts` fontos: ez nem React-komponens, ezért a fordítási eredményt nem jó egyszerűen létrehozáskori stringként tárolni. A locale-váltás közbeni helyes újrarajzoláshoz **kulcs + interpolációs paraméter** formában kell tárolnia az állapotot, a fordítás pedig a React renderben történjen.

Ajánlott forma:

```ts
export interface StreamingActivity {
  key: string;
  values?: Record<string, string | number>;
}

// Store: csak a szemantikus állapotot rögzíti.
this.streamingActivity = { key: "chat.activity.analyzing" };
this.streamingActivity = { key: "chat.activity.toolRunning", values: { toolName } };

// Komponens: a pillanatnyi kiválasztott locale-ra fordít.
const label = state.streamingActivity
  ? t(state.streamingActivity.key, state.streamingActivity.values)
  : "";
```

Ez megakadályozza, hogy nyelvváltás után egy futó válasz kínai állapotcímkét hagyjon a magyar felületen.

### 3.3 Hiányzó kulcsok a jelenlegi két nyelvben

A statikus `t("…")` hívások és a katalógus összevetése öt hiányzó kulcsot talált. Ezek jelenleg fallbackből működnek, de a magyar bevezetés előtt a két meglévő katalógusba is fel kell venni őket:

- `common.clear` — `SkillsPanel.tsx:442,590`
- `common.collapseSidebar` — `Notebook.tsx:129`, `WorkspaceBrowser.tsx:503,636`
- `common.expandSidebar` — ugyanott
- `settings.editModel` — `SettingsPanel.tsx:138`
- `settings.form.apiType` — `SettingsPanel.tsx:147,299`

A fordítási kód minőségkapujában a fallbackek nem elfedhetik a hiányzó saját kulcsokat.

### 3.4 HTML nyelvi metaadat és kezdeti nyelv

- `web/index.html:2` jelenleg rögzített `<html lang="zh-CN">` értéket használ.
- `web/src/i18n/index.ts:8-12` csak mentett `zh-CN`/`en` értéket fogad el, egyébként kínai nyelvű indulást kényszerít.

A `setLocale()` műveletkor `document.documentElement.lang`-ot kötelező frissíteni. Induláskor még a React render előtt a localStorage-ból kiolvasott támogatott locale-t kell alkalmazni. A helyes `lang` értékek: `zh-CN`, `en`, `hu`.

### 3.5 Content Hub címkék

A Simple Mode ténylegesen a Hub `preset.json` fájljaiból érkező `name`, `description`, `category` mezőket jeleníti meg:

- backend: `app/apps/inno-agent/src/presets/preset-store.ts:28-34,117-143`;
- frontend típus: `web/src/types/presets.ts:1-7`;
- Skill könyvtár típus: `web/src/types/skills.ts:13-18`.

Az UI fordítása nem fordítja át a külső Hubban lévő „AI4Math…”, kínai vagy angol presetneveket. Ez helyes V1-határ: a jelenlegi metadata-séma csak egy `name`/`description` értéket definiál.

A V2-höz javasolt, visszafelé kompatibilis Hub-séma:

```json
{
  "id": "lesson-plan",
  "name": "教案生成",
  "description": "…",
  "localized": {
    "en": { "name": "Lesson Planner", "description": "…" },
    "hu": { "name": "Óratervkészítő", "description": "…" }
  }
}
```

A kliensnek a kiválasztott locale szerinti `localized[locale]` értéket kell választania, majd az alap `name`/`description` mezőre visszaesnie. Ez csak a V2-ben szükséges; a V1-et nem szabad ettől függővé tenni.

## 4. Javasolt V1 architektúra

### 4.1 Egyetlen támogatott-locale definíció

Hozzunk létre egy központi definíciót az `i18n` modulban:

```ts
export const SUPPORTED_LOCALES = ["zh-CN", "en", "hu"] as const;
export type SupportedLocale = (typeof SUPPORTED_LOCALES)[number];

export const LOCALE_LABEL_KEYS: Record<SupportedLocale, string> = {
  "zh-CN": "settings.languageOptions.zh-CN",
  en: "settings.languageOptions.en",
  hu: "settings.languageOptions.hu",
};
```

Ezt használja a kezdőérték, a `setLocale`, a Settings `<select>`, a validáció és a `document.lang` szinkron. Így az `"zh-CN" | "en"` union többé nem marad szétszórva a komponensekben.

### 4.2 Kezdőnyelv logika

Ajánlott prioritás:

1. korábban a felhasználó által választott, érvényes `inno.locale`;
2. `navigator.languages` / `navigator.language` támogatott megfelelője (`hu-*` → `hu`, `en-*` → `en`, `zh-*` → `zh-CN`);
3. meglévő kompatibilis fallback: `zh-CN`.

Ez nem változtatja meg a régi felhasználók mentett választását, de magyar böngészőn első induláskor automatikusan magyar UI-t ad. Ha termékdöntés szerint a kínai alapértelmezés változatlanul maradjon, a 2. lépés kikapcsolható; a nyelvválasztó ettől függetlenül működik.

### 4.3 Fordítási katalógus

Új fájl:

`app/apps/inno-agent/web/src/i18n/locales/hu.json`

Kiindulópontként az `en.json` **teljes szerkezeti másolata** szolgáljon. Minden kulcs változatlan; csak a stringértékek fordulnak. A fordításhoz rögzített szabályok:

- `{{count}}`, `{{time}}`, `{{name}}`, `{{message}}` és minden i18next interpoláció változatlan;
- technikai azonosítók nem fordulnak: `API Key`, `Base URL`, `Cron`, `GitHub`, `Feishu`, `WeChat`, `L1/L2/L3`, `CLI`, `OAuth`;
- „Skill” termékkifejezés az első UI-kiadásban maradhat „Skill”; ne keverjük esetlegesen a „készség”, „képesség” és „modul” fordításokat;
- felhasználó felé kimondottan magyar, cselekvő, magázás nélküli rövid feliratok legyenek: „Mentés”, „Mégse”, „Új beszélgetés”, „Munkaterület”, „Ütemezett feladatok”;
- a nyelv neve a legördülőben natív önelnevezés: `中文`, `English`, `Magyar`.

### 4.4 Locale-érzékeny dátumsegéd

Hozzunk létre egy új, tiszta segédmodult:

`app/apps/inno-agent/web/src/i18n/format.ts`

Példa API:

```ts
import type { SupportedLocale } from "./index.js";

const DATE_LOCALES: Record<SupportedLocale, string> = {
  "zh-CN": "zh-CN",
  en: "en-US",
  hu: "hu-HU",
};

export function formatShortDateTime(iso: string | undefined, locale: SupportedLocale): string {
  if (!iso) return "-";
  const date = new Date(iso);
  if (Number.isNaN(date.getTime())) return iso;
  return new Intl.DateTimeFormat(DATE_LOCALES[locale], {
    month: "short", day: "numeric", hour: "2-digit", minute: "2-digit",
  }).format(date);
}
```

A komponensek `useTranslation()`-ből kapott `i18n.resolvedLanguage` értékét normalizált `SupportedLocale` formában adják át. A Lit-komponensnél vagy át kell állni a közös React `SessionSidebar` használatára, vagy az i18n singleton `languageChanged` eseményére kell feliratkozni; az előbbi kisebb hosszú távú fenntartási kockázat.

## 5. Végrehajtási terv (TDD)

### 1. feladat: i18n-regressziós tesztalap létrehozása

**Cél:** A harmadik nyelv soha ne maradhasson kulcshiányos.

**Fájlok:**
- Módosítás: `app/package.json`
- Módosítás: `app/apps/inno-agent/web/package.json`
- Létrehozás: `app/apps/inno-agent/web/src/i18n/i18n.test.ts`

**RED:** A teszt olvassa a `zh-CN.json`, `en.json`, `hu.json` fájlokat, lapítsa ki a kulcsokat, és állítsa, hogy a három kulcshalmaz azonos. Induláskor a `hu.json` hiánya miatt a teszt bukjon.

**GREEN:** Vegyük fel a Vitest `test` scriptet a web workspace-be, majd hozzuk létre a teljes `hu.json` katalógust.

**Ellenőrzés:**

```bash
npm --workspace inno-agent-web run test -- --run src/i18n/i18n.test.ts
```

Elvárt: a három katalógus kulcshalmaza egyezik.

### 2. feladat: támogatott locale típus és nyelvváltó

**Cél:** A `hu` teljesen támogatott értékké váljon, szórt string unionök nélkül.

**Fájlok:**
- Módosítás: `app/apps/inno-agent/web/src/i18n/index.ts:1-37`
- Módosítás: `app/apps/inno-agent/web/src/react/SettingsPanel.tsx:1172-1213`
- Módosítás: `app/apps/inno-agent/web/src/i18n/locales/zh-CN.json`
- Módosítás: `app/apps/inno-agent/web/src/i18n/locales/en.json`
- Módosítás: `app/apps/inno-agent/web/src/i18n/locales/hu.json`
- Teszt: `app/apps/inno-agent/web/src/i18n/i18n.test.ts`

**RED:** Tesztelje, hogy `setLocale("hu")` tárolja az `inno.locale=hu` értéket, `i18n.language`-et vált, és `document.documentElement.lang` értéke `hu`.

**GREEN:** Regisztráljuk a magyar resource-ot, vezessük be a `SupportedLocale` típust és a `isSupportedLocale()` őrt, bővítsük a Settings legördülőt a „Magyar” opcióval. A korábbi két nyelv továbbra is választható legyen.

**Megjegyzés:** A `navigator.language` alapú autodetekció külön tesztelendő és csak akkor kapcsolandó be, ha a termékdöntés ezt jóváhagyja.

### 3. feladat: HTML nyelvi metaadat szinkronizálása

**Cél:** A felület nyelvi deklarációja kövesse a tényleges UI-nyelvet.

**Fájlok:**
- Módosítás: `app/apps/inno-agent/web/index.html:2`
- Módosítás: `app/apps/inno-agent/web/src/i18n/index.ts`
- Teszt: `app/apps/inno-agent/web/src/i18n/i18n.test.ts`

**RED:** Induláskor mentett `hu` locale mellett a dokumentum `lang` attribútuma `hu`; váltás után szintén frissül.

**GREEN:** Az index HTML maradhat biztonságos kezdeti `lang="zh-CN"` értéken, de az i18n bootstrap még első React paint előtt szinkronizálja a dokumentumot. Alternatívaként minimális inline bootstrap olvashatja a localStorage-t; ezt csak FOUC/akadálymentesítési mérés alapján válasszuk.

### 4. feladat: dátum- és időformázás lokalizálása

**Cél:** Magyar mód esetén magyar formátum és magyar hónapnevek jelenjenek meg.

**Fájlok:**
- Létrehozás: `app/apps/inno-agent/web/src/i18n/format.ts`
- Módosítás: `web/src/react/JobsPanel.tsx:46-58`
- Módosítás: `web/src/react/LearnerProfilePanel.tsx:21-33`
- Módosítás: `web/src/react/SessionSidebar.tsx:67-79`
- Módosítás vagy kivezetés: `web/src/components/sidebar/session-sidebar.ts:41-52`
- Teszt: `web/src/i18n/format.test.ts`

**RED:** Egy fix ISO időpont `hu` esetén a `hu-HU` szerinti, `en` esetén angol, `zh-CN` esetén kínai formátumot ad; hibás dátum az eredeti stringet adja vissza.

**GREEN:** Egységes helper használata, közvetlen `toLocaleString("zh-CN", …)` hívások megszüntetése.

### 5. feladat: streaming és fallback UI-szövegek i18n-be emelése

**Cél:** Magyar nyelvnél egyetlen felhasználónak látható állapotjelzés se maradjon kínaiul.

**Fájlok:**
- Módosítás: `web/src/stores/chat-store.ts:77-647,828-846`
- Módosítás: `web/src/react/ChatCenter.tsx`
- Módosítás: `web/src/react/WorkspaceBrowser.tsx`
- Módosítás: `web/src/react/SettingsPanel.tsx`
- Módosítás: `web/src/react/SessionSidebar.tsx`
- Módosítás: mindhárom locale JSON.

**RED:** A store szemantikus kulcsot ad vissza; a React komponens `t()`-vel fordít. Nyelvváltás után a már látható stream-állapot is magyarra vált, új tool esemény nélkül.

**GREEN:** A beégetett végfelhasználói szövegek eltűnnek a store-ból és a fallbackekből. A kínai fejlesztői kommentek maradhatnak, mert nem UI-szövegek.

### 6. feladat: hiányzó meglévő kulcsok rendezése

**Cél:** A fallbackek ne rejtsenek valódi katalógushiányt.

**Fájlok:** mindhárom locale JSON, illetve a fenti i18n-teszt.

**Új kulcsok:** `common.clear`, `common.collapseSidebar`, `common.expandSidebar`, `settings.editModel`, `settings.form.apiType`.

**RED:** A statikus kulcs-ellenőrző teszt a fenti öt kulcsot elvárja mindhárom lokalizációban.

**GREEN:** Töltsük fel mindhárom nyelven; az érintett komponensek fallbackjei csak vészhelyzeti kompatibilitási értékek maradjanak vagy szűnjenek meg.

### 7. feladat: kézi UI-elfogadási teszt

**Cél:** A teljes magyar felületet futó alkalmazásban ellenőrizni.

**Lépések:**

1. `npm run build`
2. Indítsuk a szervert: `npm run server -- --home ./runtime --workspace ./workspace --port 3000`
3. Nyissuk meg a Beállításokat, válasszuk a `Magyar` értéket.
4. Frissítsük az oldalt; a magyar választás maradjon meg.
5. Ellenőrizzük: egyszerű/normál mód, oldalsáv, chat üres állapot, Settings, Skills, Jobs, Notebook, Profile, Workspace Browser, QuestionDialog, terminal és office preview feliratok.
6. Nyissunk vagy hozzunk létre ütemezett feladatot; dátum, hét napjai, cron-humánosítás magyarul jelenjen meg.
7. Váltsunk angolra, majd kínaira; ne legyen sérült felirat, hiányzó kulcs vagy konzolhiba.
8. Képernyőolvasó / DevTools alapján ellenőrizzük a `<html lang>` értéket: `hu`, `en`, `zh-CN`.

## 6. V2: magyar Content Hub és pedagógiai lokalizáció

A V1 befejezése után döntés kell arról, hogy a Hub-tartalom is magyar nyelvű legyen-e. Ez nem csak fordítás:

- a K–12 Skill-eket a magyar közoktatási/felsőoktatási célokhoz kell igazítani;
- a magyar ékezetes példák, hivatkozások és dokumentumsablonok validálása kell;
- a modellek számára írt `agent.md` és `SKILL.md` promptok fordítása megváltoztathatja a viselkedést, ezért funkcionális tesztelés kell;
- az upstream kínai/angol tartalom licence és provenance-e minden módosított csomagnál megtartandó.

Javasolt V2 pilot: csak három, magyar intézményi használathoz közeli preset: **Óratervkészítő**, **Tudásmagyarázó**, **PPT-készítő**. Ezekhez készülhet `localized.hu` metadata, magyar `agent.md`, és szükség szerint saját, forkolt Skill-csomag.

## 7. Elfogadási kritériumok

A V1 akkor kész, ha:

- a Settings-ben kínai, angol és magyar UI választható;
- a választás újratöltés után megmarad;
- a három locale JSON kulcshalmaza 100%-ban azonos;
- nincs közvetlen felhasználói kínai szöveg a chat streaming, workspace-preview és beállítási állapotokban;
- dátum/idő magyar UI esetén `hu-HU` szerint formázódik;
- a dokumentum `lang` attribútuma `hu` a magyar felületen;
- `npm run build` sikeres;
- az összes új Vitest teszt zöld;
- angol és kínai regressziós kézi teszten is átmegy.

## 8. Kockázatok és nyitott termékdöntések

1. **UI vs. agentnyelv:** a UI `hu` nem kényszeríti ki, hogy az LLM magyarul válaszoljon. A magyar alapértelmezett agentnyelv külön workspace-/system-prompt beállítás.
2. **Első indulás:** legyen automatikus böngészőnyelv-felismerés, vagy maradjon kínai alapértelmezés? Ajánlás: autodetekció, mentett választás elsőbbségével.
3. **Content Hub:** a vegyes kínai/angol preset- és Skill-címek V1 után is látszanak. Ez nem i18n-hiba, hanem lokális tartalom hiánya.
4. **Terminológia:** a „Workspace”, „Skill”, „Preset”, „Job”, „Notebook” fogalmakhoz az első sprint előtt rövid magyar termszótár kell, hogy ne váltakozzanak a fordítások.
5. **Release:** a repón nincs jelenleg automatikus UI-teszt vagy i18n CI-minőségkapu; ezt a V1 tesztlépésben be kell vezetni.
