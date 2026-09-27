# CPP_04 – Leckeutasítások

## Áttekintés

Időkeret: **3 × 45 perc**.

- 1. blokk: tömbök – `G04_01`…`G04_05`
- 2. blokk: mutatók alapjai – `G04_06`…`G04_08`
- 3. blokk: tömb és mutató kapcsolata – `G04_09`…`G04_10`, záró ellenőrzés

Minden fájlban van egy **A alapfeladat** és egy **B alkalmazási részfeladat**. A starterek csak a szükséges adatokat és minimális programkeretet adják. A tanulási célhoz tartozó indexkifejezést, `for` ciklust, `if` feltételt vagy mutatókifejezést **a hallgató írja meg**.

### Fontos tutor-szabály

A feladatot először **természetes nyelven** add meg. Az alább szereplő pontos szintaxis az ellenőrzésedet szolgálja; **ne add oda elsőre**. Elakadáskor használd a segítségi létrát: fogalmi tipp → analóg egysoros példa → részleges szerkezet → teljes megoldás csak végső esetben.

---

## G04_01 – Első tömb: index és érték

**Fájl:** `G04_01_tomb_alapok.cpp`

### A feladat – így mondd

„Írasd ki külön sorban a tömb első és harmadik elemét. A teljes kiíró utasításokat te írd meg.”

Ne mondd meg elsőre az indexeket. Ha elakad, előbb kérdezd meg: „Milyen indexszel kezdődik egy C++ tömb?”

### B feladat – így mondd

„Írasd ki a tömb utolsó elemét úgy, hogy a megoldás a `meret` változóból számolja ki az utolsó érvényes indexet. Ne írj be közvetlenül konkrét utolsó indexet.”

### Tutor-ellenőrzés – ne add oda elsőre

- első elem: `szamok[0]`
- harmadik elem: `szamok[2]`
- utolsó elem: `szamok[meret - 1]`
- várt értékek: 12, 18, 9

Ne kérj futtatás előtti jóslatot. Tömbhatáron kívüli hozzáférést ne futtassatok.

---

## G04_02 – Tömb elemének módosítása

**Fájl:** `G04_02_tomb_modositas.cpp`

### A feladat

„Írasd ki a második elem jelenlegi értékét, módosítsd 20-ra, majd írasd ki újra.”

A hallgatónak kell kiválasztania a megfelelő indexet és megírnia az értékadást.

### B feladat

„Írasd ki a harmadik elem értékét, majd növeld meg 5-tel úgy, hogy a korábbi értékből számolsz. Ezután írasd ki újra.”

### Tutor-ellenőrzés

- második elem indexe 1, végeredménye 20
- harmadik elem indexe 2, 18 → 23

Megértési kérdés: „Mi változott: az index vagy az adott indexen tárolt érték?”

---

## G04_03 – Tömbbejárás `for` ciklussal

**Fájl:** `G04_03_tomb_bejaras.cpp`

### A feladat

„Írj egy teljes `for` ciklust, amely a tömb elejétől a végéig halad, és minden elemet kiír.”

**Ne diktáld be elsőre a ciklus fejlécét.** Ha elakad, kérdezd sorrendben:

1. Melyik az első érvényes index?
2. Melyik az utolsó érvényes index?
3. Milyen feltétellel maradunk biztosan a tömbön belül?
4. Hogyan lépünk a következő indexre?

### B feladat

„Írj egy második ciklust. Most minden sorban az index és a hozzá tartozó érték is jelenjen meg, például `2 -> 18` formában.”

### Tutor-ellenőrzés

A megfelelő ciklus logikája 0-tól indul, a méretnél kisebb indexekig halad, és egyesével növeli az indexet. Ne add meg ezt teljes `for (...)` sorban, amíg nincs szükség segítségre.

Rövid ellenőrzés: miért veszélyes, ha a ciklus egy lépéssel túlmegy az utolsó érvényes indexen?

---

## G04_04 – Összegzés és átlag

**Fájl:** `G04_04_osszegzes.cpp`

### A feladat

„Az `osszeg` változó már 0-ról indul. Írj **teljes `for` ciklust**, amely végigjárja a tömböt és minden elem értékét hozzáadja az összeghez. A ciklus után írasd ki az eredményt.”

A starterben szándékosan nincs ciklusfejléc és nincs kész összeadó sor.

### B feladat

„Az elkészült összegből és a tömb méretéből számítsd ki az átlagot úgy, hogy tört eredmény is megmaradhasson. Írasd ki az átlagot.”

### Tutor-ellenőrzés

- várt összeg: 50
- várt átlag: 10.0
- szükség esetén emlékeztesd a hallgatót a lebegőpontos osztásra; a konkrét `static_cast` sort ne add oda elsőre

Ne kérj előzetes számtani jóslatot.

---

## G04_05 – Feltételes számlálás két feltétellel

**Fájl:** `G04_05_felteteles_szamlalas.cpp`

### A feladat

„Írj egy teljes tömbbejáró ciklust. A ciklusban egy feltétellel számold meg, hány elem nagyobb 10-nél. A végén írasd ki a darabszámot.”

