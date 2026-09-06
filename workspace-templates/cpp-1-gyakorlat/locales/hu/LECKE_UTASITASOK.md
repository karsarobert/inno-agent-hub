# C++ alapok – belső foglalkozási forgatókönyv

Ez a fájl az asszisztensnek és az oktatónak szól. A hallgató a feladatokat
beszélgetésben kapja; ne hivatkozz erre a fájlra vagy a belső lépésazonosítókra.
Olvasd el a teljes aktuális leckét és a tényleges forrást, mielőtt elkezded.

## A lépések használata

**Bemutatás:** magyarázat és megfigyelés; a várt eredmény előre megmutatható.
**Ellenőrző kérdés:** a kód, a bemenet és egy kérdés közlése után várd meg a
választ. A „Válasz után” részt addig ne idézd, még kommentként vagy tippként sem.
Ezek a magyarázatok az oktatónak előre rendelkezésére állnak, a hallgatóhoz
viszont csak a megfelelő pillanatban kerüljenek.

Az ellenőrző kérdés után értékeld a választ, tisztázd a várható működést, majd
add ki a próbát. A végrehajtást csak megfigyelés vagy hallgatói megerősítés után
jelöld késznek. Minden módosítás után legyen mentés és újrafordítás; sikertelen
fordítás után ne futtass régi binárist az új kód ellenőrzéseként.
A kiinduló működés bemutatása után ne kérdezd vissza előrejelzésként az éppen
megmutatott eredményt. Használd a következő változtatást vagy az indoklást.

A kimeneti blokkok a szabványos kimenetet mutatják; a hallgató által begépelt
válaszok és a külön megjelölt hibakimenet nem részei ezeknek. A részleteket
külön jelöljük. A források az órai CPP_01.html példáihoz igazodnak.

## 1. Alapgyakorlat – Az első program

**Forrás:** `L01_elso_program.cpp`. Kapcsolódó órai fejezetek: 1–2. és 9.

### A1 – Ellenőrző kérdés: első kiírás

Mutasd meg a main függvény törzsét az eredményt magyarázó komment nélkül.
Kérdés: „Milyen szöveget vársz a program futtatásakor?” Várd meg a választ.

**Válasz után:** A cout a szabványos kimeneti folyam; a << operátorral írunk
bele. A '\n' újsorkarakter. A return 0; sikeres befejezést jelez, nem ír ki nullát.
A std:: előtag az std névteret jelöli. A #include az előfeldolgozáshoz tartozik,
a main a belépési pont; ezek szerepét szükség szerint, röviden magyarázd.

A próbát két lépésben vezesd: először fordítás, annak eredménye után futtatás.

```bash
g++ -std=c++20 -Wall -Wextra -pedantic -o L01 L01_elso_program.cpp
```

```bash
./L01
```

Várható kimenet:

```text
Hello, vilag!
```

A csendes fordítás szokásos, de a siker alapja a sikeres parancsvégrehajtás.
A -o L01 az elkészülő futtatható fájl nevét adja meg. Ezt ne kérdezd meg újra,
ha a hallgató már pontosan elmondta.

### A2 – Ellenőrző kérdés: mentés és újrafordítás

Eredeti sor:

```cpp
std::cout << "Hello, vilag!" << '\n';
```

Új sor:

```cpp
std::cout << "Szia, vilag!" << '\n';
```

Kérdés: „Melyik szöveg jelenik meg, ha a módosítást elmented, de újrafordítás
nélkül indítod el a korábbi L01 programot?” Várd meg a választ.

**Válasz után:** A korábbi program Hello, vilag! szöveget ír. A mentés a
forrásfájlt módosítja, a futtatható fájlt az új fordítás készíti el.

**Próba:** végezze el a sorcserét, mentsen, és futtassa a korábbi ./L01 programot.
A tapasztalat után fordítsa újra az A1 parancsával, majd futtassa: ekkor Szia,
vilag! jelenik meg. Mindkét futtatásról legyen visszajelzés. Ez a lépés nem
tekinthető elvégzettnek attól, hogy csak elmagyaráztuk.

