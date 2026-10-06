# EP_05 – A büfé továbbfejlesztése

A már működő kosárból most új információkat készítünk: hány darabot rendeltek egy termékből, mennyit költöttek rá összesen, és melyik termék adta a legnagyobb részösszeget. Végül az árjegyzékből új változatot is készíthetsz.

| Feladat | Fájl | Előfeltétel | Tervezett idő |
|---|---|---|---:|
| C1 – Darabszámok szótárban | darabszamok.py | B1 | 10 perc |
| C2 – Összevont büféblokk | osszevont_blokk.py | C1 | 15 perc |
| C3 – Legnagyobb részösszeg | reszosszeg.py | C2 | 10 perc |
| K5 – Új árjegyzék árkorrekcióval | arkorrekcio.py | A2–A3 | 10 perc |

A kezdőfájlok elindulnak, de még nem teljesítik a feladatot. A szöveges megjegyzéseket te alakítod kóddá. Az új fájlok ugyanabban a munkatérgyökérben vannak, ezért futtatásukhoz nincs új mappaváltás. Mindig ments a Futtatás előtt.
Ezek a kiválasztott bővítések a két záró teszt elé kerülnek. C1–C2 együtt 25, minden új feladat együtt 45 perc többlet a tervezett alapúthoz képest. Gyorsabb haladásnál a felszabadult időben dolgozhatsz rajtuk.

## C1 – Hány darabot rendeltek?

**Fájl:** `darabszamok.py`. **Idő:** 10 perc.

### Mit csinál majd a program?

A kosár listájában minden vásárolt darab külön elem. Az új szótárban egy terméknév egyszer szerepel kulcsként, a hozzá tartozó szám viszont megmutatja, hány darabot vásároltak. A függvény szótárat ad vissza, a főprogram írja ki. Az eredeti kosár megmarad.

### Rövid minta: belépések számlálása

```python
belepesek = {"Anna": 2}
latogato = "Béla"
korabbi = belepesek.get(latogato, 0)
belepesek[latogato] = korabbi + 1
print(belepesek)
```

A get második argumentuma az alapérték: az eddig nem látott név számlálója nulláról indul. Egy új belépés miatt eggyel nagyobb értéket tárolunk. A get maga nem módosít, a következő értékadás igen. Itt egyetlen belépés történt; a te feladatodban a kosár minden elemével el kell végezni ezt a frissítést.

### Te alakítsd át

1. A `darabszamokat_szamol(kosar)` függvényben az üres szótár a ciklus előtt jöjjön létre.
2. Saját for ciklussal járd be a kosarat; az aktuális termékhez tartozó darabszámot növeld.
3. Az elkészült szótárat a teljes bejárás után add vissza. A függvényben ne legyen print, és ne módosítsd a kosárlistát.
4. Futtasd a kezdő próbát, majd az alábbi eseteket.

### C1 ellenőrző esetek

| Azonosító | Kosár | Elvárt szótár |
|---|---|---|
| C1.1 | `["kávé", "szendvics", "kávé", "üdítő", "szendvics"]` | `{"kávé": 2, "szendvics": 2, "üdítő": 1}` |
| C1.2 | `[]` | `{}` |
| C1.3 | `["tea"]` | `{"tea": 1}` |
| C1.4 | `["kávé", "kávé", "kávé"]` | `{"kávé": 3}` |

Mindegyik esetben a főprogram által kiírt eredeti kosár maradjon változatlan. C1-nek nincs szüksége árjegyzékre; a tea itt külön felvétel nélkül is számlálható.

**Kész, ha:** új szótárat adsz vissza, minden előfordulást megszámolsz, üres kosárra üres szótár készül, a bemenet nem változik.

## C2 – Összevont büféblokk

**Fájl:** `osszevont_blokk.py`. **Idő:** 15 perc.

### Mit csinál majd a program?

Az egyik szótár darabszámot, a másik egységárat rendel ugyanahhoz a terméknévhez. A részösszeg darabszám × egységár. A számoló függvény visszaadja a teljes árat, a megjelenítő függvény termékenként egy sort és végösszeget ír ki. A kiinduló fájl már bejárja és kiírja a darabszámokat; ezt bővíted.

### Rövid minta: csomagok tömege

