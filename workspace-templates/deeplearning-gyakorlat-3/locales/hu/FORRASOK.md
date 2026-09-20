# Források és feldolgozási döntések

## A felhasználó által megadott tananyagok

- Dl_02(1).zip: a magyar Inno-tutor szerepe, új programok kötelező bemutatása,
  2 × 45 perces szerkezet, hallgatói szerkesztés és önálló futtatás,
  magyarázat → cselekvés → értelmezés sorrend, külön kísérleti eredmények.
- DL_03(1).html: veszteség, gradiens, tanulási ráta, batch/epoch,
  optimalizálás, spirálosztályozás, softmax, kimenetértelmezés, notebookpontosítások.
- PTE_DL3_1_ipynb_másolata(2).ipynb: lineáris regresszió, MSE/2 veszteség,
  súly- és biasgradiens, saját gradiensmódszer.
- PTE_DL3_spiral(2).ipynb: 600 spirálpont, három osztály, one-hot cél,
  Dense 50 → Dense 50 → Dense 3, ReLU/softmax, Adam, tanítás és kiértékelés.

A forrásfájlokat nem módosítottuk. A csomag az elméleti anyag gyakorlati
párja, nem az összes elméleti levezetés újabb számonkérése. Nincs külön
kézi backpropagation- vagy numerikusgradiens-feladatsor.

## A helyi feldolgozás fontos eltérései

1. Notebookok helyett önálló .py programok futnak az Innoagent Run gombjával.
2. A regressziós notebook hálózatról olvasott adatai helyett saját, dokumentált
   szintetikus adatokat generálunk: 100 időérték 0–10 között, pontszám
   20 + 6×idő + 4 szórású normális zaj, seed=42. Ez nem az eredeti adatfájl,
   és nem valódi hallgatói vizsgálat. MSE/2 és a hozzá tartozó gradiens megmarad.
   A ráta és epoch ehhez a más léptékű példához igazodik.
3. A spirál adatkonstrukcióját megtartjuk, de rögzített véletlen generátort
   és osztályarányt megőrző tanító/validációs/teszt felosztást használunk.
   Méretek: 360/120/120, vagyis 60/20/20 százalék.
4. A notebook X_test néven validációra is használt halmaza helyett valóban
   elkülönített tesztet tartunk fenn. A teszten csak a döntés után mérünk.
5. A színezéshez az osztályindexet adjuk át, nem a teljes softmax-vektort.
6. A notebook model/model2 névkeveredését nem visszük tovább. Minden program
   saját modelljét konfigurálja, tanítja és értékeli. Nem hasonlítunk tanított
   és véletlenül tanítatlan hálózatot aktivációsfüggvény-hatásként.
7. A kötelező modellek softmax-kimenetet használnak; a hibás ReLU-kimenetű
   összehasonlítás kimarad. Logitos kimenet külön opcionális témaként sem terheli az órát.
8. A notebook két 50-es rejtett rétegét lépcsőzetesen építjük fel:
   rejtett réteg nélküli alap → 16 rejtett neuron → 50 és 50 neuron.
   Keras alapértelmezett Dense-inicializálásával dolgozunk; nem állítjuk, hogy
   a notebook glorot_normal inicializálásának bitazonos futását reprodukáljuk.
9. Az ábrák kész segédkódból születnek. Az új fájlokhoz a Nézet mappa frissítésére
   a programok és a tutor is emlékeztet. A végső teszt nem rajzol tanulási görbét.
10. A tíz új kódértési kérdés a hallgató által feldolgozott műveletekre épül.

## Hivatalos technikai háttér

- [Keras: modellkonfigurálás, tanítás, mérés és becslés](https://keras.io/api/models/model_training_apis/).
  A compile konfigurál, a fit tanít, evaluate mér, predict becsül; a validation_data
  ellenőrzésre szolgál, közvetlen súlyfrissítés nélkül.
- [Keras: valószínűségi veszteségek](https://keras.io/api/losses/probabilistic_losses/).
  A categorical_crossentropy one-hot célokra használható; a sparse változat
  egész címkéket vár. A from_logits beállítás a kimenet értelmezését határozza meg.

A technikai API-hivatkozásokat a csomag elkészítésekor ellenőriztük.


## Az 1.1 változat módszertani forrása

A felhasználó 2026. szeptember 20-i tesztbeszélgetése: „markdown(9).md beillesztve”.
A javítások az abban megfigyelt kihagyott kódmagyarázatokra, előre megadott
összehasonlítási válaszokra, hiányzó ráta-kísérletre és a végső ábraértelmezés
elhagyására reagálnak. A tíz kérdés és a válaszkulcs tartalma megmaradt,
az előzetes tanítás és az önálló döntési feladat erősödött.