### A3 – Ellenőrző kérdés: egy pontosvessző hiánya

A működő kiíró sor végéről vegyük el a pontosvesszőt:

```cpp
std::cout << "Szia, vilag!" << '\n'
```

Kérdés: „A fordításkor vagy a program futása közben jelentkezik a probléma?”
Várd meg a választ.

**Válasz után:** Fordítási hibát várunk, mert az utasítás lezárása hiányzik.
A hallgató csak az itt megjelölt pontosvesszőt törölje; ne válasszon másik helyet.

**Próba:** mentés és fordítás. Kérd az első hibaüzenetet. Az üzenet megjelölheti
a következő return sort is; a pontos szöveg környezetfüggő. Nem készült új,
sikeresen lefordított program; a régi futtatható fájl ettől még megmaradhat.

**Visszaállítás:** pontosvessző vissza, szöveg újra Hello, vilag!, mentés,
fordítás és futtatás. A1–A3 akkor kész, ha a két változtatás és a visszaállítás
is megerősített, vagy a hallgató valamelyik lépést kifejezetten kihagyta.

## 2. Alapgyakorlat – Változók és értékek

**Forrás:** `L01b_valtozok_es_ertekek.cpp`. Kapcsolódó fejezetek: 3–4.

### B1 – Bemutatás: inicializálás és értékadás

A forrás alapján magyarázd el: inicializáláskor a változó kezdőértéket kap;
értékadáskor a már létező változó értékét módosítjuk. A constexpr itt típussal
rendelkező, fordításkor kiértékelhető állandót jelöl.

```bash
g++ -std=c++20 -Wall -Wextra -pedantic -o L01b L01b_valtozok_es_ertekek.cpp
./L01b
```

A teljes kiinduló kimenet:

```text
Darabszam: 4
Korabban kiszamitott osszeg: 750
Ujraszamitott osszeg: 1000
Egesz osztas eredmenye: 2
Lebegopontos osztas eredmenye: 2.5
A darabszam legalabb 4.
```

Az osszeg először 3 * 250 értékét tárolja. A darab = 4; ezt nem módosítja;
csak az újabb osszeg = darab * egysegar; ad neki új értéket.
Az if a bool változó igazságértéke alapján választ ágat. Az osztás magyarázatát
hagyd a B3 lépésre, ha most nincs rá kérdés. Ne terheld a bemutatást sok párhuzamos kérdéssel.

### B2 – Ellenőrző kérdés: darabszám módosítása

Eredeti sor: `darab = 4;`. Új sor: `darab = 2;`.
Kérdés: „Mennyi lesz az újraszámított összeg?” Várd meg a választ.

**Válasz után:** Az újraszámított összeg 500. Ezután szükség esetén külön
kérdésként vizsgáld meg a korábban kiszámított összeget: az 750 marad.
Az 500 választ ne minősítsd tévesnek, amikor az újraszámított összeget kérdezted.

**Próba:** sorcsere, mentés, a B1 szerinti fordítás és futtatás. Darabszám: 2;
korábbi összeg: 750; új összeg: 500; az osztási sorok változatlanok; az utolsó
sor: A darabszam kisebb 4-nel. A próba után állítsa vissza a darab = 4; sort.
A visszaállítást erősítsétek meg a következő változtatás előtt.

### B3 – Bemutatás, majd ellenőrző kérdés: az osztás típusa

Először magyarázd el a kiinduló példát: 5 / 2 esetén mindkét operandus int,
ezért az eredmény int típusú 2. Ebből lesz a double változó 2.0 értéke.
A std::cout alapértelmezés szerint itt 2-t ír ki, nem kötelezően 2.0-t.
Az 5.0 / 2 lebegőpontos osztás, eredménye 2.5.

Ezután kérj indoklást, ne a már megmutatott számokat kérdezd vissza:
„Miért nem lesz az 5 / 2 eredménye 2.5 attól, hogy double változóba tesszük?”
Várd meg a választ.