```python
dobozok = {"kis": 3, "nagy": 2}
egysegtomegek = {"kis": 2, "nagy": 5}
tipus = "kis"
darab = dobozok[tipus]
egysegtomeg = egysegtomegek[tipus]
print(f"{tipus}: {darab} db × {egysegtomeg} kg = {darab * egysegtomeg} kg")
```

A két szótárat a közös kulcs kapcsolja össze. A mintában egy kiválasztott doboztípus szerepel; a blokkban az összes megvásárolt terméket kell feldolgoznod, árakkal és Ft mértékegységgel. Feltételezzük, hogy minden kosártétel ismert kulcs az árjegyzékben.

### C2.a – Először a számítás

1. Cseréld le a kezdő `darabszamokat_szamol` definíciót a saját C1-függvényedre. Csak a függvényt vidd át.
2. Írd meg az `osszesitett_ar(darabszamok, arak)` függvényt: új összegző változóban gyűjtse a darabszámok és az egységárak szorzatát, majd adja vissza a teljes összeget.
3. A függvény ne írjon ki és ne módosítsa a bemeneteit. Üres szótárra 0-t adjon.
4. A főprogramban egy rövid saját próbahívással ellenőrizd: a kezdő kosár összege 3070 Ft. Ezután jöhet a megjelenítés.

### C2.b – A blokk sorainak kibővítése

1. A meglévő items bejárásban kérd le a termék egységárát, és számítsd ki a részösszeget.
2. A kiírt sor tartalmazza a terméket, darabszámot, egységárat és részösszeget.
3. A ciklus után a saját `osszesitett_ar` függvényed eredményét használd a végösszeg kiírásához.

```text
kávé: 2 db × 450 Ft = 900 Ft
szendvics: 2 db × 890 Ft = 1780 Ft
üdítő: 1 db × 390 Ft = 390 Ft
Összesen: 3070 Ft
```

A szóközök és a szorzásjel formája eltérhet; a termék és a számítás legyen helyes. Két azonos árú, különböző termék ne olvadjon össze.

### C2 ellenőrző esetek

| Azonosító | Adatok | Elvárt viselkedés |
|---|---|---|
| C2.1 | Kezdő kosár, alapárak | Három terméksor; részösszegek 900, 1780, 390; összesen 3070 Ft. |
| C2.2 | Üres kosár | Nincs terméksor, összesen 0 Ft. |
| C2.3 | Csak a kávé ára legyen 500, a kezdő kosár maradjon | Kávé részösszeg 1000; összesen 3170 Ft. |
| C2.4 | `arak = {"tea": 350, "kakaó": 350}`, kosár `["tea", "kakaó", "tea"]` | Két terméksor: tea 2 db, 700 Ft; kakaó 1 db, 350 Ft; összesen 1050 Ft. |

Minden új teszthez a táblázat szerinti adatokat használd. A megjelenítés nem változtathatja meg a szótárakat.
Összehasonlításként a B1-ben elkészített összegződet is használhatod ugyanarra a kosárra és árjegyzékre: ugyanazt a végösszeget kell kapnod.

**Kész, ha:** saját C1-függvényt használsz, külön számoló és megjelenítő függvényed van, termékenként egy sor készül, a négy próba megfelelő.

**Kapcsolás a büféhez, külön idő esetén:** a tanuló a saját `bufe_05.py` fájljáról készített `bufe_05_osszevont.py` másolatban átviheti a három saját definíciót. A kosárbekérés után a saját számlálójával készítsen darabszámokat, a régi blokk hívását cserélje az összevont blokk hívására. A fizetési logika marad a már működő változat. Ez opcionális további alkalmazás, nincs beleszámítva a C2 15 percébe.

## C3 – Mire költöttünk összesen a legtöbbet?

**Fájl:** `reszosszeg.py`. **Idő:** 10 perc.

### Mit csinál majd a program?

A függvény terméknév → darabszám szótárból és az árjegyzékből választ egy terméknevet. A választás alapja a részösszeg, nem az egységár és nem önmagában a darabszám. Három kávé 1350 Ft, egy szendvics 890 Ft: itt a kávé a megfelelő termék.

### Rövid minta: legnagyobb mérés

```python
legnagyobb = None
for meres in [4, 9, 6]:
    if legnagyobb is None or meres > legnagyobb:
        legnagyobb = meres
print(legnagyobb)
```

