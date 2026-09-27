# 4. gyakorlat – lépésenkénti tutori forgatókönyv

Minden új program: részletes bemutatás és kulcskód-magyarázat → működő
alapfutás → hallgatói megfigyelés és visszajelzés → egy módosítás → új futás
→ hallgatói megfigyelés → visszajelzés.
A PROGRAM_BEMUTATOK.md minden főprogramhoz kész, első futás ELŐTT elmondandó
bevezetőt ad. Az alábbi rövid „Bevezetés” bekezdések csak az óraterv emlékeztetői;
nem helyettesítik a kóddal együtt elmondott bemutatót. Az első Run-kérés csak
a megfelelő bemutató és sormagyarázat után hangozzon el.
A táblázatok a tutor tervei; a hallgatónak egyszerre csak a következő lépést add.
Az alábbi futáskódokat belső állapotként használhatod, nem kell kikérdezni őket.

## Időkeret

| Blokk | Tartalom | Perc |
|---|---|---:|
| 1. | Bemutatkozás, környezetellenőrzés | 5 |
| 1. | G04_01 – tanulási ráta | 12 |
| 1. | G04_02 – momentum | 8 |
| 1. | G04_03 – aktivációk | 10 |
| 1. | G04_04 – adatok, hálózat és első tanítás | 10 |
| 2. | G04_04 – neuronszám és epochaszám | 10 |
| 2. | G04_05 – L2-kísérletek | 10 |
| 2. | G04_06 – dropout | 10 |
| 2. | Tíz tesztkérdés, értékelés és lezárás | 15 |

Mindkét blokk 45 perc. A környezet oktatói telepítése előzetes feladat,
a szünet ezen az időkereten kívül van. A tanítások ideje része az órai keretnek.
Időhiányban rövidítsd a már megértett ismétlést, ne tedd egyszerre több új
feladattal áttekinthetetlenné a beszélgetést. Kimaradt részt ne jelents teljesítettnek.

## 0. Indítás

Bemutatkozás az agent.md szerint, majd `kornyezet_ellenorzes.py` → Run.
Várd meg a „KÖRNYEZET RENDBEN” sort. A `Látható GPU-k: []` a kívánt működés.
Kép megnyitásakor előbb Nézet-frissítés. Hiányzó csomagnál az oktató segítsége
kell; a tanuló nem kap telepítési feladatot. Ne állítsd, hogy minden későbbi
feladat kész pusztán a környezetellenőrzés alapján.

## 1. G04_01_tanulasi_rata.py – egyetlen súly

**Bevezetés:** egy súly értékét módosítjuk. A cél w=3, mert ekkor
`(w-3)**2` nulla. A program a lépések után kiírja a súlyt és a veszteséget,
majd mindkettő változásáról képet ment. Itt nincs bonyolult hálózat vagy adathalmaz.

**R1 előtt:** mutasd és magyarázd a gradiens, frissítés és veszteség sorait.
A gradiens már adott képlet; levezetést nem kérünk. Közös mintalépés:
−1 − 0,1·(−8) = −0,2; az új veszteség 10,24. Ez még a program bemutatása.

**R1 – alapfutás:** `tanulasi_rata = 0.1`, `lepesek_szama = 8`, kezdő súly −1.
Kérd az utolsó sort. A tanuló mondja meg: közelebb került-e a súly a 3-hoz?
A saját eredményét értékeld, a már elmondott bevezetőt ne ismételd végig.

**R2 – nagyobb lépés:** csak a `tanulasi_rata` legyen `0.8`. Mentés és Run.
Kérd a `tanulasi_lepesek.png` megnyitását, előtte Nézet-frissítés.
Kérdés: „A súly mindig ugyanarról az oldalról közelít a 3-hoz?” Várd meg.
Utána magyarázd a túllendülést és a csökkenő kilengést. A veszteség ettől még csökkenhet.

**R3 – túl nagy lépés:** csak a ráta legyen `1.1`. Kérd az utolsó veszteséget.
Kérdés: „A korábbi kezdő veszteséghez képest mit látsz?” Ne közöld előre a választ.
Utána kösd a növekvő eltérést a túl nagy lépéshez. Nem a gradiens előjele hibás.

