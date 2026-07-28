# Adatformátum-referencia (problem-schema)

A három bemenet (szöveg / kép / véletlen) végül ugyanabba az adathalmazba egyesül, amelyet a sablon `template/board.html` fájljának
`<script id="lesson-data">__LESSON_DATA__</script>` adatszigetébe kell beszúrni. Az adat egy három részből álló JSON-objektum:
`lesson` / `steps` / `board`.

## 1. lesson (feladatleírás / válasz / felületszövegek)

```jsonc
"lesson": {
  "language": "zh-CN",                 // A prompt nyelvét követi: zh-CN / en
  "title": "Ellipszis és dinamikus vektorszorzat-tartomány",       // Bal felső cím
  "problem": "<p>… a feladat HTML-leírása, beágyazott képlet $…$, blokk-képlet $$…$$…</p>",
  "answerLabel": "A vektorok skalárszorzatának értéktartománya",   // A válasz szöveges leírása (önellenőrzéshez, nem kötelező megjeleníteni)
  "answer": "$\\left[-3,\\ \\dfrac{7}{4}\\right]$",  // A végső válasz LaTeX-ben (önellenőrzéshez)
  "ui": { "solutionTitle": "Solution", "collapse": "Collapse", ... }  // Opcionális: angol kimenetnél felülírja a felületszövegeket
}
```

A felületszövegek alapértelmezésben kínaiak; kulcsaik a `board.html` fájl elején lévő `UI` objektumban találhatók: `consoleTitle / solutionTitle / collapse /
expand / current / theoRange`. Angol kimenethez állítsd `lesson.language="en"` értékre, és töltsd ki a `lesson.ui` mezőt.

## 2. steps (lépésenkénti levezetés)

```jsonc
"steps": [
  { "title": "Közös megoldás + Viète-tétel", "content": "<p>HTML, a képletekhez $…$ / $$…$$</p>" },
  ...
]
```

Minden lépés automatikusan sorszámot kap (01, 02…). A `content` számai **a kernelből származzanak** (`analytic_kernel.tex(expr)`); a magyarázó szöveget a modell írja a célnyelven.

## 3. board (jelenet + interaktív modell) — új mag

```jsonc
"board": {
  "view": { "xRange": [-3.6, 3.6], "yRange": [-2.6, 2.6] },   // Matematikai koordinátaablak; a motor adaptívan skáláz
  "conics": [ { "name":"C", "kind":"ellipse", "a":2, "b":1.732, "center":[0,0],
                "color":"curve", "label":"C: x²/4+y²/3=1" } ],
  "points": { "M": {"xy":[-1,0], "color":"vecA", "label":"M(-1,0)"}, "F":[1,0] },
  "param": { "name":"e", "label":"Excentricitás $e$", "min":1.05,"max":3,"step":0.01,
             "value":1.5, "unit":"", "standard":1.5, "ticks":["1","2","3"] },
  "scalars": [ { "name":"b", "expr":"sqrt(e*e-1)" } ],                             // Opcionális: a @param-ból származtatott névvel ellátott skalárok, sorban kiértékelve
  "derived": [ /* A paraméter által valós időben vezérelt konstrukciós sorozatot lásd alább */ ],
  "readouts": [ /* A konzol valós idejű értékeit lásd alább */ ],
  "rangeBar": { "of":"dot", "min":-3, "max":1.75, "label":"$[-3,\\ \\frac74]$" },  // Tartomány-/szélsőérték-feladat
  "constant": { "of":"kprod", "label":"$-\\dfrac34$" },                            // Állandóérték-feladat
  "answerBand":{ "min":1,"max":3,"lo":1,"hi":2,"label":"$e\\in(1,2]$" },           // Alakparaméter-feladat: a választartomány kiemelése a paramétertengelyen
  "trace":    { "of":"Q", "color":"locus" },                                       // Mértanihely-feladat (opcionális)
  "legend":   [ { "color":"line", "text":"Mozgó l egyenes" } ]                            // A tábla bal alsó jelmagyarázata (opcionális)
}
```
> A `rangeBar`, `constant` és `answerBand` közül a feladattípusnak megfelelően egyet válassz.

