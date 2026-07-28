---
name: edu-analytic-geometry
category: Oktatási támogatás
description: >-
  Egy analitikus-geometriai feladatot egy önálló, interaktív oktató weblappá old
  meg: bal oldali feladat + dinamikus vezérlőpult (egy változtatható paraméter-csúszka
  által vezérelt, valós idejű újraszámolt mennyiségek + elméleti tartomány/állandó
  érték kijelzés), középső KaTeX lépésenkénti megoldás, jobb oldali 2D Canvas
  dinamikus geometriai rajzlap (ellipszis/hiperbola/parabola/kör + mozgó egyenes/mozgó
  pont + vektor + címkék + rajztoll firkálás). Három belépési módot támogat —
  megadott szöveges feladat, véletlenszerű feladatgenerálás, feltöltött feladatkép
  felismerése utáni megoldás. Lefedi a standard egyenlet, húrhossz, vektor
  skaláris szorzat tartomány/állandó érték, háromszögterület szélsőértéke, fix
  pont, állandó érték (szorzat meredekségek), pályagörbe, excentricitás feladattípusokat,
  egységes „paraméteres egyenes x=my+c + egyenletrendszer + Vieta + helyettesítés/
  konstansszétválasztás" módszerrel, és sympy pontos számolás vezérli (a válasz,
  koordináták, lépésszámok és az interaktív motor elméleti tartománya egy
  forrásból származnak, konzisztensek). Más ügynök is meghívhatja ezt a skill-t
  az ilyen weblapok előállítására. Kialakításában párhuzamos az edu-solid-geometry
  skill-lel, de Canvas-2D + KaTeXet használ (nem Three.js-t).
  Trigger-szavak: analitikus geometria, kúpszeletek, ellipszis, hiperbola, parabola,
  egyenes és kúpszelet, fókuszhúr, húrhossz, skaláris szorzat tartomány, vektor
  skaláris szorzat, fix pont, állandó érték, szorzat meredekségek, háromszögterület
  szélsőértéke, pályagörbe egyenlet, excentricitás, oldd meg ezt az analitikus
  geometriai feladatot, generálj egy véletlen kúpszelet-feladatot, ezen a képen
  lévő analitikus geometriai feladat; analytic geometry, conic sections, ellipse,
  hyperbola, parabola, chord length, dot product range, fixed point, fixed value,
  locus, eccentricity, interactive analytic geometry solution page.
---

# Analitikus geometria megoldás → interaktív weblap

## Mit állít elő ez a skill
Egy böngészőben azonnal megnyitható egylapos HTML (három oszlop):
- **Bal oldali**: feladat + dinamikus vezérlőpult — egy változtatható paraméter-csúszka (pl. egyenes hajlásszöge θ / mozgópont paraméter t), amely valós idejű újraszámolt geometriai mennyiségeket vezérel (metszéspont-koordináták, meredekség, skaláris szorzat, húrhossz, terület…), valamint „elméleti tartománysáv" vagy „állandó érték kijelzés".
- **Középső**: lépésenkénti megoldás (képletekkel **KaTeX**), egyetlen kattintással összecsukható, hogy a rajzlapnak adjon helyet.
- **Jobb oldali**: 2D Canvas dinamikus geometriai rajzlap (kúpszeletek + mozgó egyenes/mozgópont + vektor + pontcímkék + rács koordinátatengelyek), rajztoll-eszköztár rávetítve.

Kialakításában megegyezik a skill `template/board.html` sablonjával.

## Függőségek (fontos)
A számítási mag `lib/analytic_kernel.py` a **sympy**-től függ. A szkript futtatása előtt győződj meg róla, hogy van egy olyan értelmező, amely importálni tudja a sympy-t: `python3 -c "import sympy"` (ajánlott Python 3.11+, sympy ≥ 1.12).

**Ha hiányzik a könyvtár**: ha az import hibát jelez (sympy vagy bármely későbbi könyvtár), **előbb kérdezd meg a felhasználót, hogy telepítheted-e**, és csak hozzájárulás után telepítsd (`python3 -m pip install <könyvtárnév>`), vagy válassz egy olyan értelmezőt, amelyen már telepítve van; **ne telepíts kérdezés nélkül**.
Az alábbi `python3` mindig ezt a függőségeket kezelő értelmezőt jelöli.

