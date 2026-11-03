# EP_08 – Fájlkezelés és szövegfeldolgozás a büfében

Két 45 perces magyar nyelvű gyakorlat az EP_08.html után. A HTML mérési és könyvtári mintáinak módszerét új, rendelési és visszajelzési adatokon alkalmazod. A kezdőfájlok futtathatók, de helykitöltő eredményeket adnak: a célmegoldást te írod meg.

A tutor minden új fájl előtt elmagyarázza a bemenetet, a feldolgozást, a kimenetet és az adott részeket. Egy összetartozó változtatást kér egyszerre. Te szerkesztesz, mentesz és a Futtatás gombbal futtatsz. A programozási részben nincs előzetes kimenetjóslás. A kódismereti záróteszt külön szakasz.

A ZIP-et új, üres munkatér gyökerébe bontsd ki. A .py, .txt, agent.md és preset.json fájlok egymás mellett legyenek. A Futtatás gomb munkamappája a megnyitott program mappája legyen; a relatív fájlnév ehhez viszonyul, nem automatikusan a .py helyéhez. Nincs feladatonkénti mappaváltás. Az adatfájlok UTF-8 kódolásúak. A minták nem kérnek inputot.

Futtatás után az új vagy átírt fájlt is nyisd meg. Ha a fájlnézet nem frissül, frissítsd a nézetet vagy nyisd meg újra a fájlt. A terminál sikeres befejezése önmagában nem bizonyít helyes mentést.

## Időterv

| Első 45 perc | Perc | Második 45 perc | Perc |
| --- | --- | --- | --- |
| Bemutatkozás és érdemi kezdés | 2 | B1.b – Tárolt árak összesítése | 6 |
| A1 – Rendelés beolvasása | 8 | Z1 – Önálló termékjelentés | 12 |
| A2 – Keresett kulcsszavak | 12 | T1 – Elméleti teszt | 10 |
| A3.a/b – Friss blokk mentése | 13 | T2 – Kódismereti teszt | 15 |
| B1.a – Tartós eladási napló | 8 | S2 – Értékelés és lezárás | 2 |
| S1 – Rövid összegzés | 2 | | |
| **Összesen** | **45** | **Összesen** | **45** |

A szünet a 90 percen kívül van. Az időterv tömörített becslés, a magyarázatok és a próbák is részei. Lassabb haladásnál pontos folytatási pont marad. A két teszt és lezárás 27 percét fenntartjuk; a C1 csak tényleges időnyereségből választható.

## Adatok és kimenetek

- Változatlan bemenetek: rendelesek.txt, rendeles_valtott.txt, velemenyek.txt, velemeny_rovid.txt, eladas_minta.txt, eladas_valtott.txt, naplo_proba.txt, naplo_regi_arak.txt, ures.txt. Pontos tartalmuk: adatok.md.
- A saját program készíti: blokk.txt, eladasok.txt, termek_jelentes.txt; C1-ben napi_riport.txt. Kezdetben ezek nincsenek a csomagban.
- A rövid analóg írásminták kizárólag a pelda_felirat.txt fájlba írnak. A feladatok ezt nem használják bemenetként.
- A próbákhoz többnyire a főprogram fájlnevét, keresett értékét vagy próbaárát módosítod; az eredeti adatfájlokat nem kell szerkesztened. A korábbi kimenetet ne használd véletlenül új bemenetként.

## A1 – Rendelés a szövegfájlból

**Fájl:** `rendeles.py`. **Tervezett idő:** 8 perc.

### Mit csinál majd a program?

A fájl egy sora egy megrendelt darab. A rendelest_beolvas függvény listát ad vissza; a hívó a listát és darabszámát mutatja. Az ismétlődés itt többszöri vásárlást jelent.

### Mi adott, és mit írsz te?

A függvény neve, fájlnévparamétere és a próbahívás adott. A return [] helykitöltő; még egyetlen sort sem olvas. A rendelesek.txt-ben szélső szóköz, üres sor és sortörés nélküli utolsó sor is van. Minden nem üres, tisztított név szerepel az alapárjegyzékben.

### Rövid analóg minta

```python
with open("ures.txt", "r", encoding="utf-8") as fajl:
    elso = fajl.readline()
print(repr(elso))
```

Az open szöveges fájlobjektumot ad, a readline egy szöveget. A valóban üres ures.txt első olvasásának eredménye "", vagyis már fájlvég van. Egy üres sor viszont "\n" lenne. A with a blokk végén lezárja a fájlt. A saját feladatban minden sort bejársz, a név szélét tisztítod és a nem üreseket összegyűjtöd.

