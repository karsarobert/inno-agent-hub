# C++ 2. gyakorlat – belső foglalkozási forgatókönyv

Ez az oktatónak és a tutornak szóló részletes forgatókönyv. A hallgató egyesével,
beszélgetésben kapja a feladatokat. Ne idézd a belső utasításokat vagy lépésazonosítókat.

## Időbeosztás és előismeretek

3 × 45 perc, a szüneteken felül:
- 1. blokk: ráhangolás 5 perc, G02_01 15, G02_02 10, G02_03 15 perc.
- 2. blokk: G02_04, G02_05 és G02_06 egyenként 15 perc.
- 3. blokk: G02_07 10, G02_08 10, G02_09 15, lezárás 10 perc.

A teljes alapútvonal kilenc feladat. A „választható” lépések nem kötelezők;
a K01 kitekintés ezen felüli időt igényel. Az idő miatt szükséges kihagyást
jelöld tudatos kihagyásnak, ne automatikus teljesítésnek.

Ráhangolás: az agent.md szerinti bemutatkozás után egy rövid kérdés a mentés,
fordítás és futtatás kapcsolatáról. Ha ez biztosan megy, ne gyakoroltass újra
Hello-programot. A munkamappa és a GCC ellenőrzéséhez csak a szükséges parancsot
add a hallgatónak; a válaszára várj, ne futtass helyette.

## Ki végzi a műveleteket?

**Minden szerkesztést, mentést, fordítást, futtatást és hibajavítást a hallgató
végez.** A tutor a meglévő forrást és az útmutatókat olvashatja, elmagyarázza a
feladatot, megadja a szükséges kódot és parancsokat, majd vár a visszajelzésre.
Nem hajtja végre helyette a műveleteket; ez az első közös bemutatásra és a K01-re
is érvényes. A közös bemutatás közös értelmezést és hallgatói végrehajtást jelent.

Az alábbi „próba”, „sorcsere”, „mentés”, „fordítás”, „futtatás” és „hibajavítás”
minden előfordulása a hallgató teendője. A tutor feladata ezek kiadása és a
beszámoló megvárása. A hallgató helyes válasza után se végezzen eszközös próbát.
Nincs rutinszerű visszaállítás: a kipróbált módosítások megmaradnak.
Csak a szándékos hibapróba hibáját kell kijavíttatni a hallgatóval.

A **„Válasz után”** részek az érvelés megbeszéléséhez és a későbbi ellenőrzéshez
adnak támpontot. A jóslat értékelése nem futási beszámoló. Műveleti kérés után
ne írd ki előre a várt eredményt megtörtént futásként, és ne lépj tovább a
hallgató konkrét megfigyelése nélkül. A kimenetet a hallgató saját gépén kapott
eredménnyel hasonlítsd össze; az oktatói adat önmagában nem igazolja a próbát.

## Közös munkaszabályok

- A magyarázat megelőzi az új fogalom önálló használatát. A bemutatásban is
  a hallgató futtat, majd az ő eredményét értelmezitek. A következő jóslat
  új adatra vonatkozzon.
- A „Válasz után” információját ne idézd a hallgató válasza előtt.
- Jóslat előtt add a szükséges aktuális kódot és a módosítást; utána várj.
  A válasz után értékelj, majd kérd a végrehajtást.
- Minden forrásmódosítás után a hallgató mentsen, fordítson, siker esetén futtasson.
  A hiba előidézésére kijelölt fordítások után nincs régi programfuttatás.
- A feladat 1. pontjának parancspárját az adott módosításoknál konkrét nevekkel
  ismételd meg, ha a hallgatónak szüksége van rá. Ne hivatkozz nem létező segédre.
- A programok stdin-bemenetet nem kérnek. A vizsgált adatot a forrásban állítjuk.
- A megjegyzések és kimeneti címkék maradjanak igazak a módosítás után is.
  Az alapmintákban nincs aposztrófos számtagolás, a tizedesjel pont.
- A megadott teljes kimenetek oktatói ellenőrző adatok, nem kötelező
  másolási feladatok. Elegendő az adott megfigyeléshez kapcsolódó sor.
- A számérték, típusa és kiírt alakja külön fogalom. A szokásos környezeti
  feltételeket mindig vedd figyelembe; az eltérésből ne következtess rögtön hibára.
- Minden feladat végén az elért, működő állapot marad meg. Nincs külön
  visszaállítási, takarítási vagy ismételt ellenőrzési kör pusztán a lezárásért.
- Az aktuális kódot kövesd: a későbbi próbában az előző módosítások érvényesek.
  A kiinduló ellenőrző kimenet csak az érintetlen csomag forrására vonatkozik.
  Folytatáskor ne próbáld azt kikényszeríteni a már módosított fájlból.
- A const-értékadás, a szűkítő inicializálás és a K01 hibapróbája után a hallgató
  csak a hibát javítsa ki. Az összes többi korábbi módosítást tartsa meg.

## A kódmagyarázó ellenőrzések használata

A „Kódértés” pontok az alapfeladat részei G02_01, G02_02 és G02_04–G02_09 esetén,
a választható próbák kihagyása esetén is. Egy pont általában 1–2 perc, az adott
feladat idején BELÜL. A korábbi rövid összefoglalókat váltja fel, nem külön vizsga.
Az 5. feladat két külön témájánál két rövid kérdés indokolt, külön üzenetben.
G02_03-ban nincs külön kódmagyaráztatás; K01-ben a javítás indoklását használjuk.

Az új fogalom tanítása után legyen hallgatói próba, majd az aktuális kódból
kiemelt részlet és egy saját szavas magyarázatot kérő kérdés. Előbb várj a válaszra,
csak utána használd az **oktatói támpontot**. Az utókérdés csak a hiányzó részhez
szól; jó magyarázat esetén hagyd el. A „Segítség után” gondolati példa nem új
kötelező szerkesztés vagy futtatás. Ha az értelmezést már önállóan igazolta,
ne ismételtesd meg. A végrehajtás és a kódértés külön értékelendő.

A mintarészletek a forgatókönyv szerinti állapotot jelzik: mindig a tényleges
forrásból idézz. A megváltozott konstans értékét tartsd meg. Ne értékeld önálló
megértésként a frissen elmondott megoldás, számérték vagy kijelölt sor megismétlését.

## 1. Tárméret és típushatárok

**Forrás:** `G02_01_tipusok.cpp`. **Cél:** a bájt, a bit és a típus értéktartományának megkülönböztetése.

### 1.1 – Közös értelmezés, hallgatói fordítás és futtatás

Kapcsolódás: az első gyakorlatban értékeket tároltunk; most a tároló méretét
és a típus határait vizsgáljuk. A sizeof bájtban ad méretet, a CHAR_BIT pedig
megmondja, hány bit egy bájt. A `sizeof(char) == 1` nem egy bitet jelent.
Magyarázd el a `<climits>` és `<limits>` fejléc célját. A
`std::numeric_limits<int>::max()` jelölést bontsd fel: std névtér;
numeric_limits az int jellemzőihez; max() a felső határt adó függvényhívás.
Az int alsó határához itt lowest() tartozik.

A kiírt méreteket előbb megfigyeljük, nem előre kérjük számon. Az alábbi kimenet
szokásos 8 bites bájtra, 32 bites int-re és IEEE 754 típusokra vonatkozik.
Ha a hallgató környezete eltér, az ő lekérdezése az irányadó.