## Munkafolyamat

### 1. lépés: problem spec megszerzése (három belépés egyesítve)
A feladatot strukturált spec-ké alakítsd (görbetípus és paraméterek, ismert pontok/feltételek, keresett típus és objektum, nyelv).
- **Szöveges feladat**: közvetlenül emeld ki.
- **Kép**: vizuális olvasással emeld ki, és **a felismert feladatot mutasd vissza a felhasználónak megerősítésre** (feladat/görbe/paraméterek/keresett/nyelv), mielőtt folytatod.
- **Véletlenszerű feladat**: válassz görbét + feladattípust, véletlenszerű paraméterek → kernel megoldása, ellenőrizd az `analytic_kernel.is_clean(...)` függvénnyel, hogy a válasz rendben van-e; ha nem, újra sorsolj.

> **A kimenet nyelve a prompt nyelvét követi**: angol prompt → angol weblap, kínai → kínai. A spec rögzítse a `language` mezőt.

### 2. lépés: Pontos számítás kernel segítségével (ne számolj fejből)
A `references/conventions.md` megoldási receptje szerint hívd meg a `lib/analytic_kernel.py` és `lib/conics.py` modulokat:
- `conics.ellipse/hyperbola/parabola/circle(...)` → görbeobjektum (pontos a,b,c, fókuszpontok, csúcsok, direktrix, aszimptoták, `eq_latex`, és a frontend-motor számára `board` dict).
- `chord_setup(conic, through)` — paraméteres egyenes `x=my+c` egyenletrendszerbe állítása → y másodfokú egyenlete + Vieta-mennyiségek (pontosan).
- Célmennyiségek: `dot_product_expr` / `chord_len_sq_expr` / `triangle_area_expr` / `slope_product_central` …
- Tartomány: `range_over_m(expr, horizontal_valid=?)` — **nyílt/zárt végpont megítélése** (kritikus helyeségi pont, lásd lent).
- Állandó érték: `is_constant_in_m(expr)`.

A kernel parancssorból is önellenőrizhető:
```bash
python3 lib/analytic_kernel.py      # beépített állítások önellenőrzése
```

> ⚠️ **A végpont nyílt/zárt = helyeségi kritikus pont**: a fókuszponton átmenő húr esetén a vízszintes egyenes (x-tengely, θ=0) és a függőleges egyenes (θ=90) egyaránt érvényes egyenes; az általuk felvett végpontokat számolni kell. Példa: ellipszis MA·MB feladat, x-tengely felveszi −3, függőleges egyenes felveszi 7/4, tehát a válasz **zárt intervallum** `[-3, 7/4]` (sok tankönyv tévesen nyitottként `(-3, 7/4]` írja). A `range_over_m` ezen dönt, és így a válasz konzisztens az interaktív eszközzel — a csúszkát 0°-ra húzva −3 olvasható le. A parabola fókuszhúrjának „tengelyirányú" egyenes degradált (csak egy metszéspont), ennek határvégpontját nem kell számolni (`horizontal_valid=False` vagy paramétertartomány korlátozása).

### 3. lépés: Adatok összerakása és sablonba injektálása

> 📍 **Kimeneti hely & egyetlen termék (legfontosabb)**: a felhasználónak átadott **egyetlen `.html`**, amelyet az **aktuális munkakönyvtárba (`Path.cwd()`)** írsz (kivéve, ha a felhasználó explicit útvonalat ad meg). A cwd-ben **ne hagyj semmilyen más fájlt** — a build-szkript (`.py`), `__pycache__`, ellenőrző képernyőképek (`.png`), átmeneti fájlok **nem termékek**, ezeket tedd a `/tmp`-be vagy töröld használat után.
> **Soha ne** írd a skill saját könyvtárába (`skills/edu-analytic-geometry/output/` belső minta).

