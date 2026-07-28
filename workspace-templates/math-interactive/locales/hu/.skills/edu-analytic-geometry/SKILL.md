---
name: edu-analytic-geometry
description: >-
  Egy analitikus geometriai feladatot önálló, interaktív oktatási weboldallá old meg:
  bal oldalon feladatleírás és dinamikus konzol (változóparaméter-csúszka által
  valós időben újraszámolt geometriai mennyiség + elméleti tartomány/állandóérték-jelzés),
  középen KaTeX-es lépésenkénti levezetés, jobb oldalon 2D Canvas dinamikus
  geometriatábla (ellipszis/hiperbola/parabola/kör + mozgó egyenes/pont + vektorok
  + feliratok + rajzeszköz). Három bemenetet támogat: szöveges feladat, véletlen
  feladat és feltöltött feladatkép felismerése utáni megoldás. Lefedi a standard
  egyenletet, húrhosszt, vektor skalárszorzatának tartományát/állandó értékét,
  háromszög-terület szélsőértékét, fix pontot, állandó értéket (meredekségek
  szorzata), mértani helyet, excentricitást és hasonló feladatokat. Egységesen az
  "paraméteres egyenes x=my+c + közös megoldás + Viète + változócsere/konstans
  szétválasztása" megközelítést alkalmazza, sympy pontos számításaival hajtva
  (azonos forrásból származó válasz, koordináták, lépésszámértékek és interaktív
  motor elméleti tartománya). Más agentek is használhatják ilyen oldalak készítésére.
  Formája párhuzamos az edu-solid-geometry készséggel, de Canvas-2D + KaTeX-et
  használ (nem Three.js-t).
  Kiváltó szavak: analitikus geometria, kúpszeletek, ellipszis, hiperbola, parabola,
  egyenes és kúpszelet, fókuszhúr, húrhossz, skalárszorzat tartománya, vektor
  skalárszorzata, fixpont-feladat, állandóérték-feladat, meredekségek szorzata,
  háromszög-terület szélsőértéke, mértani hely egyenlete, excentricitás, oldd meg
  ezt az analitikus geometriai feladatot, adj véletlen kúpszelet-feladatot, az ezen
  a képen lévő analitikus geometriai feladat; analytic geometry, conic sections,
  ellipse, hyperbola, parabola, chord length, dot product range, fixed point, fixed
  value, locus, eccentricity, interactive analytic geometry solution page.
---

# Analitikus geometriai feladat megoldása → interaktív weboldal

## Mit állít elő ez a skill

Egy böngészőben közvetlenül megnyitható, egyoldalas HTML-t (három oszlopban):
- **Bal oszlop**: feladatleírás + dinamikus konzol — egy változóparaméter-csúszka (például egyenes dőlésszöge θ / mozgópont-paraméter t) által valós időben újraszámolt geometriai mennyiségek (metszéspont-koordináták, meredekség, skalárszorzat, húrhossz, terület stb.), valamint "elméleti tartománysáv" vagy "állandóérték-jelzés".
- **Középső oszlop**: lépésenkénti levezetés (**KaTeX** képletekkel), amely egy kattintással összecsukható, hogy több hely maradjon a táblának.
- **Jobb oszlop**: 2D Canvas dinamikus geometriatábla (kúpszelet + mozgó egyenes/pont + vektorok + pontfeliratok + koordinátatengelyes rács), ráhelyezett rajzeszköz-eszköztárral.

A forma megfelel e skill `template/board.html` sablonjának.

## Függőségek (fontos)

A számítási mag `lib/analytic_kernel.py` fájlja **sympy**-t igényel. A szkriptek futtatása előtt ellenőrizd, hogy létezik olyan értelmező, amely importálni tudja a sympy-t: `python3 -c "import sympy"` (javasolt: Python 3.11+, sympy ≥ 1.12).

**Hiányzó könyvtár esetén**: ha az import hibát ad (sympy vagy bármely későbbi könyvtár), **először kérdezd meg a felhasználót**, telepíthető-e; beleegyezés után telepítsd (`python3 -m pip install <könyvtár_neve>`), vagy válassz olyan értelmezőt, amelyben már telepítve van. **Ne telepíts kérdés nélkül.** A továbbiakban `python3` mindig ezt, a függőségeket futtatni képes értelmezőt jelenti.

