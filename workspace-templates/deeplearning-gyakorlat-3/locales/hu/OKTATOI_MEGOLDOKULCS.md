# Záróteszt – oktatói megoldókulcs

A tutor ezt használja a válasz UTÁNI visszajelzéshez; előre ne mutassa meg.
Egyetlen helyes válasz kérdésenként. Első válasz: 1 vagy 0 pont. Segítség
esetén a pont mellett külön jelezze, hogy nem önálló válasz volt.

| Kérdés | Válasz | Vizsgált fogalom |
|---|---|---|
| 1 | B | Egy minta bemeneti jellemzői |
| 2 | C | Rejtett rétegek és kimeneti réteg |
| 3 | A | One-hot cél, softmax, keresztentrópia |
| 4 | D | A fit tanít |
| 5 | B | Epochon belüli batch-ek |
| 6 | D | Gradienssel ellentétes frissítés |
| 7 | A | Mintánkénti argmax, 0-tól induló index |
| 8 | C | Validációs mérés |
| 9 | B | Keresztentrópia és pontosság eltérése |
| 10 | C | Mentett modell független értékelése |

## 1. B

A 2 a mintánkénti jellemzőszám. A két koordináta egy pont leírása.
A: a mintaszám másik dimenzió; C: három kimeneti osztályunk van;
D: a rejtett rétegek számát a rétegsorok adják, itt egy van.
Segítség: különítsd el a pontok számát és egy pont adatait.

## 2. C

Két Dense(50, relu) a két rejtett réteg, Dense(3, softmax) a kimenet.
A: két egymás utáni 50-es réteg nem azonos egy 100-assal;
B: a kimeneti réteget nem számítjuk rejtettnek;
D: a neuronszámokat felcseréli.
Segítség: az utolsó Dense a kimenet; olvasd el az előtte álló sorokat.

## 3. A

Három one-hot célértékhez három softmax-érték és categorical_crossentropy illik.
B: a sparse változat egész osztályindexet vár, nem ilyen one-hot vektort.
C: egy sigmoid-kimenet nem ezt a háromosztályos one-hot feladatot írja le.
D: a két kimenet nem illeszkedik a háromelemű one-hot célvektorhoz.
Segítség: nézd meg a cél alakját, és a kimeneti neuronok számát.

## 4. D

A fit számol gradienseket és frissíti a tanulható paramétereket.
A: compile konfigurál; B: evaluate metrikákat mér; C: predict becslést ad.
Segítség: melyik hívásnak adtuk meg a tanítópárokat és az epochok számát?

## 5. B

11 × 32 = 352, és 360 − 352 = 8. A rövid utolsó batch is lefut, így 12 batch van.
A: a feladat szerint nem dobjuk el a maradékot;
C: a batch_size a batch mintaszáma, nem a batch-ek száma;
D: ez batch_size=1 esetén lenne igaz.
Segítség: oszd el a mintaszámot 32-vel, és a maradékot is vedd figyelembe.

## 6. D

1 − 0.1 × (−4) = 1 + 0.4 = 1.4. A negatív gradiens kivonása növeli a súlyt.
A: a gradiens előjelét figyelmen kívül hagyja;
B: csak a ráta és a gradiens szorzata, nem az új súly;
C: csak a rátát adja hozzá, figyelmen kívül hagyva a gradienst.
Segítség: először a szorzat előjelét döntsd el.

## 7. A

Az első sor maximuma az 1-es, a másodiké a 0-s indexen van: [1,0].
B: maximumértékeket ad, nem indexeket;
C: 1-től kezdődő számozást használ;
D: oszloponkénti argmax eredménye lenne, axis=0-val.
Segítség: axis=1 esetén külön-külön járd végig a sorokat.

## 8. C

A validációs párokból ellenőrző mérés készül; nincs közvetlen súlyfrissítés.
A: összekeveri a tanító- és validációs szerepet;
B: a tanítóadatokat nem váltja le;
D: ehhez külön korai leállítási callback kellene, ilyen itt nincs.
Segítség: mérni és tanítani két külön művelet.

## 9. B

Mindkét vektor maximuma az 1-es osztályhoz tartozik, és ez a helyes címke.
A veszteség az adott one-hot célhoz −ln(p_helyes), tehát −ln(0.6) ≈ 0.511-ről
−ln(0.8) ≈ 0.223-ra csökken. Az egymintás pontosság mindkét esetben 1.
A: a nagyobb helyes-osztály valószínűség kisebb veszteséget ad;
C: a kezdeti döntés is helyes, és a veszteség változik;
D: a helyes index mindkét esetben a legnagyobb értéké.
Segítség: külön nézd meg a legnagyobb érték helyét és a helyes osztály valószínűségét.

## 10. C

A load_model a korábbi rétegeket és súlyokat tölti be, evaluate a kijelölt
adatokon mér. Nincs fit, tehát nincs új tanítás.
A: nem új súlyokkal indul, és nem tanít;
B: nincs modellkeresés vagy választás ezekben a sorokban;
D: a tanítás folytatásához fit kellene.
Segítség: keresd meg, van-e tanítóhívás a részletben.

## Visszajelzés

A válasz előtti rávezetést különítsd el a válasz utáni rendes magyarázattól.
A lezárásban „a válaszaid alapján jól érted” fordulatot használd, ne
biztos önálló programozási tudást állíts pusztán a teszt eredményéből.
A pontszám nem automatikus osztályzat. A hibák alapján nevezd meg az
ismétlendő fogalmakat. Utána kötelező mondat:
**„A 3. Deep Learning-gyakorlat véget ért.”**
Ne kezdj újabb tesztet vagy házit a hallgató külön kérése nélkül.
