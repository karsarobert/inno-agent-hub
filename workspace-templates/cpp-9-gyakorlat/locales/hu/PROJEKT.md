# CPP_09 – Színházi jegypénztár

**Egyetlen forrás:** `P09_jegypenztar.cpp`. **Idő:** 45 perc. Hat lépésben ugyanazt a programot fejleszted tovább. A tutor mindig az aktuális részt magyarázza; az egész listát nem kell egyszerre megírnod.

## A helyzet és a modell

A nézőtéren 3 sor van, mindegyikben 4 szék. Egy jegy egy konkrét sor–szék párt jelöl. Az első sor ára 4000, a második és harmadik soré 3000 pénzegység. A gyakorló pénztár egyszerre legfeljebb 4 jegyet tárol; ez a tároló mérete, nem a teljes nézőtér 12 férőhelye.

`Jegy`: egy hely adatai és ára. `Jegypenztar`: több jegy felvétele, keresése, visszaváltása, listázása és összegzése. A jegyek az osztály saját adattagjai; a pénztár tartalmazza őket. Két pénztárnak külön tárolt jegyei és darabszáma van.

A példákban kézzel megadott kis egész adatok szerepelnek. Nem kell menü, billentyűzetes adatbekérés, ügyfélnév, dátum, fizetés vagy fájlmentés. A „bevétel” az aktuálisan tárolt jegyek árösszege, nem történeti könyvelés.

Forrássorrend: include-ok és névtér → szükséges konstans → `Jegy` → `Jegypenztar` → szabad függvény prototípusa, ha már kell → `main` → szabad függvény definíciója. A tagfüggvényeket az osztályon belül írjuk meg. A pontos osztályneveket és interfészt használd, hogy követhető legyen a feladat, de az egyenértékű belső megoldás elfogadható.

## P1 – Jegyek létrehozása, 7 perc

**Minta:** M5; az inicializáláshoz az ismert M1–M2 elvét idézzük fel.

Készíts `Jegy` osztályt privát `int sor` és `int szek` adattaggal.

- `Jegy()` → 0/0, még nem használható helyfoglalás.
- `Jegy(int ujSor, int ujSzek)` → helyes pár megtartása; hibás párból 0/0.
- `int sorLeker() const`, `int szekLeker() const`.
- `bool ervenyesE() const` → sor 1–3 ÉS szék 1–4.
- `int ar() const` → érvénytelen jegynél 0, első sorban 4000, másik két sorban 3000.

Az árat számítjuk, nem tároljuk külön mezőben. A paraméteres konstruktorban mindkét mező kapjon kezdőértéket inicializálólistában. Olvasható megoldás: előbb 0/0 inicializálása, majd a törzsben mindkettő beállítása, ha a teljes pár helyes. A lista az inicializálás, a törzsbeli sorok későbbi értékadások. A lényeg: a konstruktor végén teljes, következetes állapot legyen. Nem kötelező ide is `?:`-t erőltetni.

Próbák, a lekérdezőkből kiírva:

| Létrehozás | Tárolt sor/szék | Érvényes? | Ár |
|---|---|---|---:|
| Argumentum nélkül | 0/0 | hamis | 0 |
| 1, 2 | 1/2 | igaz | 4000 |
| 3, 4 | 3/4 | igaz | 3000 |
| 4, 1 | 0/0 | hamis | 0 |
| 2, 0 | 0/0 | hamis | 0 |

Legalább egy jegy legyen `const`, és arról is kérdezd le az állapotot.

## P2 – Üres pénztár és hozzáadás, 8 perc

**Minta:** M6. A jelzőpanel fix két elemétől eltérően itt a kapacitáson belül csak egy előtag aktív.

Készíts `const int KAPACITAS = 4;` konstanssal méretezett `Jegypenztar` osztályt. Privát tagjai: `Jegy jegyek[KAPACITAS]` és `int darab`. Az argumentum nélküli konstruktor a darabszámot inicializálólistában 0-ra állítja. A négy jegy alapértelmezett konstruktorai ettől függetlenül lefutnak.

