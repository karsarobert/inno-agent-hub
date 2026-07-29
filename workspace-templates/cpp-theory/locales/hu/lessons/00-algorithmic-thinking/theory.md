# 1. lecke — Algoritmikus gondolkodás és az első modern C++ program

> **Cél:** egy hétköznapi problémát pontos feladattá, ellenőrizhető algoritmussá, majd fordítható C++20-programmá alakítani. A lecke végére értsd azt is, milyen modern C++ eszközökkel fogunk később tisztábban és biztonságosabban kódolni.

## Hogyan használd ezt az anyagot?

Ez az elmélet a gyakorlófeladat előtt olvasandó. Nem kell minden felsorolt modern C++ eszközt most azonnal fejből írnod. Az első alkalom **kötelező magja** az algoritmus, a bemenet–feldolgozás–kimenet modell, a `main`, a kiírás, a fordítás és a tesztelés. A későbbi részek előretekintők: megmutatják, hogyan lesznek ugyanezek az alapok nagyobb programokban pontosabbak és kevésbé hibaveszélyesek.

A gyakorlati feladat: `exercises/00-algorithmic-thinking/01-snack-automata.md`.

---

## 1. Mit jelent programozni?

A program nem „utasítások véletlen sora”, hanem egy probléma megoldásának pontos, a gép számára végrehajtható leírása. A gép nem egészíti ki a hiányzó lépéseket, és nem találja ki a szándékunkat. Ezért a programozás elsődleges munkája a gondolkodás és a tervezés; a C++-kód ennek a pontos átírása.

Egy jó algoritmus:

- **véges**: befejeződik;
- **egyértelmű**: minden lépés pontosan értelmezhető;
- **végrehajtható**: minden lépés elvégezhető az adott eszközökkel;
- **helyes**: a megadott bemenetekből a kívánt eredményt adja;
- **ellenőrizhető**: példákkal, szélső esetekkel és nyomkövetéssel vizsgálható.

Példa: „Számold ki a visszajárót” még nem algoritmus. Ahhoz meg kell nevezni a bemenetet (`ar`, `fizetett`), a számítást (`fizetett - ar`), a feltételezést (kezdetben `fizetett >= ar`) és a kívánt kimenetet.

## 2. A bemenet–feldolgozás–kimenet (IPO) modell

Egy kezdő feladatot először ezzel a három kérdéssel bonts fel:

| Rész | Kérdés | Uzsonnaautomata példa |
|---|---|---|
| **Bemenet** | Milyen adatot kap a program? | az uzsonna ára, a fizetett összeg |
| **Feldolgozás** | Mit számít vagy dönt el? | `visszajaro = fizetett - ar` |
| **Kimenet** | Mit közöl a felhasználóval? | `Visszajáró: 350 Ft` |

Az IPO modell azért hasznos, mert megakadályozza a tipikus kezdő hibát: a kódírást akkor kezdjük el, amikor még nem tudjuk, milyen adatból mit kell előállítani.

### Specifikáció

A specifikáció a feladat ellenőrizhető megfogalmazása. Az uzsonnaautomata minimális specifikációja:

- **Bemenet:** két nem negatív egész szám: `ar` és `fizetett`.
- **Előfeltétel:** az első változatban `fizetett >= ar`.
- **Kimenet:** a `fizetett - ar` különbség forintban.
- **Példa:** `650` és `1000` esetén `350`.

A specifikáció nem C++-kód. Mielőtt programoznánk, emberi nyelven is egyértelműnek kell lennie.

## 3. Pszeudokód: híd a gondolat és a C++ között

A pszeudokód nem valódi programnyelv. Rövid, strukturált leírás arról, mit kell tennie a programnak.

```text
OLVASD BE ar
OLVASD BE fizetett
SZÁMÍTSD KI visszajaro = fizetett - ar
ÍRD KI visszajaro
```

Ezzel már ellenőrizhető a logika C++-szintaxis nélkül. Ha a pszeudokód hibás vagy hiányos, a C++-változat is hibás vagy hiányos lesz.

### Nyomkövetés (trace)

A pszeudokód ellenőrzésének egyszerű módja, hogy egy konkrét bemenettel lépésről lépésre végigköveted:

| Lépés | `ar` | `fizetett` | `visszajaro` |
|---|---:|---:|---:|
| beolvasás után | 650 | 1000 | még nincs értéke |
| számítás után | 650 | 1000 | 350 |
| kiírás | 650 | 1000 | 350 Ft jelenik meg |

