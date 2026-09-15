# EP_02 – te írod a következő programrészt

**Két 45 perces óra.** A korábbi büféprogramból saját függvényekkel és döntésekkel működő változatot készítesz. A tutor minden új elem célját és működését elmagyarázza, rövid mintát ad, majd te írod be a saját módosításodat. A programot elmented, futtatod, és az eredmény alapján javítod.

A munkamenet: **cél és magyarázat → rövid minta → saját kódírás → mentés → Futtatás → megbeszélés**. A várt eredmények ellenőrzési feltételek: nem kell őket előre kitalálnod. A fő feladat most a működő kód elkészítése.

A minták működő kiindulópontok. Új függvényt mindig a fájl elején, a hívások elé írj, az előző függvény után két üres sort hagyva. A meglévő saját megoldásaidat a későbbi feladatban felhasználhatod. A teljes fájlt csak akkor cseréld le, ha az instrukció ezt kéri; általában néhány sort módosítunk vagy egy függvényt adunk hozzá.

| Szakasz | Fájl a python_gyakorlat mappában | Tervezett idő |
|---|---|---:|
| E0 – első futás és mentés | koszontes.py | 5 perc |
| F1 – saját köszöntő függvény | koszontes.py | 10 perc |
| F2 – számoló függvény returnnel | tetel.py | 15 perc |
| B1 – a büfé számításának átszervezése | bufe_02.py | 12 perc |
| S1 – első óra összegzése | a meglévő fájlok | 3 perc |
| D1 – kedvezmény és fizetés | dontes.py | 12 perc |
| D2 – egy rendeléskategória kiválasztása | kategoriak.py | 7 perc |
| B2 – összeépítés | bufe_02.py | 16 perc |
| Z1 – önálló kódírás | onallo.py | 7 perc |
| S2 – lezárás | a meglévő fájlok | 3 perc |

Az összes `.py` ugyanabban a mappában van. A [részletes HTML](EP_02.html) a fogalmakhoz ad további segítséget; itt a munkalap feladatait kövesd. A HTML olvasási és jóslási gyakorlatai ezen az órán nem külön teendők.

## E0 – a megfelelő fájlt indítsuk el

**Cél:** a szerkesztőben megváltoztatott, elmentett program induljon a Futtatás gombbal. A szerkesztőben Python-kódot írsz; a terminálban parancsot adsz ki vagy a már futó program kérdésére válaszolsz.

1. Nyisd meg a `python_gyakorlat/koszontes.py` fájlt az Inno Agent szerkesztőjében.
2. A Futtatás gomb a fájl munkatérhez viszonyított útvonalát kezeli. **Ne lépj be előtte a `python_gyakorlat` almappába.** A szokásos használathoz nem kell `pwd`, `ls` vagy könyvtárváltás; ezek csak futtatási hiba esetén segítenek.

3. A megnyitott fájlban csak a köszöntés szövegét cseréld erre: `Szia, kezdjük a második gyakorlatot!` A `def` sorhoz egyelőre ne nyúlj; a következő részben elmagyarázzuk.
4. Ments, majd kattints a **Futtatás** gombra. A megváltoztatott mondat jelenjen meg.

A megfelelő `.py` fájlt nyisd meg és minden módosítás után mentsd el. Fájlváltáskor nem kell külön mappát váltanod a terminálban; a Run gomb adja a futtatandó fájl útvonalát.

Ha a gomb nem indul, a tutorral ellenőrizzétek a hibát. A munkatér gyökeréből a kézi tartalék:

```bash
python3 python_gyakorlat/koszontes.py
```

Ha egy korábbi utasítás miatt már a munkatér közvetlen `python_gyakorlat` almappájába léptél, és a Run-hibában kétszer szerepel ez a mappanév, a shellben egyszer `cd ..` paranccsal térj vissza a munkatér gyökerébe, majd használd újra a Run gombot. Csak ennél az igazolt mappahelyzetnél kell ez a helyreállítás.

