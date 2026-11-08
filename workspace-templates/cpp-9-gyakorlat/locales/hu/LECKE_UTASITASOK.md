# CPP_09 – Alapozó feladatok

Indítás 3 perc; G09_01 8, G09_02 12, G09_03 12, G09_04 10 perc. A tutor mindig egy részlépést ad. Te írod a kódot; a minták eltérő problémákat oldanak meg. Minden próbánál a valódi objektumot kérdezd le, ne az elvárt eredményt írd be a cout-ba.

## G09_01 – Versenyző létrehozása

**Forrás:** `G09_01_versenyzo.cpp`. **Minta:** M1.

### G09_01_A

Készíts `Versenyzo` osztályt privát `int rajtszam` és `int pontszam` adattaggal. Az adattag az egyes objektumokhoz tartozó tárolt adat. Írj argumentum nélküli konstruktort 0/0 kezdőállapottal és egy rajtszámot kapó konstruktort, amely mellett a pontszám 0. Mindkettő használjon inicializálólistát.

Írj `int rajtszamLeker() const` és `int pontszamLeker() const` lekérdezőt. Készíts egy argumentum nélküli és egy 17-es rajtszámú objektumot. Ellenőrzés: 0/0 és 17/0. A 0 itt még nem azonosított versenyzőt jelöl; nem érvényességi feladat.

### G09_01_B

Adj hozzá két egész paramétert kapó konstruktort, amely a rajtszámot és pontszámot is inicializálja. Egy 23-as rajtszámú, 12 pontos objektum adatai 23/12 legyenek. Az első két létrehozás továbbra is működjön. Készíts legalább egy `const` objektumot, amelyen a lekérdezők hívhatók.

A konstruktor neve megegyezik az osztály nevével, nincs elé írt visszatérési típus. Az inicializálólista a törzs előtt ad kezdőértéket a tagoknak. A tagokat deklarációs sorrendben inicializáld. Nem szükséges setter, saját másoló konstruktor vagy új téma.

## G09_02 – Fényerő és feltételes kifejezés

**Forrás:** `G09_02_fenyero.cpp`. **Minta:** M2.

### G09_02_A

Készíts `KijelzoFenyero` osztályt privát `int szint` adattaggal. A tartomány 0–100, mindkét végpont megengedett. Az argumentum nélküli konstruktor 50-et állítson be. Az egy értéket kapó konstruktor helyes értéket tartson meg, máskülönben 50-et válasszon. Legyen `int leker() const`.

A paraméteres konstruktorban az inicializálólistán belül használd a `?:` kifejezést. Inno előbb részletesen magyarázza el az M2 programját, utána a fényerő feltételét te fogalmazd meg. Nincs kész célfeltétel a starterben.

**Olvasási sorrend:** először a `?` előtti feltételt vizsgáljuk. Igaz esetben a `?` és a `:` közötti, hamis esetben a `:` utáni kifejezés adja az eredményt. Csak a kiválasztott ág értékelődik ki. Az eredmény kerül az adattag kezdőértékébe. A konstruktor paraméterlistája utáni kettőspont az inicializálólistát kezdi; a belső kettőspont a két választási lehetőséget választja el.

Próbák: -1 → 50, 0 → 0, 40 → 40, 100 → 100, 101 → 50. Argumentum nélkül 50 legyen. Ne készíts bonyolult, egymásba ágyazott feltételes kifejezéseket.

### G09_02_B

Készíts `bool beallit(int ujSzint)` műveletet. Tartományon belül módosít és igazat ad; hibás kérésnél hamis és változatlan korábbi állapot szükséges. A main a sikerességet és az aktuális lekérdezett értéket is írja ki.

40-es objektumon: 70 beállítása igaz/70; utána 120 hamis/70; 0 igaz/0; 100 igaz/100. Az ellenőrzés a módosítás előtt történjen. A konstruktor 50-es választása és a setter elutasítása szándékosan eltérő szabály; egyik sem a C++ automatikus hibajavítása.

## G09_03 – Küldemény és díjszámító

**Forrás:** `G09_03_kuldemeny.cpp`. **Minta:** M3.

### G09_03_A

Készíts `Kuldemeny` osztályt privát `int gramm` és `bool surgos` mezőkkel, kétparaméteres konstruktorral és `int grammLeker() const`, `bool surgosE() const` lekérdezőkkel. Adott, helyes, 1–5000 grammos egész bemenetekkel dolgozunk.

A `Dijszamito` privát adattagjai `int alap`, `int lepcso`, `int felar`. Konstruktorban kapja meg a három értéket. Az `int dij(Kuldemeny kuldemeny) const` a küldemény nyilvános lekérdezőit használja; a privát mezőket nem éri el közvetlenül.

A díj: alapdíj + minden megkezdett 500 gramm díja + sürgősség esetén felár. A megkezdett egységek számát pozitív egész grammokra `(gramm + 499) / 500` adja. Miért? 1–500 esetén 1, 501–1000 esetén 2 az egész hányados. A képlet itt a feldolgozás magyarázott része, nem új matematikai felfedezés a hallgatónak.

800 alap, 300 egységdíj és 600 sürgősségi felár mellett: 450 g normál → 1100; 500 g normál → 1100; 501 g sürgős → 2000.

### G09_03_B

Ugyanazt az 501 grammos sürgős küldeményt egy másik, 1000/200/400 beállítású díjszámítóval is dolgozd fel: eredmény 1800. A küldeményt nem kell átalakítani. A díjszámító saját beállításokat tárol; ezért itt szerepe van a külön osztálynak. Más feldolgozó később ugyanebből a küldeményből címkét is készíthetne.

A paraméter itt érték szerinti, tehát a függvény saját paraméterobjektumot kap. Ezt csak olvassa. A számítás nem tárolja el a küldeményt a díjszámító adattagjaként; ez alkalmi együttműködés, nem kompozíció.

## G09_04 – Eredménylap és kompozíció

**Forrás:** `G09_04_eredmenylap.cpp`. **Minták:** M4 és az M6 tömbelemlétrehozási része. Az ismert M1-et nem kell újra végigelemezni.

### G09_04_A

Másold át a saját G09_01-ben elkészült `Versenyzo` osztályodat ebbe az önálló forrásba. Ne másik fájl main-jét másold mellé. Készíts `Eredmenylap` osztályt privát, két `Versenyzo` objektumot tartalmazó tömbbel.

Konstruktora négy egész számot kap: első rajtszám és pontszám, második rajtszám és pontszám. A konstruktor törzsében paraméteres `Versenyzo` objektumokból értékadással töltsd a tömbelemeket. A két tömbelem már a törzs előtt létrejön a saját alapértelmezett konstruktorával. A törzsbeli feltöltés ezután értékadás. Ezért kell a G09_01 argumentum nélküli konstruktora is.

### G09_04_B

Az `int pontOsszeg() const` a két objektum `pontszamLeker()` műveletét használja. 17/8 és 23/12 adatokból 20 pont adódjon. Egy belső blokkban készíts második eredménylapot 31/0 és 32/5 adatokkal: 5 pont. A blokk után az első lap továbbra is 20 pontot ad.

A második lap objektuma a belső blokk végén megszűnik. A külső lap tovább él; nem hivatkozunk a már megszűnt lapra. Nincs saját destruktor vagy megőrzött mutató.

Az eredménylap versenyzőket tartalmaz, ez kompozíció. A következő projektben a pénztár jegyeket tartalmazó objektumtömböt kezel, már változó tényleges elemszámmal.