A „még nincs értéke” fontos megfigyelés: egy változót nem szabad kiolvasni, mielőtt értéket kapott.

## 4. A programfejlesztés kis ciklusa

Kis feladatnál is kövesd ezt a ciklust:

1. **Értsd meg és specifikáld** a feladatot.
2. **Tervezd meg** IPO-val és pszeudokóddal.
3. **Írd meg** a legkisebb működő változatot.
4. **Fordítsd le** figyelmeztetésekkel.
5. **Futtasd** ismert bemenetekkel.
6. **Ellenőrizd** a kimenetet a specifikációhoz képest.
7. **Javíts és egyszerűsíts**, ha kell.

Ne próbáld elsőre az egész, végleges programot megírni. Egy kis, működő részletet könnyebb megérteni, fordítani és tesztelni.

## 5. Az első C++20 program szerkezete

```cpp
#include <iostream>

int main() {
    std::cout << "Szia, C++!\n";
    return 0;
}
```

Soronként:

- `#include <iostream>`: a szabványos be- és kimeneti eszközök deklarációit kéri a fordítótól. Innen érkezik többek közt a `std::cout` és a `std::cin`.
- `int main()`: a program belépési pontja. Amikor az operációs rendszer elindítja a programot, innen kezdődik a végrehajtás.
- `{ ... }`: blokk; a `main` törzse.
- `std::cout`: szabványos kimeneti folyam, általában a terminálra ír.
- `<<`: a kiíró operátor; az utána álló értéket a kimenetre küldi.
- `"Szia, C++!\n"`: szövegliterál. A `\n` új sort kér.
- `return 0;`: sikeres befejezést jelez az operációs rendszernek. A modern C++-ban a `main` végén elhagyható, de kezdő példában láthatóvá teszi a program eredménykódját.

### Bemenet és számítás

```cpp
#include <iostream>

int main() {
    int ar{};
    int fizetett{};

    std::cout << "Add meg az uzsonna árát: ";
    std::cin >> ar;
    std::cout << "Add meg a fizetett összeget: ";
    std::cin >> fizetett;

    const int visszajaro = fizetett - ar;
    std::cout << "Visszajáró: " << visszajaro << " Ft\n";
}
```

- `int` egész szám típus. Ebben a feladatban a forintokat egész számként kezeljük.
- `int ar{};` és `int fizetett{};` kapcsos inicializálással nullára inicializálja a változókat. A későbbi `std::cin` ezeket felülírja.
- `std::cin >> ar;` beolvas egy egész számot a szabványos bemenetről.
- `const int visszajaro = ...;`: a kiszámított érték ezen a néven nem módosítható. Ha egy értéknek a számítás után nem szabad változnia, a `const` ezt a szándékot a fordítónak is jelzi.

> **Miért nincs itt `using namespace std;`?** Mert a `std::` megmutatja, hogy a `cout`, `cin` és más nevek a C++ szabványos névteréből jönnek. Kis oktatási példában működhet nélküle is, projektkódban azonban a `std::` biztonságosabb és egyértelműbb.

## 6. Fordítás, futtatás és a hibák három fajtája

A `.cpp` fájl még forráskód. A fordító alakítja futtatható programmá. A Run gomb a jelenlegi környezetben C++20 módban fordít, a következő lényeges kapcsolókkal:

```text
g++ -std=c++20 -Wall -Wextra -pedantic forras.cpp -o program
```

- `-std=c++20`: C++20 szabályait és könyvtári felületét kéri.
- `-Wall -Wextra`: hasznos figyelmeztetéseket kapcsol be.
- `-pedantic`: jelzi a nem szabványos, kétes konstrukciókat.

Három eltérő hibakategóriát különböztess meg:

1. **Fordítási hiba:** a program nem készül el, például hiányzik egy pontosvessző vagy ismeretlen névre hivatkozol.
2. **Futásidejű hiba:** a program elindul, de futás közben hibás állapotba kerülhet.
3. **Logikai hiba:** a program lefordul és lefut, de rossz eredményt ad. Például véletlenül `ar - fizetett`-et számítasz.

A fordító üzeneténél először a fájlt, a sort és az első valódi hibát keresd. Sok későbbi üzenet csak következmény.

## 7. Tesztelés az első naptól

A teszt nem egyszerűen „elindítom egyszer”. A specifikációból választott bemenetekkel ellenőrzöd a viselkedést.