### 3.1 conics[*] (kúpszeletek)
| kind | Kötelező paraméterek | Magyarázat |
|---|---|---|
| `ellipse` | `a`(x féltengely), `b`(y féltengely), `center` | |
| `hyperbola` | `a`(valós féltengely), `b`(képzetes féltengely), `center`, `orient`("x"/"y") | `asymptotes:true` aszimptotákat rajzol |
| `parabola` | `p`, `center`(csúcs), `axis`("x"/"y") | `(y-cy)²=2p(x-cx)` vagy `(x-cx)²=2p(y-cy)` |
| `circle` | `r`, `center` | |

Általános opcionális mezők: `color`, `label` (jelmagyarázat szövege), `dashed`, `hidden`, `legend:false`.
**Használd közvetlenül a `conics.py` által visszaadott objektum `board` mezőjét**, majd egészítsd ki `name/color/label` mezőkkel.

> **Paraméterezett görbékhez (alakparaméter-feladat, például excentricitás)**: az `a/b/c/r/p` és a `center` koordinátái is lehetnek **kifejezéskarakterláncok** (`@param` neve vagy `p` álnév, továbbá `sqrt/sin/cos/abs/pow/min/max/PI` és `+ - * / ^`). A motor minden képkockában az aktuális csúszkaértékkel számolja újra, majd újrarajzolja a görbét, fókuszokat és aszimptotákat. Példa: a hiperbola `{"a":1,"b":"sqrt(e*e-1)"}` az `e` értékével változtatja alakját.

### 3.2 points (statikus, névvel ellátott pontok)

Az érték lehet `[x,y]` vagy `{xy:[x,y], color, label, emphasis, hidden}`. Az `emphasis:true` nagyobb, fehér szegélyű kört rajzol (fix ponthoz); a `hidden:true` csak a konstrukcióban használja, nem jeleníti meg; elhagyott `label` esetén a pont neve jelenik meg.
A koordináták is lehetnek **kifejezéskarakterláncok** (a `@param` értékével változnak), például `"xy":["e","0"]`, `"xy":["2/e","sqrt((e*e-1)*(4/(e*e)-1))"]`. Ha egy kifejezés `NaN` értéket ad (például negatív gyök alatt), a pont **automatikusan elrejtőzik**, és a tőle függő szakaszok/vektorok/leolvasások is eltűnnek (így természetesen jelezhető a „nem létezik” állapot).

### 3.3 param (változó paraméter; elhagyása = statikus ábra)

`min/max/step/value`, `unit` (megjelenített utótag), `standard` (a feladatban rögzített érték, a „visszaállítás” gomb erre áll), `label` (tartalmazhat LaTeX-et), `ticks` (a csúszka alatti skálafeliratok tömbje). Az aktuális paraméterérték a motorban `@param`; a kifejezésekben a **paraméter nevén** kell hivatkozni rá (érvényes azonosító, például `e`/`t`/`k`) vagy a `p` álnévvel.

### 3.3b scalars (opcionális: paraméterből származtatott, névvel ellátott skalárok)

`[{name, expr}]`, tömbbeli sorrendben kiértékelve (a későbbi elem hivatkozhat korábbira); a számított skalárok bekerülnek a kifejezéskörnyezetbe, ezért a `conics` / `points` / `readouts` kifejezései hivatkozhatnak rájuk. Példa: `[{"name":"c","expr":"e"},{"name":"b","expr":"sqrt(e*e-1)"}]`.

### 3.4 derived (konstrukciós sorozat, sorrendben megoldva; hivatkozhat korábbi eredményre)

`type` áttekintése (a motor konstrukciós könyvtára, az `analytic_kernel` megfelelőivel):