Add ki a hallgatónak a fordítási parancsot; ő futtassa a terminálban:

```bash
g++ -std=c++20 -Wall -Wextra -pedantic G02_01_tipusok.cpp -o G02_01
```

Sikeres fordítás után a hallgató futtassa a programot:

```bash
./G02_01
```

Várd meg a hallgató eredményét, és csak utána értelmezzétek a kimenetet.

**Oktatói ellenőrző adat – várt kiinduló kimenet, nem elvégzett próba:**

```text
Egy bajt bitjei: 8
int merete bajtban: 4
float merete bajtban: 4
double merete bajtban: 8
int also hatara: -2147483648
int felso hatara: 2147483647
Pontszam: 12
Pontszam tarmerete bajtban: 4
```

Ez a közös bemutatás ellenőrző mintája. A későbbi önálló kérdéshez más adatot vagy
módosítást használj; a frissen látott kimenetet ne kérd vissza jóslatként.

### 1.2 – Alappróba: nagyobb érték, ugyanaz a típus

Mutasd a meglévő sort: `int pontszam = 12;`.
A tervezett új sor: `int pontszam = 1200;`.
Kérdés: „Megváltozik-e ettől a pontszam változó sizeof eredménye? Miért?”
Várd meg a választ, és értékeld az érvelést. Ezután add ki a műveleti feladatot:

> Most cseréld ki a sort az `int pontszam = 1200;` sorra a
> `G02_01_tipusok.cpp` fájlban, majd mentsd el. A terminálban fordítsd le:

```bash
g++ -std=c++20 -Wall -Wextra -pedantic G02_01_tipusok.cpp -o G02_01
```

> Sikeres fordítás után futtasd:

```bash
./G02_01
```

> Másold be a pontszámot és a tárméretét mutató utolsó két sort.
> Ha fordítási hibát kapsz, ne futtasd a programot; az első hibaüzenetet küldd el.

**Itt állj meg, és várd meg a hallgató próbáját.** Ne szerkeszd vagy futtasd a
fájlt, és ne válaszold meg helyette a kimeneti feladatot. A továbblépés feltétele
az ő beszámolója, nem az, hogy az előző kérdésre helyesen válaszolt.

**Válasz után:** az érték 1200 lesz, a típushoz tartozó tárméret nem változik;
szokásos környezetben továbbra is 4 bájt. Elegendő az utolsó két sor.
A bájt–bit átszámítást csak akkor kérdezd külön, ha még nem magyarázta el.
Ne mondd ki előbb a szorzatot, majd kérd vissza ugyanazt a számot; ha már
elhangzott, hagyd el az ismétlést. A feladat kódértési pontja alább következik.

### 1.3 – Rövid típuscsere

A hallgató által cserélendő teljes kiíró sor:

```cpp
std::cout << "int merete bajtban: " << sizeof(int) << '\n';
```

Erre:

```cpp
std::cout << "long long merete bajtban: " << sizeof(long long) << '\n';
```

Előbb kérdés: „Miért kell a feliratot is megváltoztatnod?” A válasz megbeszélése
után kérd a hallgatótól a sorcserét, mentést, fordítást és futtatást. Várd meg
a long long méretéről szóló kimeneti sort. A kimeneti címke a ténylegesen vizsgált típust nevezze meg.
A long long szokásos mérete 8 bájt, de ne ezt követeld minden gépen.
A többi kiírás továbbra is az eredeti típusra vonatkozik.
**Megmaradó állapot:** `pontszam` 1200, a típusméretet vizsgáló kiírás
`long long` típust és ennek megfelelő feliratot használ. Nincs további művelet.

### Kódértés – tárméret és értékhatár

A próba után a forrás alábbi két kifejezését emeld ki:

```cpp
sizeof(pontszam)
std::numeric_limits<int>::max()
```

**Kérdés:** „Mit tudunk meg ezzel a két kifejezéssel, és miben különbözik a jelentésük?” Várj.

**Oktatói támpont – csak a válasz után:** az első bájtban mért tárméret,
a második az int legnagyobb ábrázolható értéke. Egyik sem az aktuális pontszám.
A típust és a saját környezetet vegye figyelembe, ne számadatot memorizáljon.
**Utókérdés, ha kell:** „A max() a pontszam mostani értékét vizsgálja?”
**Segítség után:** gondolatban legyen pontszam 25; magyarázza el, melyik
lekérdezés eredménye változna. A forrásban az 1200 megmarad.

**Blokkzárás és forrásállapot:** Az 1200-as érték és a long long-kiírás maradjon meg. A kódértési pontot ne kövesse újabb sizeof-definíció visszakérdezése.

## 2. Inicializálás, értékadás, konstans

**Forrás:** `G02_02_inicializalas.cpp`. **Cél:** kezdőérték és későbbi módosíthatóság megértése.

### 2.1 – Közös értelmezés, hallgatói fordítás és futtatás

Mutasd meg a `pontszam{}` inicializálást, majd a `pontszam = 72;` értékadást.
A rogzitett_pontszam az aktuális érték másolatát kapja és const; a maximalis_pontszam
constexpr, fordításkor ismert beállítás. A forrás minden adatnak ad kezdőértéket.
A const és constexpr részletes nyelvi elmélete helyett a példabeli szerepet tanítsd.

Add ki a hallgatónak a fordítási parancsot; ő futtassa a terminálban:

```bash
g++ -std=c++20 -Wall -Wextra -pedantic G02_02_inicializalas.cpp -o G02_02
```

Sikeres fordítás után a hallgató futtassa a programot:

```bash
./G02_02
```

Várd meg a hallgató eredményét, és csak utána értelmezzétek a kimenetet.

**Oktatói ellenőrző adat – várt kiinduló kimenet, nem elvégzett próba:**

```text
Kezdo pontszam: 0
Aktualis pontszam: 72
Rogzitett pontszam: 72
Maximalis pontszam: 100
```

Ez a közös bemutatás ellenőrző mintája. A későbbi önálló kérdéshez más adatot vagy
módosítást használj; a frissen látott kimenetet ne kérd vissza jóslatként.

### 2.2 – Alappróba: egy konstans módosítása

A `const int rogzitett_pontszam = pontszam;` sor UTÁN ideiglenesen ezt írnánk:

```cpp
rogzitett_pontszam = 80;
```

Kérdés: „Fordításkor vagy futás közben derül ki, hogy ez nem megengedett?”
Várd meg a választ. Utána tisztázd: ezt a próbát csak fordítjuk; sikertelen
fordítás után a régi programot nem futtatjuk. A hibát az érvénytelen értékadás törlésével javítja majd a hallgató.

**Válasz után:** fordítási hiba, mert const objektumot próbálunk értékadással
módosítani. A hibaüzenet például read-only változót említ, de a pontos szöveg
verziófüggő. Kérd csak az első lényeges diagnosztikát.
**Hibajavítás:** a hallgató kizárólag a const változó érvénytelen értékadását
törölje, mentsen és fordítson. Minden más módosítását tartsa meg; várd meg a visszajelzését.

### 2.3 – Választható: a változó módosítása és a másolat

A fordítási hiba kijavítása után a programban a hallgató a const másolat létrehozása UTÁN szúrja be:

```cpp
pontszam = 80;
```

Előbb kérdezd, melyik későbbi kiírt érték változik. Válasz után próba.
Az aktuális pontszám 80, a rögzített továbbra is 72. A működő `pontszam = 80;` értékadás maradjon meg.