Az „adatok összerakása + sablonba injektálása" **build-szkriptet tedd átmeneti könyvtárba** (pl. `/tmp/ag_build.py`), és **csak az `.html`-t írd a cwd-be**; a szkript építse fel a `lesson` / `steps` / `board` adatokat (séma: `references/problem-schema.md`), hívd meg a `generate.render_html(data, out)` függvényt az injektáláshoz a `template/board.html` sablonba, **futtatás után töröld a szkriptet**:

```python
# A build-szkript a /tmp-be kerüljön (ne a cwd-be): /tmp/ag_build.py
import sys; sys.dont_write_bytecode = True            # ne hozz létre __pycache__-et
sys.path.insert(0, "<skill-könyvtár>/scripts")
import generate
from pathlib import Path
data = {"lesson": {...}, "steps": [...], "board": {...}}
out = Path.cwd() / "solution-<feladat-rövid-leírás>.html"   # egyetlen termék, a felhasználó aktuális könyvtárában
generate.render_html(data, out)
```

```bash
python3 -B /tmp/ag_build.py && rm -f /tmp/ag_build.py   # -B: nem ír bytecode; futtatás után töröld az ideiglenes szkriptet, cwd-ben csak .html marad
```

- A `steps[*].content` számai **közvetlenül a kernel eredményeiből származzanak** (`K.tex(...)` LaTeX kimenete), a modell csak a magyarázó szöveget szervezi (a célnyelven).
- A `board` a kernel által adott görbe `board` dict-jét, pontos pontkoordinátáit, `param`, `derived` építési sorozatát, `readouts`, `rangeBar` (tartomány-feladat) / `constant` (állandó érték feladat) / `answerBand` (**alakparaméter-feladat**, pl. excentricitás tartomány) felhasználásával épüljön.
- **Alakparaméter-feladat (csúszka = excentricitás e stb.)**: ha a természetes dinamikus mennyiség maga a görbe alakja (nem mozgó egyenes/pont), a csúszka legyen ez a paraméter, a görbe `a/b/c`, fókuszpontok, mozgópont koordináták legyenek `@param`-függő **kifejezés-stringek** (a motor minden képkockán újra rajtolja a görbét/fókuszpontokat/aszimptotákat), `status` kijelzéssel az egyenlőtlenség állapotáról, `answerBand` a paraméter-tengelyen kiemelve a válaszintervallumot. Lásd a conventions „alakparaméter-feladat" szakaszát.
- **Közvetlenül másolható minták**: a `scripts/generate.py` 6 `build_*` függvénye lefedi az interakciós paradigmákat: `ellipse_dot_range` (tartománysáv), `ellipse_chord_range`, `ellipse_area_max`, `ellipse_slopeprod_const` (állandó érték · közép-szimmetria), `parabola_dot_const` (állandó érték · parabola), `hyperbola_ecc_range` (**alakparaméter**: csúszka=e, a görbe vele újrarajzolva + `status` + `answerBand`).

Regisztrált feladat közvetlenül előállítható (`-B` nem ír bytecode-ot; ha nem adunk meg útvonalat, alapértelmezetten a skill output könyvtárába ír; ha a felhasználónak adjuk át, mindenképpen cseréld le cwd alatti `.html`-re):
```bash
python3 -B scripts/generate.py list                      # feladattípusok listázása
python3 -B scripts/generate.py ellipse_dot_range ./sol.html
python3 -B scripts/generate.py all ./out_dir             # az összes feladattípus
```

### 4. lépés: Önellenőrzés (helyességi séma)
- kernel válasz == válaszkártya `lesson.answer` == utolsó lépésben megjelenített érték == **JS standard pozíció/szakasz újraszámított értéke**, mind a négy egyezik (a `build_*` már tartalmaz `assert`-et).
- A `rangeBar` végpontjai a kernel `range_over_m` értékeiből; a `constant` értéke a kernel állandó értékéből származik.
- Indíts egy helyi statikus szervert (a **kimeneti fájlt tartalmazó könyvtárat**, azaz cwd-t szolgáld ki), és ellenőrizz előnézettel: nincs konzolhiba, KaTeX renderel jól, a csúszka valós idejű újraszámolása helyes, a tartománysáv/állandó/fixpont/pályagörbe viselkedés megfelelő, a rajztoll és az összecsukható panel használható.
  (A skill repóján belüli fejlesztéskor használható a `.claude/launch.json` `ag-preview`-je, 4601-es port; máshol futtatva a cwd-re indíts egy ideiglenes statikus szervert.)
