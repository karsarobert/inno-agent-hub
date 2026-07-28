# Egyezmények és megoldási receptek (conventions)

## 1. Koordinátarendszer és a görbék standard alakja

Az analitikus geometriában közvetlenül a **matematikai síkkoordinátákat** használjuk (x jobbra, y felfelé); nincs szükség a térgeometriában előforduló z↔y tengelycserére. A frontend motor a `(x,y)` matematikai koordinátát képernyőre képezi: `sx = offX + x·scale`, `sy = offY − y·scale` (y megfordítva). A `scale` a `view` ablakhoz adaptív, a numerikus értékeket nem befolyásolja.

A `conics.py` standard koordinátázása (a középpont/csúcspont alapértelmezésben az origó):
- `ellipse(a, b)` — `x²/a² + y²/b² = 1`; a=x féltengely, b=y féltengely; a fókuszok a nagytengelyen vannak, `c=√|a²−b²|`.
- `hyperbola(a, b, orient)` — `orient='x'`: `x²/a²−y²/b²=1`; `'y'`: `y²/a²−x²/b²=1`. a=valós féltengely, b=képzetes féltengely, `c=√(a²+b²)`, az aszimptoták meredeksége `±b/a` (x irányban).
- `parabola(p, axis)` — `axis='x'`: `y²=2px`, fókusz `(p/2,0)`, vezéregyenes `x=−p/2`; `'y'`: `x²=2py`.
- `circle(center, r)` — `(x−h)²+(y−k)²=r²`.

## 2. Alapminta: paraméteres egyenes + közös megoldás + Viète

**Elsődlegesen `x = m·y + c` formát használj** (ne `y = kx + b`-t): ez természetesen tartalmazza a függőleges egyenest (`m=0`), és elkerüli a „meredekség nem létezik” kérdését; a vízszintes egyenes `m→∞`-nek felel meg (a frontend csúszka θ=0° állásában). A `(x₀,y₀)` rögzített ponton átmenő egyenesnél `c = x₀ − m·y₀`.

A `chord_setup(conic, through)` az `x=my+c` értéket helyettesíti a görbébe, y szerinti másodfokú egyenletet ad, és visszaadja a pontos `A,B,C` együtthatókat, `ysum=−B/A`, `yprod=C/A`, valamint a `disc` diszkriminánst. A Viète-mennyiségekkel a célmennyiség m szerinti kifejezéssé írható:
- `x₁+x₂ = m·ysum + 2c`, `x₁x₂ = m²·yprod + m·c·ysum + c²`.

## 3. Megoldási recepttábla (query.type → kernel → interaktív minta)

| query.type | Kernel-függvény / képlet | Interaktív minta |
|---|---|---|
| `standard_equation` standard egyenlet keresése | Oldd meg a,b,c értékét (vagy h,k,r értékét) excentricitásból/ponton átmenésből/fókuszból | Statikus felirat |
| `chord_length` húrhossz (tartomány) | `chord_len_sq_expr`, `|AB|²=(1+m²)[ysum²−4·yprod]` | Forgó egyenes + tartománysáv |
| `dot_product` skalárszorzat (tartomány/állandó érték) | `dot_product_expr` + `range_over_m`/`is_constant_in_m` | Forgó egyenes + tartománysáv/állandó érték |
| `triangle_area` terület (szélsőérték) | `triangle_area_expr=½·|AB|·d`, szélsőérték változócserével | Forgó egyenes + tartománysáv |
| `slope_product` meredekségek szorzata (állandó érték) | `slope_product_central` (középpontos szimmetria) stb. | Forgó pont + állandó érték |
| `fixed_value` állandó érték | Írd a célt m szerinti kifejezéssé → `is_constant_in_m` | Paraméter forgatása + állandó érték |
| `fixed_point` fix pont | Paraméteres egyenes: a „paraméteres tag együtthatója=0” feltételből oldd meg a fix pontot | Paraméter forgatása + mozgó egyenes a fix ponton át (`emphasis`) |
| `locus` mértani hely | Legyen a mozgópont `(x,y)`, ejtsd ki a paramétert egyenletté | Csúszka vezérelte pont + `trace` pálya + ráhelyezett egyenlet |
| `tangent` érintő | Diszkrimináns=0 / pont-érintő alak (`tangent_at`) | Statikus / forgó érintési pont |
| `eccentricity` excentricitás (érték/tartomány) | `e=c/a` + feltételegyenlőtlenség (például `ecc_range_focal_ratio`) | **csúszka=e**·alakváltozó görbe + `status` + `answerBand` |

Segédfüggvények: `tex(expr)` (LaTeX-kimenet), `fnum(expr)` (float), `is_clean(expr)` (rendezettség vizsgálata véletlen feladatnál), `interval_latex(lo,hi,lo_closed,hi_closed)`.