| Eset | Bemenet (`ar`, `fizetett`) | Elvárt eredmény | Mit ellenőriz? |
|---|---:|---:|---|
| átlagos | 650, 1000 | 350 | az alapképlet helyes-e |
| pontos fizetés | 650, 650 | 0 | nulla különbség kezelése |
| kis összeg | 1, 2 | 1 | nincs rejtett minimumérték |
| még nem támogatott | 650, 500 | negatív eredmény | a következő leckében bevezetendő ellenőrzés szükségessége |

Az utolsó sor nem hiba a jelenlegi specifikációban: azt jelzi, hogy a feladat következő változatához döntésre (`if`) lesz szükség. Ne adj hozzá funkciót csak azért, mert „talán kell”; előbb pontosítsd a specifikációt.

---

# Modern C++ előretekintő — a `C++Programming.pdf` 1. fejezete

A könyv első fejezete a modern C++ magnyelvi eszközeit mutatja be. Ezeket ebben a kurzusban fokozatosan használjuk. Az alábbi összefoglaló minden fejezetbeli témát tartalmazza; a `Most` jelölés azt jelenti, hogy kezdőként már használhatod, a `Később` azt, hogy előbb szükség van változókra, függvényekre vagy osztályokra.

## 8. `auto`: típus következtetése — **Most, mértékkel**

Az `auto` azt kéri a fordítótól, hogy a kezdőértékből következtesse a változó típusát.

```cpp
const auto darab = 3;        // int
const auto ar = 599.0;       // double
```

Az `auto` nem „bármilyen típus”; a típus fordításkor pontosan meghatározott. Akkor jó választás, ha a kezdőérték egyértelmű, vagy ha a tényleges típus hosszú és a név nem ad hozzá érthetőséget. Kezdő adatbeolvasásnál gyakran a kifejezett `int` vagy `double` olvashatóbb.

Figyelem: a kapcsos lista különleges:

```cpp
auto x = {1, 2, 3}; // std::initializer_list<int>
auto y{1};         // C++17-től int
```

## 9. Típusaliasok és alias template-ek — **Később**

A `using` érthető nevet ad egy meglévő típusnak, nem új típust hoz létre.

```cpp
using Forint = int;
using NevLista = std::vector<std::string>;
```

Sablonos aliasnál paraméteres rövidítés készül:

```cpp
template <typename T>
using Szamok = std::vector<T>;
```

Az alias fő értéke a szándék megmutatása: a `Forint` többet mond az olvasónak, mint egy magányos `int`.

## 10. Egységes (kapcsos) inicializálás — **Most**

C++11-től a `{}` többféle típusnál egységesen használható:

```cpp
int darab{42};
double ar{599.0};
std::vector<int> jegyek{4, 5, 5};
```

Előnye, hogy tilt több veszélyes, adatvesztő átalakítást:

```cpp
int egesz{1.5}; // fordítási hiba: 1.5 nem fér el veszteség nélkül int-ben
```

Két fontos kivétel:

- `std::vector<int> v{5};` egyetlen, 5 értékű elemet tartalmaz.
- `std::vector<int> v(5);` öt, alapértékkel inicializált elemet tartalmaz.

A kapcsos inicializálás a listás konstruktort részesíti előnyben, ezért a zárójel és a kapocs nem mindig cserélhető fel.

## 11. Nem statikus adattagok inicializálása — **Később, osztályoknál**

Osztályban az adattagoknak lehet alapértéke, és a konstruktor paraméterből származó tagokat inicializálólistával érdemes létrehozni:

```cpp
class Meres {
    std::string nev{"ismeretlen"};
    int ertek{};

public:
    Meres(std::string uj_nev, int uj_ertek)
        : nev(std::move(uj_nev)), ertek(uj_ertek) {}
};
```

Ez nem ugyanaz, mint előbb alapértelmezetten létrehozni a tagot, majd a konstruktor törzsében értéket adni neki. Az inicializálólista sok típusnál hatékonyabb, és `const` vagy referencia adattagnál szükséges is lehet. A tagok tényleges inicializálási sorrendje a **deklaráció sorrendje**, nem a lista sorrendje.

## 12. Igazítás és igazítás lekérdezése — **Később, alacsony szintű téma**

A memóriában egy objektum címe bizonyos típusoknál meghatározott többszörösre kell essen. Ezt hívjuk igazításnak (alignment). A C++-ban az `alignof(T)` lekérdezi a követelményt, az `alignas(N)` erősebb igazítást kérhet.