### 2.4 – Választható: szűkítő inicializálás

Eredeti sor: `int pontszam{};`. Új sor: `int pontszam{3.7};`.
Előtte magyarázd el a kapcsos zárójel szerepét, majd kérdezd a várható hibafajtát.
A fordítás hibás, mert double → int szűkítés történne. Ne ígérj futásidejű
3 vagy 4 értéket. A hallgató javítsa a szűkítő inicializálást `int pontszam{3};`
alakra, mentsen és fordítson. Siker esetén futtasson: az első kiírás így 3.
A későbbi értékadások miatt a további sorok az előző próbák szerint alakulnak.
Várd meg a beszámolót; a 3-as kezdőérték és a korábbi működő módosítások megmaradnak.
Inicializálatlan kiolvasási próbát ne adj.

### Kódértés – érték másolása és módosíthatóság

A sikeres hibajavítás után, az esetleges további próbák előtt is elvégezhető:

```cpp
const int rogzitett_pontszam = pontszam;
```

**Kérdés:** „Mondd el saját szavaiddal, mi történik ebben a sorban!” Várj.

**Oktatói támpont – csak a válasz után:** új int objektum kapja a pontszam
akkori értékének másolatát; a const miatt ezt később nem írhatjuk át.
Nem élő kapcsolatot hoz létre a két változó között. A „nem változtatható”
önmagában még nem magyarázza az inicializálást és a másolatot.
**Utókérdés, ha kell:** „Ha később csak a pontszam értékét átírjuk, mi történik a másolattal?”
A const és constexpr eltérését csak bizonytalanság esetén kérdezd külön a
`constexpr int maximalis_pontszam = 100;` sorral: miért alkalmas itt a constexpr?
A const inicializálója futás közben is meghatározható; a constexpr-é itt
állandó kifejezés kell legyen. Ne állítsd, hogy a const mindig futásidejű.
**Segítség után:** gondolatban legyen a másolat készítésekor a pontszam 65,
majd később 90; magyarázza el a másolat értékét. Ha a választható másolatpróbában
már ezt önállóan indokolta, ne kérdezd újra.

**Blokkzárás és forrásállapot:** A hallgató által elért, fordítható változat maradjon meg. A kihagyott választható lépéseket ne jelöld elvégzettnek.

## 3. Nyolc bit kétféle értelmezése

**Forrás:** `G02_03_bitmintak.cpp`. **Cél:** a kettes komplemensű −1 és −127 megkülönböztetése.

### 3.1 – Közös értelmezés, hallgatói fordítás és futtatás

A nyolc int változó 0 vagy 1 értéke nyolc bitet SZEMLÉLTET. A változók tényleges
memóriamérete ettől nem egy bit, és a program nem memóriabájtokat vizsgál.
A legfelső bit előjel nélkül +128, kettes komplemensben −128 helyiértékű.
Az alsó hét bit közös részösszegét egyszer számoljuk ki és beszédes névvel tároljuk.
A 64, 32, ... a helyiértékek, nem önkényes feladatparaméterek. Itt még nem kell
bitművelet, tömb vagy ciklus. A kezdő minta 01111111, mindkét értelmezése pozitív.

Add ki a hallgatónak a fordítási parancsot; ő futtassa a terminálban:

```bash
g++ -std=c++20 -Wall -Wextra -pedantic G02_03_bitmintak.cpp -o G02_03
```

Sikeres fordítás után a hallgató futtassa a programot:

```bash
./G02_03
```

Várd meg a hallgató eredményét, és csak utána értelmezzétek a kimenetet.

**Oktatói ellenőrző adat – várt kiinduló kimenet, nem elvégzett próba:**

```text
Bitminta: 01111111
Elojel nelkul: 127
Kettes komplemens: 127
```

Ez a közös bemutatás ellenőrző mintája. A későbbi önálló kérdéshez más adatot vagy
módosítást használj; a frissen látott kimenetet ne kérd vissza jóslatként.

### 3.2 – Alappróba: csak a bal szélső bit változik

Eredeti sor: `int bit7 = 0;`. Új sor: `int bit7 = 1;`.
Kérdés: „Milyen előjeles értéket jelent majd ez a minta kettes komplemensben?”
A megoldás előtt várj. Válasz után módosítás és futtatás.

**Válasz után:** a minta 11111111. Az előjeles összeg −128 + 127 = −1,
az előjel nélküli 128 + 127 = 255. Ha −127-et mond, az előjel–abszolútérték
elképzelését javítsd: nem teszünk egyszerű mínuszjelet a maradék 127 elé.

### 3.3 – Alappróba: a −127-hez tartozó minta

A bitváltozók nyolcsoros blokkját erre cserélnénk, minden mást megtartva:

```cpp
int bit7 = 1;
int bit6 = 0;
int bit5 = 0;
int bit4 = 0;
int bit3 = 0;
int bit2 = 0;
int bit1 = 0;
int bit0 = 1;
```

Kérdés: „Mennyi most a kettes komplemensű összeg?” Várd meg, majd próba.
**Válasz után:** 10000001; előjel nélkül 129; előjelesen −128 + 1 = −127.
A nyolc sor cseréje egyetlen összetartozó bitminta-beállítás; ne szórd szét
nyolc felesleges újrafordításra. Más változót ne módosítsanak.

**Megmaradó állapot:** az alappróba végén 10000001; a bitváltozókat ne állíttasd át újra.
Választható új kérdés: 10000000 értelmezése (előjel nélkül 128, előjelesen −128).
A bitváltozókba 0-n és 1-en kívüli értéket ne kérj.

**Blokkzárás és forrásállapot:** A modell azonos bitek kétféle értelmezését mutatja. Az utoljára kipróbált bitminta maradjon meg.

## 4. Osztás és a konverzió helye

**Forrás:** `G02_04_osztas.cpp`. **Cél:** a művelet előtti és utáni konverzió elkülönítése.

### 4.1 – Közös értelmezés, hallgatói fordítás és futtatás

Vezesd végig a három képletet. Két int operandus egész osztást végez; az
eredmény csak utána kerül double-be. A static_cast<double>(osszes_pont)
a művelet előtt ad double értéket, az eredeti változót nem módosítja.
A teljes egész osztás köré írt cast már a csonkított eredményt alakítja át.
Az elso/masodik/harmadik nevek a három összehasonlított változatot jelölik.
A std::cout itt alapértelmezett formátumot használ: a double 3.0 kiírása 3.

Add ki a hallgatónak a fordítási parancsot; ő futtassa a terminálban:

```bash
g++ -std=c++20 -Wall -Wextra -pedantic G02_04_osztas.cpp -o G02_04
```

Sikeres fordítás után a hallgató futtassa a programot:

```bash
./G02_04
```

Várd meg a hallgató eredményét, és csak utána értelmezzétek a kimenetet.

**Oktatói ellenőrző adat – várt kiinduló kimenet, nem elvégzett próba:**

```text
Elso szamitas: 3
Masodik szamitas: 3.5
Harmadik szamitas: 3
```

Ez a közös bemutatás ellenőrző mintája. A későbbi önálló kérdéshez más adatot vagy
módosítást használj; a frissen látott kimenetet ne kérd vissza jóslatként.

### 4.2 – Alappróba: új adatok

