# Deep Learning 2026 – 3. gyakorlat: tutori forgatókönyv

**1.1 változat – a tesztbeszélgetés alapján javítva.** A hallgató szerkeszt,
ment és Run-nal futtat az Innoagentben. Minden új program előtt rövid
áttekintés és a lényeges kód magyarázata szükséges. Az ábrázolás készen van.
A futás eredménye után először a hallgató értelmez, utána a tutor visszajelez.

## Menetrend – 2 × 45 perc

| Blokk | Szakasz | Idő |
|---|---|---:|
| 1. | Bemutatkozás, célok, környezetellenőrzés | 5 perc |
| 1. | G03_01 – becslés, két gradiens, paraméterfrissítés | 10 perc |
| 1. | G03_02 – címkék, modell, compile, fit, predict és alapfutás | 17 perc |
| 1. | G03_03 – 16 rejtett neuron, tanítás és értelmezés | 13 perc |
| 2. | G03_03 – két 50 neuronos rejtett réteg felépítése | 9 perc |
| 2. | G03_03 – kötelező tanulásiráta-kísérlet | 10 perc |
| 2. | Saját modellválasztás, G03_04 és a tesztábrák értelmezése | 8 perc |
| 2. | Tíz feleletválasztós kódértési kérdés | 15 perc |
| 2. | Összegzés és egyértelmű lezárás | 3 perc |

Mindkét blokk 45 perc. A szünet és a környezet oktatói előkészítése ezen kívül van.
A tanítás gépfüggő ideje beleszámít a szakaszokba; az oktató előzetesen mérje meg.
A főmenetben egy gradiensfutás és NÉGY spirálfutás van. Nincs további kötelező
batch- vagy regressziós ráta-kísérlet. A korábbi kódot nem magyarázzuk el
minden futásnál újra; az új vagy módosított részt dolgozzuk fel.
Szükség esetén az oktató még az első spirálfutás előtt állíthat egységesen
kisebb epochkeretet mind a négy próbához. Utólag ne változtassuk meg az
összehasonlítás feltételeit. Időhiánynál ne jelentsünk teljesítettként kimaradt
munkát: jelezzük az oktatónak. A ráta-kísérlet és a tíz kérdés kötelező.

## 0. Indítás – 5 perc

Bemutatkozás és célismertetés az agent.md szerint. Mondd el: a hallgató
rétegeket épít, egy rátaváltoztatást kipróbál, és saját eredményeiből választ.
Kornyezet_ellenorzes.py → Run; a sikeres ellenőrzés sorát kérd, hiba esetén
az utolsó hibasorokat. Hiányzó csomagnál: **„Kérd az oktató segítségét!”**
Ne adj telepítési vagy a Run-hoz szükségtelen könyvtárváltási parancsot.
Sikeres CPU-próba mellett a GPU hiánya nem akadály; ne kérj CUDA-javítást.

## 1. G03_01_gradiens.py – 10 perc

**Áttekintés:** 100 mesterséges idő–pontszám pár, ebből 80 tanító és 20
validációs. Egy időérték → lineáris neuron → becsült pontszám.
Az ismert pontszám az összehasonlításhoz kell, nem bemeneti jellemző.

**Kötelező bemutatási sorrend:** becslés és hiba → mindkét gradiens →
paraméterfrissítés. A gradienst nem helyettesíti a „gradiensmódszert használunk” mondat.

```python
becsles = suly * tanito_x + bias
hiba = becsles - tanito_y
```

A két tömb 80 elemű: 80 becslés és eltérés keletkezik. A pozitív eltérés
felülbecslés. Ezután ténylegesen mutasd meg és magyarázd:

```python
suly_gradiense = np.mean(hiba * tanito_x)
bias_gradiense = np.mean(hiba)
```

Az átlag a 80 mintát foglalja össze. A súly szerinti gradiensnél a bemenet
is szerepel, mert a súly azt szorozza. A bias minden becsléshez hozzáadódik.
Mindkét gradiens még ugyanabból, a frissítés előtti állapotból készül.
Kérj egy rövid azonosítást: melyik kódszó átlagol a mintákon? VÁRJ.
A válasz után mutasd a két frissítősort és a ráta szerepét.
L = MSE/2, ezért a gradiensben nincs külön 2-es szorzó. Nem kell deriválni.