```cpp
struct alignas(16) NegyVektor {
    float x, y, z, w;
};

static_assert(alignof(NegyVektor) >= 16);
```

Erre általában speciális hardverközeli, SIMD- vagy bináris interfészhelyzetben van szükség. Kezdő alkalmazáskódban nem optimalizálunk ezzel találomra.

## 13. Hatókörös felsorolások (`enum class`) — **Később, de könnyen használható**

Egy felsorolás véges, névvel ellátott értékkészlet. A modern forma az `enum class`:

```cpp
enum class FizetesiMod { keszpenz, kartya, utalas };

FizetesiMod mod = FizetesiMod::kartya;
```

Előnye, hogy a nevek nem ömlenek ki a környező névtérbe, és nem keverednek észrevétlenül egészekkel. C++20-ban csak tudatosan alakítsd át egész számmá, például `static_cast<int>(mod)`-dal; a könyvben említett `std::to_underlying` C++23-as eszköz.

## 14. `override` és `final` virtuális függvényekhez — **Később, öröklődésnél**

Ha egy származtatott osztály egy virtuális függvényt felülír, az `override` jelzi a fordítónak, hogy ezt szándékoztuk:

```cpp
struct Alakzat {
    virtual double terulet() const = 0;
};

struct Kor final : Alakzat {
    double terulet() const override { return 0.0; }
};
```

Az `override` elkapja a rejtett elírásokat vagy eltérő paraméterlistát. A `final` megtilthatja egy virtuális függvény további felülírását, illetve osztályon a további származtatást. Mindkettő a szándékot dokumentálja és ellenőrizhetővé teszi.

## 15. Tartományalapú `for` ciklus — **Később, gyűjteményeknél**

A range-based `for` elemenként jár be egy tömböt vagy konténert:

```cpp
for (const int jegy : jegyek) {
    std::cout << jegy << '\n';
}
```

Nagyobb vagy összetett elemnél felesleges másolat elkerülésére `const auto&` a jó alapértelmezés:

```cpp
for (const auto& nev : nevek) {
    std::cout << nev << '\n';
}
```

Ha módosítani kell az eredeti elemeket, a `const` elmarad: `for (auto& ertek : ertekek)`.

## 16. Saját típus bejárhatóvá tétele — **Haladó, később**

Egy saját típus akkor használható range-forban, ha a fordító meg tudja találni a `begin()` és `end()` határokat (tagfüggvényként vagy a típus névterében szabad függvényként). Így a saját gyűjteményed ugyanolyan természetesen bejárható, mint a `std::vector`.

A lényeg: a range-for nem „varázslat”; a bejárás elejét és végét használja. Ezt majd iteratoroknál és konténereknél mélyítjük el.

## 17. `explicit` konstruktorok és konverziós operátorok — **Később**

Egy egyparaméteres konstruktor külön jelölés nélkül akaratlan automatikus átalakítást engedhet:

```cpp
class Forint {
public:
    explicit Forint(int ertek) : ertek_(ertek) {}
private:
    int ertek_;
};
```

Az `explicit` miatt a `Forint f = 1000;` nem fordul, viszont `Forint f{1000};` igen. Ez megakadályozza, hogy két fogalmilag különböző dolog észrevétlenül összekeveredjen. Ugyanez az elv a felhasználói konverziós operátorokra is: csak akkor legyen automatikus átalakítás, ha valóban meglepődésmentes.

## 18. Névtelen névterek belső implementációhoz — **Később, több forrásfájlnál**

Egy `.cpp` fájlban a névtelen névtérben lévő név csak abban a fordítási egységben érhető el:

```cpp
namespace {
    int seged_szamitas(int x) { return x * 2; }
}
```

Ez modern C++-ban a fájl-lokális segédek szokásos eszköze a globális `static` helyett. A publikus felületet nem szennyezi, és csökkenti a névütközés esélyét.

## 19. Inline névterek verziózásra — **Haladó, könyvtárfejlesztésnél**

Az inline névtér egy könyvtár API-verzióját rejtheti el úgy, hogy a felhasználónak mégsem kell minden névnél verziót írnia:

```cpp
namespace fizetes {
    inline namespace v1 {
        struct Szamla {};
    }
}

fizetes::Szamla s;
```

Ez nem az `inline` függvénykulcsszó jelentése. Elsősorban nyilvános C++ könyvtárak kompatibilitási kérdése; kezdő alkalmazásban ritkán indokolt.

