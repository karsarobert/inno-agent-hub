# Fogalmi útmutató — tutor

| Fogalom | A notebookban így jelenik meg |
| --- | --- |
| Előre tanult szóvektor | W03 a 100 dimenziós GloVe-reprezentációt betölti. W05 egy szóból a hozzá tárolt vektort keresi ki. A notebook neve Word2Vec, de új szóvektorokat nem tanít. |
| Koszinusz-hasonlóság | A skalárszorzatot elosztjuk a hosszúságok szorzatával. Két azonos irányú, eltérő hosszúságú nem nulla vektor hasonlósága 1. W08-ban a legnagyobb értéket keressük. |
| Analógia és kilógó elem | A pozitív és negatív szóvektorok irányt adnak a szomszédkereséshez. A `doesnt_match` a csoporthoz a betöltött vektortérben legkevésbé illeszkedő szót keresi. A korpuszban tanult kapcsolat nem bizonyít kulturális vagy életrajzi állítást. |
| Karakterszótár | `char2idx` karakterből egész indexet, `idx2char` indexből karaktert ad. A szóköz, sortörés és központozás ugyanúgy része a szótárnak, mint a betűk. A két notebook beágyazásai egymástól függetlenek. |
| Következő karakter | Egy `abcd` darabból a modell `abc` bemenetet és `bcd` célt kap. A 101 hosszú darabból ezért képezhető két 100 hosszú sorozat. A keverés a párok sorrendjét érinti. |
| Batch, időlépés, karakterosztály | T21-ben egy `(64, 100)` bemenetből `(64, 100, vocab_size)` kimenet készül. A GRU minden időlépéshez ad állapotot, a Dense pedig minden karakterosztályhoz logitot. |
| Logit és veszteség | A logit nyers pontszám. A keresztentrópia az egész célindexet a logitokkal veti össze, `from_logits=True` beállítással. A tanítási veszteség alakulása önmagában nem igazolja az általánosítást. |
| Stateful GRU | A GRU a batch pozícióihoz tartozó belső állapotokat viszi tovább; a keverés miatt ez a notebook nem követi folyamatosan a könyv sorrendjét a batchek között. A tanító modell batchmérete 64, a generáló példányé 1. |
| Checkpoint | A callback epochánként ment. A legutóbbi mentés útvonalát a T33 keresi; `None` azt jelenti, hogy nem talált mentést. Az új, 1-es batchméretű modellbe a tanult súlyokat töltjük be. |
| Autoregresszív mintavétel | A generálás kezdetén a notebook nullázza az állapotot. A legutolsó időlépésből kiválasztott karakter indexe lesz a következő bemenet. A generálás megváltoztathatja a belső állapotot, a súlyokon nem tanít tovább. |