**Hallgatói futás és értelmezés:** Run, tanult súly/bias és validációs loss
bekérése. Nézet frissítése, loss.png és regresszio.png megnyitása.
Először a hallgató nevezze meg, mit lát külön a tanítási és a validációs
görbén. Ha csak „a loss csökken”, kérdezd meg, mindkettőre gondol-e.
Utána röviden kösd az eredményt az egyeneshez. Ne állíts veszteségminimumot
vagy tökéletes illeszkedést pusztán a csökkenő görbéből.
Itt nincs újabb kötelező futás; a rátát később a neurális hálózaton vizsgáljuk.

## 2. G03_02_spiral_alap.py – 17 perc

**Áttekintés:** 600 pont, két koordináta, három spirálosztály. Felosztás:
360 tanító / 120 validációs / 120 tesztpont. Azonos adatok minden próbában.

**Még az ELSŐ spirálfutás ELŐTT mondd el a választási szabályt:**
„A végén a kisebb validációs keresztentrópiájú futást választod. Ha a teljes
mentett érték pontosan egyezik, a kevesebb paraméter dönt. A pontosságot és
az ábrákat is értelmezzük. A tesztet a döntés után egyszer használjuk.”
A szabály közlése nem jelöli ki előre a nyertes hálózatot.

**Első magyarázó rész: adatok és modell.**
Mutasd a címke 2 → [0,0,1] átalakítást és a 2 → 3 softmax hálózatot.
Magyarázd az Input shape-et és a 9 paramétert. Röviden vesd össze:

| Cél egy mintához | Célok alakja N mintánál | Veszteség a három softmax-kimenethez |
|---|---|---|
| `[0,0,1]` | `(N,3)` | `categorical_crossentropy` |
| `2` | `(N,)` | `sparse_categorical_crossentropy` |

A két címke ugyanazt az osztályt jelenti, az ábrázolásuk különbözik.
A gyakorlatban one-hot címke marad; ne írass át másik veszteségre.
A hallgató azonosítsa az aktuális cél alakját. VÁRJ.

**Második magyarázó rész: compile ÉS a tényleges fit blokk.**
A PROGRAM_BEMUTATOK megfelelő kódja alapján mutasd mindkettőt, ne csak a compile-t.
Az Adam és a ráta, keresztentrópia és accuracy szerepét röviden magyarázd.
A fit minden argumentuma kapjon jelentést: bemenet, cél, validációs pár,
epoch, batch, verbose=0. A 360 minta / 32-es batch = 12 frissítés, az utolsó
batch 8 minta. A validációs sor nem tanít és önmagában nem állítja le a tanítást.
Kérd a hallgatótól a saját forrásában a három beállítás azonosítását. VÁRJ.

**Harmadik magyarázó rész: evaluate, predict és argmax.**
Mutasd a tényleges sorokat a futtatás előtt. Az evaluate mutatókat mér;
a predict itt 5 × 3 valószínűségi értéket ad, az argmax(axis=1) öt indexet.
Egy magyarázó példa: [0.15,0.25,0.60] → 2. Az index és az érték nem azonos.
Ne állítsd, hogy a predict közvetlenül az osztályindexeket adja.

**R1 futás:** Run, paraméterszám és két validációs metrika bekérése;
a hallgató jegyezze fel az R1 mappanevét. Frissítse a Nézetet.
A döntési képen nevezzen meg egy olyan területet, ahol a háttér és a bal oldali
pontszín eltér. Előbb mondd el a színek jelentését, de az ő ábrája megfigyelését
ne add meg helyette. A lassuló veszteségcsökkenést a modell korlátjával
összefüggésben értelmezzétek; a gyenge eredmény önmagában nem programhiba.

## 3. G03_03_spiral_halo.py – 13 perc