## Munkafolyamat

### 1. lépés: problem spec előállítása (a három bemenet egységesítése)

Rendezd a feladatot strukturált specifikációvá: görbetípus és paraméterei, adott pontok/feltételek, a keresett típus és objektum, nyelv.
- **Szöveges feladat**: közvetlenül vedd ki az adatokat.
- **Kép**: vizuálisan olvasd ki, és **jelenítsd meg a felismert feladatot a felhasználónak megerősítésre** (feladatleírás/görbe/paraméterek/keresett érték/nyelv), mielőtt folytatod.
- **Véletlen feladat**: válassz görbét + feladattípust, generálj véletlen paramétereket → oldd meg a kernellel; `analytic_kernel.is_clean(...)` segítségével vizsgáld az eredmény rendezettségét, és rendezetlen válasz esetén generálj újra.

> **A kimenet nyelve kövesse a prompt nyelvét**: angol prompt → angol weboldal, kínai prompt → kínai. A spec rögzítse a `language` értékét.

### 2. lépés: pontos számítás a kernellel (ne fejben számolj)

A `references/conventions.md` megoldási receptje szerint hívd a `lib/analytic_kernel.py` és `lib/conics.py` fájlokat:
- `conics.ellipse/hyperbola/parabola/circle(...)` adja a görbeobjektumot (pontos a,b,c, fókuszok, csúcspontok, vezéregyenesek, aszimptoták, `eq_latex`, valamint a frontend motornak szánt `board` dict).
- `chord_setup(conic, through)` az `x=my+c` paraméteres egyenest a görbével együtt oldja meg, y szerinti másodfokú egyenletet és pontos Viète-mennyiségeket ad.
- Célmennyiségek: `dot_product_expr` / `chord_len_sq_expr` / `triangle_area_expr` / `slope_product_central` …
- Értéktartomány: `range_over_m(expr, horizontal_valid=?)` — **a nyílt/zárt végpontok megállapításával** (kritikus helyességi pont; lásd alább).
- Állandó érték: `is_constant_in_m(expr)`.

A kernel parancssorból is önellenőrizhető:
```bash
python3 lib/analytic_kernel.py      # Beépített assert-önellenőrzés a kiemelt feladathoz
```

> ⚠️ **A végpontok nyíltsága/zártsága a helyesség kulcsa**: fókuszon átmenő húrnál a vízszintes egyenes (x-tengely, θ=0) és a függőleges egyenes (θ=90) egyaránt érvényes. Az általuk felvett végpontokat be kell számítani. Példa: ellipszis MA·MB feladatban az x-tengely −3 értéket, a függőleges egyenes 7/4 értéket ad, tehát a válasz **zárt intervallum**: `[-3, 7/4]` (sok segédanyag tévesen nyíltként `(-3, 7/4]` írja). A `range_over_m` ezt figyelembe veszi; így a válasz egyezik az interaktív eszközzel — a csúszkát 0°-ra húzva −3 olvasható. Parabola fókuszhúrjánál a "tengelyirány" degenerált egyenes (csak egy pontban metszi a görbét), ezért a határérték nem számít bele (`horizontal_valid=False` vagy korlátozott paramétertartomány).

### 3. lépés: adatok összeállítása és beszúrása a sablonba

> 📍 **Kimeneti hely és egyetlen termék (legfontosabb)**: a felhasználónak átadott eredmény **pontosan egy `.html`**, amelyet az **aktuális munkakönyvtárba (`Path.cwd()`)** kell írni (kivéve, ha a felhasználó kifejezetten más útvonalat ad). A cwd-ben **ne maradjon más fájl** — építőszkript (`.py`), `__pycache__`, önellenőrző képernyőkép (`.png`) és ideiglenes fájlok nem átadandó eredmények; tedd őket `/tmp` alá vagy töröld használat után. **Soha ne írj** a skill saját könyvtárába sem (`skills/edu-analytic-geometry/output/` a skill belső mintakönyvtára).

