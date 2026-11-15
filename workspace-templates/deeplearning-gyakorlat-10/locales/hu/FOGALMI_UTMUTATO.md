# Fogalmi útmutató

## Az osztályozó rész

`conv5_block3_out`:(batch, 7, 7, 2048), `predictions` kernelsúlya:(2048, 1000). A képi jellemzőtérkép csatornáit egy kiválasztott osztály súlyoszlopa súlyozza. A bias nem térbeli térkép, külön hozzáadott konstans. GAP→Dense esetén `mean(nyers CAM)+bias = logit`. A softmax az összes logitból készít osztályértékeket, ezért más mennyiség.

A klasszikus CAM architektúrához kötött súlyozott összegzés. A Grad-CAM gradiensből képez csatornasúlyokat; itt nem azt számoljuk. Az általános magyarázhatósági térkép nem pixelmaszk vagy oksági bizonyíték. A közös színskála számokat tesz összehasonlíthatóvá; a külön normalizálás saját maximumot is kiemelhet kis osztálypontszám mellett.

A kitakarás előre rögzített:[64: 176, 64: 176], szürke 127.5. A cél az eredeti top-1 marad. Nem választjuk át a célt úgy, hogy a változás látszólag kedvezőbb legyen.

## A regressziós rész

A ResNet-bázis befagyasztott és training=False módú. A GAP-vektor 2048 érték; a lineáris fej 2048 súlyt+1 biast tanít. Kezdetben nulla kernel és tanítómedián bias miatt minden becslés a baseline. Nincs softmax vagy automatikus valószínűségi intervallum. MAE = abs(becslés−címke) átlaga, évben. A negatív előjeles hiba alábecslés, a pozitív felülbecslés.

A 0–19, 20–39, 40–59, 60+ csoportok előre rögzítettek. A csoportos táblázatban n és hiba együtt értelmezendő; kis elemszám nem népességi bizonyítás. Nem kapcsolunk automatikus vásárlási döntést a modellhez.

X01 a megtanult regressziós kernelsúlyokat alkalmazza a térbeli jellemzőkre. A térképátlag+bias az előrejelzés; az előjelek megmaradnak. Ez ugyanazt a lineáris gondolatot kapcsolja másik célkimenethez, nem valós arcrész-kort mutat.

## Új szintaxis

- `iter` bejáró, `next` következő elem: az elem itt egy egész batch-pár.
- `argsort` rendezési indexek; `[::-1]` fordítás; `[: 5]` első öt.
- `get_layer` név szerinti réteg; `get_weights` tömbök, rendszerint kernel és bias.
- `tensordot(..., axes=([-1],[0]))` az utolsó aktivációs és az első súlytengelyt párosítja/összegzi.
- `map` a Dataset elemein ugyanazt az átalakítást végzi; `batch` kötegeket képez.
- `GAP` térbeli átlag, a csatornákat megőrzi.
- `preprocess_input` modellfüggő transzformáció, itt nyers RGB 255→BGR−ImageNet-átlag; nem egyszerű /255.
- `shuffle` a fej tanítómintáinak sorrendjét változtatja. A képi kinyerés és teszt sorrendje rendezett marad.

## Értelmezési szabályok

A saját kimenet az irányadó, nincs kötelező osztály, pontszámesés vagy cél-MAE. Az elefánt/napraforgó fájlnév nem ellenőrzött ImageNet-címke. A képek és az eredmények automatikusan nem láthatók az agentnek. Megjelenítési hibánál elfogadható a kép szöveges leírása; nem találunk ki képi hibát.

A kész kódban nincs feladatként visszahagyott rész. A műszaki ellenőrzések nem külön hallgatói algoritmusírási feladatok. A FOLYTATAS.md technikai helyreállítás, nem új vizsga. Nincs beadás.
