# Fogalmi támpontok és folytatás · 1.1

## A feladat célja

A kódot megkapjuk; futtatás és értelmezés útján ismerjük meg a transzfer tanulást. A bemutatók ételes és kutya–macska feladatok voltak, itt öt virágkategória és MobileNetV2 szerepel. Az agent mindig csak az aktuális cellához szükséges részt magyarázza.

| Új művelet | Jelentés és helye |
|---|---|
| def, függvényhívás | E02-ben a felosztas_elokeszitese már meg van írva. D02 négy bemenettel meghívja, és két eredményt kap: mappagyökér és képenkénti jegyzék. |
| Dataset | D03 három bejárható adatfolyamot hoz létre: tanító, validációs, teszt. A tényleges képek batch-enként érkeznek. |
| iter és next | D04 bejárót készít az adatfolyamhoz és elkéri egy elemét. Egy elem itt egy teljes képek–címkék batch-pár. |
| shape és dtype | A képbatch alakja (16,224,224,3), típusa float32. A címkék alakja (16,), egész int32. |
| preprocess_input | F01 a MobileNetV2 saját, 0–255-ről −1..1 közé skálázó műveletét mutatja. Nem azonos modellbetöltéssel. |
| GAP | A térbeli jellemzőtérképekből csatornánkénti átlagot, képenként 1280 jellemzőt készít. |
| Dropout | Tanításkor véletlen aktivációelhagyás, előrejelzéskor kikapcsol. |
| trainable | Mely súlyok frissülhetnek? |
| training=False | Hogyan fusson a bázis? BN-nél a tárolt statisztikák érvényesek. A kijelölt konvolúciós súlyok gradiense ettől még számolható. |
| startswith és == | T02A előtag vagy pontos név alapján mutat rétegkiválasztást; itt még nincs taníthatóság-módosítás. |
| isinstance | Megvizsgálja, BN-réteg-e az adott objektum. T02-ben az ilyen réteg nem lesz tanítható. |
| Compile | Beállítás, nem tanítás. Taníthatóság módosítása után ismét szükséges, új optimalizálóval. |
| Argmax, axis=1 | V00 kis példán, V01 valódi tömbön: soronként az osztályértékek legnagyobb elemének indexe. |
| append és concatenate | Az adagok címkéit előbb listába gyűjtjük, majd sorrendben egy tömbbé fűzzük. |
| Accuracy és loss | Az előbbi helyes osztályarány, az utóbbi a valódi osztályhoz rendelt valószínűségre is érzékeny. |

## Adatfelosztás, kimenet és teszt

Öt kategória, 100/40/40 kép osztályonként, összesen 500/200/200. A címke 0–4 egész szám, ezért sparse categorical veszteség kell; nincs one-hot. A végső fej öt softmax értéket ad. A softmax sorösszege közel 1, de ez nem bizonyít helyes előrejelzést.

A tanító frissíti a súlyokat. A validáció befolyásolja a megállást és a modellválasztást. A teszt csak a rögzített döntés után következik. A nem kevert tesztsorrend szükséges a becsült és valódi címkék összepárosításához. A mátrix sorai valódi, oszlopai becsült osztályok; a főátló helyes döntés.

## Állítások és bizonyítékok

A két ellenőrző True a BN-állapotról és a Conv_1-ről szól, nem automatikusan minden réteg súlyairól. A kiválasztási szabályt a T02 kódja és réteglistája is ellenőrzi. A legjobb val_loss checkpoint visszatöltése után kapott accuracy eltérhet az utolsó epocha accuracy értékétől. Több tanítás várható haszna a csökkenő görbéből nem garantálható. Egy képi megfigyelésből nem következik bizonyított hibaok.

## Újracsatlakozás és folytatás

Colabban GPU: [] esetén E01-nél álljunk meg és váltsunk GPU-ra a leckeutasítás szerint. Az új futtatókörnyezetben korábbi változók elveszhetnek. Helyi Jupyterben az eszközkörnyezetet az oktatóval tisztázzuk.

Kernelújraindításnál a fogalmi teljesítést nem kell megismételni, de az importoknak, segédeknek és adatfolyamoknak újra létezniük kell. E01–E02, D02–D05, F01–F04 a technikai alap. A checkpoint csak súlyokat ad, a modell szerkezetét előbb létre kell hozni. F05 végén stage_head.json, T04 végén stage_fine.json tárolja a történetet és időket; T05 selection.json fájlja őrzi a döntést.

Ha a checkpointok megmaradtak, ne indíts új tanítást szükségtelenül: a teljes megadott F05/T04 kódból csak a szükséges definíciók/útvonalak helyreállítását vezesse az agent, majd visszatöltés következzen. A technikai folytatási részhez is teljes futtatható kódot kell adnia. A T01/T05 validációs összevetés rekonstruálható, de teszt alapján nem választunk újra. Ha a naplók elvesztek, ne találjunk ki időadatot.

## Lezárás

Az agent a saját futási eredményt és a rövid értelmezést beszéli meg. A notebook mentése saját célra választható. Nem kell beküldeni, feltölteni vagy megosztani, és mentési bizonyítékot sem kérünk. Nincs új automatikus feladat.
