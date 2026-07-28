---
name: storm-research
category: Kutatás és információkeresés
description: >-
  Forrásalapú, nyomon követhető mély kutatás. Többnézőpontú kérdésfelvetés + valós
  online keresés + kötelező hivatkozás, amely wikipédia-stílusú teljes kutatási
  jelentést állít elő. Akkor aktiválódik, ha a felhasználó azt mondja: „mély
  kutatás", „kutass után X témának", „írj egy forrásolt áttekintést",
  „több szemszögből vizsgáld".
---

# Többnézőpontú, keresésalapú mély kutatás

A kutatás szűk keresztmetszete nem a „megírás", hanem a „kérdésfelvetés". Ha a témát egyenesen a modellre bízzuk, csak a mainstream keretek átlagos válaszát kapjuk. Ez a módszer azt parancsolja a modellnek, hogy úgy dolgozzon, mint egy PhD-hallgató az előzetes kutatás során: **több, egymással szembenálló nézőpontból kérdez + minden választ valós kereséssel alapoz meg + minden mondatot vissza lehet vezetni forráshoz**.

A módszertan elveit lásd `reference/methodology.md`.

## Három pillér (egy hiánya is degenerálja)

1. **Több nézőpont (Multi-perspective)** — a különböző nézőpontok teremtik a kérdések szélességét és mélységét; a nézőpontok közötti feszültség olyan dolgokat tár fel, amelyeket egyetlen keret nem lát
2. **Keresésalapúság (Retrieval)** — minden válasznak a keresőeszközök által visszahozott valós tartalmon kell alapulnia; forrás hiányában egyértelműen visszautasítja a válaszadást, sosem talál ki
3. **Kötelező hivatkozás (Citation)** — a szövegben minden állításhoz inline `[n]`, a végén valós URL-ek

**Vörös vonal: a keresés átugrása után már nem kutatás, hanem egy modell, amely több szerepet játszva magában beszél — közös vakfoltjaik vannak, és magabiztosan együtt hallucinálnak. Inkább lassú, mint forrás nélküli.**

## Végrehajtási folyamat (Step 0 + 8 lépés)

Ezt a folyamatot egy információ-finomító folyamatnak tekintsd. Először egy egyszeri Step 0 képességfelderítés, majd fokozatosan 8 lépés; az egyes lépések prompt-magjai a `prompts/` alatt találhatók.

### Láthatósági szerződés (kötelező betartani, különben a folyamat fekete dobozzá válik)

Ennek a módszernek az értéke fele-fele arányban a következtetésben és a **folyzat utólagos ellenőrizhetőségében** rejlik: a felhasználónak látnia kell, milyen nézőpontokat állítottál be, mit kérdeztél, és honnan származik minden állítás. Ezért **minden ismeretszerzési lépés (Step 0–5) befejezése után előbb egy tömör checkpointot mutass a felhasználónak, és csak utána lépj tovább** — nem végzel el mindent, hogy aztán egyszerre adjad át.

- **A checkpoint legyen rövid, áttekintő, fix formátumú**, nem pedig naplószerű. A cél: „a felhasználó 5 másodperc alatt megértse, mit állított elő ez a lépés", nem pedig minden közbülső gondolat kiköreztetése.
- **Nem számít, ha a nézőpontokat/kérdéseket csak egy al-ügynök promptjába ágyazod**. Step 1 és 2 termékeit előbb kifejezetten ki kell adni a felhasználónak, és csak azután lehet erre építeni a keresést.
- **Al-ügynök keresésre való felhatalmazásakor előbb mondd el a felhasználónak, melyik ügynök melyik nézőpontot / kérdéscsoportot kapja** — ne váljon a „4 párhuzamos ügynök" a felhasználó számára érthetetlen fekete dobozzá.
- A szintézis fázis (Step 6–8) közvetlenül a végleges jelentésben is megjelenhet (a vázlat → szöveg → önteszt-jelentés amúgy is termék), nem kell külön checkpoint.

Minden lépés checkpoint-formája:

| Lépés | Kötelezően látható checkpoint |
|-------|------------------------------|
| Step 0 | Felderített keresési képességek listája (eszköz/skill/ügynök, prioritással) |
| Step 1 | Nézőpont-lista: `nézőpont neve — egy mondatos fókusz`, benne a fedő nézőpont |
| Step 2 | Nézőpontonkénti kérdéslista (szembenálló nézőpontok 2–3 mély kérdés; fedő nézőpont témabontási listája) |
| Step 3 | Keresési felosztás + hivatkozási tábla vázlata: melyik ügynök/eszköz melyik kérdéscsomagot keresi; visszatérés után `[n]→{url,cím,eszköz}` tábla |
| Step 4 | Nem külön álló kimenet, beolvad a hivatkozási táblába és a későbbi írásba |
| Step 5 | Ellentmondás-térkép: vitapontok, felek álláspontjai, egyező tételek, vakfoltok |

> Egy mondatos fegyelem: **A felhasználónak a végleges jelentés előtt már látnia kell a nézőpontokat, kérdéseket, keresési felosztást és az ellentmondás-térképet.** Ha nem látja, ez a lépés nem készült el rendesen.

### Step 0 — Keresési képességfelderítés (a kutatás kezdete előtt, egyszeri) (lásd `prompts/00_findsearchtools.md`)

A hivatalos kutatás előtt egyszeri környezetfelfedezés: **felderíti és listázza az összes elérhető keresési képességet**, a teljes folyamat során újrahasználva. Témafüggetlen, csak egyszer kerül sor rá.

> ⚠️ **Alapszabály: a memóriára hagyatkozás kötelezően kihagy. Ténylegesen végig kell járni, tételeként szűrni — nem kategória-alapú asszociáció alapján.**