Ha a régi szöveg látszik, előbb a mentést és a megnyitott/futtatott fájlt ellenőrizd. Ha fájlhiányt kapsz, a `pwd` és `ls` segít. Ha a program kérdésre vár, a választ írd be és nyomj Entert; ne indíts újabb futást. A Futtatás gomb hibája nem feltétlenül Python-kódhiba.

**Kész, ha:** az általad átírt mondat jelent meg az elmentett fájl futásakor.

## F1 – a köszöntés kapjon adatot

**Fájl:** `koszontes.py`. **Cél:** ugyanaz a függvény különböző vendégeket tudjon megszólítani.

### Előbb értsük meg

A `def` egy függvényt hoz létre. A neve megmondja, milyen műveletet végez. A kettőspont utáni, négy szóközzel behúzott sorok a törzséhez tartoznak. Ezeket a sorokat a függvényhívás indítja el. A fájlban most ezt a szerkezetet látod; az E0-ban a kiírt mondatot már átírtad:

```python
def koszont():
    print("Szia, üdv a büfében!")


koszont()
```

Ez egy teljes kiinduló program. A `def` önmagában még nem köszön. Az alsó `koszont()` sor hívja meg a függvényt. A zárójelpár adat nélkül is szükséges.

Ha a fejlécben egy nevet adunk meg a zárójelben, az **paraméter** lesz: a híváskor átadott adatot ezen a néven használhatjuk. A hívás konkrét adata az **argumentum**. Rövid, külön szemléltető minta:

```python
def termeket_mutat(termek_neve):
    print(f"Mai ajánlat: {termek_neve}")


termeket_mutat("tea")
```

A `termek_neve` paraméter a hívásban kapott `"tea"` szöveget jelöli, ezt helyettesíti az f-string. A minta célja az adatátadás megmutatása; nem kell külön fájlba másolnod.

### Most te írd meg

1. A saját `koszont` függvényednek legyen `nev` paramétere. A törzsben f-string írja ki a kapott nevet: `Szia, Anna!` formában, az adott vendéggel.
2. A korábbi adat nélküli hívást cseréld névvel történő hívásra. Ments és futtass Annával.
3. Ha ez működik, adj hozzá egy második hívást Bélával. Ugyanaz a függvény szolgálja ki mindkét vendéget; ne készíts második definíciót.

**Ellenőrzés:** két sor, `Szia, Anna!` és `Szia, Béla!`. A különbséget az argumentum adja, nem a függvénybe beírt állandó név.

**Kész, ha:** egy paraméteres függvényed és két működő hívásod van. A következő fájlba majd a függvényt viheted át, a próbahívásokat nem kell vele együtt átmásolnod.

## F2 – a kiszámított összeget adjuk vissza

**Fájl:** `tetel.py`. **Cél:** egy termék árát ne csak kiírjuk, hanem a program további számításaihoz is megkapjuk.

### Előbb értsük meg

A mintafájlban a `tetel_arat_kiir` két adatot kap: egységárat és darabszámot. A szorzatot kiírja. A `print` az embernek jelenít meg valamit; a hívó programnak nem ezt a számot adja vissza.

A **return** visszaadja az értéket a hívónak, és befejezi az adott függvényhívást. Példa más számítással, teljesen futtatható programként:

```python
def teglalap_terulete(szelesseg, magassag):
    terulet = szelesseg * magassag
    return terulet


eredmeny = teglalap_terulete(4, 5)
print(eredmeny)
```

A két paraméter 4 és 5, a helyi `terulet` 20. Ezt a `return` visszaadja; a hívó az `eredmeny` névhez rendeli, és a külső `print` írja ki. A helyi név a függvényen belül használható. Nem a külső változó nevét adjuk át kötelezően: az értékeket adjuk át a paraméterekhez.

Ha egy függvény explicit visszatérés nélkül ér véget, a hívó `None` értéket kap. A kiírt szám ettől még látszhat a terminálban. A `print` és a `return` tehát eltérő feladatot végez.

### Most te írd meg