Írd az "adatok összeállítása + sablonba szúrás" **építőszkriptjét ideiglenes könyvtárba** (például `/tmp/ag_build.py`); a szkript **csak a `.html` fájlt írja a cwd-be**. Állítsa össze a `lesson` / `steps` / `board` adatokat (a séma: `references/problem-schema.md`), hívja meg a `generate.render_html(data, out)` függvényt a `template/board.html` kitöltéséhez, majd **futás után töröld a szkriptet**:

```python
# Az építőszkript /tmp alatt legyen (ne a cwd-ben): /tmp/ag_build.py
import sys; sys.dont_write_bytecode = True            # Ne hozzon létre __pycache__ könyvtárat
sys.path.insert(0, "<skill_directory>/scripts")
import generate
from pathlib import Path
data = {"lesson": {...}, "steps": [...], "board": {...}}
out = Path.cwd() / "solution-<problem_summary>.html"   # Egyetlen termék, a felhasználó aktuális könyvtárában
generate.render_html(data, out)
```

```bash
python3 -B /tmp/ag_build.py && rm -f /tmp/ag_build.py   # -B: nincs bytecode; futtatás után töröld az ideiglenes szkriptet, a cwd-ben csak .html marad
```

- A `steps[*].content` számai **közvetlenül a kernel eredményeire hivatkozzanak** (`K.tex(...)` használatával a LaTeX-hez); a modell feladata kizárólag a magyarázó szöveg megfogalmazása (a célnyelven).
- A `board` a kernel által adott görbe-`board` dictet, pontos pontkoordinátákat, `param`, `derived` szerkezetsorozatot, `readouts`, `rangeBar` (tartományfeladat) / `constant` (állandóérték-feladat) / `answerBand` (**alakparaméter-feladat**, például excentricitás-tartomány) használjon.
- **Alakparaméter-feladatoknál (csúszka = excentricitás e stb.)**: ha a természetes dinamikus mennyiség maga a görbe alakja, és nem egy mozgó egyenes/pont, legyen a csúszka ez a paraméter. A görbe `a/b/c` értékeit, a fókuszokat és a mozgópont koordinátáit `@param`-es **kifejezéskarakterláncként** írd meg (a motor minden képkockában újrarajzolja a görbét/fókuszokat/aszimptotákat), a `status` leolvasóval jelezd az egyenlőtlenség állapotát, az `answerBand` pedig emelje ki a választartományt a paramétertengelyen. Lásd a conventions „Alakparaméter-feladatok” részét.
- **Közvetlenül másolható minta**: a `scripts/generate.py` 6 `build_*` függvénye a különböző interaktív mintákat fedi le: `ellipse_dot_range` (tartománysáv), `ellipse_chord_range`, `ellipse_area_max`, `ellipse_slopeprod_const` (állandó érték, középpontos szimmetria), `parabola_dot_const` (állandó érték, parabola), `hyperbola_ecc_range` (**alakparaméter**: csúszka=e, a görbe újrarajzolása + `status` + `answerBand`).

Regisztrált feladat közvetlen előállítása (`-B` nem ír bytecode-ot; útvonal nélkül alapértelmezésben a skill output könyvtárába ír, ezért felhasználói átadásnál kötelező cwd-beli `.html` útvonalat adni):
```bash
python3 -B scripts/generate.py list                      # Feladattípusok listája
python3 -B scripts/generate.py ellipse_dot_range ./sol.html
python3 -B scripts/generate.py all ./out_dir             # Minden feladattípus
```