**R4 – több kis lépés:** térjen vissza a ráta `0.1` értékére, és az R1 alapfutáshoz
képest csak a lépésszámot növelje `25`-re. Ezt két szerkesztési utasításként
add: előbb a korábbi alapbeállítás visszaállítása, majd az új kísérlet változója.
Az összehasonlítás **R1 és R4**, nem R3 és R4. Kérd az utolsó súlyt és a rövid következtetést.

**Továbblépés:** a tanuló érti, hogy a nagyobb ráta nem egyenlő jobb tanulással,
és különbséget tesz lépésméret és lépésszám között.

## 2. G04_02_momentum.py – emlékezet a frissítésben

**Bevezetés:** most két paramétert változtatunk. A függvény az egyik irányban
laposabb, a másikban meredekebb. A két kép ugyanazt a függvényt, kezdőpontot,
tanulási rátát és lépésszámot mutatja. Az egyik módszer megőrzi a korábbi sebesség hatását.

**M1 előtt:** magyarázd el a `hely`, `gradiens`, `sebesseg` sorokat és a
`momentum` → `beta` kapcsolatot. A sebesség két koordinátát tartalmaz;
a tömbökkel végzett számítás elemenként működik. Mondd el, mi a szintvonal.

**M1 – alapfutás:** momentum `0.9`, ráta `0.1`, 40 lépés. Run, majd `utvonalak.png`.
Kérd: nevezzen meg egy különbséget a két útvonalban. Ne mondja csak azt, hogy „más”.

**M2 – memória nélkül:** csak a `momentum` legyen `0.0`. Run, két végpont bekérése.
Kérdés: „Mennyiben különbözik most a két eredmény?” A magyarázat után emeld ki:
beta=0 esetén az előző sebesség eltűnik, ezért a két szabály azonos lesz.

Nem következtetünk arra, hogy a momentum minden feladaton és minden beállítással jobb.
Az x és y itt paraméterkoordináták, nem a következő regressziós feladat mintapárjai.

## 3. G04_03_aktivaciok.py – kimenet és visszafelé haladó jel

**Bevezetés:** egy kész számsort háromféle aktivációval alakítunk át.
Nincs tanítás. A táblázat külön oszlopban mutatja az aktiváció kimenetét,
a lokális deriváltat és a 2-es beérkező gradiensből visszaadott értéket.

**A1 előtt:** a programbemutató alapján magyarázd el az aktivációt, a
lokális deriváltat és a beérkező / visszaadott gradienst. Mutasd meg a
sigmoid számítását és a három eredménytömb sorait. Közös mintapontként
z=0 használható: kimenet 0,5, derivált 0,25, visszaadott gradiens 0,5.

**A1 – sigmoid:** alapfutás, a bemenetek −6, −1, 0, 1, 6.
Kérd a 0 és 6 bemenethez tartozó lokális derivált összevetését.
Ezután kösd a megfigyelést a sigmoid telítődéséhez.

**A2 – telítődő bemenet:** csak a bemeneti sor két szélső eleme változzon:
`np.array([-8.0, -1.0, 0.0, 1.0, 8.0])`. Ez egyetlen vizsgált tényező,
a bemeneti számsor. Run; hasonlítsa a 6 és 8 bemenethez kapott sigmoid-deriváltat.
Utána térjen vissza az eredeti bemeneti számsorhoz az aktiváció-összehasonlításhoz.

**A3 – ReLU:** az eredeti bemeneteken csak `aktivacio = "relu"`.
Mutasd a `np.maximum(0, z)` és a deriváltválasztás szerepét. Run után kérd
a −1 bemenethez tartozó kimenetet és deriváltat. Ez pillanatnyi inaktivitás,
nem önmagában bizonyíték egy neuron végleges „halálára”.

**A4 – Leaky ReLU:** csak `aktivacio = "leaky_relu"`, a negatív meredekség 0,1 marad.
Mutasd a `np.where` két ágát. Run után a −1 bemenet sorát hasonlítsa A3-hoz.