**Válasz után:** Az osztás az operandusok típusa szerint történik, az eredmény
csak utána alakul double-lé. Ha ezt önállóan elmondta, nincs szükség újabb hosszú magyarázatra.

**Vezetett próba:** az eredeti sort

```cpp
double egesz_osztas = 5 / 2;
```

cserélje erre:

```cpp
double egesz_osztas = 5.0 / 2;
```

Mentés, fordítás és futtatás után ennél a kiírásnál is 2.5 látszik. A kiírás
címkéje a kiinduló példára utal, ezért a próba után állítsa vissza az eredeti
sort, majd fordítsa le és futtassa a programot. A B2 és B3 változtatásai is a
lecke részei; ne zárd le B1 után.

## 3. Alapgyakorlat – Beolvasás és szövegek

**Forrás:** `L04_io_string_hibakes.cpp`. Kapcsolódó fejezetek: 4–9.

### C1 – Bemutatás: kiinduló működés

```bash
g++ -std=c++20 -Wall -Wextra -pedantic -o L04 L04_io_string_hibakes.cpp
./L04
```

A név kérdésére Anna, az életkor kérdésére 19 a bemenet; mindkettőt Enter zárja.
A teljes szabványos kimenet:

```text
Add meg a teljes neved:
Add meg az eletkorod egesz szamkent:
Szia, Anna!
A nevben tarolt char elemek szama: 4
Jovore 20 eves leszel.
A kor valtozo erteke: 19
Eletkor szovegkent: 19
Korabban kiolvasott karakter: m
Modositott szoveg: aleafa
A modositott szoveg hossza: 6
```

A kérdések a hozzájuk tartozó bemenet előtt jelennek meg. A kor + 1 nem
módosítja a kor értékét. A to_string számból szöveget készít. A teljes kimenet
helyett egy adott kérdéshez csak a szükséges, részletként jelölt sorokat mutasd.

### C2 – Ellenőrző kérdés: teljes név

Változatlan kód, név: Kiss Anna, életkor: 19.
Kérdés: „Hány char elemet tárol ez a név?” Várd meg a választ.

**Válasz után:** Kilencet; a szóköz is beleszámít. A getline a teljes sort
beolvassa; az újsorkaraktert beolvassa, de nem tárolja a névben.

**Próba:** új futtatás, kódmódosítás nélkül. Üdvözlés: Szia, Kiss Anna!;
a tárolt char elemek száma 9. Elég e két sor megerősítése.

### C3 – Ellenőrző kérdés: a beolvasás módjának cseréje

Eredeti sor:

```cpp
std::getline(std::cin, nev);
```

Új sor:

```cpp
std::cin >> nev;
```

Kérdés: „Mi történik az életkor beolvasásakor, ha névként Kiss Anna sort adunk meg?”
Várd meg a választ; előtte ne mondd el, mi marad a bemenetben.

**Válasz után:** A fordítás sikeres. A nev csak Kiss lesz, az Anna a bemenetben
marad. Az életkort kérő üzenet még megjelenik, de a következő beolvasás az Anna
szöveget próbálja egész számként értelmezni; új életkor begépelésére nem vár.

**Próba:** sorcsere, mentés, fordítás, futtatás. Csak a Kiss Anna nevet kell
begépelni. Az életkorra vonatkozó kérdés után ez a hibakimenet várható:

```text
Hiba: az eletkort nem sikerult egesz szamkent beolvasni.
```

A >> alapértelmezés szerint kihagyja a kezdő whitespace karaktereket, és
szövegbeolvasáskor a következő whitespace karakternél áll meg. Whitespace
például a szóköz, a tabulátor és az újsorkarakter.

**Visszaállítás:** getline sor vissza, mentés, fordítás, próba Kiss Anna és 19
bemenettel. Az aktuális sorrendben nincs szükség std::ws használatára.

