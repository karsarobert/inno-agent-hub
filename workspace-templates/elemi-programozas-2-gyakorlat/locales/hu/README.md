# EP_02 – függvények és feltételek, saját kódírással

**Két 45 perces óra, az EP_01 folytatása.** Az Inno Agentben az `agent.md` vezeti a magyarázó tutort. A hallgató a [tanulói munkalap](tanulo_lap.md) alapján írja, menti és futtatja a Python-kódot. A tutor magyarázatot, rövid mintát és javítási támpontot ad, a megoldásfájlokat nem szerkeszti a hallgató helyett.

## Órai menet

| Első óra | Perc | Második óra | Perc |
|---|---:|---|---:|
| E0 – munkakörnyezet és Futtatás gomb | 5 | D1 – kedvezmény, fizetés, if–else | 12 |
| F1 – saját köszöntő függvény | 10 | D2 – kategóriák, if–elif–else | 7 |
| F2 – paraméterek és return | 15 | B2 – a büfé összeépítése | 16 |
| B1 – számoló függvények a büfében | 12 | Z1 – önálló kódírás | 7 |
| S1 – összegzés, folytatási pont | 3 | S2 – összegzés, lezárás | 3 |
| **Összesen** | **45** | **Összesen** | **45** |

A köztes szünet nem része a 90 percnek. A számok tervezési keretek. Ha az első óra elhúzódik, a D2 önálló kategorizálását későbbre lehet tenni; az `elif` fogalmát ilyenkor még nem tekintjük teljesítettnek. A magyarázatot és a hallgató kódírását nem váltjuk ki kész megoldás bemásolásával az idő kedvéért.

A [további gyakorlás](tovabbi_gyakorlas.md) alapértékei, összetett adatellenőrzése és párosságfeladata külön folytatás; ezek nem férnek bele automatikusan a fenti 90 percbe. Az [EP_02.html](EP_02.html) részletes referencia, megtartott színes kódokkal. Nem kell mind a 32 példáját és 16 kérdését feldolgozni ezen az órán. A HTML-ben megmaradt jóslási részek helyett az innoagentes gyakorlaton a munkalap kódírásos lépéseit használjuk. A HTML kész programja tanulási forrás, a munkalap célja viszont a saját változat megírása.

## Fájlok és indítás

Minden Python-fájl a `python_gyakorlat/` mappában van. Ezek **működő kiinduló minták, nem kész feladatmegoldások**. A `bufe_02.py` ugyanabban a fájlban fejlődik B1-től B2-ig. Nem tartalmaz előre megírt függvényes vagy kedvezményes megoldást.

1. Nyisd meg a `python_gyakorlat/koszontes.py` fájlt.
2. Módosítsd és mentsd a megnyitott fájlt.
3. Nyomd meg a **Futtatás / Run** gombot. Előtte nem kell belépni a `python_gyakorlat` mappába: a gomb a munkatérhez viszonyított fájlútvonalat használja.

A terminál maradjon a munkatér gyökerében; a szokásos indításhoz nincs szükség kézi könyvtárváltásra vagy kötelező `pwd`/`ls` vizsgálatra. Ha egy korábbi utasítás miatt a közvetlen `python_gyakorlat` almappában áll, és a Run-hiba megkettőzi ezt az útvonalrészt, egyszer `cd ..` után használd újra a gombot. A Run nem garantálja a kézzel elállított munkakönyvtár automatikus helyreállítását.

Kézi tartalék a munkatér gyökeréből: `python3 python_gyakorlat/koszontes.py`. A gomb jelenlegi alapértelmezett parancsa `python`; ha ez hiányzik, a `python3` tartalék használható. A csomag gyökeréből a `bash ./futtatas.sh koszontes.py`, a gyakorlómappából a `bash ../futtatas.sh koszontes.py` is működik. A segéd nem módosítja a szülőterminál mappáját vagy a gomb beállítását. Inputra váró programnál a választ a terminálba írd; ne indíts második példányt.

## Telepítés és a csomag szerepei

A ZIP tartalmát új, üres Inno Agent-munkatérbe bontsd ki az almappákkal együtt. A ZIP gyökerében van az `agent.md` és a `preset.json`, ugyanúgy, mint az EP_01 csomagban. Az EP_01 munkatér tanulói fájljait ne írd felül. A ZIP-et helyi használatra készítettük; a hubra nem kerül fel automatikusan.