**A5 – meredekség:** csak a `negativ_meredekseg` legyen `0.2`.
Run; ugyanazon −1 bemenet mellett mit változtatott ez a kimeneten és a deriválton?
Rövid visszajelzés után hangsúlyozd: itt mi írjuk át a meredekséget; ez Leaky ReLU,
nem tanulható PReLU-paraméter. A 0 töréspont kézi deriválása nem feladat.

## 4. G04_04_kis_halozat.py – valódi, kis CPU-s tanítás

**Bevezetés:** 192 mesterséges pont, 64 tanító és 128 validációs.
Egy pont bemenete egyetlen x szám, célja egy zajos y szám.
Az ismert zaj nélküli görbe az ábrán magyarázó referencia, nem ezt adjuk célként a hálózatnak.
Adatút: 1 bemenet → ReLU rejtett réteg → 1 lineáris becslés.
A modell a zajos tanítócélokból tanul. A validációt csak mérésre használja.

**H1 előtt:** mondd el a teljes hálózatos programbemutatót: adatok,
modellépítés, compile és fit eltérése, MAE, epocha és batch. Mutasd a modell
és a fit kódját. A kész adatcsomagok 16-os batch-eket adnak; 64 tanítómintánként
4 frissítés történik. A `validation_data` csak mér, a 120 epocha nem 120 mintát
jelent. A kimenet egy szám becslése. Ez a magyarázat előzze meg az első tanítást.

**H1 – alapfutás:** 8 neuron, 120 epocha. Run, majd a végső tanítási és validációs
MAE bekérése; utána `becsles.png`. A hallgató azonosítsa a tanítópontokat,
a validációs pontokat és a hálózat becslését a jelmagyarázat alapján.
Az első blokk végén itt tarthatunk szünetet.

**H2 – több neuron:** csak `REJTETT_NEURONOK = 64`, az epochaszám marad 120.
Run; kérd a végső két MAE-t és a paraméterszámot. Ne követeld fejből a számolást.
Kérdés: „A nagyobb modell ezen a futáson javított-e a validációs hibán?”
Hasonlítsátok H1-hez. Akkor is elfogadható a következtetés, ha alig van különbség.

**H3 – hosszabb tanítás:** a 64 neuron marad, csak `EPOCHOK = 400`.
Hasonlítsátok **H2-höz**. A `tanulasi_gorbek.png` két görbéjét külön nevezze meg.
Egy olyan szakaszt keressen, ahol a két hiba eltérően alakul; ha nem látszik,
ezt mondja ki. Egyetlen ingadozás nem elég általános következtetéshez.

Tanári cél: a tanuló ne az epochák vagy neuronok számából mondja meg,
„jobb-e” a modell. A kisebb tanítási hiba és a jobb általánosítás nem ugyanaz.
A kód az utolsó állapotot értékeli; a korai leállítást most nem kapcsoljuk be.

## 5. G04_05_l2_regularizacio.py – csak a büntetés változik

**Bevezetés:** új, önálló fájl, fix 64 neuron és 120 epocha. Ez H2 keretéhez
igazodik, nem a 400 epochás H3-hoz. A veszteséghez a súlymátrixok négyzetösszegének
λ-szorosát adjuk. Mindkét Dense kernelje kap büntetést, a biasok nem.

**REG0 előtt:** mutasd meg a két `kernel_regularizer` argumentumot és a
külön MAE-metrikát. Magyarázd el a büntetést és a teljes loss eltérését.
Közös számpélda: súlyok [2,−1], λ=0,01 → büntetés=0,05;
MAE=0,12 → teljes loss=0,17. Ezek szemléltető számok, nem futási eredmények.

**REG0 – alapfutás:** `L2_EROSSEG = 0.0`. Run, két MAE és teljes loss bekérése.
A fájl megnyitásakor külön ellenőriztesd: 120 epocha szerepel benne.
Az azonos kezdeti súlyazonosító H2 és REG0 között mutatja az azonos indulást.
A hallgatónak ezt „büntetés nélküli alapfutásnak” nevezd.

