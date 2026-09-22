# EP_03 – ciklusok és kosaras büfé, saját kódírással

**Teljes, magyar nyelvű Inno Agent-munkatér két 45 perces órára**, az EP_02 felépítését követve. Az EP_03.html fogalmaiból válogatott, egymásra épülő programozási feladatok. Az összes feladatot nem adja ki egyszerre az ágens: előbb magyaráz, kis mintát mutat, majd egy értelmes kódrész megírását kéri. A tanuló szerkeszt, ment, futtat és javít.

## Indítás

1. A ZIP **tartalmát** új, üres Inno Agent-munkatér gyökerébe bontsd ki. Az `agent.md`, a `preset.json` és az `indulas.py` közvetlenül a munkatér gyökerében legyen; ne maradjanak egy plusz EP_03 almappában.
2. A korábbi EP_02 munkatér tanulói fájljait ne írd felül. Ez önálló új csomag, nem javítócsomag.
3. Indíts a munkatérhez kapcsolt beszélgetést, például: „Kezdjük a harmadik gyakorlatot.”
4. A tanuló az `indulas.py` szövegét módosítja, ment, majd a **Futtatás** gombot használja.

Az összes `.py` a munkatér gyökerében van. **A munkatér gyökere és a Python-fájlok mappája így azonos.** Normál induláskor nincs szükség cd parancsra. Ezzel nem ismételjük meg az EP_02 korábbi, almappát kétszer megadó útvonalhibáját. Ha a terminált korábban máshova léptették, a tényleges útvonal alapján kell a munkamappába visszaállni.

A program input-kérdéseire a terminálban válaszoljunk Enterrel. Futó programra ne indítsunk új példányt. Kézi tartalék a gyökérből: `python3 indulas.py`, vagy a tényleges fájlnévvel. Opcionális segéd: `bash futtatas.sh indulas.py`. A segéd a saját gyermekfolyamatának munkakönyvtárát állítja be, **nem** a felület terminálját vagy a Futtatás gomb konfigurációját.

## Mi fér a két órába?

| 1. óra | Perc | 2. óra | Perc |
|---|---:|---|---:|
| E0: első mentett futás | 3 | L1: listaalap és bejárás | 8 |
| W1: while és állapotfrissítés | 8 | B2: kosárösszegző függvény | 9 |
| W2: újrakérő függvény | 9 | C1: blokk, ismeretlen termék, continue | 8 |
| F1: for/range | 7 | B3: saját részek összeépítése, fizetési ciklus | 10 |
| B1: napi összesítő, break | 15 | Z1: önálló termékszámlálás | 7 |
| S1: összegzés | 3 | S2: lezárás | 3 |
| **Összesen** | **45** | **Összesen** | **45** |

A szünet külön idő. A keret tartalmazza a magyarázatot, írást és próbát is. Lassabb haladásnál a pluszpróbák és minden K-feladat kimaradnak; szükség esetén B3 pénzpótlási bővítése folytatásra marad. A tutor a ténylegesen elkészült részt zárja le, nem állít teljesítést a hiányzó kódról. A magyarázatot és a tanulói kódírást időnyerésből sem váltjuk kész megoldásra.

A napi összesítő már kifizetett rendelési összegekkel dolgozik. A kosaras változat előre megadott terméklistát használ. A teljes, vendégneveket is ismételten bekérő alkalmazás K1 kiegészítő; a futás közbeni kosárépítés későbbi tananyag. A szeletelés, a ciklus-else és a turtle külön gyakorlás.

## Az 1.0.1-es változat módosítása

C1 külön `blokk.py` fájlba került: a blokk kiírása után a program véget ér. B3-ban kerül elő a `bufe_03.py`, ahová a tanuló a saját kész blokkfüggvényét viszi át a kezdő definíció helyére. A munkalap, a tutorutasítások és a próbák ezt a két lépést követik; az időkeret változatlan.

Új kipróbáláshoz új munkateret használj. Korábbi EP_03-munkatérben a tanuló már megírt Python-fájljait ne írd felül a kezdőmintákkal.