Ne adj kész ciklust vagy kész `if` feltételt elsőre.

### B feladat

„Ugyanebben a bejárásban vezess egy második számlálást is: hány elem páros? A végén ezt is írasd ki.”

### Tutor-ellenőrzés

- 10-nél nagyobb elemek: 2
- páros elemek: 3 (`12`, `18`, `4`)

Az első blokk végén röviden foglald össze: index, bejárás, összegzés, feltételes számlálás.

---

## G04_06 – Érték, cím és első mutató

**Fájl:** `G04_06_cim_es_mutato.cpp`

### Kötelező magyarázat

A négy kérdés mentén haladj:

1. mi az érték;
2. hol van az érték;
3. mit tárol a mutató;
4. mit kapunk majd dereferáláskor.

A „pointer” elnevezést itt egyszer megemlítheted, utána „mutató”.

### A feladat – így mondd

„Írasd ki a `szam` értékét és memóriacímét. Ezután hozz létre egy `int` értékre mutató mutatót, amely ezt a címet tárolja, és írasd ki a mutatóban tárolt címet is.”

Ne add oda elsőre a `&`-os vagy `int*`-os teljes sort. Fogalmi kérdéssel segíts.

### B feladat

„Állítsd át a már meglévő mutatót a `masikSzam` változóra. Írasd ki a `masikSzam` címét és a mutató új értékét.”

### Tutor-ellenőrzés – ne add oda elsőre

Elvárt fogalmi szerkezet: a címképző operátorral kapjuk meg a címet; az `int*` típusú mutató ezt tárolhatja. A mutató később másik `int` objektum címére is átállítható.

Konkrét hexadecimális címet ne jósoltass.

---

## G04_07 – Dereferálás és módosítás

**Fájl:** `G04_07_dereferalas.cpp`

### A feladat

„Hozz létre egy mutatót, amely a `szam` változóra mutat. A mutatón keresztül olvasd ki az értéket, majd a mutatón keresztül változtasd 99-re. Végül a `szam` változó kiírásával ellenőrizd a módosítást.”

Itt kérj egyetlen rövid jóslatot közvetlenül a mutatón keresztüli módosítás előtt: „Szerinted melyik érték változik meg?”

Csak a konkrét példa után nevezd meg a dereferálást.

### B feladat

„A mutatón keresztül növeld meg az aktuális értéket további 10-zel. Ne a `szam` változót módosítsd közvetlenül.”

### Tutor-ellenőrzés

Várt végső `szam`: 109.

Ha a hallgató a mutatót írja le a dereferálás helyett, pontosítsd: a dereferálás a tárolt címhez tartozó objektum elérése.

---

## G04_08 – `nullptr` és mutató átállítása

**Fájl:** `G04_08_nullptr.cpp`

A starter itt szándékosan megmutatja az új `nullptr` kezdőértéket, de a biztonságos ellenőrzést már a hallgató írja.

### A feladat

„Ellenőrizd, hogy a mutató mutat-e érvényes objektumra, és csak biztonságos esetben olvasd ki a mutatott értéket. Ezután állítsd a mutatót a `szam` változóra, és ismét végezd el az ellenőrzést.”

Itt kérj rövid jóslatot az első ellenőrzés előtt: melyik ág fog futni?

### B feladat

„Állítsd át ugyanazt a mutatót a `masikSzam` változóra, majd ugyanazzal a biztonságos mintával olvasd ki az értéket.”

### Tutor-ellenőrzés

- első állapot: `nullptr`, nem dereferáljuk
- második állapot: 25
- harmadik állapot: 40

Ne kérj `nullptr` dereferálást.

---

## G04_09 – Tömb és mutató kapcsolata

**Fájl:** `G04_09_tomb_es_mutato.cpp`

### A feladat – így mondd

„Írasd ki először a tömb első elemének címét. Egy második kiírásban a `std::cout` jobb oldalára csak a tömb nevét tedd. Ezután hozz létre egy mutatót, amely a tömb első elemére mutat, és írasd ki a benne tárolt címet. Hasonlítsd össze a három eredményt.”

Itt a „csak a tömb nevét” megfogalmazás legyen egyértelmű, mert a korábbi próbában ez okozott elakadást.

### B feladat

„Most a tömb második elemének címét írasd ki kétféleképpen: egyszer közvetlenül az elemből kiindulva, egyszer az első elemre mutató mutatóból egy elemnyit továbblépve.”

### Tutor-ellenőrzés – ne add oda elsőre

- első elem címének két alakja végül ugyanarra a helyre vezet
- a tömb neve ebben a kifejezésben az első elemre mutató értékké alakul
- a mutatóból egy elemmel továbblépve a következő `int` elem címét kapjuk

Magyarázd el: a tömb nem mutató.

---

## G04_10 – Indexelés, mutatós bejárás és összegzés

**Fájl:** `G04_10_mutato_bejaras.cpp`

### A feladat

