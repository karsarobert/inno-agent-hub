# EP_05 – A két záró teszt megoldókulcsa

Oktatói és tutori értékelési segéd. Ne mutasd meg a válaszadás előtt.
A munkatéri fájl technikailag hozzáférhető a tanulónak is: ez önellenőrző tanulási teszt, nem titkos vizsgarendszer.

## Pontozás

- Elmélet: 10 × 1 pont, az alábbi részpontokkal. A helyes saját megfogalmazás elfogadható.
- Kódismeret: 10 × 1 pont. KÓD1–KÓD5: 0,5 pont a teljes helyes kimenetért, 0,5 pont a kért indoklásért. KÓD6–KÓD10: 0,5 pont a hiba/ok azonosításáért, 0,5 pont a működő javításért (KÓD10-nél a helyes eredménnyel együtt).
- A hibák neve (például TypeError) nem kötelező, ha az okot a tanuló helyesen elmagyarázza.
- Nincs negatív pont és nincs automatikus érdemjegy. Eredmény: elmélet x/10, kódismeret y/10, összesen z/20.
- A beadott első, segítség nélküli válasz számít az önálló eredménybe. Ha előbb kapott érdemi segítséget vagy futtatott, jelöld támogatottnak; önálló pontot abból ne következtess. Külön jelezd a később sikerült javítást.
- A kihagyott kérdés és a hibás válasz külön állapot. Befejezett tesztnél a kihagyott kérdés 0 pont, de ha még várjuk a választ, a teszt részleges.

## T1 – Elmélet

### E1

A kulcs a `"tea"` sztring, az érték a `320` egész szám.

Pontozás: 0,5 pont a kulcs, 0,5 pont az érték helyes megnevezéséért.

### E2

A közvetlen indexelés KeyError hibát okoz; a get külön alapérték nélkül None-t ad vissza. Egyik sem vesz fel kulcsot.

Pontozás: 0,5 pont a hibáért (a KeyError név nem kötelező), 0,5 pont a None eredményért.

### E3

A szótár kulcsai között keres.

Pontozás: 1 pont a kulcsokért.

### E4

Az adott bejegyzés kulcsát, illetve a hozzá tartozó értéket kapják. A büfében ez a terméknév és az ár.

Pontozás: 0,5 pont változónként; az összetartozó pár jelentése számít.

### E5

Ha a kulcs már szerepel, felülírja az értékét; ha nem szerepel, új kulcs–érték párt vesz fel.

Pontozás: 0,5 pont esetenként.

### E6

A 0 is hamis igazságértékű, pedig lehet érvényes ár. Az is None kifejezetten a hiányjelzést különbözteti meg.

Pontozás: 0,5 pont a 0 igazságértékéért, 0,5 pont a hiány és az érvényes nulla megkülönböztetéséért.

### E7

A hívó tovább használhatja az értéket például a kedvezményhez és fizetéshez; a számítás elkülönül a megjelenítéstől.

Pontozás: 1 pont az újrafelhasználható visszatérési érték indoklásáért; a saját példa is elfogadható.

### E8

Csak a megvásárolt tételek számítanak, és a kosárban ismétlődő terméket többször kell beleszámítani. Az árjegyzék a teljes kínálatot tárolja.

Pontozás: 0,5 pont a vásárolt tételekért, 0,5 pont az ismétlődésekért.

### E9

Így mindkettő ugyanabból az adatból dolgozik, és egy árváltozás mindkét helyen érvényesül. Nem kell külön árlistákat karbantartani.

Pontozás: 1 pont a közös, következetes adatforrás indoklásáért.

### E10

599, 600 és 601 Ft: az első kettő elfogadható, az utolsó nem. A <= feltétel ezt fejezi ki.

Pontozás: 0,5 pont a három határ körüli árért, 0,5 pont a helyes elfogadási döntésekért.

## T2 – Kódismeret

### KÓD1

320; None; False. A kakaó nincs a szótárban; a víz ára létező 0, nem None.

### KÓD2

3; 350; 200. A tea meglévő kulcs értékét írtuk át, a víz új kulcs.

### KÓD3

["tea", "keksz"]. A tea pontosan a keretbe fér, és a <= elfogadja az egyenlőséget is.

### KÓD4

820, mert 320 + 180 + 320. A tea két külön kosártétel.

### KÓD5

340; 340. A függvény ugyanazt a szótárat módosítja; a paraméterátadás nem készített másolatot.

### KÓD6

Az if not ar a 0-t is hiánynak tekinti. Javítás: if ar is None:. Így a víz ára 0 Ft-ként jelenik meg.

### KÓD7

A return a ciklusban van, ezért az első tétel után kilép. A return kerüljön a for után, a for sorával azonos behúzásra. Az eredmény így 500; üres kosárra 0.

### KÓD8

Hiányzik a kulcs létezésének vizsgálata. Javítás: if termek in arak and uj_ar > 0:. Az új kulcs így nem jön létre; a két kiírás False.

### KÓD9

Az items() előbb kulcsot, utána értéket ad: az ar itt szöveget kap. Sztringet hasonlítunk számhoz, ami TypeError. Javítás: for termek, ar in arak.items():. A tea jelenik meg.

### KÓD10

A >= a pontos határértéket is elfogadja. Javítás: if arak[termek] > 320:. Csak a kakaó számít, a helyes eredmény 1.

## Visszajelzés

Az eredményt fogalmakhoz kösd: kulcs–érték, hiány és nulla, módosítás, bejárás, ismétlődés, return helye, határérték.
Adj legfeljebb két konkrét gyakorlási célt. A 20/20 sem bizonyítja önmagában, hogy a tanuló egy teljes programot önállóan meg tud írni; a programozási munka eredménye külön marad.
A javítás után ne írd felül az első eredményt: „Első válasz: …; magyarázat után javította: …”.