A None azt jelzi, hogy még nincs kiválasztott érték. A bal oldali feltétel igaz értékénél az or jobb oldalát nem kell kiértékelni, így nem hasonlítunk számot None-hoz. A saját feladatodban a kiszámított részösszeg mellett a hozzá tartozó terméknevet is meg kell őrizned. Ne használd a max vagy sorted függvényt: most a kereső ciklust írod meg.

### Te alakítsd át

A `legtobb_bevetelt_ado_termek(darabszamok, arak)` a legnagyobb részösszeghez tartozó nevet adja vissza. Üres darabszámszótárra None az eredmény. Azonos részösszegnél az először bejárt termék maradjon; ehhez a pontos egyezés ne cserélje le a korábbi választást. A darabszámok pozitív egészek, a kulcsok ismertek. Nincs szükség bemenetellenőrzésre vagy kiírásra a függvényben.

### C3 ellenőrző esetek

| Azonosító | Darabszámok és árak | Eredmény |
|---|---|---|
| C3.1 | `{"kávé": 3, "szendvics": 1}`, alapárak | `"kávé"` (1350 > 890) |
| C3.2 | `{"kávé": 1, "szendvics": 2}`, alapárak | `"szendvics"` (1780 > 450) |
| C3.3 | `{}`, alapárak | `None` |
| C3.4 | Darabok `{"tea": 2, "kakaó": 1}`, árak `{"tea": 300, "kakaó": 600}` | `"tea"`, mindkét részösszeg 600 Ft. |
| C3.5 | Az előző darabszámokat fordított sorrendben írd be: `{"kakaó": 1, "tea": 2}` | `"kakaó"`, a most először bejárt termék. |

**Kész, ha:** részösszeg alapján választasz, megőrzöd a hozzá tartozó nevet, üres adatra és holtversenyre is megfelelő az eredmény, a bemenetek változatlanok.

## K5 – Új árjegyzék készítése árkorrekcióval

**Fájl:** `arkorrekcio.py`. **Idő:** 10 perc.
A korábbi K1 az eltávolító feladat maradt, ezért az új árkorrekció K5 azonosítót kap.

### Mit csinál majd a program?

A2-ben a kapott szótár egy értékét módosítottad. Most egy új árjegyzéket adsz vissza, amelyben minden ár ugyanannyi forinttal magasabb. Az eredeti árjegyzék változatlan marad, így össze lehet hasonlítani a két változatot.

### Rövid minta: külön teremterv

```python
ferohelyek = {"A": 20, "B": 30}
terv = ferohelyek.copy()
terv["A"] = 24
print(ferohelyek)
print(terv)
```

A copy új szótárat készít; az egyszerű `terv = ferohelyek` csak ugyanarra a szótárra adna másik nevet. A példában egész számértékek vannak, ezért ez a másolat elegendő. A saját feladatban minden termék árát az `emeles` paraméter alapján kell kiszámítani, nem egyetlen kulcsot átírni.

### Te alakítsd át

Az `emelt_arjegyzek(arak, emeles)` az eredeti szótár bejárásával töltse fel az előkészített üres szótárat. Minden kulcs maradjon meg, az új érték a régi ár és az emelés összege legyen. Az új szótár a ciklus után térjen vissza; a függvényben ne legyen print. Az emeles nemnegatív egész, az alapárak pozitív egészek; most nem kérünk általános típusellenőrzést.

### K5 ellenőrző esetek

| Azonosító | Adatok | Elvárt új szótár |
|---|---|---|
| K5.1 | Alapárak, emelés 50 | kávé 500, szendvics 940, üdítő 440, croissant 570 |
| K5.2 | Alapárak, emelés 0 | Ugyanazok az árak egy új szótárban. |
| K5.3 | `{}`, emelés 50 | `{}` |
| K5.4 | `{"tea": 350}`, emelés 25 | `{"tea": 375}` |

Mindig ellenőrizd a főprogram kiírásán, hogy az eredeti árjegyzék változatlan. K5.2-ben a hívás után a főprogramban módosítsd az új szótár kávéárát 999-re: az eredetiben továbbra is 450 legyen. Ez külön ellenőrzi, hogy valóban két külön szótár készült.

**Kész, ha:** az összes kulcsot feldolgozod, az emeles paramétert használod, új szótárat adsz, az eredeti és az új későbbi módosításai nem keverednek.