- `agent.md`: a tutor szerepe, kommunikációja és a tanulói kódírás szabályai.
- `tutor_utmutato.md`: a lépések magyarázatai, segítségnyújtás és időkezelés.
- `tanulo_lap.md`: a fő útvonal instrukciói és módosítandó mintái.
- `ellenorzo_esetek.md`: konkrét bemenetek és elvárt eredmények a saját futásokhoz.
- `zaro_feladatok.md`: rövid önálló kódírás.
- `haladas.md`: változatlan, választható kézi lap. A tutor alapértelmezésben az L1 memóriába rögzít; ezt a fájlt nem nyitja meg és nem írja át automatikusan.
- `tovabbi_gyakorlas.md`: időn kívüli kiegészítők.
- `feladatok.json`, `verzio.json`: a csomag tartalmi jegyzéke és verziója; nem új Inno Agent-alkalmazásbeállítások.
- `preset.json`: az EP_01 alapján megtartott szerkezetű kártyaleírás.

Nincs automatikus tesztfuttató vagy rejtett teljes megoldókulcs a tanulói csomagban. Az ellenőrzés célja a kód és a tényleges futás összevetése, nem a kiírt szám visszaküldése. Az agent a tényleges fájlt olvassa, szükség esetén a tanulótól kéri el a hiányzó részletet. Nem módosítja automatikusan a tanuló kódját.


## 1.0.1 – célzott javítás a kipróbálás alapján

Csak a Run/munkakönyvtár utasításai és a haladás tárolási helye változott. A Python-minták, a feladatsor, a 2 × 45 perces időterv, az EP_02.html és a haladási lap tartalma megmaradt.

A haladás helye az **L1 tanulói profil és eseménynapló**. Az agent a `record_learning_event` eszközt használja, amely a profilt is frissíti. A folytatási összegzésben megmarad a feladat, fájl, állapot, próba, segítség és következő lépés. Az L2 wiki tananyag tárolására való, az L3 a korábbi beszélgetések visszakeresését támogatja; egyik sem új munkatérbeli haladási fájl.

**Beállítási feltétel:** a jelenlegi forrás szerint Egyszerű módban az L1 memória le van tiltva, akkor is, ha a memória beállításai között korábban engedélyezve volt. A tartós L1-rögzítéshez az Egyszerű mód legyen kikapcsolva, az L1 tanulói memória pedig engedélyezve. Ezeket a csomag nem kapcsolja át automatikusan. Kikapcsolt vagy hibás memória esetén a tutor rövid chat-összegzést ad, nem állít sikeres mentést és nem kezd helyette Markdown-lapot írni. A tesztbeszélgetésben látható eszköznevek önmagukban nem bizonyítják a mentést; az eszköz eredménye is számít.

**Meglévő munkatér frissítése:** a javító ZIP csak a megváltozott útmutatókat és verzióadatokat tartalmazza. Ezeket másold a meglévő EP_02-munkatér gyökerébe, a megfelelő nevű fájlok helyére. A saját `.py` megoldásokat, az EP_02.html-t és a kitöltött `haladas.md`-t ne cseréld le. Az új utasítás a korábbi, téves könyvtárváltási és automatikus lapírási instrukciókat felülírja; a tanuló munkáját nem kell újrakezdeni.

Források, ellenőrizve a `3e08cdfbbbd9568591f5d8abff32184e3d5ea9ab` forrásállapothoz kapcsolódóan:

- [Memóriarétegek áttekintése](https://github.com/karsarobert/inno-agent/blob/main/README.md)
- [L1 eszközök és paramétereik](https://github.com/karsarobert/inno-agent/blob/main/apps/inno-agent/src/memory/learner/learner-tools.ts)
- [Profil és eseménynapló tárolása](https://github.com/karsarobert/inno-agent/blob/main/apps/inno-agent/src/memory/learner/profile-store.ts)
- [Memóriarétegek engedélyezése és a tanulói kontextus betöltése](https://github.com/karsarobert/inno-agent/blob/main/apps/inno-agent/src/agent/inno-extension.ts)
- [A Run gomb parancsképzése](https://github.com/karsarobert/inno-agent/blob/main/apps/inno-agent/web/src/utils/run-command.ts)
