# CPP_05 – Leckeutasítások

## Áttekintés

Időkeret: **3 × 45 perc**.

- 1. blokk: függvények alapjai – `G05_01`…`G05_04`
- 2. blokk: projekt – `P05_meresi_adatok.cpp`, P1…P7
- 3. blokk: ZH-felkészítő – 20 előre rögzített kérdés

A hallgató kódol. A tutor minden új projektrész előtt rövid mintát mutat és
elmagyaráz, de nem írja meg automatikusan a projekt megoldását.

---

# 1. blokk – függvények alapjai

## G05_01 – Első saját függvény

**Fájl:** `G05_01_elso_fuggveny.cpp`

### A feladat

A hallgató készítsen `negyzet` nevű függvényt, amely egy egész számot kap és
visszaadja annak négyzetét. A `main()`-ben a meglévő `ertek` változóval hívja meg,
majd írja ki az eredményt.

**Várt eredmény:** 36.

Ne add oda elsőre a teljes `int negyzet(int szam)` fejlécet. Ha szükséges, a
függvény részeit külön idéztesd fel: visszatérési típus, név, paraméter, `return`.

### B feladat

Készítsen `dupla` nevű függvényt, amely egy egész szám kétszeresét adja vissza.
Hívja meg ugyanazzal az `ertek` argumentummal.

**Várt eredmény:** 12.

Rövid megértési kérdés: melyik név a paraméter, és melyik változó az argumentum a hívásban?

---

## G05_02 – Több paraméter

**Fájl:** `G05_02_parameterek.cpp`

### A feladat

Készítsen `teglalapTerulet` nevű `double` függvényt, amely két `double` paraméterből
kiszámítja a téglalap területét.

**Várt eredmény:** 13.5.

### B feladat

Készítsen `teglalapKerulet` függvényt ugyanazzal a két paraméterrel.

**Várt eredmény:** 15.

A futás után emeld ki, hogy ugyanazokat az argumentumokat két külön részfeladatot
végző függvény kapja meg.

---

## G05_03 – `void` eljárás

**Fájl:** `G05_03_void.cpp`

### A feladat

Készítsen paraméter nélküli `fejlecKiirasa` nevű `void` függvényt, amely például
kiírja:

```text
=== MERESI EREDMENYEK ===
```

### B feladat

Készítsen `meresKiirasa` nevű `void` függvényt, amely egy egész paramétert kap és
`Meres: <ertek>` formában kiírja.

A blokkban egyszer kérdezd meg: miért nem használható a `fejlecKiirasa()` hívás
egy `int eredmeny = ...` értékadás jobb oldalán? Várt gondolat: `void` nem ad vissza
értéket.

---

## G05_04 – Prototípus

**Fájl:** `G05_04_prototipus.cpp`

A fájlban az `osszead` definíciója szándékosan a `main()` után áll.

### A feladat

1. A hallgató írjon hívást a `main()`-be az `osszead(a, b)` eredményének kiírására.
2. Fordítsa le. A fordító a hívás helyén még nem ismeri az `osszead` függvényt.
3. A definíciót hagyja a `main()` után, és oldja meg a problémát függvényprototípussal.

**Várt eredmény a javítás után:** 11.

### B feladat

A hallgató készítsen a `main()` után egy `kulonbseg` definíciót és a `main()` elé
hozzá prototípust, majd írja ki `a - b` eredményét.

**Várt eredmény:** 5.

### Kötelező magyarázat

A prototípus akkor hasznos, amikor:

- a függvény definícióját a `main()` után szeretnénk tartani;
- a program elején gyorsan át akarjuk látni, milyen műveletek hívhatók;
- később több forrás- és fejlécfájlra bontjuk a programot;
- a fordító már a hívás helyén ellenőrizheti a visszatérési és paramétertípusokat.

A prototípus nem a függvény végrehajtása és nem helyettesíti a definíciót.

---

# 2. blokk – projekt: Mérési adatok elemzője

**Fájl:** `P05_meresi_adatok.cpp`

Minden lépés előtt mutasd a megjelölt mintát a `MINTAKODOK.md` alapján.
A mintát 2–5 mondatban értelmezd, majd kérd a projektváltozat elkészítését.

A projektben a hallgató minden függvényhez prototípust készít a `main()` előtt,
a definíciókat pedig a `main()` után tartja. Ezzel a G05_04-ben tanult szerkezetet
azonnal alkalmazza.

## P1 – `adatokKiirasa`

**Minta:** M2.

Mutasd be az M2 `pontokKiirasa` példát. Magyarázd el:

- `void`: nincs visszatérési érték;
- `const int*`: a függvény a tömb elemeit olvassa, nem módosítja;
- a méret külön paraméter;
- a ciklus az indexen keresztül éri el az elemeket.

Ezután a hallgató készítsen a projekthez `adatokKiirasa` függvényt és hívja meg a
`main()`-ből.

**Várt adatsor:** 18 24 11 29 21 17.

## P2 – `osszeg`

**Minta:** M3.

Mutasd be az M3 összegző mintát, külön kiemelve az akkumulátor 0 kezdőértékét,
a ciklust és a `return` szerepét.

A hallgató készítsen `osszeg` függvényt a projekthez.

**Várt eredmény:** 120.

## P3 – `atlag`

**Minta:** M4, majd szükség esetén idézd fel az M3 mintát.

Az `atlag` függvény **ne írjon új összegző ciklust**. Hívja meg a projekt saját
`osszeg` függvényét, és abból számítsa az átlagot. Az eredmény `double` legyen.