### Alakparaméter-feladatok (a csúszka közvetlenül a görbét vezérli, például excentricitás-tartomány)

Bizonyos feladatok természetes dinamikus mennyisége nem „mozgó egyenes/pont”, hanem magának a görbének az **alakparamétere** (leggyakrabban az e excentricitás). Ilyenkor legyen **a csúszka = ez a paraméter**, és a görbe `a/b/c` értékeit, a fókuszokat, illetve a mozgópont koordinátáit ennek a paraméternek a **kifejezéskarakterláncaiként** add meg (schema 3.1/3.2/3.3b); a motor minden képkockában újraszámolja és újrarajzolja a görbét, a fókuszokat és az aszimptotákat. Kapcsolódó minta:
- Rögzíts egy skálát (például `a=1`; ekkor `c=e`, `b="sqrt(e*e-1)"`), a többi mennyiséget pedig kifejezésekkel add meg.
- `status` readouttal jelezd a létezést/egyenlőtlenség teljesülését (például a P pont létezik a jobb ágon ⇔ `e≤2`); a `NaN` értékű kifejezésű pont **automatikusan elrejtőzik**, így szemléletesen megjelenik a „nem létezik” állapot.
- Az `answerBand` a paramétertengelyen kiemeli a válaszintervallumot (a végpontokat a kernel adja, például `ecc_range_focal_ratio(3)` → `e∈(1,2]`).
A példát a `generate.py` `build_hyperbola_ecc_range` függvényében találod.

## 4. Nyílt/zárt végpontok eldöntése (a helyesség kulcsa)

A `range_over_m(expr, horizontal_valid=True)` az m∈ℝ tartományon meghatározza az értékkészletet és a végpontok nyíltságát/zártságát:
- Gyűjtsd össze a stacionárius pontok értékeit, az `m=0` (függőleges, mindig érvényes) értéket és az `m→±∞` (vízszintes egyenes) határértékeket.
- Egy végpont akkor „zárt”, ha valamely **valódi, érvényes egyenes** felveszi.
- `horizontal_valid=True`: a vízszintes egyenes is érvényes húr (például belső ponton átmenő ellipszishúr), ezért a határértéke **beleszámít (zárt)**. Példa: ellipszis `MA·MB`, x-tengelyen −3, függőleges egyenesen 7/4 → **`[-3, 7/4]`** (ne írd nyíltként: `(-3, 7/4]`).
- `horizontal_valid=False`: a vízszintes/degenerált egyenes nem érvényes, vagy a rajz degenerálódását okozza (például a `△OAB` háromszög területe 0, mert a pontok kollineárisak; parabola fókuszhúrjának tengelyirányában csak egy metszéspont van), ezért a határérték **nem számít bele (nyílt)**. Példa: `△OAB` területe `(0, 3/2]`.

**Ez garantálja a válasz és az interaktív eszköz egyezését is**: ha a csúszka a végpontnak megfelelő θ értékig húzható, a leolvasásnak pontosan a válasz végpontértékét kell mutatnia.

## 5. Helyességi önellenőrzés (kötelező)
- A kernel válasza == válaszkártya `lesson.answer` == utolsó lépésben megjelenő érték == **frontend JS szabványos helyzetben/szakasz-söpréskor újraszámolt értéke**; a négynek egyeznie kell. A `scripts/generate.py` minden `build_*` függvénye beépített `assert`-ot tartalmaz; új feladattípushoz ennek mintájára adj assertot.
- A `rangeBar` végpontjai a `range_over_m` eredményéből, a `constant` értéke az `is_constant_in_m`/megfelelő kernelfüggvény eredményéből származzon.
- Véletlen feladat: hasonlítsd össze a kernel által generáláskor adott standard válasszal.
- Generálás után indíts helyi statikus szolgáltatást és előnézetben ellenőrizd: nincs konzolhiba, a KaTeX helyesen renderel, a csúszka valós időben jól számol, a tartománysáv/állandóérték/fixpont/mértani hely viselkedése megfelelő, a rajzeszköz és az összecsukható panel használható. **Az előnézet végeztével kötelező bezárni a portot.**

## 6. Tapasztalati értékek a nézethez (view)

A görbe fő része körül hagyj körülbelül 10–15% margót: ellipszishez `xRange≈[-1.8a,1.8a]`; parabola nyitási irányában több hely kell (például `y²=4x` esetén `xRange:[-2,7]`); hiperbola aszimptotákkal ne kapjon túl nagy ablakot, mert a görbe túl laposnak látszik. A `param` tartománya kerülje a degenerált értékeket (parabola fókuszhúrjánál a tengelyirányt θ≈0/180; középpontos szimmetrián alapuló meredekségszorzatnál azt a paramétert, amelynél a mozgópont és a rögzített pont egybeesik).
