---
name: edu-solid-geometry
category: Oktatási támogatás
description: >-
  Egy szilárdtest-geometriai feladatot egy önálló, interaktív oktató weblappá old
  meg: bal oldalon MathJax lépésenkénti megoldás, jobb oldalon Three.js
  interaktív 3D modell (lépésenkénti kiemelés + kameraváltás). Három belépési
  módot támogat — megadott szöveges feladat, véletlenszerű feladatgenerálás,
  feltöltött feladatkép felismerése utáni megoldás. Lefedi a kocka/téglatest,
  gúla/osztlop, henger/kúp esetén az egyenes-sík szöget, hajlásszöget, kitérő
  egyenesek szögét, pont-sík távolságát, térfogat feladattípusokat, egységesen
  „koordináta-rendszer felállítása + vektormódszerrel", sympy pontos számítás
  vezérli (a válasz, 3D koordináták, lépésszámok egy forrásból származnak,
  konzisztensek). Más ügynök is meghívhatja ezt a skill-t az ilyen weblapok
  előállítására.
  Trigger-szavak: szilárdtest-geometria, egyenes-sík szög, hajlásszög, kitérő
  egyenesek, pont-sík távolság, négyszög alapú gúla, kocka szögszámítás, oldd
  meg ezt a geometriai feladatot, generálj egy véletlen szilárdtest-geometriai
  feladatot, ezen a képen lévő szilárdtest-geometriai feladat; solid geometry,
  line-plane angle, dihedral angle, angle between skew lines, distance to plane,
  interactive geometry solution page.
---

# Szilárdtest-geometria megoldás → interaktív weblap

## Mit állít elő ez a skill
Egy böngészőben azonnal megnyitható egylapos HTML: bal oldalon feladat/válasz/lépésenkénti megoldás (képletekkel MathJax-szel), jobb oldalon a feladatnak megfelelő 3D modell (Three.js, forgatható/zoomolható, lépésenként kiemeli a kulcselemeket és váltja a kamerát).
Kialakításében megegyezik a `template/lesson.html` sablonnal.

## Függőségek (fontos)
A számítási mag `lib/geometry_kernel.py` a **sympy**-től függ. A szkript futtatása előtt győződj meg róla, hogy van egy olyan `python3`, amely importálni tudja a sympy-t: futtasd `python3 -c "import sympy"`.

**Hiányzó könyvtár kezelése (fontos)**: ha az import hibát jelez (sympy vagy bármely később használt könyvtár esetén ugyanez érvényes), **előbb kérdezd meg a felhasználót, hogy telepítheted-e**, és hozzájárulás után segíts telepíteni (`python3 -m pip install <könyvtárnév>`), vagy válassz egy olyan értelmezőt, amelyen már telepítve van; **ne telepíts kérdezés nélkül**.
Az alábbi parancsokban a `python3` mindig ezt a függőségeket kezelő értelmezőt jelöli.

## Munkafolyamat

### 1. lépés: problem spec megszerzése (három belépés egyesítve)
A feladatot strukturált spec-ké alakítsd (formátum: `references/problem-schema.md`): geometriai test típusa és méretei, ismert konstrukciós pontok/feltételek, keresett típus és objektum, **nyelv**.
- **Szöveges feladat**: közvetlenül emeld ki.
- **Kép**: vizuális olvasással emeld ki, és **a felismert feladatot mutasd vissza a felhasználónak megerősítésre** (feladat/geometriai test/méretek/keresett/nyelv), mielőtt folytatod.
- **Véletlenszerű feladat**: válaszd ki a geometriai testet és feladattípust, a kernel véletlenszerű paraméterekkel oldja meg; ha a válasz nem rendben, újra sorsolj.

> **A kimenet nyelve a prompt nyelvét követi**: angol prompt → angol weblap, kínai → kínai. A spec rögzítse a `language` mezőt.

### 2. lépés: Pontos számítás kernel segítségével (ne számolj fejből)
A `references/conventions.md` koordináta-rendszer-felállítási konvenciói és megoldási receptje szerint hívd meg a `lib/geometry_kernel.py`-t: kapj pontos koordinátákat, kulcsvektorokat, normálvektorokat, végleges választ, valamint az egyes lépésekben megjelenítendő közbülső mennyiségeket (mind LaTeX-stringként).
A csúcsok three.js koordinátáit a `kernel.to_three(points, scale)` függvénnyel kapd meg.

A kernel parancssorból is ellenőrizhető, például:
```bash
python3 lib/geometry_kernel.py    # beépített minta önellenőrzése
```

### 3. lépés: lesson data összerakása és sablonba injektálása

> 📍 **Kimeneti hely (fontos)**: a kész HTML-t mindig a **felhasználó aktuális munkakönyvtárába (`Path.cwd()`)** írd, kivéve, ha a felhasználó explicit útvonalat ad meg.
> **Soha ne** írd a skill saját könyvtárába (`skills/edu-solid-geometry/output/` stb.) — az a skill belső fejlesztési mintakönyvtára.
> Az ideiglenes build-szkriptet is tedd a cwd-be vagy egy átmeneti könyvtárba (pl. `/tmp`), és használat után törölheted.

Írj egy **ideiglenes build-szkriptet**, amely importálja a kernel, bodies, generate modulokat, felépíti a `lesson` / `steps` / `model` adatokat (séma: `references/problem-schema.md`), majd meghívja a `generate.render_html(data, out)` függvényt a sablon injektálásához és a HTML előállításához.
Az `out` a **cwd alatti abszolút útvonal** legyen:

```python
from pathlib import Path
out = Path.cwd() / "solution-<feladat-rövid-leírás>.html"   # a felhasználó aktuális könyvtárába kerül, nem a skill könyvtárába
generate.render_html(data, out)
```

- A `steps[*].content` összes számát **közvetlenül a kernel számítási eredményeiből vedd**, a modell csak a magyarázó szöveget szervezi (a célnyelven).
- A `model.points` a `kernel.to_three(...)` eredménye; a `model.spheres`/`edges` a `lib/bodies.py` topológiáját használja (`quad_pyramid` / `tri_pyramid` / `cuboid` / `cube` / `prism`); ritka geometriai testnél az edges kézzel is megírható.
- Minden lépéshez adj `highlight`-ot (a lépésben látható elemek abszolút halmaza) és `cameraPos`-t.
- **Ha a feladat oldalhosszakat ad meg**: a megfelelő élhez adj `measure` elemet (`label` LaTeX-szel, pl. `2\sqrt{2}`), és tedd a „koordináta-rendszer felállítása / ismert feltételek felsorolása" lépés `highlight`-jába, hogy a 3D ábrán a pontnál fel legyen tüntetve a hossz (lásd problem-schema).
- Angol kimenet esetén töltsd ki a `lesson.ui` angol szövegeit és állítsd be `lesson.language="en"`.

**Közvetlenül használható minták**: a `scripts/generate.py` `build_data()` (négyszög alapú gúla · egyenes-sík szög), `build_cube_data()` (kocka · egyenes-sík szög), `build_box_volume_data()` (téglatest · térfogat) mind teljes minták, ezeket módosítva lehet követni.

A `generate.py` közvetlenül előállíthatja a regisztrált feladatokat; **ha nem adsz meg útvonalat, alapértelmezetten a cwd-be ír**; megadható a cwd alatti fájlnév is (a skill könyvtárában lévő `scripts/generate.py` segítségével, a kimenet a cwd-be kerül):
```bash
python3 <skill-könyvtár>/scripts/generate.py cube ./cube.html
python3 <skill-könyvtár>/scripts/generate.py box  ./box.html
```

**Véletlenszerű feladat**: `generate.py random <seed> [kimenet.html]`, belsőleg `kernel.is_clean(...)` dönti el, hogy a válasz rendben van-e, ha nem, újra sorsol:
```bash
python3 <skill-könyvtár>/scripts/generate.py random 7 ./random.html   # útvonal megadása nélkül alapértelmezett ./random.html (cwd)
```
Véletlen feladattípus bővítésekor követtesd a „véletlenszerű paraméter → megoldás → is_clean, ha nem megfelelő, újra sorsol" sémát.

### 4. lépés: Önellenőrzés (helyességi séma)
- kernel válasz == válaszkártya `answerValue` == utolsó lépésben megjelenített végleges érték (a generate.py már tartalmaz példa assert-et).
- A 3D csúcskoordináták a `kernel.to_three`-ből származnak (ugyanabból a forrásból, mint a megoldás).
- Indíts egy helyi statikus szervert (a **kimeneti fájlt tartalmazó könyvtárat**, azaz cwd-t szolgáld ki), és ellenőrizz előnézettel: nincs konzolhiba, a képletek jól renderelnek, a lépésenkénti kiemelés/kameraváltás megfelelő.
  (A skill repóján belüli fejlesztéskor használható a `.claude/launch.json` `geom-preview`-je; máshol futtatva a cwd-re indíts egy ideiglenes statikus szervert.)

> ⚠️ **Be kell zárnod a portokat/szervereket, amiket indítottál**: amint vége az előnézetnek, azonnal állítsd le a helyi szervert, **soha ne hagyj portot lefoglaló folyamatot**.
> - A preview eszköz által indított: ellenőrzés után azonnal `preview_stop` (add meg a megfelelő serverId-t).
> - Közvetlenül indított `http.server`: használat után `kill`, vagy ellenőrizd `lsof -nP -iTCP:<port> -sTCP:LISTEN` segítségével, hogy felszabadult-e.
> - Az átadás előtt győződj meg róla, hogy a port felszabadult, csak utána mondd meg a felhasználónak az eredményt. Ha kinyitod és nem zárod = befejezetlen önellenőrzés.

### 5. lépés: Átadás
A készterméket a **felhasználó aktuális munkakönyvtárába (cwd)** írd, nevét `solution-<feladat-rövid-leírás>.html` alakban, mondd meg a (cwd alatti) útvonalat a felhasználónak, és böngészővel azonnal megnyitható.
Átadás előtt győződj meg: **(1)** a termék a cwd-ben van, nem a skill könyvtárában; **(2)** nincs hátrahagyott helyi szerver/port a mostani előnézetből.

## Bővítés
- **Feladattípus hozzáadása**: a `geometry_kernel.py`-ba adj megoldó függvényt (lásd a conventions recepttábláját), a `generate.py`-ba adj egy `build_*` függvényt.
- **Geometriai test hozzáadása**: a `geometry_kernel.py`-ba adj koordináta-építő függvényt, a `bodies.py`-ba adj él-topológiát.

## Könyvtár
- `template/lesson.html` — adatvezérelt sablon (általános 3D megjelenítő + adatsziget `__LESSON_DATA__`)
- `lib/geometry_kernel.py` — sympy pontos számítási mag
- `lib/bodies.py` — geometriai test él-topológiai könyvtára
- `scripts/generate.py` — sabloninjektálás + minta építő függvények
- `references/problem-schema.md` — adatformátum
- `references/conventions.md` — koordináta-rendszer konvenciók, megoldási recept, önellenőrzés
