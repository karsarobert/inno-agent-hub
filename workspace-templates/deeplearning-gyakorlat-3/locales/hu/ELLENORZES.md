# Ellenőrzés – oktatói feljegyzés

## Az első kiadás technikai próbái

Ellenőrzés dátuma: 2026. szeptember 20.
Környezet: Linux x86-64, Python 3.12.14, TensorFlow CPU 2.20.0,
Keras 3.15.1, NumPy 2.3.5, Matplotlib 3.10.8, scikit-learn 1.8.0.
A próbák külön ellenőrző másolatban futottak. A kiosztott csomagban nincsenek
kész hallgatói eredmények vagy kitöltött végső modellválasztási mezők.

### Az első kiadásnál ténylegesen elvégzett ellenőrzések

- Mind a hat Python-fájl szintaktikailag helyes.
- A környezetellenőrzés a teljes környezetben sikeres, a TensorFlow-próba eredménye 6.
- TensorFlow nélküli környezetben az ellenőrző nem telepít; kiírja, hogy
  a hallgató kérje az oktató segítségét, és hibakóddal leáll.
- G03_01 teljes alapfutás: veszteséggörbe, regressziós ábra, beállítások mentése sikeres.
- G03_02 teljes 150 epochos alapfutás: tanítás, validáció, négy ábra, modellmentés sikeres.
- G03_03 teljes 150 epochos futás 16 neuronnal, majd a hallgatói feladat szerinti
  50–50 rejtett rétegekkel: mindkettő sikeres, 99 és 2853 paraméterrel.
- A G03_04 a kisebb validációs loss alapján előzetesen kiválasztott modellt
  sikeresen visszatöltötte és értékelte, újratanítás nélkül.
- A mentett validációs táblák futásonként 120 sort tartalmaznak. A három softmax-
  érték összege a lebegőpontos tűrésen belül 1. A címkékből számított pontosság
  megfelel a kiírt validációs metrikának.
- A tanítási/validációs görbék, döntési ábrák és konfúziós mátrixok vizuális
  ellenőrzése megtörtént. A képek magyar feliratokkal, olvasható tengelyekkel készülnek.
- A tesztben pontosan tíz kódrészletes kérdés szerepel, mindegyik A–D válaszokkal.
  A megoldókulcs és a számítások ellenőrizve.

### Az első kiadás próbaeredményei – nem kötelező hallgatói célszámok

| Modell | Validációs loss | Validációs pontosság |
|---|---:|---:|
| 2 → 3 | 0.682190 | 0.566667 |
| 2 → 16 → 3 | 0.042400 | 1.000000 |
| 2 → 50 → 50 → 3 | 0.020447 | 0.991667 |

A kijelölt szabály a kisebb validációs veszteség volt, ezért a két 50-es
rétegű modell került a végső tesztre. Annak tesztvesztesége 0.012168,
tesztpontossága 1.000000 lett ezen a 120 szintetikus mintán. Ez nem bizonyít
általános tökéletességet, és más verzióval / gépen nem garantált ugyanez.

A 16 neuronos modell magasabb validációs pontossága és a nagyobb hálózat
kisebb vesztesége hasznos példa arra, hogy a két mutató eltérően rendezhet modelleket.
A végső teszt hibátlan lehet; ilyenkor a tutor nem kér nem létező tévesztést,
hanem a mátrix átlóját és az átlón kívüli nullákat értelmezteti.

A regressziós alapfutás súlya 7.3598, biasa 10.1694, validációs MSE/2 értéke
23.7610 lett 120 lépés után. Ez véges tanítás eredménye, nem a veszteségminimum
elérésének bizonyítéka, és nem közvetlenül összevethető a keresztentrópiával.

### Az első technikai ellenőrzés határa

A Python-programokat és az előállított fájlokat ténylegesen ellenőriztük.
A felhasználó saját Innoagent-felületén nem történt élő tutori beszélgetés vagy
Run/Nézet kattintásos próba. Az ottani presetbetöltés és Python-választás
helyi beállítás; az oktató az óra előtt ellenőrizze. A tutor bemutatkozását,
segítségkérését, kérdésenkénti várakozását és lezárását az agent.md előírja.


## Az 1.1 javított változat ellenőrzése

A felhasználó az első változatot élő Innoagent-beszélgetésben is kipróbálta;
a rendelkezésre bocsátott teljes tesztbeszélgetés alapján módosítottuk a
módszertant. Az új 1.1 utasításokkal élő tutori újratesztelést még nem végeztünk.
A programok technikai ellenőrzése ettől külön, tényleges futtatással történt.

- A menetrend mindkét blokkja 45 perc; négy kötelező spirálfutást tartalmaz.
- Az agent, forgatókönyv, bemutatók, kezdő útmutató és kísérleti jegyzet
  ugyanazt a kötelező 0.01 → 0.001 tanulásiráta-próbát írja elő.
- A címke–veszteség párosítás, két gradiens, fit argumentumok és predict/argmax
  bemutatása kifejezetten a futtatás előtti szakaszba került.
- A választási szabály közlése, a hallgatói döntés és indok megvárása,
  valamint a tesztábra-értelmezés külön továbbhaladási feltétel.
- Mind a hat .py fájl szintaktikai ellenőrzése sikeres. A G03_01, G03_02,
  segedletek és környezetellenőrző kódja az első kiadással bájtszinten egyezik.
  G03_03 futási logikája változatlan, a munkamenet kommentje bővült.
- Az 50–50 hálózat 0.01 és 0.001 rátával, 150 epochon és 32-es batch-csel
  újra lefutott külön ellenőrző másolatban. Mindkét futás 2853 paramétert,
  150 soros görbetáblát és 120 soros validációs becslést mentett.
- A softmax-sorösszegek a numerikus tűrésen belül 1-ek. A képek és modellek
  mentése sikeres; az új rátapróba loss-képe vizuálisan ellenőrzött.

| Ellenőrző futás | Ráta | Validációs loss | Validációs accuracy |
|---|---:|---:|---:|
| R3 – 50–50 | 0.01 | 0.0204438064 | 0.9916666746 |
| R4 – 50–50 | 0.001 | 0.0338100046 | 1.0000000000 |

Ezek oktatói próbaeredmények, nem helyettesítik a hallgató saját futásait.
A kisebb ráta ebben a próbában simábban csökkenő görbét és nagyobb végső
validációs veszteséget adott, miközben a pontosság magasabb lett.
A két mutató különbségét ezért saját eredményből lehet megbeszélni.
Más környezetben az értékek eltérhetnek; az irány nem garantált.

A friss G03_04 a 0.01 rátás mentett modell betöltésével ténylegesen lefutott:
tesztloss körülbelül 0.0122, tesztpontosság 1.0. A módosított záróüzenet
előbb ábraértelmezést kér, és csak utána jelzi a kódértési kérdéssort.
Az értékelés során újratanítás nem történt.

A tíz kérdés és a helyes válaszok megmaradtak; minden kérdésben Python-kód
és pontosan négy A–D lehetőség van. A kiosztott csomagban továbbra is a
16 neuronos, 0.01 rátás kezdőmodell és üres végső választási mezők szerepelnek.
A próbafutások mappái nem kerülnek a hallgatói ZIP-be.