1. A `tetel_arat_kiir` nevét a definíciónál és a hívásnál is változtasd `tetel_ara` névre. A függvény a két paraméter szorzatát **adja vissza**, a törzsében ne maradjon kiírás.
2. A hívás eredményét rendeld `kave_osszeg` névhez. A függvényen kívül írj egy f-stringes kiírást: `Kávék ára: 900 Ft` a 450 Ft-os egységár és 2 darab esetén.
3. Ha működik, a darabszámot a hívásban változtasd 3-ra, és futtasd újra. Az új kiírás `Kávék ára: 1350 Ft` legyen.
4. Ugyanazzal a függvénnyel számold ki két, egyenként 890 Ft-os szendvics árát is. Az eredmény külön névhez és külön kiíráshoz kerüljön.

Az egységár az első, a darabszám a második argumentum. A számolásnál mindegy lehet a szorzás sorrendje, a paraméterek jelentését ettől még következetesen tartsd meg.

**Kész, ha:** ugyanaz a függvény a 450 és 2 adatra 900-at, a 450 és 3 adatra 1350-et, a 890 és 2 adatra 1780-at ad vissza. A kiírás a függvényen kívül történik; nem egy előre beírt eredményt látsz.

## B1 – a büfé számításai rendezett részfeladatok lesznek

**Fájl:** `bufe_02.py`. **Cél:** az EP_01-ről ismert program ugyanazt számolja, de a számításait saját függvények szervezzék.

### Előbb értsük meg az egész fájlt

A kiinduló program bekéri a nevet és a két darabszámot. A darabszámot `int` alakítja egész számmá. Ezután két szorzás és egy összeadás adja a rendelés összegét, amelyet f-string jelenít meg. A kávé 450 Ft, a szendvics 890 Ft. Most a bekérés és a kiírás marad ismerős; a számítást rendezzük át.

Egy függvény másik függvényt is meghívhat. Rövid szemléltető program:

```python
def dupla(szam):
    return szam * 2


def dupla_plusz_egy(szam):
    return dupla(szam) + 1


print(dupla_plusz_egy(4))
```

A külső hívás 4-et ad át. A `dupla_plusz_egy` előbb meghívja a `dupla` függvényt, amely 8-at ad vissza. Ehhez hozzáad 1-et, és 9-cel tér vissza. A belső részfeladatnak és az összetett műveletnek külön neve van. A büfénél egy termék részösszegét és a teljes rendelés összegét választjuk szét.

### Most te építsd át

1. A `bufe_02.py` elejére másold át a **saját** `tetel_ara` függvényed definícióját a `tetel.py` fájlból. A próbahívásait és próba-kiírásait ne másold át.
2. Írj `rendeles_osszege` nevű függvényt. Két paramétere legyen: `kave_darabszam` és `szendvics_darabszam`. A két egységárat ennek a függvénynek a belsejében add meg, jól elnevezett helyi változóként; a fájl eleji külön ár-értékadások így átköltöznek ide.
3. A függvényben a `tetel_ara` kétszeri meghívásával számold ki a két részösszeget. Ezek összegét add vissza. A függvényben ne kérj be adatot és ne írj ki.
4. A bekérés utáni korábbi három számolósort cseréld egy hívásra: a két bekért darabszámot add át a `rendeles_osszege` függvénynek, eredményét a már meglévő `rendeles_osszeg` változó kapja. A köszöntés és a kiírás maradhat a helyén.

Ezeket a lépéseket egymás után végezd el. A másolás itt saját, korábban megírt kód újrafelhasználása, nem a teljes kész büfémegoldás átvétele. A `rendeles_osszege` összetartozó rendelési részfeladatot nevez meg, nem pusztán minden sort külön függvénybe teszünk.

**Futtatás:** a `bufe_02.py` legyen megnyitva és elmentve. A Futtatás gombhoz ne adj ki külön könyvtárváltási parancsot. Az `input` kérdéseire sorban válaszolj:

| Név | Kávé | Szendvics | Elvárt rendelési összeg |
|---|---:|---:|---:|
| Anna | 2 | 1 | 1790 Ft |
| Béla | 3 | 2 | 3130 Ft |