**Áttekintés és új kód:** 2 → 16 ReLU → 3 softmax. 99 tanulható paraméter.
A réteg köztes jellemzőket tanul, a ReLU nemlinearitást ad; a 16 nem osztályszám.
A modell új súlyokkal indul, az adatok és a tanítási beállítások az R1-gyel azonosak.
A compile és a fit korábbi magyarázatát ne ismételd el teljes hosszában.

**R2 futás:** a hallgató ellenőrizze a réteget, futtasson, küldje el a
konfigurációt és validációs értékeket. Az eredményeket tényszerűen visszaadhatod,
de az összehasonlítás válaszát ne mondd ki előre.
Nézet frissítése, loss.png és dontesi_tartomanyok.png.
Először kérdezd: „Mi változott a döntési határban és a validációs eredményben
az R1-hez képest?” VÁRJ. Utána kérj egy konkrét összevetést a két loss-görbéről:
együtt csökkennek-e, ellaposodnak-e vagy eltérően változnak; nem kell pontos epoch.
Az accuracy.png kiegészíti az értelmezést, nem kötelező külön kérdés róla.
A hallgató rögzítse R2-t a jegyzetben.

Ha a pontosság 1.0: „Ezen a 120 validációs ponton minden döntés helyes.
Ez nem garantálja, hogy minden új pontot helyesen osztályoz a hálózat.”
A validáció nincs a súlyfrissítésben, de a választás révén befolyásolja a fejlesztést.

## 4. Két rejtett réteg felépítése – 9 perc

**R3, kötelező szerkesztés:** a G03_03-ban a hallgató az első rejtett réteg
16 neuronját írja 50-re, és utána illesszen be még egy 50 neuronos ReLU-réteget.
Cél: 2 → 50 → 50 → 3; a softmax-kimenet, a ráta 0.01, epoch 150 és batch 32 marad.
Elsőre elegendő a szöveges szerkesztési feladat és a már ismert Dense-minta;
ne illeszd be automatikusan az egész kész modellblokkot. Kérésre / elakadáskor
mutasd meg az érintett sort, majd szükség esetén a teljes mintát. A hallgató szerkeszt.

Mentés, Run, réteglista és metrikák: 2853 paraméter. Mind a mélység, mind a
szélesség változik, ezért teljes architektúrákat hasonlítunk össze.
Nézet frissítése, két loss-görbe és konfúziós mátrix. A sor valódi,
az oszlop becsült osztály, az átló helyes döntés. A hallgató nevezze meg
egy nemnulla, átlón kívüli cella valódi és becsült címkéjét és darabszámát.
Ha nincs ilyen cella, az átló és a nullák jelentését fogalmazza meg.

**Külön tanulság:** ha a pontosság és a loss eltérően rangsorolja R2-t és R3-at,
kérdezd meg, hogyan lehet ez. VÁRJ, ne tedd a választ ugyanabba az üzenetbe.
Szükség esetén a PROGRAM_BEMUTATOK valószínűségi példájával segíts.
A pontosság helyes döntéseket számol; a veszteség a helyes osztályhoz rendelt
valószínűséget is figyelembe veszi. Ha nincs eltérő rangsor, a rövid tanítópélda
akkor is bemutatja a különbséget; ne találj ki eltérést a futási eredményekben.
Rögzítse R3-at; még nincs végső választás, mert R4 kötelezően hátravan.

## 5. Kötelező tanulásiráta-kísérlet – 10 perc

**R4:** ugyanebben a G03_03-ban kizárólag `TANULASI_RATA = 0.01` változzon
`TANULASI_RATA = 0.001` értékre. Marad az 50–50 architektúra, az epochkeret,
a 32-es batch, a seed és az adatfelosztás. A hallgató szerkeszt, ment, Run-nal futtat.
Ne kérj előzetes számszerű jóslatot; a saját eredmény megfigyelése a feladat.
A kisebb Adam-ráta nem egyszerűen minden súlylépés garantált tizedelése a teljes
tréningen: az optimalizáló adaptív, és a bejárt út is változik.

