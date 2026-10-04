# Óraterv – DL05, autoencoder · 2 × 45 perc

A lépésazonosítók belső állapotjelölések. Nem kell felolvasni őket.
Minden új program előtt a PROGRAM_BEMUTATOK megfelelő bemutatása kötelező.
Egy feladat után várj eredményre; egy üzenetben ne add fel a teljes táblázatot.
A helyes megfigyelés lehet az is, hogy nincs egyértelmű javulás.
MINDEN sikeres futásra adott válaszban legyen Nézet-frissítési emlékeztető;
a számok bekérése és a program saját kiírása ezt nem helyettesíti. Minden fájl
megnyitásakor előbb a számozott kódblokkokat mutasd be, utána kérj futtatást.

## Első blokk – 45 perc

### E0 · Környezet · 5 perc

Bemutatkozás után `kornyezet_ellenorzes.py`. Bizonyíték a KÖRNYEZET RENDBEN sor.
`[]` GPU-lista rendben van. Hiba: a vége és az értelmező útvonala; oktatói segítség.
A részleges ellenőrzés nem teljes siker. Hiányzó TensorFlow esetén az oktató
engedélyével G01, G03, G04 mehet, G02 kimaradását jelöld.

### A1–A3 · EKG-adatok · 10 perc

**A1:** új program bemutatása, kulcskód, majd `G05_01_ekg_adatok.py` alapfutás,
`minta_index = 0`. Kérd az „Egy jel 140 mintapontot tartalmaz” sort. Frissítse a Nézetet,
nyissa meg a mostani `ekg_jelek.png` képet.

**A2:** egyetlen megfigyelési kérdés: „Miben tér el a két jel alakja?”
Ne követelj orvosi értelmezést; elég csúcs, völgy, jelalak vagy eltérés helye.
A címke az adathalmazból származik, nem a szemünk által felállított diagnózis.

**A3:** előbb mondd el: másik jeleket vizsgálunk, a 0–1–2–3 index az első–második–harmadik–negyedik
példát jelenti. A negyedik normál és negyedik rendellenes jelet külön kiemeljük,
a jelértékeket nem változtatjuk. Ugyanebben a fájlban `minta_index = 3`; mentés, Run, Nézet-frissítés, új kép.
Kérj egy rövid összehasonlítást az előző párral. Tisztázd: 140 érték minden sorban,
index 0 az első, index 3 a negyedik példa; a két csoport azonos indexe nem betegpár.

### B1–B3 · Az első autoencoder · 20 perc

**B1:** teljes bemutató a G02 előtt: 140 → 32 → 16 → 8 → 16 → 32 → 140,
azonos bemenet és cél, normál tanítás, sigmoid-amplitúdók, compile és fit.
Alapfutás: `epochok_szama = 10`, `szuk_keresztmetszet = 8`.
Várja meg a FUTÁS KÉSZ jelzést. Kérd a normál validációs MAE-t és a 0. normál
példa MAE-ját (két rövid összetartozó sor, nem teljes log).

**B2:** a mostani `rekonstrukcio.png`. Kérdés: „Hol követi jól, és hol kevésbé
jól a rekonstruált jel az eredetit?” Hallgasd meg, majd magyarázd a két görbét
és az eltérést jelző árnyalást. Ne kérj a képről leolvashatatlan pontos számot.

**B3:** `tanulasi_gorbek.png`. Kérdés: „Hogyan változik a normál validációs hiba
a tanítás során?” A validáció nem tanít; nem szükséges monotonnak lennie.
Ebben a csomagban mindkét görbe normál adatokból származik, eltérően az eredeti
notebook vegyes validációjától. Itt nincs korai leállítás vagy legjobb súly-visszaállítás.

### B4–B5 · Hosszabb tanítás · 10 perc

**B4:** csak `epochok_szama = 30`. A bottleneck marad 8. Mondd el, hogy új
modellt indítunk ugyanabból a kezdetből: nem a tíz korábbi epochát folytatjuk.
Mentés, Run, ugyanaz a két MAE-sor, majd a mostani rekonstrukciós kép.

**B5:** frissítse a Nézetet, a mostani 30 epochás mappából nyissa meg az
`osszehasonlitas.png` képet. Ezen ugyanaz a jel és a két saját rekonstrukció azonos
tengelyskálával szerepel, alul a pontonkénti abszolút eltérésekkel. A képen látszó
futásnevekkel azonosítsátok a két mérést; ne emlékezetből hasonlítsatok.
Ha nincs kép, a program megmondja, hogy nem talált megfelelő, új formátumú saját
10 epochás futást. Ezt tisztázzátok; ne állíts kész összehasonlítást.
Ezután hasonlítsátok össze a 10 és 30 epochás futást. Egy kérdésben a látható
változásra kérdezz, utána egyeztesd a számokkal. Az állapotban rögzítsd a két
futás azonosítóját és a megfigyelést. Ha eltérő lett a kezdősúly-azonosító,
ellenőrizzétek, nem változott-e más beállítás vagy a környezet.

**Blokkzáró mondat:** „A hálózat a normál jelek visszaállítását tanulta. Most
megvizsgáljuk, mit árul el a rekonstrukció hibája a különböző jelekről.”
Ha szünetet tartanak, innen folytasd, új köszöntés és új környezetellenőrzés nélkül.

## Második blokk – 45 perc

### C1–C4 · Rekonstrukciós hiba · 15 perc