| type | Mezők | Eredmény |
|---|---|---|
| `line_through_angle` | `name, point, angle`(szám vagy `"@param"`) | Egyenes (adott ponton át, megadott dőlésszöggel) |
| `line_through_slope` | `name, point, slope` | Egyenes (adott ponton át, megadott meredekséggel) |
| `line_x_eq_my_c` | `name, m, c` | `x=my+c` egyenes |
| `line_through_points` | `name, a, b`(pontnevek) | Két pontot összekötő egyenes |
| `line_through_point_dir` | `name, point, dir:[dx,dy]` | Egyenes adott ponton át, adott iránnyal |
| `point_on_conic` | `name, conic, t`(szög°/paraméter) | Paraméteres pont a görbén |
| `intersect_line_conic` | `name:[n1,n2], line, conic, colors` | Egyenes∩görbe (két pont t szerinti növekvő sorrendben; kevesebb esetén alapértelmezetten rejtett) |
| `intersect_line_line` | `name, a, b`(egyenesnevek) | Két egyenes metszéspontja |
| `midpoint` | `name, a, b` | Felezőpont |
| `point_reflect` | `name, of, center` | Középpontos tükörpont: `2·center − of` |
| `foot_perp` | `name, point, line` | Merőleges vetület talppontja |
| `reflect` | `name, point, line` | Tükrözés egyenesre |
| `tangent_at` | `name, conic, point` | A görbe érintője rajta levő pontban |
| `vector` | `name, from, to`(pontnevek) | Vektornyíl |
| `segment` | `name, a, b, dashed, color` | Szakasz |
| `polygon` | `name, pts:[...], color, stroke` | Sokszög (félig átlátszó kitöltés, háromszög-területhez) |

A konstrukciós objektumokhoz `color` (szemantikus név vagy hex), `label`, `dashed` is adható.

### 3.5 readouts (a konzol valós idejű numerikus értékei)

Minden elem alakja `{id, label, type, ..., color, highlight}`. A `highlight:true` cián jelvénnyel emeli ki (rendszerint a célmennyiséget). Az `id`-t a `rangeBar.of` / `constant.of` használja követésre.

| type | Mezők | Megjelenítés |
|---|---|---|
| `coord` | `of`(pontnév) | `(x, y)` |
| `length` | `a,b`(pontok) vagy `of`(vektornév) | Hossz |
| `distance` | `a,b`(pontok) | Két pont távolsága |
| `dot` | `a,b`(vektornevek) | Skalárszorzat |
| `slope` | `of`(egyenesnév) | Meredekség (függőlegesnél „nem létezik”) |
| `slope_product` | `a,b`(egyenesnevek) | Meredekségek szorzata |
| `area_triangle` | `pts:[p,q,r]` | Háromszög területe |
| `distance_point_line` | `point, line` | Pont távolsága egyenestől |
| `expr` | `expr`(kifejezés), `digits` | Kifejezés numerikus értéke (`@param`/scalars használható, például fél fókusztávolság `c`) |
| `status` | `expr, op, rhs, okText, badText` | Egyenlőtlenségi állapot: `expr op rhs` (op∈ `< <= > >= ==`) teljesülésekor zöld „teljesül”, különben piros „nem teljesül” |

### 3.6 rangeBar / constant / answerBand / trace
- `rangeBar` (tartomány-, szélsőérték-feladat): az `of` egy **skalár** readout `id`-ját követi; a `min/max` a kernel elméleti tartományának lebegőpontos értéke; a `label` intervallum-LaTeX (`$…$`-sel). A mutató az aktuális értékkel a min–max között mozog.
- `constant` (állandóérték-feladat): az `of` egy readoutot követ; a `label` állandóérték-LaTeX (`$…$`-sel); megjelenítése: „állandó érték ≡ …”.
- `answerBand` (**alakparaméter-feladat**, például excentricitás-tartomány): a **paramétertengelyen** rajzolja meg a `[min,max]` tartományt, kiemeli a válasz `[lo,hi]` részintervallumát, a mutató az aktuális paraméterérték, a `label` pedig válasz-LaTeX (`$…$`-sel). Azon feladatokhoz való, ahol a csúszka maga a keresett változó, például „határozd meg e értéktartományát”.
- `trace` (mértanihely-feladat): az `of` egy `derived` pont neve; a motor a paraméter teljes tartományán mintavételezi és megrajzolja a pont pályáját (összevetésként a kernel mértanihely-egyenlete `conics` görbeként is ráhelyezhető).

### 3.7 Szemantikus színnevek (COLORS)

`curve`(arany·főgörbe) · `curve2`(rózsaszín·másodgörbe) · `line`(cián·mozgó egyenes) · `line2`(égszínkék) · `aux`(szürke segédvonal) · `asymptote` · `directrix` · `ptA`(piros) · `ptB`(kék) · `point`(világosszürke) · `given`(lila) · `fixed`(smaragdzöld·fix pont) · `vecA`(piros) · `vecB`(kék) · `vec`(borostyán) · `locus` · `area`(félig átlátszó cián). Közvetlenül hex érték is használható.