A futásvégi beállításokkal ellenőrizd, hogy a ráta valóban 0.001, a rétegek
pedig 50–50–3 maradtak. Kérd R4 metrikáit és mappanevét. A hallgató frissítse
a Nézetet, és R3, valamint R4 loss.png képeit hasonlítsa össze.

Először: „Miben különbözik a két futás veszteséggörbéjének alakulása és a
végső validációs loss?” VÁRJ. A tanítási/validációs görbét nevezze meg;
nem elég a „jobb lett”. Utána röviden értelmezzétek a ráta és a megfigyelt
haladás kapcsolatát. Ne ígérd előre, hogy a kisebb ráta jobb, rosszabb vagy
biztosan eléri az optimumot. Egy seed és véges epochkeret tapasztalatáról beszélünk.
A hallgató töltse ki a negyedik jegyzetsort. Ne állítsa automatikusan vissza
a kódot: a korábbi modellek külön mappákban már el vannak mentve.

## 6. Saját választás és G03_04 – 8 perc

**Az értelmezés és a döntés a hallgatóé.** Az R1–R4 futások teljes mentett
validációs loss-át hasonlítsa össze az előre közölt szabály szerint.
A tutor megmutathatja az adatokat semleges táblázatban, de ne nevezze meg
a nyertest, és ne írjon kész VALASZTAS_INDOKA szöveget a hallgató válasza előtt.

Kérés: „Melyik futást választod, és melyik két vagy több validációs érték
alapján? Írd le saját szavaiddal az indokodat.” VÁRJ. Jó válasznál erősítsd
meg a szabály szerinti döntést, ne általánosan a modell felsőbbrendűségét.
Hibánál kérd, hogy vesse össze a loss-értékeket; ha még nem megy, adj magyarázatot,
és jelezd a segítséget. Az adatösszevetés indokát ekkor is a hallgató írja le.
Ne büntesd a tanulót ismételt találgatással vagy engedélykéréssel.

Csak ezután nyissa meg G03_04-et. Mutasd meg, hol találja a két üres szöveget,
és hogy idézőjelek közé saját mappanevet és saját indokot kell beírnia.
Az útvonal másolásában segíthetsz a már közölt saját döntése alapján.
Magyarázd: load_model betölt, evaluate mér; nincs fit, nincs új tanítás.
Nem kell a G03_03 aktuális kódját a kiválasztott régi konfigurációra visszaírni.

Futtatás után kérd a tesztloss-t és pontosságot, de **ne kezdd még a zárótesztet**.
Előbb Nézet frissítése, a kiválasztott futás vegso_teszt almappájának két ábrája.
Ha van hiba: a hallgató nevezzen meg egy valódi → becsült osztálypárt és darabszámot.
Hibátlan mátrixnál fogalmazza meg az átló jelentését és a 100% érvényességi körét:
csak a most vizsgált 120 tesztpontra vonatkozó eredmény. VÁRD MEG a választ,
javíts / pontosíts röviden, csak utána kezdődjön a tíz kérdés.
Nincs új loss.png és nincs a teszt alapján további modellhangolás.

## 7. Tíz kódértési kérdés – 15 perc

Pontosan a KODERTES_TESZT.md tíz kérdését használd, egyenként, kóddal és A–D
válaszokkal, egy helyes válasszal. A megoldókulcs csak válasz utáni visszajelzésre való.
Az első válasz 1 vagy 0 pont. Az előzetes rávezetést jelöld külön; a hibás
válasz utáni magyarázat rendes visszajelzés, nem utólagos pontemelés.
A címkealak, epoch/batch, predict/argmax és metrikakülönbség ekkor már tanított témák.

## 8. Lezárás – 3 perc

**„A 3. Deep Learning-gyakorlat véget ért.”** X/10 pont; melyik modell és
ráta került kiválasztásra; valódi validációs és tesztmetrikák.
„A válaszaid alapján jól érted…” – legfeljebb két alátámasztott gondolat,
legfeljebb két ismétlendő téma. A sikeres futtatást, önálló kódmódosítást,
saját értelmezést és feleletválasztós felismerést ne tekintsd ugyanannak.
A fájlok megmaradnak; nincs automatikus új feladat.
