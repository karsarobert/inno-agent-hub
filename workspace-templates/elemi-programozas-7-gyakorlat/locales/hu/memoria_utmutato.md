# EP_07 – Tanulói előrehaladás és folytatási pont

Belső útmutató. Az EP_05 módszertanát követi: a tanuló kódját nem váltja fel automatikusan megnyíló Markdown-napló. A memória képességét és sémáját az aktuális alkalmazás határozza meg, a csomag nem konfigurálja.

## Elérhetőség

Csak ténylegesen elérhető és engedélyezett tanulói L1-memóriát használj. A korábbi EP_05 útmutató szerint a vizsgált Inno Agent-verzióban a Simple Mode letiltotta a memóriarétegeket; ez történeti támpont, nem állítás minden jelenlegi telepítésről. A tényleges állapotot és a visszajelzést vedd figyelembe. A beállítás oktatói feladat, a tutor ne módosítsa automatikusan.

L2 tartalmi tudástár, nem tanulói napló. L3 engedélyezett előzmény-visszakeresés segíthet a folytatásban, de nem a letiltott L1 megkerülésére való. Hiba vagy tiltás után egyszer jelezd, hogy a beszélgetésben őrzitek a folytatási pontot; a hibás hívást ne ismételd minden üzenetben.

## Mit őrizz meg?

Egy érdemi, összetartozó próbálkozásról egy esemény elegendő. A korábbi csomagban használt record_learning_event, exercise_attempt, milestone_reached és feedback_received neveket csak akkor használd, ha az aktuális eszköz ténylegesen támogatja őket. Ne találj ki új eszközt vagy kötelező sémamezőt.

- Feladat és szakasz: például A3.b vagy B1.a.
- Ténylegesen olvasott fájl és a tanuló saját módosítása.
- Állapot: nem kezdte; folyamatban; támogatással megoldott; önállóan igazolt átalakítás; technikai akadály; későbbre téve.
- Próbánként azonosító, akkori bemenet/kódváltozat, tényleges eredmény és a bizonyíték forrása.
- Segítség szintje: általános magyarázat, fogalmi irány, analóg minta, konkrét célkódsegítség.
- Hiányzó próba vagy rész, és egyetlen konkrét következő teendő.
- Tényleges indulási/hátralévő idő, kizárólag ha ismert; a tervezett percek nem mért időadatok.

A topic vagy rövid összefoglaló tartalmazza a következő lépést is, mert a rendszer lehet, hogy ezt emeli be később. Fogalomazonosítóként a feladatok.json ep07.* értékeit használd. Valós goal/session/workspace azonosítót csak ismert értékkel küldj, ne találj ki.

Ha az aktuális eszköz támogatja a derived_signals.mastery_delta mezőt, az adminisztratív állapotnaplóhoz legyen 0. A /20 tesztpont és a kész feladatok száma nem automatikus elsajátítási százalék. A record_learning_event mellett ugyanarra az eseményre ne küldj automatikusan második profilfrissítést; külön profiljavítás csak valóban új diagnózis esetén indokolt.

## Bizonyíték és ismétlés

Külön kezeld az olvasott aktuális kódot, a látott azonosítható futást és a tanulói beszámolót. A normatív eredmény nem elvégzett futás. A tanuló világos, nem ellentmondó beszámolója elfogadható beszámolóként, de ne mondd rá, hogy magad nézted meg.

A már igazolt próbát csak érintő kódváltozás vagy ellentmondás esetén kérd ismét. A végső fájlban nem kell egyszerre megmaradnia minden korábbi próbahívásnak. A3.a, A3.b részleges készültsége nem teljes A3; B1.a és B1.b külön állapot. B1.b.2 ugyanazon halmaz két egymást követő hívása, nem két új programfutás.

Folytatáskor a beszélgetés utolsó állapota, az elérhető tanulói kontextus és a valós fájl együtt számít. Ha hiányos, egy célzott kérdéssel tisztázz, például: „A B1.a eredetmegőrzési próbái már megvoltak, vagy még a másolat készítésénél tartottál?” Ne állíts vissza kezdőkódot. Memóriaeszköz után a következő lépést folytasd, ne ismételd az előző feladatot vagy dicséretet.

## Záró teszt és lezárás

E1–E10 és KÓD1–KÓD10 szerint tartsd számon az első választ, pontját, segítségét és későbbi javítását. A hiányzó választ ne minősítsd sikeresnek. A programozási munka állapotát és a tesztpontot külön őrizd. Egy összefoglaló esemény elegendő lehet az eszköz tényleges sémájában.

Sikert csak az eszköz visszajelzése alapján állíts. Disabled vagy hiba esetén nem történt sikeres mentés. Ne hozz létre haladas.md-t, eredmeny.md-t, rejtett JSON-t vagy más adminisztrációs fájlt. Ne módosítsd a munkalapot és a tanuló kódját naplózási célból. A beszélgetésben mindig legyen rövid, valós folytatási pont.