## A fájlok szerepe

- `agent.md`: tutorviselkedés, bemutatkozás, tanítási ritmus, tanulói szerkesztés, értékelés.
- `tanulo_lap.md`: főút, részletes instrukciók és rövid analóg minták.
- `tutor_utmutato.md`: fogalmi magyarázatok, hibakeresési támpontok, időkezelés.
- `ellenorzo_esetek.md`: előírt és választható próbák, elvárt viselkedés.
- `zaro_feladatok.md`: Z1 önálló programozási feladat.
- `tovabbi_gyakorlas.md`: K1–K6 kiegészítők a 90 percen túl.
- `memoria_utmutato.md`: haladás az engedélyezett tanulói memóriában, fájlírás nélkül.
- Kilenc `.py`: futtatható kiinduló minták, amelyekből a tanuló készít megoldást.
- `EP_03.html`: változatlan részletes tananyag, színezett kódokkal és szemléltetőkkel.
- `feladatok.json`, `verzio.json`: helyi tartalmi metaadatok; nem új alkalmazáskonfigurációs kulcsok.
- `preset.json`: az EP_02 mintáját követő kártyaleírás. A csomag nem kerül fel automatikusan a hubra.
- `futtatas.sh`: opcionális kézi futtatási segéd.

A HTML-ben szereplő teljes program tanulási referencia, nem bemásolandó feladatmegoldás. A munkalap saját célkódot és módosítást kér. Nincs külön, elrejtett kész megoldókulcs vagy automatikus pontozó a tanulói csomagban.

## Haladás a kódszerkesztő megszakítása nélkül

A tutor nem ír haladas.md-t vagy más munkatéri naplófájlt. Az elérhető és engedélyezett L1 memória tanulási eseményeit használja. A vizsgált Inno Agent-kódban az L1-hez **kikapcsolt Simple Mode és engedélyezett L1** szükséges. Ha ez nem elérhető, a tanítás folytatódik; a folytatási pont a beszélgetésben marad. A csomag nem állít át memóriabeállításokat automatikusan.

A memóriamentés nem garantált pusztán attól, hogy egy eszköz neve látszik. A tutor ellenőrzi a sikerjelzést, és elkülöníti a saját maga által olvasott kódot a tanuló által közölt futási eredménytől. A megadott próbaadat nem elvégzett próba.

## Oktatói induló próba

A tanulói próba új munkatérben történjen. A „kezdjük” után magyar bemutatkozást, a büfé folytatásának rövid áttekintését és egy konkrét szerkesztési feladatot várunk. Ellenőrizd, hogy az ágens nem írja és nem futtatja a tanuló kódját, nem nyitogat haladási Markdown-fájlt, és nem adja oda azonnal a feladat kész megoldását. A tényleges tutorviselkedés az alkalmazásban használt modelltől is függ; a csomag tartalmi és kódellenőrzése nem helyettesíti ezt a rövid órai próbát.

## Források és ellenőrzött integráció

- A csomag közvetlen tartalmi alapja az EP_03.html, az előző csomag szerkezeti alapja az EP_02_innoagent.zip.
- [SZTE – Python 3. gyakorlat](https://okt.inf.szte.hu/progalap-py/gyakorlat/gyak03/), illetve Kégl Tímea: Snake it easy 1., 3. fejezet; részletes hivatkozások a HTML végén.
- [Inno Agent futtatási parancs](https://github.com/karsarobert/inno-agent/blob/main/apps/inno-agent/web/src/utils/run-command.ts): Python esetén a forrásfájl relatív útvonalát használja.
- [Tanulói memóriaeszközök](https://github.com/karsarobert/inno-agent/blob/main/apps/inno-agent/src/memory/learner/learner-tools.ts) és [memóriakapcsolók](https://github.com/karsarobert/inno-agent/blob/main/apps/inno-agent/src/agent/inno-extension.ts).

A futtatási és memóriarészeket a csomag készítésekor, 2026-09-21-én elérhető forrás alapján ellenőriztük. Nem kerültek a presetbe kitalált memória- vagy terminálbeállítások.