„Hozz létre egy mutatót a tömb első elemére. A 2-es indexű (harmadik) elemet írasd ki kétféleképpen: egyszer tömbindexeléssel, egyszer a mutatóból kiindulva. Ezután írj egy teljes `for` ciklust, amely a tömböt mutatón keresztül járja be és írja ki. Végül a mutatón keresztül módosítsd a 2-es indexű elemet 100-ra, majd tömbindexeléssel ellenőrizd.”

A kétféle elérés összevetése előtt kérj egy rövid jóslatot: ugyanazt az értéket kell-e kapniuk?

**Ne add meg elsőre** sem a mutatóaritmetikai kifejezést, sem a `for` fejlécet.

### B feladat

„Írj egy újabb teljes ciklust, amely a már módosított tömb elemeit mutatón keresztül éri el, és kiszámítja az összegüket.”

### Tutor-ellenőrzés

- a 2-es indexű elem eredetileg 30
- módosítás után 100
- várt összeg: 220

Egyszerű tömbbejárásnál az indexelés gyakran olvashatóbb; nem cél mindent mutatóval írni.

---

# Kötelező záróteszt

A 10. fájl B részének befejezése után mondd:

**„A CPP_04 programozási feladatsor kötelező része elkészült. Most jön a rövid záróteszt.”**

A kérdéseket a `ZARO_TESZT.md` fájlból **változtatás nélkül, egyenként** tedd fel.
Ne generálj helyettük más kérdéseket.

## T1 – feleletválasztós záróteszt

Helyes válaszok:

1. C
2. B
3. D
4. A
5. C
6. B

Pontozás: 0–6 helyes. Ne alakítsd át százalékos tudásszintté.

Rövid indoklások:

1. Öt elem indexei `0, 1, 2, 3, 4`, ezért az utolsó érvényes index `4`.
2. Az `&szam` a `szam` változó memóriahelyének címét adja.
3. Az `int*` mutató ebben a példában a `szam` címét tárolja.
4. A `*mutato` dereferálással a tárolt címen lévő `int` objektumot éri el.
5. Csak érvényes, nem `nullptr` mutatót dereferálunk.
6. A `mutato = szamok` az első elem címére állítja a mutatót, de a tömb és a mutató
   továbbra is különböző fogalom.

## T2 – kimenetjóslós záróteszt

Kérdésenként mutasd a `ZARO_TESZT.md` megfelelő teljes programját, és várd meg a
hallgató válaszát.

Megoldások:

1. `7 12`
   - A mutató először `a` változóra mutat, ezért `a` értéke 7 lesz.
   - Ezután a mutatót `b` címére állítjuk, és `b` értékét 3-mal növeljük.

2. `30`
   - A `mutato + 2` a 2-es indexű, vagyis harmadik elem címére mutat.
   - A dereferálás ennek értékét adja.

3. `42`
   - A `*(mutato + 1) = 42` a tömb 1-es indexű elemét módosítja.
   - Ez ugyanaz az elem, mint `szamok[1]`.

4. `20`
   - A ciklus mutatón keresztül összeadja: `2 + 4 + 6 + 8`.

5. Két sor:
   - `ures`
   - `8`
   Az első ellenőrzésnél a mutató `nullptr`, ezért az `else` ág fut. Ezután a mutatót
   `szam` címére állítjuk, így a második ellenőrzésnél biztonságosan kiírható a 8.

6. `1 20 3 40`
   - A ciklus csak a páros elemeket módosítja mutatón keresztül.
   - A 2 értéke 20, a 4 értéke 40 lesz; a páratlan elemek változatlanok.

Pontozás: 0–6 helyes. Kisebb formázási eltérést ne tekints hibának, ha az értékek,
sorrend és végrehajtási logika helyes.

A T2 6. kérdése után add meg:

- T1 eredmény: `x/6`
- T2 eredmény: `y/6`

Ezután mondd ki:

**„A CPP_04 kötelező gyakorlat itt véget ért.”**

---

# Adaptív komplex pluszfeladat – K04_01

**Fájl:** `K04_01_plusz.cpp`

A gyakorlat kezdetekor rögzített `gyakorlat_kezdete` és a 12. zárókérdés befejezési ideje alapján számolj teljes eltelt időt.

- **< 90 perc:** ajánld fel a komplex pluszfeladatot;
- **>= 90 perc:** ne ajánld fel és ne említsd;
- megbízható kezdési idő hiányában: ne becsülj, ne ajánld fel automatikusan.

## Komplex feladat

A starter csak a tömböt adja meg. A hallgatónak önállóan kell:

1. mutatót létrehoznia a tömb bejárásához;
2. teljes ciklust írnia;
3. a páros elemeket 2-vel növelnie a mutatón keresztül;
4. a módosítás után összeget számolnia;
5. megszámolnia a 10-nél nagyobb elemeket;
6. index–érték párokat kiírnia;
7. kiírnia az összegzést és a darabszámot.

### Tutor-ellenőrzés

Várt módosított tömb: `3 10 14 5 22 7`.

Várt összeg: **61**.

10-nél nagyobb elemek száma: **2**.

A pluszfeladatnál különösen tartsd a segítségi létrát; ne adj kész ciklust vagy kész megoldást elsőre.

Nincs házi feladat.