Eredeti sor: `int osszes_pont = 7;`. Új sor: `int osszes_pont = 9;`.
Kérdés: „Melyik számítás őrzi meg a törtrészt, és mennyi lesz az értéke?”
Várd meg, majd futtatás.
**Válasz után:** a második 4.5; az első és harmadik double értéke 4.0,
alapértelmezett kiírásuk 4. Az eltérő típuskifejezés az ok, nem a változó neve.

### 4.3 – Alappróba: egy sor javítása

Az új, 9-es adat marad. Kérd, hogy az első számítás is valódi átlagot adjon.
Ha kell, mutasd az eredeti sort:

```cpp
const double elso_atlag = osszes_pont / hallgatok_szama;
```

A segítségként adható csere, csak az önálló válasz után:

```cpp
const double elso_atlag = static_cast<double>(osszes_pont) / hallgatok_szama;
```

Mentés, fordítás, futtatás: az első és második 4.5, a harmadik 4.
A harmadik érték szerepét az alábbi kódértési pontban tisztázd, ha még szükséges.
**Megmaradó állapot:** osszes_pont 9; az elso_atlag a javított, művelet előtti
konverziót használja. Az első és második eredmény 4.5, a harmadik 4 marad.

### 4.4 – Választható: csonkítás negatív értéknél

Az aktuális, már javított forrásban a return ELÉ szúrható két sor:

```cpp
const double meresi_ertek = -3.9;
std::cout << "Egeszre alakitva: " << static_cast<int>(meresi_ertek) << '\n';
```

Előbb magyarázd el a nulla felé csonkítást másik számon, majd kérdezd az eredményt.
Itt −3, nem −4. A kiegészítő két sor a próba után is megmaradhat.
A hallgatok_szama nem lehet nulla; ilyen hibapróbát ne adj.

### Kódértés – az osztás végrehajtási sorrendje

A javítás sikeres próbája után emeld ki az aktuális helyes képletet:

```cpp
const double elso_atlag = static_cast<double>(osszes_pont) / hallgatok_szama;
```

**Kérdés:** „Vezesd végig, hogyan számítja ki a program ezt a kifejezést!” Várj.

**Oktatói támpont – csak a válasz után:** az osszes_pont értékéből double
érték képződik, majd a nevező is double-re konvertálódik az osztáshoz;
lebegőpontos osztás történik. Az eredmény inicializálja a const double változót.
Az eredeti osszes_pont típusa nem változik meg. Más helyes megoldásnál annak
működését értékeljük. A „4,5” önmagában csak eredmény.
**Utókérdés, ha kell:** „Mi lenne más, ha a konverzió a teljes osztás körül állna?”
Ez váltja fel a harmadik eredmény változatlanságáról szóló ismétlő kérdést.
**Segítség után:** gondolatban 11 pont és 2 hallgató esetén indokolja a művelet
sorrendjét és az eredményt; nincs új szerkesztés.

**Blokkzárás és forrásállapot:** A két helyes átlagot és egy csonkított eredményt mutató kód maradjon meg; a választható kiegészítés is megtartható.

## 5. Tartományhatárok és nagyobb számítás

**Forrás:** `G02_05_tartomanyok.cpp`. **Cél:** előjel nélküli körbefordulás és megfelelő műveleti típus.

### 5.1 – Közös értelmezés, hallgatói fordítás és futtatás

Először csak a számlálós részt magyarázd. A numeric_limits<unsigned int>
a vizsgált típust választja ki, max() annak maximumát adja. A kapott érték
inicializálja a szamlalo változót. A novekmeny név az ismételten használt lépést
nevezi meg. Az 1u ugyanaz az egy érték, mint az 1, de unsigned int típusú;
u az unsigned utótagja, nem egység vagy változónév. A művelet körbefordulása
előjel nélkül meghatározott. Az első kiírt szám a gép unsigned int tartományától függ.

Csak ezután a szorzás: a matematika 2 500 000 000-et ad. A szorzás ELŐTT
long long-ra alakított operandus miatt a program ezt helyesen kezeli.
A teljes_ar const, mert kiszámítása után nem módosítjuk.

Add ki a hallgatónak a fordítási parancsot; ő futtassa a terminálban:

```bash
g++ -std=c++20 -Wall -Wextra -pedantic G02_05_tartomanyok.cpp -o G02_05
```

Sikeres fordítás után a hallgató futtassa a programot:

```bash
./G02_05
```

Várd meg a hallgató eredményét, és csak utána értelmezzétek a kimenetet.

**Oktatói ellenőrző adat – várt kiinduló kimenet, nem elvégzett próba:**

```text
Szamlalo elotte: 4294967295
Szamlalo utana: 0
int felso hatara: 2147483647
Teljes ar: 2500000000
```

Ez a közös bemutatás ellenőrző mintája. A későbbi önálló kérdéshez más adatot vagy
módosítást használj; a frissen látott kimenetet ne kérd vissza jóslatként.

### 5.2 – Alappróba: másik növekmény

Eredeti sor: `constexpr unsigned int novekmeny = 1u;`.
Új sor: `constexpr unsigned int novekmeny = 2u;`.
Kérdés: „Mennyi lesz a számláló értéke a hozzáadás után?” Válasz után próba.
**Válasz után:** 1; a legnagyobb értéket a 0, majd az 1 követi.
Az eredmény a típus szélességétől függetlenül 1. A szorzás sorai változatlanok.
A 2u növekmény maradjon meg; a következő szorzáspróbában is 1 lesz a számláló végeredménye.

### 5.3 – Alappróba: a számítás típusa

Eredeti sor: `int darabszam = 50000;`. Új sor: `int darabszam = 60000;`.
Kérdés: „Elfér-e a matematikai eredmény a gép int típusában, és miért képes
mégis helyesen számolni ez a program?” A saját gépen látott felső határt használd.
Válasz után próba. Az eredmény 3 000 000 000; 32 bites int-be nem fér,
a long long szorzásban igen. Ne módosítsátok a helyes castot az alapfeladatban.
**Megmaradó állapot:** darabszam 60000, novekmeny 2u, a szorzás előtti helyes cast változatlan.
A hibás szorzás csak a külön K01 bemutatóban szerepelhet.

### Kódértés – számláló és nagy szorzás

A két független témát két rövid kérdésben dolgozd fel. Az első az 5.2 próbája
után, a második az 5.3 próbája után következhet. Ne kérdezd újra azt, amit
az adott próbában a hallgató már saját szavaival megmagyarázott.

```cpp
unsigned int szamlalo = std::numeric_limits<unsigned int>::max();
szamlalo = szamlalo + novekmeny;
```

**Első kérdés:** „Honnan kapja a számláló a kezdőértékét, és hogyan változtatja meg a következő sor?” Várj.
**Oktatói támpont – csak a válasz után:** numeric_limits az unsigned int
jellemzőit választja ki, max() a felső határát adja; a következő sor a régi
számlálóhoz adja a növekményt, és visszaírja az eredményt. Előjel nélkül a
körbefordulás meghatározott. A jelenlegi 2u növekménynél az eredmény 1.
**Utókérdés, ha kell:** „Mit jelent az u az aktuális növekmény literáljában?”
Az 1u és 2u unsigned int típusú egész literál; az u nem mértékegység.
**Segítség után:** gondolatban a maximum helyett 10-ről indulva magyarázza el
ugyanezt az értékadást; így látszik, érti-e a jobb és bal oldal szerepét.

Csak az első beszélgetés lezárása és a szorzáspróba után:

```cpp
const long long teljes_ar = static_cast<long long>(darabszam) * egysegar;
```

**Második kérdés:** „Miért képes ez a sor kiszámítani a mostani nagy szorzatot?” Várj.
**Oktatói támpont – csak a válasz után:** a konverzió a szorzás előtt történik,
a másik operandus is long long-ra konvertálódik; a szorzás ebben a típusban
zajlik. Nem önmagában a célváltozó típusa védi meg a számítást.
**Utókérdés, ha kell:** „Milyen típusban történne a szorzás a cast nélkül?”
**Segítség után:** gondolatban az egysegar előzetes konverzióját magyarázza el.
A hibás változatot itt ne írja be és ne futtassa.

**Blokkzárás és forrásállapot:** A módosított, működő kód maradjon meg. A konverzió magyarázatát a kódértési pontban ellenőrizd; utána ne kérd újra.

## 6. Lebegőpontos pontosság

**Forrás:** `G02_06_pontossag.cpp`. **Cél:** értékes számjegyek és közelítő tárolás megértése.

### 6.1 – Közös értelmezés, hallgatói fordítás és futtatás

Két részben haladj. Először a 0.1f és 0.1 tárolását figyeljétek meg: az f
utótag float, az utótag nélküli törtliterál double. A setprecision(17) itt
értékes jegyeket kér; nem új pontosságot ad. A szokásos bináris formátumban
0,1 ismétlődő tört, ezért kerekítve tárolódik. A hosszú számot nem kell
előre kiszámolni, megjegyezni vagy minden sorát bemásolni.

A kiírt példák a szokásos IEEE 754 binary32/binary64 formátumokat feltételezik.
Ha eltérés van, előbb az aktuális literált, típust, formázást és környezetet nézd.
Ne nevezz automatikusan hibásnak más érvényes környezeti kimenetet.

Add ki a hallgatónak a fordítási parancsot; ő futtassa a terminálban:

```bash
g++ -std=c++20 -Wall -Wextra -pedantic G02_06_pontossag.cpp -o G02_06
```

Sikeres fordítás után a hallgató futtassa a programot:

```bash
./G02_06
```

Várd meg a hallgató eredményét, és csak utána értelmezzétek a kimenetet.

**Oktatói ellenőrző adat – várt kiinduló kimenet, nem elvégzett próba:**

```text
float: 0.10000000149011612
double: 0.10000000000000001
Rovid kiiras: 1.23457
Kozepes kiiras: 1.234568
Hosszu kiiras: 1.23456788
```

Ez a közös bemutatás ellenőrző mintája. A későbbi önálló kérdéshez más adatot vagy
módosítást használj; a frissen látott kimenetet ne kérd vissza jóslatként.

### 6.2 – Alappróba: pontosan ábrázolható tört

Eredeti két sor:

```cpp
float meres_float = 0.1f;
double meres_double = 0.1;
```

Új két sor:

```cpp
float meres_float = 0.5f;
double meres_double = 0.5;
```

Az 1/2 és a bináris helyiértékek kapcsolatára építve kérdezd:
„Hogyan indokolnád, hogy a 0,5-öt pontosan tudjuk-e tárolni ezekben a típusokban?”
Várd meg a választ. Ne jelentsd ki előbb a pontos ábrázolhatóságot. Ha az alap
még hiányzik, magyarázd el a 0,5 = 1/2 = 0,1₂ kapcsolatot; ez segített tanulás,
nem önálló jóslat. A részletes kódértést a 6.3 pont ellenőrzi.
Válasz után sorcsere, mentés, fordítás és futtatás.
**Válasz után:** nem; a két kiírás 0.5 lesz. A további három sor változatlan.
A 17 értékes jegy kérése nem ír kötelezően 17 jegyet; a felesleges nullák
alapértelmezett formázásnál nem jelennek meg.
A 0.5f és 0.5 literálok maradjanak meg. A következő megfigyelés az ettől
független reszletes_meres változóra és az utolsó három kiírásra vonatkozik.

### 6.3 – Kódértés: tárolás és kiírt számjegyek

A sikeres 0.5-ös próba után az aktuális forrásból emeld ki:

```cpp
float meres_float = 0.5f;
double meres_double = 0.5;
std::cout << std::setprecision(reszletes_szamjegyek);
```

**Kérdés:** „Melyik sor határozza meg a tárolás típusát, és melyik a kiírás módját? Magyarázd el a különbséget!” Várj.

**Oktatói támpont – csak a válasz után:** a deklarációk float és double
változót hoznak létre; az f a literál float típusát jelöli, nélküle itt double.
A setprecision a kimeneti folyam beállítása, ebben a programban fixed nélkül
értékes jegyeket kér. A reszletes_szamjegyek 17, de ettől a float nem tárol
17 értékes tízes számjegyet. A kiírás rövidebb is lehet, mint a kért jegyszám.
**Utókérdés, ha kell:** „Ha csak a setprecision értékét növeljük, mi történik a már tárolt adattal?”
**Segítség után:** gondolatban `double meres_double = 0.5f;` esetén kérdezd,
milyen típusú maga a változó. Így ellenőrizhető a literál és a változó típusának
megkülönböztetése; a fájlt nem kell módosítani.

A reszletes_meres utolsó három kiírását ezután röviden kösd a magyarázathoz,
ne újabb igen/nem kérdéssel: a forrás 1.23456789f, a 9 jegyes kiírás szokásos
binary32 esetén 1.23456788; a tárolt közelítés körülbelül 1.2345678806304932.
A bevezető nullák nem értékes jegyek: 123456,7 és 0,001234567 is hét értékes jegy.
A digits10 binary32 esetén 6, a hetedik jegy nem minden értékre garantált.
Ha a hallgató ezt már elmagyarázta, elég a rövid megerősítés.

### 6.4 – Választható: a nagy számhoz adott egy elveszhet

A hallgató az aktuális program return sora ELÉ szúrja be:

```cpp
const float nagy_ertek = 16777216.0f;
constexpr float novekmeny = 1.0f;
const float novelve = nagy_ertek + novekmeny;
std::cout << "Nagy ertek novelve: " << std::setprecision(reszletes_szamjegyek)
          << novelve << '\n';
```

Előbb a közeli ábrázolható értékek távolságát magyarázd, majd megfigyelést kérj.
Szokásos binary32 és legközelebbi értékre kerekítés mellett az eredmény 16777216.
Ez pontossági, nem értéktartomány-korlát. Kérdés: „Miért nem elég, hogy a szám
belefér a float véges tartományába?” A működő kiegészítő blokk maradjon meg a forrásban.

**Blokkzárás és forrásállapot:** A 0.5-ös adatok és az esetleges működő kiegészítés maradjanak meg. A megfigyelt közelítést ne nevezd több tárolt tizedesjegynek.

## 7. Kimenetformázás

**Forrás:** `G02_07_formazas.cpp`. **Cél:** a formázás és a tárolás elkülönítése.

### 7.1 – Közös értelmezés, hallgatói fordítás és futtatás

Az előző feladat setprecision hívásai alapértelmezett formátumban értékes
jegyeket adtak. Itt a fixed miatt a tizedesjegyek számát állítjuk.
Bontsd fel a tényleges láncot: cout a kimeneti folyam; fixed a mód beállítása;
setprecision(rovid_tizedesjegyek) a két tizedesjegy kérése; hanyados az adat;
az újsorkarakter a sortörés. A manipulátorok maguk nem írják ki a nevüket vagy
az átadott 2 értéket. A << ugyanazt a folyamot adja vissza, ezért láncolható.
A fixed a következő sorra is megmarad. A két kiírás között a hanyados változatlan.