A tört rész megőrzéséhez szükség esetén mutass analóg példát `static_cast<double>`
használatára, de ne írd meg rögtön a projekt teljes return sorát.

**Várt eredmény:** 20.

Kötelező rövid magyarázat: egy saját függvény meghívhat egy másik saját függvényt;
ez csökkentheti a kódismétlést.

## P4 – `maximum`

**Minta:** M5.

A hallgató készítsen `maximum` függvényt. Feltételezhető, hogy `meret > 0`.
A kezdeti maximum legyen a tömb első eleme; a bejárás a következő elemtől indulhat.

**Várt eredmény:** 29.

## P5 – `kuszobFelettiDarab`

**Minta:** M6.

A projektfüggvény paraméterei:

- adatok;
- elemszám;
- küszöb.

Szigorúan a küszöbnél nagyobb értékeket számolja.

**Várt eredmény 20-as küszöbnél:** 3.

A minta `>=` feltételt használ, a projekt viszont **`>`** feltételt kér. Hívd fel
erre a figyelmet, de a konkrét `if` sort a hallgató írja meg.

## P6 – `novel`

**Minta:** M7.

A hallgató készítsen `novel` nevű `void` függvényt egy `int*` paraméterrel. A
függvény a mutatott egész értéket növelje 1-gyel.

Hívás előtt kérj egyetlen rövid jóslatot: az eredeti `riasztasiKuszob` változik-e?
Ezután hívja meg a `riasztasiKuszob` címével.

**Várt új küszöb:** 21.  
**Várt darabszám 21 felett:** 2.

Kapcsold össze a korábbi leckével: érték szerinti `int` paraméter esetén másolatot
kapnánk; a cím átadásával a függvény eléri az eredeti változót.

## P7 – `tavolsag`

**Minta:** M8.

A hallgató készítsen `tavolsag(double x, double y)` függvényt, amely a `<cmath>`
`sqrt` függvényét használja. A `using namespace std;` miatt itt `sqrt(...)` írható;
a teljes név `std::sqrt`.

**Várt eredmény `3.0`, `4.0` esetén:** 5.

A végén röviden foglald össze a projekt szerkezetét: prototípusok → `main()` →
függvénydefiníciók; a `main()` szervez, a függvények részfeladatokat oldanak meg.

---

# 3. blokk – ZH-felkészítő teszt

A kérdéseket a `ZARO_TESZT.md` fájlból, változtatás nélkül, egyenként tedd fel.

## T1 megoldókulcs

1. B – a függvények csökkenthetik a kódismétlést és szétválasztják a részfeladatokat.
2. A – paraméter a definícióban szereplő bemeneti változó.
3. C – argumentum a híváskor átadott konkrét érték/kifejezés.
4. B – a `return` értéket ad vissza és befejezi az adott hívást.
5. A – `void` esetén nincs visszatérési érték.
6. C – egyszerű értéktípusnál másolat készül a paraméterbe.
7. A – a prototípus előre ismerteti a függvény felületét a fordítóval.
8. B – a lokális változó a saját hatókörében látható.
9. B – az include és a using külön feladatot végez.
10. C – a `<cmath>` matematikai függvények deklarációit adja.

## T2 megoldókulcs

### T2/1
`14`

Indoklás: `dupla(4)=8`, `dupla(3)=6`, összesen 14.

### T2/2
`10`

Indoklás: a `modosit` `szam` paramétere másolat; az eredeti `ertek` nem változik.

### T2/3
`25`

Indoklás: `3*3 + 4*4 = 9 + 16 = 25`.

### T2/4
`20`

Indoklás: `2 + 5 + 3 + 10 = 20`.

### T2/5
`6`

Indoklás: a függvény megkapja `x` címét és a mutatott eredeti értéket növeli.

### T2/6
Fő probléma: az `osszead` hívásakor még nincs ismert deklaráció. Legkisebb javítás:
`int osszead(int a, int b);` prototípus a `main()` elé, vagy a teljes definíció
áthelyezése a `main()` elé. Elsődleges várt válasz a prototípus.

### T2/7
A függvény `void`, ezért nem adhat vissza `a + b` értéket. Javítás lehet az
`int osszead(...)` visszatérési típus, vagy ha valóban `void` kell, ne adjon vissza
értéket és más módon használja az eredményt. A kérdéshez az `int`-re javítás a
legkézenfekvőbb.

### T2/8
A `terulet` két paramétert vár, de a hívás csak egy argumentumot ad. A hívásnak két
megfelelő argumentumot kell átadnia.

### T2/9
A `<= meret` miatt `i == meret` esetén `adatok[meret]` elérése történik, ami már a
tömbön kívül van. A biztonságos feltétel itt `i < meret`.

### T2/10
A `cout` az `std` névtérben van. Javítás: `std::cout`, vagy a fájlban megfelelő
`using namespace std;` / `using std::cout;` használata. A kurzusban a
`using namespace std;` mintát használjuk.

## Tesztértékelés

- T1: 10 pont.
- T2: 10 pont.
- Minden kérdés 1 pont; az első érdemi válasz számít.
- A hibakeresésnél fogadd el a szakmailag egyenértékű helyes javítást.
- A végén csak a tényleges hibák alapján nevezz meg ismétlendő témákat.

Javasolt témacímkék:

- függvény részei / paraméter és argumentum;
- `return` és `void`;
- érték szerinti paraméterátadás;
- prototípus és fordítási sorrend;
- lokális hatókör;
- névtér és fejlécek;
- ciklushatárok és tömbök;
- mutatóval végzett módosítás;
- saját függvények egymásból hívása.
