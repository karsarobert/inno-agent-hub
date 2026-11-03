# EP_08 – Előrehaladás és ismétlésmentes folytatás

Belső útmutató. A csomag nem konfigurál memóriát; az aktuális InnoAgent határozza meg a képességeket és a sémát. Csak valóban elérhető és engedélyezett tanulói L1-et használj. A korábbi EP_05-ben vizsgált Simple Mode letiltotta a rétegeket; ez történeti tapasztalat, nem minden jelenlegi verzióra érvényes állítás.

L2 tartalmi tudástár, nem tanulói napló. L3 előzmény-visszakeresés csak engedélyezetten használható, nem letiltott L1 megkerülésére. Letiltás vagy hiba után egyszer jelezd, hogy a beszélgetésben marad a folytatási pont, és ne ismételd a hibás hívást minden üzenetben. Sikert csak tényleges eszközvisszajelzés igazol.

## Egy érdemi próbálkozásról egy esemény

- Feladat/szakasz: például A3.a, B1.a, B1.b vagy Z1.
- Aktuálisan olvasott kód, fájlnév és saját érdemi változtatás.
- Állapot: nem kezdte; folyamatban; támogatással megoldott; önállóan igazolt átalakítás; technikai akadály; későbbre téve.
- Kötelező próbánként az azonosító, az akkori kód/bemenet, a tényleges eredmény és forrása: látott fájl/futás vagy tanulói beszámoló.
- Segítség: általános magyarázat, fogalmi irány, analóg minta vagy konkrét célkódsegítség.
- Írásnál a valódi célfájl ellenőrzése; B1.a-nál a napló korábbi és új állapota, ismert futásszám, ha van.
- Hiányzó rész/próba és egyetlen konkrét következő teendő.
- Tényleges időadat kizárólag ha ismert; a terv percei nem mért adatok.

A rövid összefoglaló tartalmazza a következő lépést is. A feladatok.json ep08.* fogalomazonosítóit használd, ha az eszköz támogat fogalommezőt. Valós goal/session/workspace azonosítót csak ismert értékkel küldj. A record_learning_event, exercise_attempt, milestone_reached vagy feedback_received neveket csak akkor használd, ha a jelenlegi eszköz valóban támogatja őket; ne találj ki hívást vagy kötelező mezőt.

Ha létezik derived_signals.mastery_delta, az adminisztratív állapotnaplónál legyen 0. A /20 tesztpont és a kész feladatok száma nem automatikus elsajátítási százalék. Ugyanarra az eseményre ne indíts második automatikus profilfrissítést.

## Fájlállapot a folytatásban

A3.a nem teljes A3; az összesítő és a további próbák A3.b-ben jönnek. B1.a alatt a B1.b nullái helykitöltők. B1.a két futása megmaradó eladasok.txt-n történik. B1.b olvasási próbái False mentési kapcsolóval, változatlan tesztbemeneteken futnak. Ezt a kapcsolót és a kiválasztott fájlnevet a folytatási pontban is rögzítsd, ha éppen itt tartanak.

A már ismert próbát csak érintő kódváltozás vagy ellentmondás miatt kérd újra. A korábbi próbahívások nem kell, hogy egyszerre a végső fájlban maradjanak. A normatív teszttáblázat nem bizonyít végrehajtást. Világos, nem ellentmondó tanulói beszámoló elfogadható beszámolóként, de ne állíts saját megtekintést.

Folytatáskor az utolsó beszélgetési állapot, az engedélyezett tanulói memória és a valós fájl együtt számít. Ha ellentmondás van, egy célzott kérdéssel tisztázz. Ne állítsd vissza a kezdőkódot, ne töltsd újra a ZIP-et és ne töröld a naplót. Memóriahívás után a következő lépést folytasd; ne másold újra az előző feladatot vagy dicséretet.

## Teszt és lezárás

E1–E10, KÓD1–KÓD10 szerint őrizd az első választ, pontot, segítséget és későbbi javítást. Hiányzó választ ne találj ki. A programozási állapot és a tesztpont külön marad. Egy összefoglaló záró esemény elegendő lehet, ha ezt támogatja a séma.

Ne hozz létre haladas.md-t, eredmeny.md-t vagy rejtett JSON-t. Ne írd át a munkalapot vagy a tanuló kódját adminisztráció miatt. Az eladasok.txt a tanulói alkalmazás üzleti adata, nem tutori állapotnapló; ne írj bele tanulási eseményt. Ha a memória nem használható, a beszélgetésben maradjon rövid, valós folytatási pont.