### Most te alakítsd át

1. A függvényben r móddal, UTF-8-ként nyisd meg a paraméterben kapott fájlt.
2. Járd be a sorokat. A sor.strip() eredményét kezeld terméknévként; az üres tisztított sort hagyd ki. A többit sorrendben gyűjtsd listába.
3. A listát az egész bejárás után add vissza; a függvény ne írjon ki és ne módosítsa a forrásfájlt.
4. Ments, futtass, majd a próbahívás fájlnevét változtatva végezd el a három próbát.

### Kész, ha

- Új lista az eredmény; a sorrend és az ismétlődő kávé megmarad.
- A szélső whitespace és az üres sor a kimondott szabály szerint eltűnik.
- Fájlnévparaméterből dolgozik; üres fájlt is kezel; minden szükséges próba ismert.

### Próbák

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| A1.1 | `rendelesek.txt` | `["kávé", "szendvics", "kávé", "üdítő"]`, darab 4. A forrás 5 fizikai sora közül az üres kimarad. |
| A1.2 | `rendeles_valtott.txt` | `["tea", "víz", "tea"]`, darab 3. Csak a fájlnév változik. |
| A1.3 | `ures.txt` | `[]`, darab 0; nincs hiba. |

Kapcsolódó magyarázat: [EP_08.html](EP_08.html#szamadatok).

## A2 – Csak a keresett kulcsszavak gyakorisága

**Fájl:** `velemeny.py`. **Tervezett idő:** 12 perc.

### Mit csinál majd a program?

A büfé szöveges visszajelzéseiből csak a paraméterként megadott szavakat számolod. Az eredmény minden keresett szóhoz egész darabszámot rendel, találat nélkül is nullát.

### Mi adott, és mit írsz te?

A kulcsszóhalmaz már kisbetűs, nem üres, írásjel nélküli neveket tartalmaz. A return {} most helykitöltő. A szó itt whitespace mentén kapott darab, kisbetűsítve, majd a szélein a . , ! ? ; : " ( ) karakterektől megtisztítva. Belső karaktert nem törlünk; teljes nyelvi elemzés nem cél.

### Rövid analóg minta

```python
nyers = "(CSENDES!)"
szo = nyers.lower().strip(".,!?;:\"()")
print(szo)
print(szo in {"csendes", "világos"})
```

A lower új, kisbetűs szöveget ad. A strip argumentuma levágható karakterek gyűjteménye, nem egyben keresett részszöveg. A minta csak egy darabot tisztít és tagságot vizsgál. A saját feladatban fájlsorokat darabolsz split()-tel, és a keresett kulcsok számlálóját frissíted.

### Most te alakítsd át

1. A megadott kulcsszavak mindegyikéhez hozz létre 0 kezdőértéket az eredményszótárban.
2. with és for segítségével olvasd a sorokat; a sor.split() szavait külön dolgozd fel.
3. A kimondott szabállyal tisztíts. Csak a keresett kulcsszó számlálóját növeld; a többi szó és a tisztítás után üres darab ne kerüljön be kulcsként.
4. A teljes bejárás után add vissza a szótárat. A kulcsszóhalmaz és a fájl maradjon változatlan. Végezd el az A2-próbákat.

### Kész, ha

- Pontosan a paraméterként kapott kulcsok szerepelnek az eredményben, egész értékkel; a hiányzó is 0.
- A kis-/nagybetű és a megadott szélső írásjelek kezelése helyes.
- Nem az összes szó gyakoriságát adja; nem égeti be a finom/gyors/olcsó neveket. A bemenetek megmaradnak.

### Próbák

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| A2.1 | `velemenyek.txt`; `{ "finom", "gyors", "olcsó" }` | `{"finom": 2, "gyors": 2, "olcsó": 0}`. Más szó nem kulcs. A szótár sorrendje közömbös. |
| A2.2 | `velemeny_rovid.txt`; ugyanaz a kulcsszóhalmaz | `{"finom": 1, "gyors": 2, "olcsó": 1}`. A csak írásjelből álló darabok nem számítanak. |
| A2.3 | `ures.txt`; ugyanaz a kulcsszóhalmaz | `{"finom": 0, "gyors": 0, "olcsó": 0}`; nem üres szótár. |
| A2.4 | `velemenyek.txt`; `{"kávé", "drága", "hiányzik"}` | `{"kávé": 2, "drága": 1, "hiányzik": 0}`. A kulcsszavak paraméterből származnak. |

Kapcsolódó magyarázat: [EP_08.html](EP_08.html#szovegstatisztika).

## A3.a – Blokk tételsorai

**Fájl:** `blokk.py`. **Tervezett idő:** 6 perc.

### Mit csinál majd a program?

Az A1 saját beolvasójának eredményéből friss blokkot készítesz. Egy rendelési darab egy tételsor, névvel és az árjegyzékből vett árral. A blokk nem az eredeti rendelési fájl.

### Mi adott, és mit írsz te?

A két függvény aláírása, az árjegyzék és a főprogram adott. A beolvasó [] és a mentő pass része még helykitöltő. Az A1-ben már megírt saját beolvasó definícióját hozd át; a főprogramját ne. Az árak egész, nemnegatív forintértékek. A kosár minden neve ismert kulcs; a 0 ár érvényes.

### Rövid analóg minta

```python
with open("pelda_felirat.txt", "w", encoding="utf-8") as fajl:
    fajl.write("Első felirat\n")
    fajl.write("Második felirat\n")
```

A w a megnyitáskor kiüríti a meglévő célt, vagy létrehozza. A write nem ad hozzá automatikusan sortörést, ezért a mintában mindkét szöveg végén szerepel a \n. A saját blokk sorait a kosárból és az árjegyzékből állítod elő; ezt nem végzi el helyetted a minta.

### Most te alakítsd át

1. A saját A1-függvényed definíciójával váltsd ki a beolvasó helykitöltőjét.
2. A blokkot_ment a fajlnev paraméterbe w móddal írjon. A kosarat járd be: egy névhez az arak paraméterből vedd az árat.
3. Minden darab külön, sortöréssel lezárt sorba kerüljön, például kávé: 450 Ft. Az ismétlődéseket ne vond össze.
4. Futtasd és nyisd meg a blokk.txt-t. Ha nem jelenik meg rögtön, frissítsd a munkatér fájlnézetét. Most a tételsorokat ellenőrizzük; az összesítő az A3.b része.

### Kész, ha

- Az A1 saját beolvasója dolgozik; négy, helyes sorrendű tételsor készül.
- A mentő a kapott kosárból és árjegyzékből dolgozik, a bemeneteket nem módosítja.
- Külön célfájlt ír, minden tételsor végén van sortörés.

### Próbák

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| A3.a.1 | Az A1 saját függvénye; `rendelesek.txt`; alapárak | Négy tételsor, ebben a sorrendben: `kávé: 450 Ft`, `szendvics: 890 Ft`, `kávé: 450 Ft`, `üdítő: 390 Ft`. Mindegyik külön sor; végső összesítő még nem követelmény. |

Kapcsolódó magyarázat: [EP_08.html](EP_08.html#iras).

## A3.b – Blokkösszeg és felülírás ellenőrzése

**Fájl:** `blokk.py`. **Tervezett idő:** 7 perc.

### Mit csinál majd a program?

A tételsorok után egy összesítő sort mentesz. A második futás új blokkot készít, ezért a régi rendelés sorai nem maradhatnak a fájlban.

### Mi adott, és mit írsz te?

Az A3.a saját tételkiírásod már megvan. Ugyanabban a mentő függvényben kell az aktuális árak összegét számítani. Nincs mennyiségmező: egy kosárelem egy darab, ezért a két kávé kétszer ad árat.

A w a fájl megnyitásakor hat, nem csak akkor, amikor az első nem üres tételt kiírjuk. Ezért üres kosárnál is friss cél készül. A 0 kezdőösszeg az üres kosárhoz is helyes.

### Most te alakítsd át

1. A tételsorok bejárása alatt az aktuális árakat add össze.
2. A ciklus után, de az írási with blokkon belül írj egy Összesen: … Ft sort, sortöréssel. A függvény ne printtel helyettesítse a fájlírást.
3. Végezd el az alap-, ismételt, üres és módosított adatú próbát. Újraolvasás vagy a fájl megnyitása igazolja a mentést.
4. Az alapárak átállítása és a bemeneti fájl cseréje a főprogram próbaadata; a feldolgozó függvényt ne írd át.

### Kész, ha

- Az összeg az aktuális kosár minden darabjának aktuális árából készül.
- A végső összesítő mindig pontosan egy sor; üres kosárnál is elkészül 0 Ft-tal.
- Az ismételt futás nem dupláz, új rendelés után nem marad régi sor. A normatív próbák ismertek.

### Próbák

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| A3.b.1 | Az alapadatok teljes blokkja | A négy tételsor után `Összesen: 2180 Ft`. Összesen 5, sortöréssel lezárt sor. |
| A3.b.2 | Ugyanazt a blokkot készítsd el még egyszer | Továbbra is ugyanaz az 5 sor; nincs duplázódás. |
| A3.b.3 | A kosár forrása `ures.txt` | A cél egyetlen sora `Összesen: 0 Ft`. Az előző tételek eltűnnek. |
| A3.b.4 | A kosár forrása `rendeles_valtott.txt`; az árjegyzékben a tea árát előbb állítsd 400-ra | Tételárak 400, 0, 400 Ft; utolsó sor `Összesen: 800 Ft`. Nem változik a feldolgozó kód. |

Kapcsolódó magyarázat: [EP_08.html](EP_08.html#iras).

## B1.a – Eladási események hozzáfűzése

**Fájl:** `naplo.py`. **Tervezett idő:** 8 perc.

### Mit csinál majd a program?

A blokk friss eredményt mutatott; a napló több programfutás eladásait őrzi. Minden eladott darabhoz eltárolod a nevét és az akkori árát, pontosvesszővel elválasztva.

### Mi adott, és mit írsz te?

A mentő és a még nem kész B1.b-összesítő aláírása adott. A főprogramban a mentes_bekapcsolva True, a kosár két darab: kávé és tea. Az eladasok.txt nincs a csomagban: a saját mentőd első helyes futása hozza létre. A két helykitöltő kezdetben 0, 0 kiírást eredményez, fájlírás nélkül.

### Rövid analóg minta

```python
with open("pelda_felirat.txt", "a", encoding="utf-8") as fajl:
    fajl.write("Új megjegyzés.\n")
```

Az a megőrzi a korábbi tartalmat, és a végére ír. A pontosvesszős rekordban a terméknév és az ár külön mező. A saját fájl első sorának például kávé;450 alakúnak kell lennie, nem blokkfeliratnak. A terméknevek nem tartalmaznak pontosvesszőt vagy sortörést; az ár érvényes, nemnegatív egész.

### Most te alakítsd át

1. A vasarlasokat_ment a kapott fájlnevet a móddal nyissa.
2. A kosár minden darabjához a paraméterként kapott árjegyzékből vett aktuális árat írja: terméknév;pontos_egész_ár, a végén sortöréssel.
3. Új munkatérben először egyszer, majd ugyanazt még egyszer futtasd a fájl megtartásával. Nyisd meg/frissítsd a fájlnézetet, és az eladasok.txt sorait ellenőrizd.
4. Ebben a részben a naplot_osszesit még helykitöltő marad: a terminál 0-ja nem a mentett fájl valódi összesítése. A két ismert hozzáfűzés után ne indíts felesleges újabb mentést.

### Kész, ha

- Első futáskor létrehozza a naplót; minden darab saját, kétmezős, sortöréssel lezárt rekord.
- A második futás megőrzi a korábbi sorokat és még kettőt hozzáfűz.
- A bemeneti kosár és árjegyzék változatlan; a B1.b kiírása még nem kész eredmény.

### Próbák

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| B1.a.1 | Új munkatérben eladasok.txt még nincs. Alapárak, kosár `["kávé", "tea"]`; mentes_bekapcsolva=True; egy futás | A fájl két sora: `kávé;450` és `tea;350`. Mindkettő sortöréssel lezárt. A B1.b kiírása most még helykitöltő. |
| B1.a.2 | Ugyanazzal a kóddal/adattal még egy futás, a fájl megtartásával | A fájl négy sora a két előző sor kétszeri ismétlése. A korábbi sorok megmaradnak. A `naplo_proba.txt` ennek változatlan ellenőrző mása. |

Kapcsolódó magyarázat: [EP_08.html](EP_08.html#hozzafuzes).

## S1 – Két perc összegzés

A már kész saját program alapján röviden foglald össze: mit őriz meg a rendelési lista, miért marad nulla kulcs az A2-ben, és miért eltérő a blokk és napló megnyitási módja. Nem új program vagy kötelező szóbeli vizsga. A B1.a után a folytatás B1.b; a naplót és a kész kódot ne állítsd vissza.

## B1.b – A napló saját árai alapján összesítünk

**Fájl:** `naplo.py`. **Tervezett idő:** 6 perc.

### Mit csinál majd a program?

A kétmezős sorból nevet és tárolt árat olvasol. Minden rekord egy darab; a bevételt a fájlban rögzített árakból számítod. A mai árjegyzék később változhat, a régi eladás bevétele ettől nem változik.

### Mi adott, és mit írsz te?

A B1.a saját mentője megmarad. Mielőtt olvasási próbát futtatsz, állítsd False-ra a mentes_bekapcsolva változót, így a próba nem fűz hozzá új adatot. A naplo_proba.txt és naplo_regi_arak.txt változatlan tesztbemenet, nem a saját eladasok.txt naplód. A fájlok minden nem üres sora pontosan két mező; az ár egész és nemnegatív.

### Rövid analóg minta

```python
sor = "R12;7\n"
azonosito, szam_szoveg = sor.strip().split(";")
ertek = int(szam_szoveg)
print(azonosito, ertek + 1)
```

A strip a sor szélét tisztítja, a split(";") két szöveges mezőt készít, a kicsomagolás nevet ad nekik. A második mező int után számként összegezhető. Ez kötött formátumú szöveg, nem teljes CSV-kezelés. A saját függvény nem keresi újra az árat az arak szótárban.

### Most te alakítsd át

1. False mentési kapcsolóval a naplo_fajl értékét előbb naplo_proba.txt-re állítsd. A mentőhöz most ne nyúlj.
2. A naplot_osszesit a sorokat r/UTF-8 móddal járja be. A tisztítás után üres sort hagyja ki; a többit bontsa névre és árra.
3. Minden rekord növelje a darabszámot; a konvertált tárolt ár a bevételt. A teljes bejárás után (darab, bevetel) tuple térjen vissza.
4. Végezd el a három olvasási próbát False kapcsolóval. A próba után a saját eladasok.txt is olvasható ugyanígy, új mentés nélkül.

### Kész, ha

- A darabszám minden rekordot számol, a nulla árút is; a bevétel a tárolt árak összege.
- (0,0) az üres eredmény; általánosan két egészből álló tuple tér vissza.
- A függvény csak olvas; nem használ globális árjegyzéket; a kötelező próbák nem változtatják a tesztfájlokat.

### Próbák

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| B1.b.1 | Előbb mentes_bekapcsolva=False; naplo_fajl="naplo_proba.txt"; alapárak | Visszatérés `(4, 1600)`; a fájl tartalma változatlan. |
| B1.b.2 | False marad; naplo_fajl="naplo_regi_arak.txt"; a kávé jelenlegi árát állítsd 999-re | `(3, 1150)`; a régi, fájlban tárolt 400, 450, 300 Ft számít. Az aktuális árjegyzék nem adatforrás. |
| B1.b.3 | False marad; naplo_fajl="ures.txt" | `(0, 0)`; a bemeneti fájl továbbra is 0 bájtos. |

Kapcsolódó magyarázat: [EP_08.html](EP_08.html#mezok).

## Z1 – Önálló termékjelentés

12 perc. Részletes követelmények és próbák: [zaro_feladatok.md](zaro_feladatok.md). Először saját megoldást készítesz; a tutor a célt és az előfeltételeket mondja el, kész algoritmust nem ad előre.

## C1 – Egyetlen választható bővítés

Összes termék napi riportja, 15 perc. Csak Z1 után, a tesztek előtt, legalább 42 ténylegesen fennmaradó perc esetén. Részletek: [bovites.md](bovites.md). A teljes tervezett út C1-gyel 105 perc; a 90 percbe csak gyorsabb tényleges haladással fér. Nincs automatikus második extra vagy kötelező házi feladat.

## T1 és T2 – Két záróteszt

T1: 10 feleletválasztós elméleti kérdés, 10 perc. T2: 5 kódértelmezési és 5 hibakeresési kérdés, 15 perc. A tutor alapból ötös csoportokban mutatja a teljes kérdéseket, kérésre egyesével. A kezdeti önálló válaszadás alatt a tesztkódokat nem futtatod és a megoldókulcsot nem nyitod meg. A teljes T2 után közösen értékeltek, és javításkor már futtathatsz. Ez gyakorló teszt, a munkatérben elérhető kulcs miatt nem titkos vizsga.

## S2 – Lezárás

2 perc. A tutor külön összegzi a programozási munka állapotát, a tesztek pontszámait és a segítséggel javított részeket. Ha valami hiányzik, pontos folytatási pontot ad. Ezután az óra véget ér; új feladat nem indul automatikusan.