**Csak kérésre bővítsd:** ha számbeolvasás után jönne getline, a bent maradt
újsorkarakter miatt üres sort olvashatna. A std::getline(std::cin >> std::ws, nev)
elhagyja a kezdő whitespace karaktereket, ezért nem megfelelő, ha az üres sor
vagy a kezdő szóköz megőrzendő adat. A jelenlegi program sorrendje más.

### C4 – Ellenőrző kérdések: beolvasási és tartományhiba

Minden próba új futtatás, névként Anna. A kód változatlan.
Először csak ezt kérdezd: „A -1 életkort melyik ellenőrzés utasítja el?”
Válasz és próba után külön kérdés következzen az alma bemenetre.
Ne mutasd meg előre az alábbi értékelési táblázatot.

**Válasz után, oktatói ellenőrző adatok:**

| Bemenet | Várható viselkedés | Indok |
|---|---|---|
| -1 vagy 200 | Tartományhiba; nincs üdvözlés. | A szám beolvasható, de kívül van a 0–120 tartományon. |
| alma | Beolvasási hiba; nincs üdvözlés. | Nem olvasható egész számként. |
| 0 | Végigfut, jövőre 1. | Az alsó határ is elfogadott. |
| 120 | Végigfut, jövőre 121. | A felső határ is elfogadott; az ellenőrzés a beolvasott életkorra vonatkozik. |
| 19abc vagy 19.5 | Végigfut a 19 értékkel. | A >> a kezdeti egész számot beolvassa, a maradékot nem dolgozza fel. |

A -1 és alma próbát dolgozzátok fel; a többi határesetből a haladás szerint
válassz egyet vagy többet. A kihagyott bemeneteket ne tekintsd kipróbáltnak.
A ! logikai tagadás; a || logikai „vagy”. Az első if a beolvasást, a második a
megengedett tartományt ellenőrzi. A cerr a szabványos hibakimenet; a return 1;
itt hibás befejezést jelez. Az if általános elágazás, többféle célra használható.

Az üres névsor hibát ad, a csak szóközöket tartalmazó név nem üres string,
ezért azt a minta elfogadja. A program nem végez teljes név- vagy teljes sorra
kiterjedő számellenőrzést. Ezt szükség esetén magyarázd; ne nyiss új feladatot
az előző kérdés megválaszolása közben.

### C5 – Bemutatás, majd ellenőrző kérdés: másolás és módosítás

A kiinduló mintában az alma indexei: 0: a, 1: l, 2: m, 3: a. A betu az s[2]
értékének másolatát kapja; az s módosítása nem módosítja a betu értékét.
Ezután az eredeti `s[2] = 'e';` sort cserélnénk `s[2] = 'o';` sorra.

Kérdés: „Milyen szöveg lesz s értéke a módosítás és a fa hozzáfűzése után?”
Várd meg a választ.

**Válasz után:** aloafa, a hossza 6. A korábban kiolvasott betu értéke m marad.
Ha csak az aloa választ kapod, ismerd el, hogy ez a karaktercsere utáni állapot;
csak a hozzáfűzés eredményére kérdezz rá.

**Próba:** sorcsere, mentés, fordítás, futtatás Anna és 19 bemenettel.
**Visszaállítás:** az eredeti 'e' vissza, mentés és újrafordítás.
Érvénytelen [] index használatát ne kérd; kivételt dobó indexellenőrzéshez az
órai at() kész példája használható. Referenciákat csak kifejezett kérésre vezess be.

### C6 – Ellenőrző kérdés: hossz UTF-8 esetén

Előzetes ismeret: a size() a tárolt char elemek számát adja, nem általános
betűszámláló. Kérdés: „Biztosan három lesz az Ági szöveg size() eredménye?”
Várd meg a választ; bizonytalanságnál megfigyelésként is folytatható.

**Válasz után:** UTF-8 esetén Á két bájt, g és i egy-egy bájt, ezért az eredmény
4. A látható betűk száma három. A tényleges bemeneti kódolás a termináltól függ.

**Próba:** változatlan kód, név Ági, életkor 19. Elegendő a hossz megfigyelése.
A lezáró nullkarakter nem számít bele a size() eredményébe. Az ASCII-szövegek
indexelésénél egy char elem felel meg egy látható karakternek.