**C1:** `G05_03_rekonstrukcios_hiba.py` bemutatása. Ez nem a saját legutóbbi
modellt olvassa, hanem a mellékelt, 30 epochás referencia rekonstrukcióit.
Így mindenki ugyanazokat a jeleket vizsgálhatja, tanítás nélkül. Magyarázd el
az abszolút eltérést, átlagot és `axis=1` szerepét egy rövid közös mintán.

**C2a:** alapfutás `minta_index = 0`; kérd a két kiemelt MAE-sort. Frissítse a Nézetet,
majd nyissa meg az `axis_1.png` képet. A két szemléltető sor saját átlaga 0,2 és 0,4;
a közös átlag 0,3. Kérdezd: „Miért két eredmény tartozik az axis=1 művelethez?”
VÁRJ, majd értékeld. Szükség esetén mutass rá, hogy egy sor egy jel. Ezután
kapcsold a valódi (128,140) → (128,) átalakításhoz.

**C2b:** a frissítési emlékeztető után nyissa meg a
`rekonstrukciok.png` képet. Kérdés: „A hibaszámok és a görbék ugyanazt a
különbséget mutatják-e?” Ne mondd előre, melyik a nagyobb.

**C3:** magyarázd el, hogy most a két csoport negyedik példáját választjuk
külön vizsgálatra (0 az első, 3 a negyedik). `minta_index = 3`; Run, Nézet-frissítés és új ábra. Egy megfigyelés. A különböző
bemenetekhez külön hiba tartozik; egy példa alapján ne általánosítsatok.

**C4:** a mostani `hibaeloszlas.png`. Mutasd meg a tengelyek jelentését,
majd kérdezd, van-e átfedő hibatartomány. Az indexváltás nem változtatta a
hisztogramot, mert az továbbra is mind a 128+128 példát mutatja.

### D1–D5 · Küszöb és téves döntések · 15 perc

**D1:** `G05_04_kuszob.py` bemutatása: `hiba >= kuszob`; pozitív = rendellenes.
Először csak TP/FN/FP/TN közérthető darabszámait magyarázd. A precision és recall
képleteit majd a darabszámok megértése után vezesd be. Nincs új tanítás: a rögzített
rekonstrukciókból ugyanazokat a MAE-értékeket számítjuk újra.

**D2:** alapfutás `kuszob = 0.04`. Kérd a négy darabszámot, majd frissítse a
Nézetet és nyissa meg a `dontesek.png` képet. Kérdés: „Mit jelent itt a téves
riasztás?” A hallgató fogalmazza meg, utána pontosítsd.

**D3:** csak `kuszob = 0.025`. Run és négy darabszám. Kérdés: „Mi változott
az alapfutáshoz képest?” Lehet, hogy nem lesz több TP, mert már minden
rendellenest jelzett az alapérték. Ne állíts előre kötelező növekedést!
A `hibaeloszlas.png` ugyanazt az eloszlást, más helyen álló függőleges vonalat mutatja.

**D4:** csak `kuszob = 0.06`. Run és darabszámok. Kérdés: „Milyen árat fizetünk
itt a kevesebb riasztásért?” Előbb válasz, utána a tényleges FP és FN alapján visszajelzés.

**D5a:** a már ismert 0.06-os futásból vezesd be a precisiont. Nincs új futás.
Frissítse a Nézetet, nyissa meg a `precision_recall.png` képet. Először csak a
felső sávot értelmezd: a riasztásokból indulunk, itt 127 = 121 jogos + 6 téves.
Precision = 121/127 ≈ 95,3%. Kérdezd: „Miért a 127 riasztással osztunk itt?” VÁRJ.

**D5b:** a válasz után az alsó sáv: a valódi rendellenességekből indulunk,
128 = 121 észlelt + 7 elnézett. Recall = 121/128 ≈ 94,5%. Kérdezd: „A hét
elnézett rendellenesség melyik csoportban szerepel, és miért számít a recallnál?” VÁRJ.
A számokat mindig a hallgató tényleges kimenetéhez igazítsd; a fenti értékek a referencia.

**D5c:** foglald össze: ugyanaz a 121 helyes észlelés, de más a kiinduló csoport.
A küszöb nem javítja a rekonstrukciót. A modellteszt nem független végső mérés.
Csak a két megértési válasz tisztázása után kezdődhet a záróteszt.

### O1 · Opcionális bottleneck-kísérlet

Csak valóban gyors haladáskor, az agent.md időfeltételeivel. Ugyanaz a G02,
`epochok_szama = 30`, ezután egyetlen változás: `szuk_keresztmetszet = 16`.
Mutasd meg újra csak az érintett rétegsort. Kérd a validációs és a kiemelt
normál példa MAE-ját; magyarázd, hogy több belső érték nem garantál jobb anomáliaészlelést.
A kapott számok csak a normál rekonstrukcióról szólnak. **G03/G04 referenciája
ettől nem változik**, ezért az ottani régi darabszámokkal nem mérhető ez az új modell.
A módosított modell anomáliaértékelése további, az alapórán kívüli kísérlet lenne.

### T1–T10 és Z · Zárás · 15 perc

Pontosan a tíz rögzített kérdés, egyenként, magyarázatos visszajelzéssel.
Csak a végén pontszám és összegzés. Ne hagyj ki kérdést önkényesen időhiány miatt:
ha az óra megszakad, rögzítsd a valódi állapotot, ne nevezd befejezettnek.
Nincs házi feladat és nincs CNN-előzetes feladatsor.