A számok mellé ne írj „db” vagy „Ft” szöveget. Az új rendeléshez most a kód módosítása helyett új válaszokat adsz.

**Kész, ha:** az adatbekérés után a számítást a két saját függvény végzi, mindkét próbarendelés helyes, és a számoló függvényekből az eredmény visszakerül a hívóhoz.

## S1 – az első 45 perc lezárása

Mentsd a módosított fájlokat. A tutorral röviden foglaljátok össze: a paraméter adatot ad a függvénynek, a return eredményt ad a hívónak, a függvényhívások pedig részfeladatokat kapcsolnak össze. Ha a B1 még nincs kész, a tutor a tényleges állapotot és a következő szerkesztési lépést háttérben rögzíti a tanulói memóriában. Ha a memória nem elérhető, a beszélgetésben marad a folytatási összegzés. A haladási lapot csak külön kérésre használjuk; nem nyílik meg minden lépés után.

A második órán a működő számítás mellé döntéseket írunk. A szünet után nem kell újrakezdened a fájlokat.

## D1 – kedvezmény és fizetés két lehetséges ággal

**Fájl:** `dontes.py`. **Cél:** előbb a kedvezmény összegét, majd a fizetés eredményét állapítsa meg a program. Ebben a fájlban a bemenetek kódba írt adatok; így a döntést külön tudod kipróbálni.

### Előbb értsük meg

Az `if` egy feltételt vizsgál. Igaz eredménynél az alatta behúzott blokk fut, hamis eredménynél az `else` blokkja. Mindkét sor kettősponttal végződik, a blokkok négy szóközzel beljebb állnak. Az `else` után nincs új feltétel.

Egy külön, teljes függvénydefiníció az elvhez:

```python
def belepo_ara(gyerek_e):
    if gyerek_e:
        return 700
    else:
        return 1000
```

Ez a minta önmagában nem ír ki; meghíváskor ad vissza értéket. A `gyerek_e` logikai paraméter. `True` esetén 700, `False` esetén 1000 a visszaadott ár. Az egyik ág returnje után a hívás véget ér. A függvény mindkét úton számot ad vissza.

A büfénél a jogosultság paramétere `diak_e` lesz, a visszaadott szám pedig a **kedvezmény összege**, nem a fizetendő ár.

**Megadott szabály:** egész, nemnegatív forintösszegekkel dolgozunk. Diáknak 10% kedvezmény jár; a kedvezmény összegének tört forintját elhagyjuk: `rendeles_osszeg // 10`. A `//` lefelé kerekített hányadost ad; itt csak nemnegatív értékeket használunk. Nem diáknál a kedvezmény 0. A fizetendő az alapösszeg mínusz a kedvezmény. Ez a tanpélda szabálya, nem általános pénztári kerekítés.

### D1.a – írd meg a kedvezményt

1. A fájl elején készíts `kedvezmeny_osszege` függvényt két paraméterrel: `rendeles_osszeg`, `diak_e`.
2. A kétágú döntés egyik útján add vissza a fent leírt kedvezményt, a másikon 0-t. A függvény ne írjon ki.
3. A meglévő változóértékek után hívd meg a függvényt, eredményét rendeld `kedvezmeny` névhez. Számítsd ki a `fizetendo` értékét, majd mindkettőt írasd ki a függvényen kívül.
4. Ments és futtass: 1790 Ft-nál, `True` esetén 179 Ft kedvezmény és 1611 Ft fizetendő legyen. A `diak_e` értékét `False`-ra változtatva 0 Ft kedvezmény és 1790 Ft fizetendő legyen.

### D1.b – írd meg a fizetés elágazását

A `fizetett >= fizetendo` összehasonlítás azt kérdezi, eléri-e az átadott pénz a fizetendőt. Az összehasonlítás eredménye `True` vagy `False`. A `>=` az egyenlőséget is elfogadja, a `>` nem. Az `=` értékadás, a `==` egyenlőségvizsgálat.

A számítás és a fizetendő kiírása után készíts új if–else elágazást:

- ha elég a pénz, számold ki és írd ki a visszajárót: átadott pénz mínusz fizetendő;
- egyébként számold ki és írd ki, mennyi hiányzik: fizetendő mínusz átadott pénz.

A két ág közül egy fusson. A kiírásból derüljön ki, hogy visszajáróról vagy hiányzó összegről van szó.

**Ellenőrzés:** állítsd a diákságot `True`-ra, és próbálj ki 2000, 1611, majd 1610 Ft-ot. A megfelelő eredmények: 389 Ft visszajáró; 0 Ft visszajáró; 1 Ft hiány. Ezekhez a próbákhoz most csak a `fizetett` értékét írd át, ments, és indítsd újra a fájlt.

**Kész, ha:** kedvezménnyel és anélkül is számot kapsz, a pontos fizetés elfogadott, a kevés pénzből pedig pozitív hiányzó összeg lesz.

## D2 – egy rendelés egy kategóriát kapjon

**Fájl:** `kategoriak.py`. **Cél:** kis, közepes vagy nagy rendelésből pontosan egy kategóriát válassz.

A kiinduló program két külön `if` utasítással azt jelzi, hogy az összeg eléri-e a 3000-es és az 1500-as határt. Ez két független állítás, ezért ugyanarra az összegre két kiírás is történhet. A feladat most más: egyetlen kategóriát választunk.

Az `if–elif–else` láncban az első igaz feltétel ága fut. Az `elif` jelentése: ha az előző ágak feltételei nem teljesültek, ezt is vizsgáld meg. Egy már teljesült ág után a lánc többi feltételét nem értékeljük ki.

**Írd át a meglévő kódot** egy if–elif–else lánccá, az alábbi szabályokkal:

- legalább 3000 Ft: `Nagy rendelés`;
- legalább 1500 Ft, de 3000 Ft alatt: `Közepes rendelés`;
- 1500 Ft alatt: `Kis rendelés`.

A nagyobb `>=` küszöbbel kezdj, hogy ne fogja el a középső ág a nagy rendelést. A feltételt és a hozzá tartozó kiírást együtt gondold át. Itt az egymás utáni vizsgálatból következik a középső ág felső határa; nem kell új operátort bevezetned.

**Ments és futtass** az `osszeg` különböző értékeivel:

| Érték | Pontosan egy elvárt sor |
|---:|---|
| 1499 | Kis rendelés |
| 1500 | Közepes rendelés |
| 2999 | Közepes rendelés |
| 3000 | Nagy rendelés |

**Kész, ha:** a határok mindkét oldalán a megfelelő egyetlen sor jelenik meg. A kategorizálás külön kis program maradhat; B2-höz nem kötelező újabb funkcióként hozzáadnod.

## B2 – összeépíted a saját büféprogramodat

**Fájl:** a B1-ben már megírt `bufe_02.py`. **Cél:** a bekért rendeléshez a program kedvezményt számoljon és jelezze a fizetés eredményét. A már működő számító függvényeket megtartjuk.

### Előbb tekintsük át a készülő programot

A program neveket és darabszámokat kér be, ehhez most diákságot és fizetett összeget adunk. A számoló függvények kiszámítják az alapösszeget és a kedvezményt. A fő programsorok olvasható összesítőt írnak, majd egy elágazás jelzi a visszajárót vagy a hiányt. A feladat új része a meglévő saját kódok összeillesztése és az új bemenetek átadása.

A fő órai változatban egész, nemnegatív számokat és pontosan `igen` vagy `nem` választ használunk. Ez még nem általános adatellenőrzés: a hibás szöveget és negatív számot a K2 kiegészítés vizsgálja majd. A `ketto` vagy `2.5` bemenet az `int` számára hibás, `ValueError`-t okozhat. Ilyenkor újraindítunk és a megadott formában válaszolunk; ismételt bekérést még nem írunk.

### B2.a – hozd át a saját függvényeidet