Add ki a hallgatónak a fordítási parancsot; ő futtassa a terminálban:

```bash
g++ -std=c++20 -Wall -Wextra -pedantic G02_07_formazas.cpp -o G02_07
```

Sikeres fordítás után a hallgató futtassa a programot:

```bash
./G02_07
```

Várd meg a hallgató eredményét, és csak utána értelmezzétek a kimenetet.

**Oktatói ellenőrző adat – várt kiinduló kimenet, nem elvégzett próba:**

```text
Rovid kiiras: 0.33
Reszletes kiiras: 0.3333333333
Tarmeret bajtban: 8
```

Ez a közös bemutatás ellenőrző mintája. A későbbi önálló kérdéshez más adatot vagy
módosítást használj; a frissen látott kimenetet ne kérd vissza jóslatként.

### 7.2 – Alappróba: több kiírt tizedesjegy

Eredeti sor: `constexpr int rovid_tizedesjegyek = 2;`.
Új sor: `constexpr int rovid_tizedesjegyek = 6;`.
Kérdés: „A hanyados tárolt értéke és tármérete változik, vagy a megjelenítése?”
Ne keverd a hanyados változót a ténylegesen átírt rovid_tizedesjegyek beállítással.
Várd meg, majd a sorcsere után fordítás és futtatás.
**Válasz után:** csak a megjelenítés. Az első sor 0.333333,
a második 0.3333333333. A tárméret a környezet szerinti korábbi érték marad.
A pontossági paraméter elnevezését nem kell átírni: a rövid változat továbbra is
rövidebb, mint a tízjegyes kiírás.

### 7.3 – Választható: ugyanaz a formázás nagyobb számnál

A hat tizedesjegyes beállítás maradjon meg. A hallgató csak a szamlalo konstans
értékét cserélje 1.0-ról 22.0-ra. Előbb kérdezd, mit jelent fixed mellett a hat
jegy: az összes értékes jegyet vagy a tizedespont utánit? Várd meg a választ,
majd kérd a sorcserét, mentést, fordítást és siker esetén futtatást.
Várd meg az első két kimeneti sort.

**Ellenőrző adat:** az első sor 7.333333; a második szokásos binary64 esetén
7.3333333333. A hanyados értéke megváltozott, mert a számláló is változott;
az előző próba kizárólag a formázást módosította.

### Kódértés – a kiírási lánc

A sikeres formázási próba után a tényleges forrásból emeld ki:

```cpp
std::cout << "Rovid kiiras: " << std::fixed
          << std::setprecision(rovid_tizedesjegyek) << hanyados << '\n';
```

**Kérdés:** „Magyarázd el balról jobbra, melyik rész mit csinál ebben a kiírásban!” Várj.

**Oktatói támpont – csak a válasz után:** cout a kimeneti folyam, a szöveg
felirat, fixed a formázási módot állítja, setprecision a tizedesjegyek számát
adja meg ebben a módban. A hanyados az adat, az újsorkarakter sortörést ad.
A manipulátorok neve nem kerül a kimenetre; a hanyados tárolt értéke nem módosul.
A << ugyanazt a folyamot adja vissza, ezért folytatható a lánc, de belső
operátormegvalósítást nem kell ismernie. A korábban beállított 6-os értéket használd.
**Utókérdés, ha kell:** „Miért hat a fixed a következő kiírásra is?”
**Segítség után:** gondolatban három tizedesjegyes kiírásnál mondja el, melyik
beállítás változna, és érintené-e a tárolt hanyadost. A forrás maradjon meg.

**Blokkzárás és forrásállapot:** rovid_tizedesjegyek 6; szamlalo az alappróba
után 1.0, a választható próba után 22.0. Maradjon meg az elért állapot.
Ezt a különbséget a kódértési pont alapján értékeld; ne kérdezd vissza ismét.

## 8. Összehasonlítás abszolút tűréssel

**Forrás:** `G02_08_tures.cpp`. **Cél:** feladathoz és mértékegységhez kötött közelítő összehasonlítás.

### 8.1 – Közös értelmezés, hallgatói fordítás és futtatás

A változónevek a métert is jelzik: nem mindegy, milyen egységben értjük a 0.001-et.
Ez a példában egy milliméter, de a kódban méterként tároljuk.
A mert_hossz_meter megfigyelésben változtatható; az elvart_hossz_meter és a
megengedett_elteres_meter megnevezett, rögzített feladatszabály.
Magyarázd a kivonás → std::abs → összehasonlítás lépéseit. A <cmath> szükséges
az abs lebegőpontos változatához. A bool turesen_belul igazságérték, a boolalpha
true/false szöveget ír ki a 1/0 helyett. A tűrés nem általános gépi epsilon.

Add ki a hallgatónak a fordítási parancsot; ő futtassa a terminálban:

```bash
g++ -std=c++20 -Wall -Wextra -pedantic G02_08_tures.cpp -o G02_08
```

Sikeres fordítás után a hallgató futtassa a programot:

```bash
./G02_08
```

Várd meg a hallgató eredményét, és csak utána értelmezzétek a kimenetet.

**Oktatói ellenőrző adat – várt kiinduló kimenet, nem elvégzett próba:**

```text
Abszolut elteres meterben: 0.0005
Turesen belul: true
```

Ez a közös bemutatás ellenőrző mintája. A későbbi önálló kérdéshez más adatot vagy
módosítást használj; a frissen látott kimenetet ne kérd vissza jóslatként.

### 8.2 – Alappróba: nagyobb eltérés

Eredeti sor: `double mert_hossz_meter = 1.2345;`.
Új sor: `double mert_hossz_meter = 1.2360;`.
Kérdés: „Ezt a mérést elfogadja-e a kódban megadott szabály?” Várd meg, majd próba.
**Válasz után:** nem. A kiírt abszolút eltérés 0.0020 méter; turesen_belul false.
A küszöböt és a kiírás pontosságát ne módosítsátok közben.

**Eltérő kimenet esetén állj meg itt.** Az elvárt érték 1.2340, a mért érték
1.2360 mellett a matematikai abszolút eltérés 0.0020, nem 0.0015.
A `false` egyezése nem igazolja a részszámítást. Ne fogadd el és ne magyarázd
kerekítéssel a hibás különbséget. Nézd meg az aktuális elvárt és mért értéket,
a tűrést és a képletet, vagy kérd el ezeket a sorokat. A feltételezett hibát ne
állítsd tényként. Ha a forrás megfelelő, a hallgató ellenőrizze a mentést és az
utolsó sikeres fordítást/futtatást. Szükség esetén ő javítson és próbáljon újra.
A következő, azonos nagyságú ellenkező eltérésről csak ennek tisztázása után beszélj.
Például 1.2320 és 1.2360 között 0.0040 a különbség: ez más adatpár, mint a feladaté.
A feladat rögzített elvárt értékének véletlen átírása konkrét hiba; csak ezt
javíttasd, a korábbi szándékos módosításokat ne állíttasd vissza.

### 8.3 – Alappróba: az eltérés iránya