### 4. lépés: önellenőrzés (helyességi terv)
- kernel-válasz == válaszkártya `lesson.answer` == az utolsó lépésben látható érték == **JS szabványos helyzetben/szakasz-söpréskor újraszámolt érték**; a négynek egyeznie kell (`build_*` beépített `assert`-ot tartalmaz).
- A `rangeBar` végpontjai a kernel `range_over_m` eredményéből, a `constant` értéke a kernel állandójából származzon.
- Indíts helyi statikus szolgáltatást (**a kimeneti fájl könyvtárát, azaz a cwd-t szolgáld ki**) és előnézetben ellenőrizd: ne legyen konzolhiba, a KaTeX legyen rendben, a csúszka számoljon helyesen valós időben, a tartománysáv/állandóérték/fixpont/mértani hely működjön, valamint a rajzeszköz és az összecsukható panel is használható legyen. (A skill-tároló fejlesztésekor használható a `.claude/launch.json` `ag-preview` bejegyzése a 4601-es porton; más helyen indíts ideiglenes statikus szolgáltatást a cwd-hez.)
- **Az önellenőrző képernyőképek csak neked valók**: az előnézeti eszköz közvetlenül adja vissza a képet; **ne tárolj `.png`-t a cwd-ben**. A helyi statikus szolgáltatás csak olvashat, nem hozhat létre fájlt. Átadás előtt töröld az önellenőrzés bármely ideiglenes fájlját (építőszkript `.py`, képernyőkép `.png`, `__pycache__` stb.).

> ⚠️ **Minden általad indított portot/szolgáltatást kötelező leállítani**: az előnézet végén azonnal állítsd le, **soha ne hagyj portot foglaló folyamatot**.
> - preview eszközzel indított szolgáltatás: `preview_stop` (add meg a serverId-t).
> - közvetlenül indított `http.server`: használat után `kill`, vagy `lsof -nP -iTCP:<port> -sTCP:LISTEN` segítségével ellenőrizd, hogy a port felszabadult.
> - Csak a port felszabadulásának ellenőrzése után tájékoztasd a felhasználót. Az elindított, de le nem állított szolgáltatás = befejezetlen önellenőrzés.

### 5. lépés: átadás

A kész terméket a **felhasználó aktuális munkakönyvtárába (cwd)** írd, `solution-<problem_summary>.html` formátumú névvel; add meg a felhasználónak az útvonalát. Böngészőben közvetlenül megnyitható. Átadás előtt erősítsd meg: **(1)** a kész fájl a cwd-ben van, nem a skill-könyvtárban; **(2)** nem maradt az előnézethez indított helyi szolgáltatás/port; **(3)** a cwd-be **csak ez az egy `.html`** került — nincs `.py`, `.png`, `__pycache__` vagy ideiglenes fájl (ellenőrizd egy pillantással `git status` vagy `ls` segítségével, és töröld, ha van).

## Bővítés
- **Új feladattípus**: adj célmennyiség-függvényt az `analytic_kernel.py` fájlhoz (m szerinti kifejezésként) + használd újra a `range_over_m` / `is_constant_in_m` függvényeket; a `generate.py` fájlhoz adj `build_*`-et, és válassz interaktív mintát (tartománysáv / állandó érték / fix pont / mértanihely-trace / alakparaméter-`answerBand`). Lásd a `references/conventions.md` recepttábláját.
- **Új görbe**: a `conics.py` már tartalmaz ellipszist/hiperbolát/parabolát/kört; a frontend `board.html` motor mind a négyet, az aszimptotákat és a vezéregyenesek irányát is képes megjeleníteni. Az új görbét mindkét helyen egészítsd ki.
- **Új interaktív konstrukció**: a `board.html` `buildScene` switch-e a konstrukciós könyvtár (`line_through_angle`, `intersect_line_conic`, `point_on_conic`, `point_reflect`, `tangent_at`, `foot_perp`…); igény szerint bővítsd, és vezesd fel a séma dokumentumában.

## Könyvtárszerkezet
- `template/board.html` — adatvezérelt sablon (általános 2D renderelő + paramétermotor + `__LESSON_DATA__` adatsziget)
- `lib/conics.py` — kúpszeletek sympy-alapú definíciós könyvtára (speciális pontok / LaTeX / board dict)
- `lib/analytic_kernel.py` — sympy pontos megoldási mag (közös megoldás · Viète · tartomány · állandó érték)
- `scripts/generate.py` — sablonkitöltés + 6 `build_*` minta + kötegelt/egyfeladatos előállítás
- `references/problem-schema.md` — adatformátum (board motor sémája)
- `references/conventions.md` — standard alakok, megoldási recepttábla, Viète/változócsere minták, végpont-nyíltság, önellenőrzés