A fájl elejére, a definíciók közé másold a D1-ben megírt `kedvezmeny_osszege` függvényedet. A tesztadatokat és próba-kiírásokat ne másold át. Ha a köszöntést is szeretnéd függvényből végezni, az F1-es saját `koszont` definíciót is felhasználhatod, és a későbbi köszöntő printet hívásra cserélheted; ez nem feltétele a fő feladatnak.

### B2.b – kérd be a két új adatot

A név és a két darabszám bekérése után:

1. kérdezd meg, diák-e a vendég: a szöveges választ `diak_valasz` névhez rendeld;
2. a `diak_valasz == "igen"` összehasonlításból készíts `diak_e` logikai változót;
3. kérd be a fizetett összeget, és `int`-tel alakítsd egész számmá, `fizetett` néven.

Az input szövegét nem a `bool` alakítja át a magyar szó jelentése szerint. A `bool("nem")` is True, mert a szöveg nem üres. Itt ezért tartalmát hasonlítjuk össze az `"igen"` szóval.

Ha a bekérés szintaxisát kell felidézni, ez egy külön, rövid minta egy egész szám beolvasására; nem a teljes feladat megoldása:

```python
tea_darabszam = int(input("Hány teát kérsz? "))
```

Előbb az `input` ad szöveget, aztán az `int` készít belőle számot, majd az értékadás kapcsolja a névhez. Az új összeget ennek mintájára te kérd be.

### B2.c – használd a kapott adatokat

A rendelési összeg kiszámítása után hívd meg a saját kedvezményfüggvényedet a rendelés összegével és a `diak_e` értékével. Számítsd ki a fizetendőt. Az összesítőben külön sor mutassa:

- a rendelés alapösszegét;
- a kedvezmény összegét;
- a fizetendő összeget.

Ezután írd át a D1-ben már megírt fizetési elágazásodat ebbe a programba. Itt a `fizetett` a bekért szám legyen, ne maradjon benne a teszteléshez használt állandó 2000.

### B2.d – futtasd ugyanazt a programot eltérő adatokkal

Ments, a `bufe_02.py` legyen megnyitva, és használd a Futtatás gombot. Minden sor külön futás; a kérdésekre a terminálban válaszolj.

| Név | Kávé | Szendvics | Diák? | Fizetett | Elvárt fizetendő | Fizetés eredménye |
|---|---:|---:|---|---:|---:|---|
| Anna | 2 | 1 | igen | 2000 | 1611 Ft | 389 Ft visszajáró |
| Béla | 2 | 1 | nem | 2000 | 1790 Ft | 210 Ft visszajáró |
| Anna | 2 | 1 | igen | 1611 | 1611 Ft | 0 Ft visszajáró |
| Anna | 2 | 1 | igen | 1610 | 1611 Ft | 1 Ft hiány |

Az [ellenőrző esetek](ellenorzo_esetek.md) további próbákat is adnak. A fő útvonalon a fenti négy elég a két kedvezményes út és a fizetési határ vizsgálatához; új hiba vagy célzott módosítás indokolhat további próbát.

**Kész, ha:** az új adatokat valóban bekéred, a kedvezményfüggvény használja a választ, a számítás eredményét nem égetted a kódba, és a fizetés mindhárom esete működik. A saját megoldásodnak nem kell sorra pontosan egyeznie a HTML kész programjával.

## Z1 – rövid önálló kódírás

Nyisd meg a [zárófeladatot](zaro_feladatok.md), majd az `onallo.py` fájlt. Az instrukció és az elvárt eredmények meg vannak adva; a megoldó kódot te írod meg. Segítséget itt is kérhetsz.

## S2 – lezárjuk a második órát

Mentsd el a munkádat. A tutorral a saját fájljaid alapján foglaljátok össze, hol adsz át adatot paraméterként, hol tér vissza eredmény, és melyik feltétel választja ki a végrehajtott ágat. A még nem kész vagy csak támogatással megoldott rész folytatási pontként marad meg; nem kell az óra után újabb kötelező köröket teljesíteni.

A fő gyakorlat itt véget ér. A [kiegészítő feladatok](tovabbi_gyakorlas.md) külön alkalomra vagy önálló gyakorlásra valók.
