# Ellenőrzés és tényleges referenciaeredmények

Ellenőrzés dátuma: **2026. szeptember 27.** A futási referencia alapja: **DL04 innoagent HU 1.0**; a jelen csomag **1.1**.

## Környezet

- Python: 3.12.14; Linux x86_64.
- NumPy: 2.3.5; Matplotlib: 3.10.8.
- TensorFlow CPU: 2.20.0; Keras: 3.15.1.
- GPU használata kikapcsolva; a környezetellenőrzés látható GPU-listája üres.
- A tanítóprogramok egy műveleti, egy köztes és egy adatbetöltési szálra vannak korlátozva.

## Mit ellenőriztünk?

- A környezetellenőrző program tényleges CPU-s frissítését és az ábramentést.
- **26 különböző kísérleti beállítás** sikeres folyamatindítását és kimenetét:
  21 kötelező alap/módosított eset, 5 opcionális softmax/BN eset.
- A fájlok futását a csomag mappájától eltérő munkakönyvtárból is;
  az eredmények a segédmodulhoz képest a csomag nezet mappájába kerülnek.
- A gradienspélda eredményeit független, zárt alakú összefüggéssel;
  momentum=0 mellett a két pálya egyezését.
- A sigmoid/Leaky ReLU kulcsértékeit, dropout tanítási skálázását
  és kiértékelési azonosságát, softmax eltolásinvarianciáját és összegét.
- Az azonos architektúrájú hálózati kísérletek kezdeti súlyazonosítójának egyezését;
  a büntetés nélküli G04_05 és a megfelelő G04_04 eredményének egyezését.
- Az L2-büntetés = λ × kernel-négyzetösszeg és a loss = MAE + büntetés azonosságát.
- A BN átlagát, varianciáját, skálázását és a tárolt statisztikák használatát.
- A Python-források és a tesztkérdések kódrészleteinek szintaxisát, a képfájlok
  olvashatóságát; a regressziós és L2-ábrák megjelenését szemrevételezéssel is.
- A rögzített tízkérdéses teszt szerkezetét és a tanári kulcs szakmai helyességét.

A fenti felsorolás a programok korábbi futási ellenőrzése.
A beküldött részleges Innoagent-próbabeszélgetés a G04_01–03 kísérleteit
és a G04_04 alapfutását tartalmazza. A próba megmutatta, hogy a kulcskód
magyarázata túl későn, az első futás után jelent meg. A későbbi feladatok
alkalmazásbeli végigtesztelését ez a részlet nem igazolja.

Az 1.1 változatban a tutori útmutatót és a bemutatókat módosítottuk:
minden új program előtt konkrét kóddal kísért magyarázat következik.
A Python-fájlokat és a zárótesztet bájtonként összehasonlítottuk az 1.0
csomaggal; változatlanok. Új tanítási futásokra ezért nem volt szükség.
Az új bemutatók kódrészleteit a csomag forrásaival egyeztettük, és ellenőriztük
a futás előtti sorrend következetességét. A módosított agent élő viselkedését
ebben a frissítésben nem teszteltük az Innoagent alkalmazásban. Az agent utasításai tartalmazzák a bemutatkozást, a várakozást,
a kódmagyarázatot, a memóriahasználat kereteit és a lezárást; a tényleges
alkalmazásbeli viselkedést az oktató rövid próbával ellenőrizze.

## Futási idő ezen a tesztgépen

| Programcsoport | Teljes Python-folyamat ideje |
|---|---:|
| NumPy-s példák és opcionális szemléltetések | 0,42–0,61 s |
| Neurális hálózatok, 120 vagy 400 epocha | 4,83–7,13 s |

A teljes idő az importot, a tanítást / számítást és az ábramentést is tartalmazza.
A program saját „Tanítás és mérés” sora ennél szűkebb időt mér, import és ábramentés nélkül.
Az értékek mérések, nem általános laptopos garanciák. A helyi oktatói próba szükséges.

## Egy súly tanulása

| Futás | Ráta | Lépések | Utolsó súly | Utolsó veszteség |
|---|---:|---:|---:|---:|
| R1 | 0,1 | 8 | 2,328911 | 0,450360 |
| R2 | 0,8 | 8 | 2,932815 | 0,004514 |
| R3 | 1,1 | 8 | -14,199268 | 295,814814 |
| R4 | 0,1 | 25 | 2,984888 | 0,000228 |

## A kis hálózatok tényleges eredményei

Az összes sor ugyanazt a 64/128 felosztást használja. A számok az utolsó
epocha modelljének mérései; nem korábbi legjobb értékek és nem teszteredmények.

| Futás | Neuron | Epocha | λ | Tanítási MAE | Validációs MAE | L2-büntetés | Kernel-négyzetösszeg |
|---|---:|---:|---:|---:|---:|---:|---:|
| H1 | 8 | 120 | 0,000 | 0,218931 | 0,250036 | 0,000000 | 12,290650 |
| H2 | 64 | 120 | 0,000 | 0,218428 | 0,256901 | 0,000000 | 12,343403 |
| H3 | 64 | 400 | 0,000 | 0,206139 | 0,259742 | 0,000000 | 12,348137 |
| REG0 | 64 | 120 | 0,000 | 0,218428 | 0,256901 | 0,000000 | 12,343403 |
| REG1 | 64 | 120 | 0,001 | 0,219644 | 0,251515 | 0,011500 | 11,499766 |
| REG2 | 64 | 120 | 0,050 | 0,365231 | 0,380753 | 0,279174 | 5,583480 |

A tesztfutásban a hosszabb tanítás kisebb tanítási, kissé nagyobb validációs
MAE-vel járt. Az enyhe L2 javított a 64 neuronos alapmodell validációs MAE-jén,
az erős L2 mindkét becslési hibát növelte. Ezek egy adott mag és felosztás
szemléltető eredményei. A kis különbségek nem statisztikai bizonyítékok.
A tutor a hallgató saját kimenetét értelmezze, ne ezeket a számokat követelje.

## Dropout-minták

| Futás | p | Mag | Mód | Kimenet |
|---|---:|---:|---|---|
| D1 | 0,50 | 42 | tanítási | `[0.4, 0.0, 2.6, 1.6, 0.0, 0.8, 1.4, 2.0]` |
| D2 | 0,25 | 42 | tanítási | `[0.2667, 0.6667, 1.7333, 1.0667, 0.0, 0.5333, 0.9333, 1.3333]` |
| D3 | 0,25 | 43 | tanítási | `[0.2667, 0.0, 0.0, 1.0667, 1.4667, 0.0, 0.9333, 1.3333]` |
| D4 | 0,25 | 43 | kiértékelési | `[0.2, 0.5, 1.3, 0.8, 1.1, 0.4, 0.7, 1.0]` |

## Referenciafájlok

A `mintakimenetek` mappa néhány, tényleges tesztfutásból másolt ábrát tartalmaz.
Ezek tanári minták, nem a hallgató frissen előállított eredményei. A
`ellenorzott_futasok.json` az ellenőrzött konfigurációkat és összegzéseiket rögzíti.
Nem tartalmaz modellfájlokat, a futtató környezet telepített csomagjait vagy személyes adatot.