- **Három típusú keresési eszköz felfedezése, prioritás: keresés > kutatás** (a storm lényegében research, a keresőtípusok a magok, a kutatóskill-ek kiegészítők): ① kereső/lekérdező **eszközök** ② kereső/kutató típusú **skill-ek** ③ kereső/kutató típusú **al-ügynökök**.
- **Leírást nézz, nem könyvtárnevet**: a skill-nél a `name`+`description`, az ügynöknél a `description`+`tools` mezőt olvasd, **csak a leírás mezőben szűrj** keresési/kutatási kulcsszavakra (a teljes szöveges grep zajt termel); gépi előszűrés után egyenként pontosan ítélj. Al-ügynök döntése: `tools` tartalmaz WebSearch/WebFetch vagy ezzel egyenértékű eszközt, vagy a feladat megemlíti a „kutatás/research/keresés" szót → felvesszük (pl. content-researcher / research-analyst / general-purpose) — ha a beépített eszközök falba ütköznek, ez a legerősebb keresési út.
- **Platformfüggetlen**: kompatibilis Claude Code / Codex / OpenClaw / Hermes / Cursor / Cline / Gemini / OpenCode stb. platformokkal. A platformonkénti skill/ügynök elhelyezés más és más, **a módszer nem változik, csak a könyvtár** (lásd a 00 lépés útvonaltábláját); csak azt vedd fel, amit a jelenlegi runtime ténylegesen meg tud hívni; ha nincs rá lehetőség, jelöld „nem teljesen bejárva".
- **Széles szűrés**: általános keresés / letöltés / területi keresés (jog·tudományos·dokumentum…) / kutató típusú skill / kereső al-ügynök / parancssori közvetett csatorna (curl·gh) / engedélyköteles eszközök.
- **Kizárni helyi/privát területet**: az az eszköz, amely csak helyi memóriát, helyi kódot, privát felhőt/csevegést keres, nem számít keresésalapú képességnek (alapozás csak „külső nyilvános forrás visszahozható").
- **Téma szerinti prioritás**: a szűk területi keresőeszköz előnyben részesítendő, az általános keresés kiegészítőként szolgál.
- **Korai hiba**: ha bejárás után nincs egyetlen keresési csatorna sem, azonnal mondd meg a felhasználónak, hogy „nem lehetséges forrásalapú kutatás", és ne pazarold a későbbi lépéseket.

### 1. fázis: Ismeretszerzés (a módszer lelke)

**Step 1 — Nézőpont-felfedezés** (lásd `prompts/01_personas.md`)
- A téma köré 3–5 **differenciált kutatói persona** generálása (pl.: frontvonal-gyakorló / szkeptikus / pénzügyi nyomkövető gazdasági nézőpont / történelmi mintákat ismerő történelmi nézőpont / kutatásokat olvasó akadémiai nézőpont).
- Még egy **fedő nézőpont (alapértelmezetten kötelező)**: állásfoglalás nélküli, felel a szisztematikus témabontásért (query decomposition), felsorolja a tématípus összes szabványos tématerületét, az alapvető teljesség biztosításáért.
- Minden persona mellé egy mondatos fókuszleírás.
- **Két szélességi vonal párhuzamosan**: az egymással szembenálló nézőpontok a „mély + keretek közötti" lefedettséget biztosítják, a fedő nézőpont a „mechanikus teljességet" (a tartalomkutatás kimerítő erősségét hálóként beépíti).
- ⚠️ **Előbb a nézőpontlistát add ki a felhasználónak, csak utána lépj Step 2-be**. Nem maradhat csak a fejedben, és nem dugul közvetlenül az ügynök promptjába.

**Step 2 — Nézőponti kérdésfelvetés** (lásd `prompts/02_question.md`)
- Szembenálló nézőpontok: négyzetenként 2–3 **mély kérdés**, egyszerre egy, mind mélyebbre ásó utánkövetéssel.
- Fedő nézőpont: **témabontási mód** — a szabványos tématerületek (definíció/mechanizmus/bizonyíték/biztonság/adagolás/hasonló típusok összehasonlítása/szabályozás…) kimerítő, kereshető kérdésekké bontása, amelyek a keresési folyamatba beolvadnak a szembenálló nézőpontok kérdéseivel együtt.
- Ezek a kérdések határozzák meg a kutatás szélességét és mélységét — ez a rendszer legkritikusabb lépése.
- ⚠️ **Előbb „nézőpontonként → kérdéslistáját" add ki a felhasználónak, csak utána lépj Step 3 keresésbe**. Ez az egész módszer lelke; elrejteni egyenlő a nem elvégezve.

**Step 3 — Kérdés → keresőkifejezés → valós keresés** (lásd `prompts/03_query.md`)
- Minden kérdés 1–3 keresőkifejezéssé alakítása („mit írnál be a keresőbe, hogy megválaszold ezt?").
- A **Step 0-ban felderített képességlistával** keress (ne itt fedezd fel újra az eszközöket).

- Ha több keresési képesség van, **a lehető leg többet párhuzamosan hívd meg**, több forráson keresztül keresztellenőrizve, a lefedettséget bővítve.
- **Ha egy keresőeszköz üresen/hibával tér vissza, ne állj meg**: azonnal válts a következő eszközre, vagy ismert, hiteles domainekre (PubMed, hivatalos oldalak, Wikipédia stb.) közvetlenül letöltő eszközzel keress szöveget tartalékként.
- Degradációs létra: beépített keresőeszközök → kereső típusú MCP/skill → keresőképes al-ügynök (researcher/content-research stb.) kiküldése a keresés helyett → böngészőautomatizáció tartalékként → ha egyik sincs, őszintén mondd el, hogy nem lehet forrásalapozást végezni.
- Minden visszahozott forrást sorszámozz, és rögzítsd az URL-t, címet, kulcs-snippetet, forrás-eszközt. Építs egy `[sorszám] → {url, cím, snippet, eszköz}` hivatkozási táblát, amelyet végig karbantartasz.
- ⚠️ **Al-ügynök kiküldése előtt mondd el a felhasználónak a keresési felosztást** (melyik ügynök / eszköz melyik kérdéscsomagért / nézőpontért felel); a keresés visszatérése után mutasd meg a hivatkozási tábla vázlatát. Ne legyen a párhuzamos keresés fekete doboz.

**Step 4 — Keresésalapú válaszadás (hallucináció-ellenállás)** (lásd `prompts/04_answer.md`)
- A Step 3-ban visszahozott információkra támaszkodva válaszolj, **minden mondatnak forrásalátámasztásúnak kell lennie**.
- Ha az információ nem elegendő, írd egyértelműen: „a meglévő információ alapján nem válaszolható meg", és határozd meg a rést. **A modell memóriájával kitölteni tilos**.

### 2. fázis: Szintézis és rendszerezés

**Step 5 — Ellentmondás-térkép / hiányfelfedezés** (lásd `prompts/05_contradiction.md`)
- Nézőpontok közötti szakértői vitapontok keresése: hol csapnak össze a nézőpontok, és miért.
- Amiben mindenki egyetért, nagy valószínűséggel igaz; amit senki nem említ, az a terület vakfoltja/lehetősége.
- Ez a lépés emeli a „felszíni megértést" „valódi megértéssé"; a legtöbben átugorják.

**Step 6 — Kétlépéses vázlat** (lásd `prompts/06_outline.md`)
- Először a már ismert adatokra támaszkodva írj egy vázlatpiszkozatot, majd a gyűjtött beszélgetések/információk alapján finomítsd részletesebb vázlattá.
- Hasznj `#` `##` `###` hierarchiát; nem tartalmazza magát a témanevet; nincs külön bevezető/következtető fejezet.
- **Téma-teljesség ellenőrzése**: a fedő nézőpont szabványos témalistájával szemben pontonként ellenőrizd, hiányzik-e alapvető téma a vázlatból; ha hiányzik, egészítsd ki kereséssel vagy jelöld hiányként; a fejből kitalálni tilos.

### 3. fázis: Írás és önteszt

**Step 7 — Hivatkozott írás** (lásd `prompts/07_write.md`)
- Fejezetenként haladj; minden fejezetben előbb a fejezet címével keresd ki a hivatkozási tábla vonatkozó tételeit.
- Inline `[n]` hivatkozás, ahol n a Step 3 hivatkozási tábla valódi URL-jére mutat.
- Ne írj külön introduction / conclusion fejezetet (a befejezés után egy összefoglaló bekezdés vezeti a szöveget).
- A befejezés után adj egy `# Összefoglaló` bevezető bekezdést (≤4 bekezdés: téma, háttér, miért fontos, fő vitapontok).

**Step 8 — Saját szakértői ellenőrzés** (lásd `prompts/08_review.md`)
- Rendszerszerű gyengeség: maga a folyamat nem bírálja önmagát, forrástorzítás és tényités-elrendezés keveredhet be. Ezt a lépés kifejezetten pótolja.
- Pontozd a saját kutatásodat: erős érvek / gyenge érvek / lehetséges torzítás / hiányzó szempontok / egyes források megbízhatósága.
- Távolítsd el az ismétlődő tartalmat, tartsd meg a hivatkozásokat és a szerkezetet.

## Termékek

Egy teljes markdown kutatási jelentés, amely tartalmazza:
1. `# Összefoglaló` bevezető bekezdés
2. Több nézőpont által lefedett szöveg, minden állításban `[n]` inline hivatkozással
3. `## Ellentmondás-analízis` — szakértői viták és területi hiányok
4. `## Források` — a sorszámokhoz tartozó valódi URL-lista
5. `## Önteszt-jelentés` — erős/gyenge érvek, torzítások, hiányzó szempontok, megbízhatósági értékelés

## Fontos elvek

- **A keresés nem hagyható el**: minden nézőpont válaszának valós forrással kell rendelkeznie. Ez a research és a persona-prompting közötti határvonal.
- **Őszinte határozás**: ha a keresés nem hoz eredményt, mondd meg. A jelentésben válaszd szét a „forrásalátámasztott" és a „feltételezett" állításokat.
- **Vigyázz a mainstreameken kívül**: ez a módszer lényegében az internetes mainstream vélemények szintézise, a ritka/nem-konszenzusos témáknál hajlamos a középszerűségbe süllyedni. Ilyen téma esetén az önteszt-jelentésben külön jelezd: „Ez a jelentés a mainstream keretek felé hajlik, és lehetséges, hogy nem konvencionális nézőpontokat hagy ki."
- **A módszertan elveit** lásd `reference/methodology.md`.