### C7 – Értelmezési kérdés: konverzió és összefűzés

Ez gondolkodási feladat, nem új program írása. Mutasd meg komment nélkül:

```cpp
std::string("19") + "1"
```

Kérdés: „Milyen szöveget ad ez a kifejezés?” Várd meg a választ.

**Válasz után:** A "191" szöveget. A + itt összefűz. Ezután röviden állítsd
mellé: std::stoi("19") + 1 eredménye a 20 egész szám; std::to_string(19)
eredménye a "19" szöveg. Kérésre térj ki a stoi hibáira: "19abc" esetén 19,
"alma" esetén invalid_argument kivétel. A teljes szöveg ellenőrzését és a
kivételkezelést az órai kész példa magyarázza.

C1–C7 után az alapgyakorlatok lezárhatók. A ténylegesen elvégzett részeket
nevezd meg röviden; a kiegészítő gyakorlatokra egyszer kérdezz rá.

## 4. Kiegészítő gyakorlat – Előfeldolgozás és makrók

**Forrás:** `L02_preprocesszor_makro.cpp`. Kapcsolódó fejezet: 10.

### D1 – Bemutatás: makró és előfeldolgozás

A #define KEDVENC_SZAM 42 helyettesítési szabályt ad meg. Az előfeldolgozó a
makrónév megfelelő előfordulását a 42 tokennel helyettesíti. A token a forráskód
egy eleme, például név, számliterál vagy műveleti jel. A makró nem változó,
nincs saját, változóhoz hasonló típusa és futás közbeni tárolóhelye. A 42
ugyanakkor a C++ kifejezésben int típusú egész számliterál.

```bash
g++ -std=c++20 -Wall -Wextra -pedantic -o L02 L02_preprocesszor_makro.cpp
./L02
```

Várható kimenet:

```text
A nevem: Kiss Anna.
Kedvenc szamom: 42
```

### D2 – Vezetett megfigyelés: a nagy fájl célzott megtekintése

Már a parancsok előtt mondd el: „A fejlécek miatt hosszú fájl keletkezik.
Ebben a példában a saját programunk a végén található; az utolsó húsz sort
nézzük meg.” Ne kérd először a teljes fájl megnyitását a szerkesztőben.
A létrehozási és megtekintési parancsot együtt add meg; a másodikat az első
sikeres végrehajtása után használja a hallgató.

```bash
g++ -std=c++20 -E L02_preprocesszor_makro.cpp -o L02_elofeldolgozott.ii
tail -n 20 L02_elofeldolgozott.ii
```

A -E az előfeldolgozás után megáll, nem készít futtatható programot. A tail
csak a fájl végét olvassa; nem módosítja a tartalmát. A hallgatótól csak a
Kedvenc szamom szöveget tartalmazó sort kérd, ne az egész fájlt.
Ha a kivonatban nem található a keresett sor, célzottan keressetek:

```bash
rg -n -F 'Kedvenc szamom' L02_elofeldolgozott.ii
```

Ha az rg nem érhető el:

```bash
grep -n -F 'Kedvenc szamom' L02_elofeldolgozott.ii
```

**A megfigyelés után:** a makrónév helyén 42 látható. A fájl hosszát a fejlécek
feldolgozott tartalma adja. Később assembly kód, tárgykód, majd összekapcsolással
futtatható program készül. Ne mondd, hogy a makró egyszerűen minden szövegbeli
előfordulást kicserél: a behelyettesítés tokeneken történik.

### D3 – Ellenőrző kérdés: új helyettesítő szöveg

Eredeti sor: `#define KEDVENC_SZAM 42`. Új sor: `#define KEDVENC_SZAM 7`.
Kérdés: „Mit ír ki a program a kedvenc szám helyén újrafordítás után?”
Várd meg a választ.

**Válasz után:** 7-et. A makrónév helyére most a 7 token kerül; nem az összes
42 számot cseréljük le általánosan a programban.

