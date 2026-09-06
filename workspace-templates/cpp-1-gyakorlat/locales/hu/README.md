# C++ alapok – magyar hallgatói gyakorlócsomag

A csomag a javított **CPP_01.html – C++ alapok** órai anyaghoz tartozik.
A teljes programok adottak. Először olvasd és értelmezd őket, majd fordítsd le,
futtasd, és végezd el a pontosan megadott, kis változtatásokat.
Nem kell előzetes programozási tudás vagy önálló programírás.

## Ajánlott sorrend

A korábbi fájlneveket megtartottuk, ezért a nevükben szereplő számok nem az
ajánlott feldolgozási sorrendet jelzik. A makrós példák kiegészítő feladatok.

| Sorrend | Fájl | Kapcsolódó órai témák |
|---|---|---|
| 1. Alapgyakorlat | `L01_elso_program.cpp` | Első program; mentés, fordítás és futtatás; fordítási hiba |
| 2. Alapgyakorlat | `L01b_valtozok_es_ertekek.cpp` | Inicializálás, értékadás, egész és lebegőpontos osztás, egyszerű elágazás |
| 3. Alapgyakorlat | `L04_io_string_hibakes.cpp` | Beolvasás, bemenetellenőrzés, szövegek, indexelés és konverzió |
| 4. Kiegészítő gyakorlat | `L02_preprocesszor_makro.cpp` | Előfeldolgozás, `#include`, `#define`, `-E`, `constexpr` |
| 5. Kiegészítő gyakorlat | `L03_felteteles_makro.cpp` | Feltételes fordítás, `-D`, paraméteres makrók, `assert` |

A gyakorlat lépéseit a tanulást segítő asszisztens adja meg. Először egy
kérdést vagy megfigyelési feladatot kapsz, utána kipróbálod a példát, és
megbeszélitek a tapasztalatot. A programokat nem szükséges újragépelni.
A csomagban található oktatói Markdown-fájlokat nem kell előre elolvasnod;
a gyakorláshoz a fenti forrásfájlokat nyisd meg.

Ha négy, egyenként 45 perces blokk áll rendelkezésre, az elsőben az 1–2.,
a másodikban a 3. alapgyakorlat dolgozható fel. A további blokkokban az alapok
ismétlése vagy a két kiegészítő gyakorlat következhet, az előrehaladástól függően.
A makrók ismerete nem feltétele az alapgyakorlatok megértésének.

## Előkészítés és futtatás

1. Csomagold ki a ZIP-fájlt. A forrásfájlokat a kicsomagolt munkaterület
   gyökérkönyvtárában tartsd, ne hozz létre hozzájuk almappát.
2. Nyiss terminált ebben a könyvtárban. Az számít, hogy a terminál aktuális
   könyvtára hol van; a terminálablak képernyőn elfoglalt helye nem számít.
3. A parancsok Linuxra és parancssorból elérhető, C++20-at támogató GCC-re
   készültek. A `g++ --version` paranccsal ellenőrizheted a fordító elérhetőségét.
4. Módosítás után mentsd a forrást, majd fordítsd újra. Csak sikeres fordítás
   után futtasd az elkészült programot.

Az első program konkrét parancsai:

```bash
g++ -std=c++20 -Wall -Wextra -pedantic -o L01 L01_elso_program.cpp
./L01
```

A `-std=c++20` kiválasztja a nyelvi szabványt; a `-Wall` és a `-Wextra` sok
hasznos figyelmeztetést bekapcsol, de nem az összeset. A `-pedantic` a
kiválasztott ISO nyelvi szabványtól való egyes eltéréseket jelzi.
A `-o L01` az elkészülő futtatható fájl nevét adja meg. A `./L01` futtatja azt.

A fordítás önmagában nem írja ki a program üzeneteit. Ha a fordítás sikertelen,
egy régebbi futtatható fájl még megmaradhat: annak elindítása nem az új kódot
próbálja ki.

## Nyelv és karakterek

A magyarázatok és a megjegyzések magyarul, ékezetekkel szerepelnek. A programok
kiírt üzenetei és az azonosítók magyar szavakat használnak, jellemzően ékezet
nélkül, az órai kódpéldákhoz igazodva. A `DEBUG`, `NDEBUG` és `SQUARE` makróneveket
az órai példákkal való összevetéshez megtartottuk.

A `std::string` hosszát nem nevezzük általánosan betűszámnak. A `size()` a tárolt
`char` elemek számát adja; UTF-8 szövegnél egy ékezetes betű több bájtból is állhat.
A karakterenkénti megfigyelésekhez először ékezet nélküli mintákat használj.

## Hosszú fájlok megtekintése

Az előfeldolgozás eredménye a beillesztett fejlécek miatt hosszú lehet.
A kiegészítő gyakorlatban a saját programunk a fájl végén található, ezért
a létrehozás után elég az utolsó húsz sort megnézni:

```bash
g++ -std=c++20 -E L02_preprocesszor_makro.cpp -o L02_elofeldolgozott.ii
tail -n 20 L02_elofeldolgozott.ii
```

A második parancsot az első sikeres végrehajtása után használd. A `tail` csak
megjeleníti a fájl végét, nem módosítja azt. Nem kell a teljes fájlt megnyitnod
vagy bemásolnod a beszélgetésbe.
