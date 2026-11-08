# Fogalmi támpontok és a HTML-ek használata

## A két friss bemutató

`forrasok/Batch_Normalization_HU.html`: az eredeti feltöltött, továbbfejlesztett HTML változtatás nélküli másolata. B01-ben a „Hol vannak az x₁…x₆értékek?” és „Mini-Batch(Sorok) vs.Neuronok(Oszlopok)” panel a kiindulópont. A kiválasztott oszlop egy neuron súlyozott válaszait tartalmazza különböző mintákra. Ezután a négy lépés: nyers értékek, középre tolás, osztás sqrt(variancia+epsilon)-nal, gamma/beta.

`forrasok/Skip_Connection_ResNet_HU.html`: az eredeti skip HTML. R00-ban az identitás mód és az élő vektor a lényeg, nem a történelmi pontosságok visszamondása. A degradációs ábrán külön kell olvasni a tanító és teszthibát. Nagyobb tanítási hiba nem magyarázható pusztán azzal, hogy a modell jobban túltanult. Overfittingnek azonban nem feltétele a0-hoz közeli tanítási hiba.

Ha HTML-megnyitás/CDN miatt nem működik a rajz, a beszélgetést a következő szöveges példával tartsd meg; ne blokkold a teljes leckét. BN-mátrix: [[2,10],[4,18],[6,20],[8,40]], sor=minta, oszlop=neuron. Az első oszlop átlaga 5, a másodiké 22. Skipvektor: x=[2,4,−1,3],F=[0,0,0,0],H=x+F=x,y=ReLU(H)=[2,4,0,3]. A negatív bemenet az összegben megmarad, a ReLU után nem. A notebookban ettől eltérő valódi blokkpróba is szerepel.

## Amit a szemléltetésből pontosan viszünk tovább

| Kifejezés | A gyakorlatban |
|---|---|
| Mini-batch és BN | Dense-bemenetnél egy jellemző oszlopát a batch mintái mentén normalizáljuk; Conv2D-nél a csatorna statisztikája térbeli helyeket is összesít. Nem a képen belüli RGB-csatornák összemosása. |
| Gamma/beta | Jellemzőnként tanulható skála/eltolás. A gamma előjele akár negatív is lehet; a HTML csúszka tartománya nem általános korlát. |
| Running state | Moving mean és moving variance, nem mozgószórás. Inference rögzített állapotot használ. |
| BN-előny | Segíthet optimalizálni; nem szüntet meg garantáltan minden eltűnő gradienst, és nem garantál jobb pontosságot. Az internal covariate shift történeti motiváció, nem egyetlen lezárt magyarázat. |
| Aktiváció | A sigmoid 0 körül közel lineáris, nem pontosan lineáris. Helyi aktivációs meredekség nem egy teljes háló tanulásának mérése. |
| H=x+F | Az identitás az összegre vonatkozik F=0 mellett. Utólagos ReLU esetén y=ReLU(H), ezért negatívaknál nem teljes identitás. |
| Gradiensút | A dH/dx tartalmaz identitásjárulékot; többdimenzióban identitásmátrixot. A többi ág, kioltás, projekció vagy aktiváció módosíthatja a teljes gradienst. R03-ban ezt automatikusan mérjük. |
| Veszteségfelszín | A HTML előírt pályát rajzol. Sem BN, sem skip nem garantál minden hálónak konvex veszteséget vagy globális minimumot. A notebook nem reprodukálja a történelmi 20/56 réteges kísérletet. |
| GAP/1×1Conv | GAP térbeli átlag csatornánként,1×1Conv tanulható csatornakeverés. Input-alak más korlátokat is adhat. |
| L2 | Veszteséghez adott büntetés; nem minden optimalizálónál azonos a leválasztott weight decay-jel. |

## Kódolvasási kislexikon

axis=0: oszloponként, sorokon át összesít a2D példán. axis=1: soron belüli oszlopok között keres/összesít. Broadcasting: rövidebb jellemzővektort minden mintasorra alkalmazunk. get_layer: név alapján kiválasztás; get_weights/set_weights: tömbök kiolvasása/visszatöltése. Functional API: a réteghívás a következő rétegnek átadható tenzort ad, így ágazás építhető. Add: azonos alakú tenzorok elemenkénti összege. GradientTape: műveletkövetés automatikus deriválással; nincs kézi deriválási feladat. iter/next: bejáró/egy következő elem; a Dataset eleme itt egy teljes batch-pár. argmax(axis=1): valószínűségi soronként a legnagyobb oszlop indexe.

## A kontrollált CIFAR-kísérlet

Közös8000/2000/2000 képes felosztás, rögzített sorrend, batch 64,6 epocha, külön Adam(1e-3). Conv16–opcionálisBN–ReLU–MaxPool–Conv32–opcionálisBN–ReLU–GAP–Dense10. Belső Rescaling1/255 egyszer. Nincs Dropout/L2/skip/augmentáció a két modellben. Közös induló Conv/Dense-súlyok, külön ellenőrizve. Best val_loss visszatöltés, validációs választás, csak utána teszt. Nem kötelező BN-javulás. A kevés epocha és a fix batch-sorrend oktatási kontroll, nem általános legjobb tanítási recept. Javasolt két 90 perces alkalom; tényleges órai ütemtől függően hosszabb lehet.

Környezet- és állapotproblémánál a FOLYTATAS.md használható. Az alapgyakorlat után nincs automatikus folytatás vagy beadás.