**Próba:** sorcsere, mentés, a D1 parancsaival fordítás és futtatás.
A második sor: Kedvenc szamom: 7. Az .ii fájl újragenerálása választható;
ha megismétlitek, a D2 teljes parancspárját add meg, tail-lel együtt.

**Visszaállítás:** 42 vissza, mentés, fordítás és futtatás. Ha a 7-es változathoz
az .ii fájlt is újrageneráltátok, frissítsétek az eredeti forrásból is, hogy ne
maradjon félrevezető köztes állapot. Rögzített számértékhez általában constexpr
állandót használunk; itt a makró az előfeldolgozás bemutatását szolgálja.

## 5. Kiegészítő gyakorlat – Feltételes fordítás és assert

**Forrás:** `L03_felteteles_makro.cpp`. Kapcsolódó fejezetek: 9–10.

### E1 – Bemutatás: két fordítási változat

Első változat:

```bash
g++ -std=c++20 -Wall -Wextra -pedantic -o L03 L03_felteteles_makro.cpp
./L03
```

Várható kimenet:

```text
A diagnosztikai uzenet ki van kapcsolva.
SQUARE(3) = 9
SQUARE(1 + 2) = 9
```

Második változat:

```bash
g++ -std=c++20 -Wall -Wextra -pedantic -DDEBUG -o L03_debug L03_felteteles_makro.cpp
./L03_debug
```

Ebben az első sor: A diagnosztikai uzenet be van kapcsolva. A többi sor azonos.
A -DDEBUG definiálja a makrót; az #ifdef a definiáltságot vizsgálja. Az #else
másik ágat jelöl, az #endif lezár. A kiválasztás előfeldolgozáskor történik;
a C++ if ezzel szemben a program működésének része.

A fájlnevek a megadott parancspároknál segítik a megkülönböztetést. Ha eltér a
hallgató kimenete, kérd el a tényleges utolsó fordítási és futtatási parancsot;
ne a fájlnévből következtess az előzményre. A korábbi DEBUG-os bináris nem
frissül automatikusan attól, hogy később csak az L03 fájlt fordítjuk újra.

### E2 – Ellenőrző kérdés: zárójelezés

A helyes makró: `#define SQUARE(x) ((x) * (x))`.
Mutasd meg a vizsgált változatot, a megoldás nélkül:

```cpp
#define SQUARE(x) x * x
```

Kérdés: „Mennyi lenne ezzel a SQUARE(1 + 2) értéke?” Várd meg a választ.
Ha segítség kell, először csak a behelyettesített kifejezést mutasd meg;
a számszerű eredményt még ne add meg újabb próbálkozás előtt.

**Válasz után:** 1 + 2 * 1 + 2, az eredmény 5. A szorzás erősebben köt.
A SQUARE(3) értéke továbbra is 9. A zárójelezés hiánya logikai hibát okoz.

**Próba előkészítése:** itt két összetartozó sor módosítása szükséges ugyanahhoz
a megfigyeléshez. Előbb magyarázd el az assert szerepét: aktív ellenőrzésnél a
hamis feltétel diagnosztikai üzenetet és rendellenes megszakítást okoz.
A számok zavartalan megfigyeléséhez átmenetileg kikapcsoljuk ezt az egy hívást.

1. A makró definícióját cserélje a fenti zárójelek nélküli változatra.
2. Az `assert(SQUARE(1 + 2) == 9);` sort tegye megjegyzésbe:

```cpp
// assert(SQUARE(1 + 2) == 9);
```

Mentés, majd ezzel a konkrét parancspárral fordítás és futtatás:

```bash
g++ -std=c++20 -Wall -Wextra -pedantic -o L03 L03_felteteles_makro.cpp
./L03
```

A teljes kimenet:

```text
A diagnosztikai uzenet ki van kapcsolva.
SQUARE(3) = 9
SQUARE(1 + 2) = 5
```