## 20. Structured binding: több összetartozó érték név szerinti kibontása — **Később**

Ha egy pár, tömb vagy megfelelő struktúrájú érték több részből áll, egy sorban nevezheted el őket:

```cpp
std::pair<std::string, int> meres{"hőmérséklet", 22};
const auto& [nev, ertek] = meres;
```

A `const auto&` itt másolat nélkül, csak olvasásra köti a neveket az eredeti objektum részeihez. Függvény „több értéket ad vissza” helyzetében gyakran `std::pair` vagy `std::tuple` a visszatérési típus, amit structured bindinggel kényelmes fogadni.

## 21. Class template argument deduction (CTAD) — **Később**

Sablonos osztály létrehozásakor a fordító sokszor kitalálja a sablonparamétert a konstruktorargumentumokból:

```cpp
std::pair adat{"alma", 3}; // std::pair<const char*, int> körüli levezetett típus
```

Ez rövidíti a kódot, de az első leckékben a típusok tanulásakor gyakran jobb kiírni a szándékot. Konténereknél is légy óvatos: a kiinduló elemek típusa és a kívánt tárolt típus nem mindig ugyanaz.

## 22. Az indexelő operátor (`operator[]`) — **Később, tömböknél és osztályoknál**

Tömbben vagy `std::vector`-ban indexszel kérsz elemet:

```cpp
std::vector<int> jegyek{4, 5, 3};
const int elso = jegyek[0];
```

Az indexelés nullától indul. A `[]` általában **nem** ellenőrzi a határokat; érvénytelen indexnél hibás működés lehet. Ha ellenőrzött hozzáférés kell, sok konténernél elérhető az `.at(index)`, amely hibát jelez. Saját osztályban az `operator[]` túlterhelésével természetes indexelhető felület készíthető, de azt úgy kell tervezni, hogy a határfeltételek és a módosíthatóság egyértelműek legyenek.

---

## 23. Mit kell tudnod az első gyakorlathoz?

A következőket használd biztosan:

- IPO felbontás;
- rövid pszeudokód;
- `int`, `const`, `std::cin`, `std::cout`;
- kapcsos inicializálás (`int ar{};`);
- fordítás és legalább két célzott teszt;
- annak megfogalmazása, hogy a program miért a `main`-ből indul.

A modern előretekintőből egyelőre elég felismerni: az `auto`, a `{}` inicializálás, a `const`, a `std::` és a range-for később ugyanazt a célt szolgálják: a szándék legyen világos, és a fordító minél több hibát el tudjon kapni.

## 24. Önellőrző kérdések

1. Mi a különbség a specifikáció és a C++-kód között?
2. Melyik három részre bontja a feladatot az IPO modell?
3. Miért írunk pszeudokódot, ha utána úgyis C++-ban programozunk?
4. Mi a különbség fordítási, futásidejű és logikai hiba között?
5. Mit jelent a `const int visszajaro`?
6. Miért eredményez mást a `std::vector<int> v{5};` és a `std::vector<int> v(5);`?
7. Milyen hibát segít elkapni az `override`?
8. Miért lehet célszerű a `const auto&` egy range-for ciklusban?

## 25. Következő lépés

Nyisd meg az `exercises/00-algorithmic-thinking/01-snack-automata.md` feladatot. Először írd le a saját pszeudokódodat, majd készítsd el a C++20-programot. A Run gombbal fordítsd és futtasd; teszteld legalább a `650, 1000` és a `650, 650` bemenetekkel.

## Források és feldolgozási határ

Ez az anyag önálló, magyar nyelvű oktatási összefoglaló; nem helyettesíti és nem idézi hosszasan a forráskönyveket.

- `1. Algoritmikus gondolkodas fejlesztese.pdf`: algoritmusfogalom, specifikáció, tervezés, dokumentálás, ellenőrzés, megvalósítás és tesztelés.
- `2. Bevezetés.pdf`: programfejlesztési lépések, a `main` szerepe, kiírás, olvashatóság, megjegyzések és fokozatos fejlesztés.
- Marius Bancila: *Modern C++ Programming Cookbook*, 3. kiadás, 1. fejezet (*Learning Modern Core Language Features*): `auto`, típusaliasok, kapcsos inicializálás, taginicializálás, igazítás, scoped enum, `override`/`final`, range-for, `explicit`, névterek, structured binding, CTAD és indexelés.