- **Az önellenőrző képernyőkép csak neked legyen**: a preview eszköz közvetlenül képet ad vissza, **ne ments `.png`-t a cwd-be**; a helyi statikus szerver csak olvas, nem ír, nem hoz létre fájlt. Minden átmeneti fájlt (build-szkript `.py`, képernyőkép `.png`, `__pycache__` stb.), amit az önellenőrzés hozott létre, az átadás előtt tisztítsd el.

> ⚠️ **Be kell zárnod a portokat/szervereket, amiket indítottál**: amint vége az előnézetnek, azonnal állítsd le, **soha ne hagyj portot lefoglaló folyamatot**.
> - A preview eszköz által indított: `preview_stop` (adj át serverId-t).
> - Közvetlenül indított `http.server`: használat után `kill`, vagy `lsof -nP -iTCP:<port> -sTCP:LISTEN` ellenőrzés, hogy felszabadult-e.
> - Az átadás előtt győződj meg róla, hogy a port felszabadult, csak utána mondd meg a felhasználónak. Ha kinyitod és nem zárod = befejezetlen önellenőrzés.

### 5. lépés: Átadás
A készterméket a **felhasználó aktuális munkakönyvtárába (cwd)** írd, nevét `solution-<feladat-rövid-leírás>.html` alakban, mondd meg az útvonalat a felhasználónak, és böngészővel azonnal megnyitható. Átadás előtt győződj meg: **(1)** a termék a cwd-ben van, nem a skill könyvtárában; **(2)** nincs hátrahagyott helyi szerver/port a mostani előnézetből; **(3)** a cwd-ben **csak ez az egy új `.html`** jelent meg — nincs `.py` / `.png` / `__pycache__` / átmeneti fájl (ellenőrizd `git status` vagy `ls` segítségével, ha van, töröld).

## Bővítés
- **Feladattípus hozzáadása**: az `analytic_kernel.py`-ba adj célmennyiség-függvényt (m kifejezéseként) + újrahasználd a `range_over_m` / `is_constant_in_m` függvényeket; a `generate.py`-ba adj egy `build_*` függvényt, válaszd ki az interakciós paradigmát (tartománysáv / állandó / fixpont / pálya trace / alakparaméter answerBand). Lásd a `references/conventions.md` recepttáblát.
- **Görbe hozzáadása**: a `conics.py` már tartalmaz ellipszis/hiperbola/parabola/kört; a frontend `board.html` motor már támogatja mind a négy típusú megjelenítést, aszimptotákat, direktrix-irányokat. Új görbe esetén mindkét helyen adj egy példányt.
- **Interakciós szerkezet hozzáadása**: a `board.html` `buildScene` switch-je a szerkezet-könyvtár (`line_through_angle`, `intersect_line_conic`, `point_on_conic`, `point_reflect`, `tangent_at`, `foot_perp`…), bővítsd szükség szerint és regisztráld a séma-dokumentumban.

## Könyvtár
- `template/board.html` — adatvezérelt sablon (általános 2D megjelenítő + paraméter-motor + adatsziget `__LESSON_DATA__`)
- `lib/conics.py` — kúpszeletek sympy-definíciós könyvtára (speciális pontok / LaTeX / board dict)
- `lib/analytic_kernel.py` — sympy pontos megoldó mag (egyenletrendszer·Vieta·tartomány·állandó érték)
- `scripts/generate.py` — sabloninjektálás + 6 build_* minta + tömeges/egyszeri feladatgyártás
- `references/problem-schema.md` — adatformátum (board motor séma)
- `references/conventions.md` — standard alak, megoldási recepttábla, Vieta/helyettesítés séma, végpont nyílt/zárt, önellenőrzés
