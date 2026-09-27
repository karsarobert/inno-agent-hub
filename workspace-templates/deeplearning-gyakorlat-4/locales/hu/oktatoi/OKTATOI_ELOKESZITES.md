# Oktatói előkészítés

## Környezet

A csomag tesztelt célkörnyezete Linux x86-64, Python 3.12, NumPy,
Matplotlib és CPU-s TensorFlow/Keras. Az ellenőrzött verziók és a mért futások
az ELLENORZES.md dokumentumban vannak. A `requirements.txt` a közvetlen
függőségek tesztelt verzióit rögzíti, nem minden tranzitív csomag teljes zárolása.

Az alábbi telepítés **oktatói előkészítés**, nem hallgatói feladat:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python kornyezet_ellenorzes.py
```

Ezt a kicsomagolt munkamappában hajtsa végre az oktató, ha új környezet kell.
A meglévő, megfelelő TensorFlow-környezet is használható előzetes próbával;
ne telepítsünk rá feleslegesen másik TensorFlow-változatot. Az Innoagent Run
funkciója ugyanezt a megfelelő Python-értelmezőt használja. A kiválasztás módja
az alkalmazás beállítása; a csomag nem feltételez hozzá nem ellenőrzött menüpontot.

A `cpu_kornyezet.py` import előtt letiltja a GPU láthatóságát, utána TensorFlow-
beállítással is CPU-ra korlátoz. A műveleti és adatbetöltési szálak száma
kicsi; a hálózatok 25 vagy 193 paraméteresek. Nincs CUDA- vagy GPU-telepítési feladat.
Minden fájl friss Python-folyamatban futtatható. A notebook-kernelbe történő
utólagos import nem az órai használat módja.

## Óra előtti próba

1. Nyisson új munkamappát a csomagból, és futtassa a környezetellenőrzést a Run gombbal.
2. Futtassa a G04_04 alapváltozatát. Ellenőrizze a 8 neuront, 120 epochát,
   a 64/128 mintaszámot, a CPU jelzést és a mentett ábrákat.
3. Próbálja ki a 64 neuronos, 400 epochás változatot és mérje a teljes futást.
   Óra előtt állítsa vissza a hallgatói kezdőértékeket: 8 neuron, 120 epocha.
4. Próbálja ki az L2-fájl három értékét: 0, 0.001, 0.05. A kiadott alapérték 0.
5. Ellenőrizze, hogy az agent minden új program első futtatási kérése ELŐTT
   elmondja a célt, a bemenet–számítás–kimenet kapcsolatát, és megmutatja,
   majd megmagyarázza a fontos kódrészleteket. A puszta célmegjelölés nem elég.
   Ezután kérjen egy alapfutást, várjon az eredményre, és a korábbi rendben
   folytassa a módosításokat. A promptfájlok önmagukban nem bizonyítják az
   adott Innoagent-változat tényleges viselkedését.

Az oktatói próba eredményei ne keveredjenek a hallgató saját `nezet` mappájával.
A csomag eleve nem tartalmaz kész hallgatói futásokat; a referenciaábrák az
`oktatoi/mintakimenetek` alatt külön helyen vannak.

## Miért ilyen kicsi a feladat?

A fő cél a kód és a kimenet kapcsolatának megértése. A mesterséges,
egy bemenetű feladat kiküszöböli a Spotify-adatfeldolgozás, a műfajkódolás és
a nagy adatmennyiség járulékos terhét. A mintaadatok a futásban keletkeznek,
nincs letöltés vagy CSV-előkészítés. A referenciafüggvény ismert, ezért
a becslési görbe közvetlenül értelmezhető.

A kis hálózat tanítása valódi TensorFlow/Keras-tanítás. Az aktiváció-, momentum-,
dropout-, softmax- és BN-példák matematikai szemléltetések, nem hamisított
tanítási eredmények. A dropout nem kerül bele a kötelező hálózatos kísérletbe:
először a mechanizmusát értjük meg. Az alkalmazott dropout és a korai leállítás
részletes összehasonlítása a meglévő notebookban marad.

## Tudatos egyszerűsítések és eltérések

- A kis hálózat Adamot és MAE-t használ, mint a kapcsolódó notebook, de a
  tanulási ráta itt 0.01, a feladat és az adatmennyiség különbözik.
- Az L2 itt mindkét Dense-kernelre vonatkozik. Így a teljes kernel-négyzetösszeg
  és a büntetés közvetlenül összekapcsolható. A HTML/Spotify-példa csak a
  rejtett rétegek kerneljeit regularizálja; ezt a tutor röviden jelzi.
- Nincs korai leállítás vagy automatikus legjobbállapot-visszaállítás.
  Az utolsó epocha modelljét mérjük, minden kísérletben következetesen.
- Nincs végső teszthalmaz-értékelés. A validációval végzett szemléltető
  összehasonlítás nem független teljesítménybecslés. A záróteszt a hallgató
  fogalmi megértését méri, nem a modell általánosítását.
- H1 és H2 eltérő méretű hálózat, így súlyaik nem lehetnek azonos mátrixok.
  H2/H3 és az L2-futások esetén azonos a kezdeti súlyazonosító és az adatkeverés szabálya.
- A fix mag csökkenti a véletlen eltérést, gépek és csomagverziók között
  nem ígérünk bitenként azonos eredményt.

## Időkeret és tanári döntések

Az első blokkban a kis hálózat első futásáig jutunk. A másodikban a modellméret,
tanítási idő és L2 összehasonlítása, a dropout és a záróteszt következik.
A kód átírásánál a legtöbb lépés egyetlen értékre korlátozódik.
Az agent ne oldja meg helyettük a megfigyelési kérdéseket.

Ha a helyi gépek lassabbak, az oktató még az óra előtt adhat egységesen
rövidebb tanítási keretet. A H2-alap és az L2-futások epochaszáma ilyenkor is
azonos legyen; a H3 a hosszabb keret kísérlete. A tanulási görbék így is
ellenőrzendők, a túlillesztés látványát nem szabad garantálni.
Az opcionális softmax/BN nem indítható automatikusan a kötelező idő rovására.

## Forrás és használat

A csomag a DL_04 elméleti anyaghoz készült, a DL_03 innoagent-csomag tutori
szerkezetét követi. A kódok helyben, előkészített környezetben offline futnak;
az Innoagent modellkapcsolata ettől független. A tanári megoldókulcsok a
csomagban olvashatók; ez nem zárt vizsgafelület.


## Az 1.1 változat használata folyamatban lévő próbánál

A módosítás a futás előtti magyarázatot erősíti. A Python-kódok, a kezdőértékek,
a kísérletek és a tízkérdéses teszt változatlanok.

A korábbi munkamappába ebből a csomagból az `agent.md`, a
`LECKE_UTASITASOK.md` és a `PROGRAM_BEMUTATOK.md` friss példányát másolja át.
Így megmaradnak a tanuló módosított Python-fájljai és a saját eredményei.
A többi Markdown-fájl az oktatói / indítási dokumentáció pontosítása.
Az alkalmazás megszokott módján töltse be újra a tutori utasítást; a változás
automatikus átvételét egy folyamatban lévő beszélgetésben nem feltételezzük.

A beküldött próbában a G04_04 első tanítása sikerült, és az agent a becslési
ábra értelmezésénél tartott. Ezen a ponton először pótolja a modellépítés,
compile és fit magyarázatát, majd folytassa az ábra megbeszélését. Ne kérjen
új alapfutást és ne indítsa újra a G04_01-et. Ha új beszélgetés szükséges,
az utolsó eredményt és az aktuális lépést át lehet adni a folytatáshoz.

Rövid kipróbálásnál a következő új példára váltás üzenetét vizsgálja:
szerepel-e benne konkrét kód, sormagyarázat és a kimenet értelmezése még a
Run-kérés előtt? Az új magyarázatokat a meglévő időkeretbe illesztettük;
a korábbi, futás utáni első kódismertetés került előre. A helyi beszélgetés
tempóját továbbra is az oktatói próba alapján érdemes megítélni.