Most a mert_hossz_meter értéke legyen 1.2320 (az előző sorban 1.2360 állt).
Kérdés: „Változik-e az elfogadás attól, hogy ugyanekkora eltéréssel kisebb lett a mérés?”
Várd meg, majd próba. **Válasz után:** nem; a kiírt abszolút eltérés ismét
0.0020, a válasz false. A nyers különbség negatív, abszolút értéke pozitív.
A bináris közelítések miatt ne ígérj minden bitjében azonos belső különbséget;
a megadott formázás és a tűrés szerinti besorolás azonos.

**Megmaradó állapot:** mert_hossz_meter 1.2320; a küszöb és a formázás változatlan.
A szigorú `<` a pontosan küszöbnyi matematikai eltérést nem fogadná el;
a kezdő próbákban ne válassz küszöbre eső tizedes adatot, és ne vezess be NaN-t
vagy végtelent. Nagyon eltérő nagyságrendek relatív tűrése későbbi kitekintés.

### Kódértés – eltérésből logikai eredmény

Csak az aktuális kód és a kimenet összhangjának tisztázása után emeld ki:

```cpp
const double abszolut_elteres_meter = std::abs(mert_hossz_meter - elvart_hossz_meter);
const bool turesen_belul = abszolut_elteres_meter < megengedett_elteres_meter;
```

**Kérdés:** „Hogyan jut el ez a két sor a hosszértékektől az igaz vagy hamis eredményig?” Várj.

**Oktatói támpont – csak a válasz után:** különbségképzés, az előjeltől független
nagyság meghatározása abszolút értékkel, majd összehasonlítás a megengedett
eltéréssel. A különbség méterben van, a turesen_belul bool. A `<` szigorú
összehasonlítás. A puszta „false” nem adja meg a két sor működését.
**Utókérdés, ha kell:** „Miért szükséges az abszolút érték, ha a mérés kisebb az elvártnál?”
**Segítség után:** csak gondolatban legyen az elvárt érték 2.0 méter, a mért
1.5 méter, a tűrés 0.25 méter; vezesse végig a két sort. Az egyszerű, binárisan
pontosan ábrázolható adatokkal az értelmezést ellenőrizzük, nem a kerekítést.

**Blokkzárás és forrásállapot:** Az utolsó, 1.2320 méteres mérés maradjon meg. Az abszolút érték szerepét a kódértési pontban ellenőrizd, ne külön ismétlésként.

## 9. Összekapcsoló feladat: pontszámok

**Forrás:** `G02_09_pontszamok.cpp`. **Cél:** típusválasztás, számításjavítás és megjelenítés összekapcsolása.

### 9.1 – Közös értelmezés, hallgatói fordítás és futtatás

Ez teljes, fordítható program, de a megjelölt számításban kijelölt logikai hiba van.
A rendezett formázás és beszédes nevek önmagukban nem garantálják a helyességet.
A hallgató két 0–100 közötti egész pontszámot vizsgál. Először saját szavaival
mondja el a két adat szerepét, majd kérdezd, miért lehet az átlag törtszám.
A következő kérdést külön add: milyen típus alkalmas a pontszám és az átlag tárolására?
Ezeket külön értékeld; ne adj rögtön kész javító kódot.

A kiinduló kimenet csak a futás ellenőrzéséhez tartozik. Az eredményt vessétek
össze a kézzel kiszámított átlaggal, és az eltérésre építve folytassátok.

Add ki a hallgatónak a fordítási parancsot; ő futtassa a terminálban:

```bash
g++ -std=c++20 -Wall -Wextra -pedantic G02_09_pontszamok.cpp -o G02_09
```

Sikeres fordítás után a hallgató futtassa a programot:

```bash
./G02_09
```

Várd meg a hallgató eredményét, és csak utána értelmezzétek a kimenetet.

**Oktatói ellenőrző adat – várt kiinduló kimenet, nem elvégzett próba:**

```text
Atlagos pontszam: 77.0
Atlag szazalekban: 77.0%
```

Ez a közös bemutatás ellenőrző mintája. A későbbi önálló kérdéshez más adatot vagy
módosítást használj; a frissen látott kimenetet ne kérd vissza jóslatként.

### 9.2 – Alapfeladat: a számítás önálló javítása

Az eltérés megfigyelése után kérdezd: „Hogyan javítanád az átlag számítását,
és miért oldaná meg a javaslatod a törtrész elvesztését?” Várd meg.
Ne mutasd meg előbb a hibás sort azzal a kérdéssel, hogy melyik sor hibás.
Ha már kiemelted a sort, annak működését és javítását indokoltassa a kérdés.
A hallgató ne az egész programot írja újra; először saját javaslatot adjon.

Segítség fokozatosan, csak ha szükséges:
1. Mutass az atlag_pontszam képletére, és kérdezd az operandusok típusát.
2. Emlékeztesd a művelet ELŐTTI konverzióra.
3. Végül mutasd a cserét, és jelöld segített megoldásnak.

Eredeti:

```cpp
const double atlag_pontszam = osszes_pont / hallgatok_szama;
```

Javított:

```cpp
const double atlag_pontszam = static_cast<double>(osszes_pont) / hallgatok_szama;
```

Elfogadható a nevező előzetes double-lé alakítása is. A számláló és nevező
int változójának puszta átnevezése, vagy a célváltozó ismételt double-lé tétele
nem javítás. Megfelelő más megoldást is fogadj el, ha a hallgató megindokolja.

Mentés, fordítás, futtatás: Atlagos pontszam: 77.5; Atlag szazalekban: 77.5%.
A hibapróbát jelző kommentet a hallgató a sikeres javítás után törölje: a helyes kódban
már félrevezető lenne. Az új képlet maradjon meg.

### 9.3 – Alapfeladat: két tizedesjegy

Kérdés: „Hogyan állítanád be a programban, hogy az átlag két tizedesjeggyel jelenjen meg?”
Ne emeld ki előre a módosítandó beállítást. Várd meg. Szükség esetén csere:
`constexpr int kiirt_tizedesjegyek = 1;` → `constexpr int kiirt_tizedesjegyek = 2;`.
Mentés, fordítás, futtatás után 77.50 és 77.50% jelenik meg. A tárolt átlag
ettől nem változott. Ez a beállítás is megmarad.

### 9.4 – Alappróba: új, még nem megoldott adat

A javított programban elso_pontszam legyen 73, masodik_pontszam legyen 88.
Előbb kérd a várt átlagot és rövid indoklását. A „80,5%” önmagában nem
pontátlag-magyarázat: szükség esetén kérdezz rá, hogy pontot vagy százalékot
nevezett meg. Csak ezután jöhet a két sor módosítása,
mentés, fordítás és siker esetén futtatás. **Válasz után:** 80.50 és 80.50%.
Ha a jóslatot a tutor mondta meg, más új párt használj vagy jelöld segítettnek;
például 90 és 95 esetén 92.50 és 92.50%.

### 9.5 – Kódértés: pontátlag és százalék

A javított, sikeresen kipróbált programból emeld ki a két számítást:

```cpp
const double atlag_pontszam = static_cast<double>(osszes_pont) / hallgatok_szama;
const double atlag_szazalek = atlag_pontszam / maximalis_pontszam * szazalek_szorzo;
```

**Kérdés:** „Mondd el, mit számít ki ez a két sor, és mit jelentenek az eredmények!” Várj.