Az `int darabLeker() const` az aktív darabszámot adja. A `bool hozzaad(int sor, int szek)` először ellenőrzi a pár érvényességét és a szabad tárolóhelyet. Ha nem megfelelő, visszatér hamissal módosítás nélkül. Egyébként a következő aktív helyre teszi az új jegyet, egyszer növeli a darabszámot és igazat ad.

Próbák: kezdetben 0; 1/2 felvétele igaz és 1; 0/2 felvétele hamis és továbbra is 1. A visszatérő értéket is használd. A tömbbe írás előtt kell vizsgálni a kapacitást.

Az ismételt foglalás tilalmát P3-ban adjuk hozzá; addig csak eltérő helyekkel próbálunk. Ez köztes fejlesztési állapot, nem a végleges hozzáadás.

## P3 – Kettős foglalás tiltása, 7 perc

**Minta:** M7, amely egy szám keresését mutatja. Itt két adatnak kell együtt egyeznie.

Írd meg a `bool foglaltE(int sor, int szek) const` lekérdezőt. Csak a `[0, darab)` tartományt vizsgálja. Ha a sor és a szék is egyezik egy aktív jeggyel, igazat ad; egyébként hamisat.

A `hozzaad` a meglévő ellenőrzések mellé vegye fel az ismétlés tilalmát. Az azonos sor másik székkel megengedett. Ne használj csak sorszámot vagy VAGY kapcsolatot az egyezéshez.

A következő állapotot építsd fel, külön kiírva minden sikerességet és darabszámot:

1. 1/2 felvétele: igaz, 1.
2. Újabb 1/2: hamis, 1.
3. 2/3: igaz, 2.
4. 3/1: igaz, 3.
5. 1/4: igaz, 4. Ez az első sor másik széke, ezért megengedett.
6. 2/2: hamis, 4, mert tele a tároló.

A próbákhoz a korábbi main-hívásokat egységesítsd: ugyanazt az első jegyet ne vedd fel véletlenül kétszer az új próbasor indítása előtt. Egyetlen frissen létrehozott pénztárból indulunk.

## P4 – Visszaváltás és balra mozgatás, 10 perc

**Minta:** M8. A mintában az index adott, a projektben előbb meg kell keresned a párt.

Készíts `bool visszavalt(int sor, int szek)` műveletet:

1. Keresd meg az aktív jegyek között a teljes párt. A találati indexnek legyen egyértelmű „nincs találat” jelzése.
2. Ha nincs találat, hamis és változatlan állapot.
3. Találatkor a mögötte lévő jegyeket mozgasd egy hellyel balra.
4. Csökkentsd egyszer a darabszámot és adj igazat.

A soron következő elem olvasása csak akkor megengedett, ha még az aktív tartományban van. A tutor külön elmagyarázza, miért az utolsó előtti aktív indexig tart a mozgató ciklus, és miért a ciklus után csökken a darabszám.

Az előző négy jegyből 2/3 visszaváltása igaz, a darabszám 3. A 3/1 és 1/4 foglalás továbbra is megtalálható. A 2/4 visszaváltása hamis, darabszám 3. Ezután 2/2 hozzáadása igaz, darabszám 4.

Az elemek sorrendjét P5 listázásával is ellenőrizzük. A darabszám mögötti régi elem nem aktív, ezért később nem szabad keresni, listázni vagy összegezni. Nem kell külön lenullázni.

## P5 – Lista és aktuális bevétel, 7 perc

**Minta:** M9; az adattagok helyett a `Jegy` nyilvános lekérdezőit alkalmazd.

Készíts `void lista() const` és `int bevetel() const` tagfüggvényt. A lista minden aktív jegynél kiírja a sort, széket és árat. A bevétel minden aktív jegy `ar()` értékének összege. Üres pénztárból 0 legyen, és egyetlen jegysor se jelenjen meg.