**REG1 – enyhe büntetés:** csak `L2_EROSSEG = 0.001`. Run.
Kérd a végső validációs MAE-t és a súlymátrixok négyzetösszegét.
Kérdés: „Az előző alapfutáshoz képest mit változott a becslési hiba?”
Ne ígérj javulást. Ezután nyissa meg a `loss_es_mae.png` képet, és különböztesse meg a két görbét.

**REG2 – erős büntetés:** csak `L2_EROSSEG = 0.05`. Run.
Kérd ugyanazokat a mutatókat. Magyarázat előtt a hallgató értelmezze a változást.
A súlyok csökkenése és a jobb becslés külön célok; túl erős korlátozás ronthat.
A modellek becslési minőségét a **validációs MAE**, nem az eltérő λ-val számolt
teljes loss alapján hasonlítsa. Ezen az órán nincs teszthalmazból új modellválasztás.

## 6. G04_06_dropout.py – üzemmód és véletlen maszk

**Bevezetés:** nyolc rögzített aktiváció. Ez vektorművelet, nem újabb hálózattanítás.
A maszk 0 vagy 1 értéke megtartja vagy lenullázza az adott elemet; a megmaradt
értékek a kiesési aránytól függő szorzót kapnak. A véletlenmag rögzített.

**D1 előtt:** mutasd meg a tanítási / kiértékelési ág kódját. Magyarázd
el a maszkot, a `>= kiesesi_arany` feltételt és az osztást. A 0,5 az egyes
elemek kiesési valószínűsége; nem ígér pontosan négy kiesést. Közös mintában
egy megtartott 0,8-as érték 1,6 lesz, egy eldobott érték nulla.

**D1 – alapfutás:** p=0,5, tanítási mód=True, mag=42. Run, maszk és kimenet bekérése.
A saját kimenetéből válasszon egy megtartott elemet, és értelmezze az átalakítást.

**D2 – kisebb kiesési arány:** csak `kiesesi_arany = 0.25`. Run, `dropout.png`.
A mag marad 42, ezért ugyanazokat a véletlen számokat küszöböljük másképp.
Kérdés: „Mi lett a megmaradó értékek szorzója?” Várd meg, szükség esetén 1/(1−p).

**D3 – új maszk:** csak `veletlen_mag = 43`. Run, hasonlítsa az előző maszkhoz.
Azonos arány mellett más kieső helyek is előfordulhatnak. A rögzített mag nem
szünteti meg a véletlen modelljét, csak reprodukálhatóvá teszi ezt a futást.

**D4 – kiértékelés:** csak `tanitasi_mod = False`. Run, bemenet és kimenet bekérése.
Kérdés: „Mely értékek maradtak meg, és kaptak-e külön szorzót?”
Utána magyarázd: inverted dropout esetén kiértékeléskor a réteg változatlanul továbbít.

## 7. Záróteszt és befejezés

Csak az alapfeladatok megbeszélése után térj a KODERTES_TESZT.md tíz
kérdésére. Egy kérdés, egy válasz, egy pontozás, rövid indoklás; aztán következik
a következő. A kérdések és a kulcs előre adottak. A saját futások konkrét
MAE-számai nem vizsgakérdések. A tesztnek nincs TensorFlow-futtatási igénye.

A 10. kérdés után az agent.md szerinti egyértelmű zárás. Házi és további
kötelező feladat nincs. A két opcionális fájlt ne kezdd el automatikusan.

## Opcionális kiegészítések, külön kérésre

- **Softmax:** alapfutás → `kozos_eltolas = 1000.0` → az eredmény összevetése.
  A maximum kivonása miatt az arányok nem változnak; nincs exponenciális túlcsordulás.
  Ezután külön kísérletben egyetlen logitot változtathat. 5 perc.
- **Batch normalization:** alapfutás → gamma=2, majd külön beta=1.
  Ezután tanítási mód=False mellett ugyanazokra a bemenetekre tárolt statisztikákat
  használ. Egy későbbi bemenetváltoztatás nem módosítja azokat. A gamma/beta a valódi
  rétegben tanulható, a példában kézzel állított; a tárolt átlag és variancia szemléltető. 5–8 perc.