**Oktatói támpont – csak a válasz után:** az első összpontból pontátlagot számít,
a konverzió az osztás előtt történik. A második a pontátlagot a maximális
pontszámhoz viszonyítja, majd 100-zal szorozza. A pont és százalék külön jelentés;
a 100-as maximum miatt egyezik a két számérték. A maximalis_pontszam és a
szazalek_szorzo eltérő szerepű állandó. A const az eredmények későbbi átírását tiltja.
Más helyes átlagképletnél a hallgató saját sorát értelmeztesd.
**Utókérdés, ha kell:** „Melyik eredményt érintené, ha több pontot lehetne elérni ugyanebben a dolgozatban?”
**Segítség után:** gondolatban 60 pont és 120-as maximum esetén magyarázza el
a második képletet. A várt 50%-ot ne mondd meg előre. Nincs szükség új futtatásra.
Ha az értelmezés továbbra is bizonytalan, ezt jelezd a lezárásban; a sikeres
programfuttatás nem bizonyítja önmagában a fogalom megértését.

Választható tényleges próba a javított 73/88 adatokkal: maximalis_pontszam 120.
Előbb jóslat és indoklás, utána a hallgató módosítson, mentsen, fordítson és
siker esetén futtasson; várd meg a kimenetet. Oktatói ellenőrző adat: a pontátlag
80.50 marad, a százalék szokásos környezetben 67.08%. A módosítás megmarad.

**Megőrzendő végállapot:** helyes átlagképlet, kiirt_tizedesjegyek 2,
elso_pontszam 73, masodik_pontszam 88; a hibajelző komment nélkül.
A maximalis_pontszam az alapútvonalon 100, a választható próba után 120 marad.
Az alapútvonal kimenete 80.50 és 80.50%; a választható próba után 80.50 és 67.08%.
Más, önállóan választott adatpárnál az annak megfelelő helyes eredményt fogadd el.
A forrás maradjon tiszta és fordítható; ne kérj újabb módosítást a lezárásért.

**Blokkzárás és forrásállapot:** A javított programot őrizzük meg; ez a hallgató elkészült eredménye.

## K01 – Választható, ellenőrzött túlcsordulási bemutató

**Forrás:** `G02_K01_tulcsordulas.cpp`. Nem része az alapútvonalnak.
Előtte egyszer egyeztess a hallgatóval. Ha nem kéri, kihagyva zárd le.
A szállított forrás helyes és fordítható; kezdeti kimenete `Teljes ar: 2500000000`.
A bemutató egyetlen szándékos hibás módosítása a művelet előtti cast elvétele.

### K01.1 – Feltételek és helyes kiinduló futás

Az 1. feladat eredményéből igazold, hogy a környezet int felső határa 2147483647.
Ha ettől eltér, ezt a konkrét bemutatót ne futtasd változatlan feltételezésekkel.
Mondd el előre: a hibás változattól nem várunk konkrét számeredményt;
a futásidejű hibafelismerést figyeljük meg.

Kérd a hallgatót, hogy a helyes kódot már ellenőrzéssel fordítsa le:

```bash
g++ -std=c++20 -Wall -Wextra -pedantic -O0 -fsanitize=undefined -fno-sanitize-recover=undefined G02_K01_tulcsordulas.cpp -o G02_K01_ellenorzott
```

Sikeres fordítás után a hallgató adja ki:

```bash
./G02_K01_ellenorzott
```

A `-fsanitize=undefined` futásidejű ellenőrzést ad a programhoz; a
`-fno-sanitize-recover=undefined` az észlelt hibánál megállítja. A `-O0` itt
kikapcsolja a szokásos optimalizálást, de önmagában nem teszi szabályossá a hibás kódot.
Ha a kapcsoló vagy futásidejű könyvtár nem használható, állj meg ennél a kiegészítőnél:
ne próbáld a hibás változatot ellenőrzés nélkül, és ne indíts környezeti telepítési kitérőt.

### K01.2 – Hibás szorzás felismerése

Eredeti sor:

```cpp
const long long teljes_ar = static_cast<long long>(darabszam) * egysegar;
```

Ideiglenes, szándékosan hibás sor:

```cpp
const long long teljes_ar = darabszam * egysegar;
```

Kérdés: „Miért nem véd meg önmagában a long long célváltozó?” Várd meg.
**Válasz után:** a két int operandus szorzása túlcsordul, mielőtt az eredmény
long long-ba kerülne. Nem definiált viselkedés; nem ígérünk körbefordulást vagy
szó szerinti számeredményt.

A hallgató végezze el a módosítást és mentést, majd ugyanazzal a TELJES
ellenőrzött fordítási paranccsal készítse el a programot. Csak sikeres fordítás
után futtassa. Kérd az érintett hibaüzenetet, és várd meg a visszajelzését. Az eszköz a hibás szorzásnál
signed integer overflow jellegű diagnosztikát ad, és a program hibás állapottal leáll.
Ez a hibakimenet nem a `std::cout` normál eredménye. A pontos szöveg, útvonal és
sorszám függ a környezettől. Elegendő az érintett hibaüzenet; hosszú naplót ne kérj.
A művelet túlcsordulását javítjuk, nem a hibajelzést kapcsoljuk ki.

### K01.3 – A túlcsordulási hiba javítása

Kérd a hallgatótól a hibás szorzás javítását a művelet előtti static_cast
alkalmazásával és a mentést. A fájl minden más működő módosítása maradjon meg.
Ő fordítson ugyanazzal az ellenőrzött paranccsal, majd siker esetén futtasson.
Várd meg a beszámolóját: a várt eredmény ismét 2500000000 hiba nélkül. Csak ezután
tekintsd lezártnak a bemutatót. A végleges forrás helyes marad.

### Kódértés – K01 javításának indoklása

Ha a kiegészítőt elvégezték, a sikeres javítás után a tényleges helyes szorzási
sort mutasd: „Magyarázd el, hogyan akadályozza meg a javítás a korábbi túlcsordulást!”
Várj. A művelet előtti konverzió és a szorzás típusa a lényeg, nem a hibajelzés
kikapcsolása. Ha ezt a K01.2-ben már önállóan indokolta, számítsd be és ne ismételd.
Segítség után a másik operandus előzetes konverzióját értelmeztesd gondolatban;
ne kérj újabb hibás futtatást.

## Lezárás – 10 perc

Először rövid, összefüggő visszatekintés, utána az aktuális bizonytalanságra
célzott néhány kérdés. Ne add ki egyszerre a teljes listát, és ne minősítsd
kötelező új vizsgának. A feladatsorban már igazolt megértést nem kell újra bizonyíttatni.

- Mit mér a sizeof, és hogyan kapunk belőle bitszámot?
- Miért −1 a 11111111, és miért −127 a 10000001 kettes komplemensben?
- Miért számít a konverzió helye egy osztásban vagy szorzásban?
- Mi a különbség az értéktartomány és a pontosság korlátja között?
- Miért nem lesz pontosabb a változó, ha több tizedesjegyet írunk ki?
- Milyen szerepe van az abszolút értéknek és a mértékegységnek a tűrésnél?
- A saját javított programban melyik név vagy állandó teszi érthetőbbé a kódot?

A lezárás nevezze meg a ténylegesen elvégzett alapfeladatokat, a segített és
önálló alkalmazást, valamint a folytatás helyét. A technikai akadályt külön kezeld.
A javított 9. forrás a hallgató elkészült eredménye. A következő elméleti témák
az összetett feltételek és elágazások; most ne indíts új, előre nem tervezett feladatot.