Ne tárolj külön bevételmezőt, és ne a kapacitást járd be! A visszaváltás utáni balra mozgatás nem törli feltétlenül a tömb utolsó fizikai elemét; a helyes darabszám zárja ki azt.

Az alábbi, egymást követő műveletekből készíts rendezett próbasort a main-ben. Minden eredmény az adott művelet UTÁNI állapotra vonatkozik.

| Művelet | Siker? | Darab | Bevétel |
|---|---|---:|---:|
| Üres pénztár | – | 0 | 0 |
| Hozzáad 1/2 | igaz | 1 | 4000 |
| Hozzáad 0/2 | hamis | 1 | 4000 |
| Ismét 1/2 | hamis | 1 | 4000 |
| Hozzáad 2/3 | igaz | 2 | 7000 |
| Hozzáad 3/1 | igaz | 3 | 10000 |
| Hozzáad 1/4 | igaz | 4 | 14000 |
| Hozzáad 2/2, tele tárolóba | hamis | 4 | 14000 |
| Visszavált 2/3 | igaz | 3 | 11000 |
| Visszavált 2/4, nincs ilyen | hamis | 3 | 11000 |
| Hozzáad 2/2 | igaz | 4 | 14000 |

A középső jegy visszaváltása után a lista: 1/2/4000, 3/1/3000, 1/4/4000. Az új 2/2 felvétele után ez a negyedik sorban 2/2/3000 értékkel egészül ki. Egy külön `const` üres pénztár végig 0/0 összesítést adjon.

P6 összefoglalójának kipróbálásáig tartsd meg ezt a négyjegyes állapotot. Utána egy rövid további próba: váltsd vissza az első (1/2), az utolsó (2/2), majd a megmaradt 3/1 és 1/4 helyet. A darab/bevétel rendre 3/10000, 2/7000, 1/4000, 0/0. Újabb 1/4 visszaváltása hamis, állapot 0/0. Ezután 3/4 ismét felvehető: 1/3000. Ez ugyanannak a műveletnek a határpróbája, nem új feladat.

## P6 – Visszaadott szöveg, együttműködő könyvtári osztályok, 6 perc

**Minta:** M10. Új include-ok: `<sstream>` és `<string>`. A névjegyes példa helyett a pénztár adatait kell összefoglalnod.

Írj `string osszefoglalo(const Jegypenztar* penztar)` szabad függvényt. Egy `ostringstream` helyi objektumba építse fel a szöveget a nyilvános lekérdezőkből, majd a `str()` eredményét adja vissza. A main írja ki a visszaadott `string` értéket a cout-tal. A függvény ne közvetlenül cout-ra írjon.

Az összefoglaló tartalma: `FOGLALAS=4;ERTEK=14000`, a P5 végső négyjegyes állapotán. A külön üres pénztárra `FOGLALAS=0;ERTEK=0`. A megnevezés eltérhet, de a darabszámot és az összeget mindig az aktuális objektum lekérdezői szolgáltassák.

**A mutató szerepe:** a `&penztar` egy már létező helyi objektum címét adja át. A paraméter `const Jegypenztar*`, ezért ezen az úton a megfelelő const lekérdezők hívhatók. A `->` mutatón át hív tagfüggvényt; nem nyitja meg a privát mezőket. Nem jön létre külön pénztármásolat, nincs new/delete, és nem őrzünk meg megszűnt objektumra mutató címet.

**A könyvtári együttműködés:** az ostringstream összerakja a szöveget a memóriában; a str() egy string értéket ad; a main ezt a cout szabványos kimeneti folyamra írja. A jelentés formátuma módosítható a helyfoglalási szabályok átírása nélkül. Ezek szabványos könyvtári osztályok/objektumok, nem nyelvi alaptípusok.

## Lezáró megértési pont

Egy rövid magyarázatban kapcsoljátok össze: mit garantál a Jegy konstruktorának végállapota, mit ellenőriz ehhez képest a Jegypenztar hozzáadása, és miért elég a jegyekből számolni a bevételt? Ezután a rögzített teszt következik; nem indul új projekt.