A próba után mindkét eredeti sort állítsa vissza: a zárójelezett makródefiníciót
és az aktív assert hívást. Fordítás és futtatás ugyanazzal a parancspárral;
az eredmény az E1 első változatának kimenete. Csak megerősítés után zárd le a próbát.
A SQUARE(i++) használatát ne kérd: a paraméter kétszeri behelyettesítése problémát
okozhat. Az ilyen számításokat általában függvénnyel valósítjuk meg.

### E3 – Bemutatás és fogalmi ellenőrzés: DEBUG és NDEBUG

A két makró külön szerepét először magyarázd el:

| Beállítás | A példabeli üzenet | Az assert ellenőrzése |
|---|---|---|
| Nincs -DDEBUG és nincs -DNDEBUG | Ki van kapcsolva. | Aktív. |
| Csak -DDEBUG | Be van kapcsolva. | Aktív. |
| Csak -DNDEBUG | Ki van kapcsolva. | Kimarad. |
| -DDEBUG és -DNDEBUG együtt | Be van kapcsolva. | Kimarad. |

A táblázat a megadott forrásra és más beállítással felül nem írt makrókra
vonatkozik. Az NDEBUG-nak a cassert beillesztése előtt kell definiálva lennie.
A debug/release elnevezés nem helyettesíti a tényleges beállítások ismeretét.

Ezután kérdezz indoklást: „Miért nem bízzuk csak assert-re az életkor ellenőrzését?”
Várd meg a választ. Az „assert nem fut, ha nincs DEBUG” részben téves magyarázat;
ismerd el a kikapcsolhatóság felismerését, de javítsd a makró nevét és a feltételt.

**Válasz után:** NDEBUG mellett az ellenőrzés kimarad. A bemenet ellenőrzését
az L04 if utasításai végzik. Az assert feltételébe ne tegyünk a program működéséhez
szükséges mellékhatást. Az ellenőrzés kimaradása önmagában nem jelent garantált
összeomlást; a következmény a programtól függ.

Az assert előtti kiíró utasítások végrehajtása és a szöveg tényleges megjelenése
különbözik: rendellenes megszakításkor a pufferelt kimenet hiányos maradhat.
Ne ígérj biztosan megjelenő sorokat, és ne kérj külön megszakítási próbát.

### E4 – Választható bemutatás: include guard

A többszörös beillesztés elleni védelem egy fejléc ismételt feldolgozását
akadályozza meg ugyanabban a fordítási egységben. Az órai kedvencek.h példában
az #ifndef ellenőrzi a védőmakró hiányát, a fejléc definiálja a makrót, és az
#endif lezárja a részt. Második beillesztéskor a belső tartalom kimarad.
Egyetlen .cpp-ben egy üres védőblokk ezt nem szemléltetné; ne készíttess ilyet.

## Lezárás és ismétlés

Először ellenőrizd belsőleg a lépések tényleges állapotát. A kihagyott próbát ne
írd elvégzettnek. Röviden foglald össze a feldolgozott témákat. Ha a hallgató
kér ismétlést, egyszerre egy, korábbi bizonytalanságra célzott kérdést adj.
Ne ismételd végig automatikusan az összes kérdést, ha a megértés már világos.

Lehetséges kérdések, megoldás előzetes közlése nélkül:

- Mi változik a mentéskor, és mi változik a fordításkor?
- Miért nem frissül az osszeg automatikusan a darab módosításakor?
- Miért különbözik az 5 / 2 és az 5.0 / 2 eredménye?
- Miért okoz gondot a Kiss Anna után a számbeolvasás, ha a nevet >> olvasta?
- Miért lehet eltérő a látható betűk és a tárolt char elemek száma?
- Miért marad változatlan a betu az s módosítása után?
- Miben különbözik a beolvasási hiba és a megengedett tartomány megsértése?
- Mi szabályozza az assert kikapcsolását a makrós példában?

A választ értékeld pontosan. Segített megoldás után a „megbeszéltük” állítás
helyes; az „önállóan hibátlanul megoldottad” nem. A következő foglalkozásra csak
olyan folytatást ígérj, amelyhez a szükséges állapot ténylegesen rendelkezésre áll.
