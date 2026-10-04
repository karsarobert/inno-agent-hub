# Oktatói előkészítés

## Telepítés előtt

A munkamappa gyökerében legyen az agent.md, a négy G05 fájl és a segédmodulok;
mellettük az adatok almappa. A ZIP nem Innoagent-telepítő és nem alkalmazásplugin.
A meglévő Innoagentben a munkaterülethez a szokásos módon rendeld hozzá a tutori
utasítást. Ellenőrizd, hogy az agent az aktuális mappában levő útmutatókat tudja olvasni.
Ne legyen mellette aktív, másik leckét előíró régi tutori utasítás.

## Python-környezet

A mellékelt requirements.txt a ténylegesen tesztelt Linux x86-64 / Python 3.12
csomagverziókat rögzíti. Más operációs rendszeren a TensorFlow telepítőcsomagját
az adott platformhoz kell megválasztani. Egy már működő oktatási környezetet
nem kell automatikusan lecserélni: először futtasd a környezetellenőrzést és az alapfájlokat.

Szükség esetén, **oktatói előkészítésként**, a kicsomagolt mappában:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python kornyezet_ellenorzes.py
```

Ez internetet és letöltési időt igényel; ne a tanórán, ne a tutor végezze.
Az Innoagent Run ugyanennek az előkészített környezetnek az értelmezőjét használja.
Az ellenőrző program kiírja az értelmező pontos útvonalát, ezzel ellenőrizhető az egyezés.
A Python-példák futáskor nem töltenek le adatokat és nem kérnek GPU-t.
Az Innoagent modellkapcsolatának igénye külön kérdés.

A cpu_kornyezet.py a TensorFlow importja előtt tiltja a GPU-t, korlátozza a CPU-s
szálakat, és rögzített véletlen magot állít. A tanítás tf.data csomagokat használ
korlátozott háttérszállal, hogy az egyszerű, többepochás példa kisebb környezetben is működjön.
Ezért a forrásban a bemenet=cél párosítás az adatcsomag(...) hívásban látszik;
a notebook fit(x,x) formájának tartalma megmarad.

## Óra előtti próba

1. Környezetellenőrzés: teljes siker, GPU-lista üres, ellenorzes.png létrejön.
2. G01 alapfutás és index 3. A Nézet frissítése után a megfelelő új képet nyisd meg.
3. G02: 10, majd 30 epocha, bottleneck 8. Mérd meg a teljes Run-időt a tantermi gépen.
4. G03: a helyi referencia betöltődik, TensorFlow-import nélkül.
5. G04: 0.04, 0.025, 0.06. A darabszámokat hasonlítsd az oktatói megoldásokhoz.
6. Az órai munkapéldány alapértékeit állítsd vissza: G01/G03 index 0; G02 10 epocha,
   bottleneck 8; G04 küszöb 0.04. A csomagban ezek az induló értékek.

A referenciát ne írd felül egy hallgató futásával. Az adatok és a referencia
ellenőrzőösszege dokumentált. Ha tudatosan új referenciát készítesz, a leírását,
a küszöbök oktatói eredményeit és az útmutatókat együtt kell frissíteni.

## Hibakezelés

- Csak TensorFlow hiányzik: G01/G03/G04 működhet; a teljes környezetellenőrzés
  részleges státuszt és nem nulla kilépési kódot ad. G02 kimaradása technikai okként szerepeljen.
- Hiányzó NPZ: a teljes adatok almappát kell helyreállítani az eredeti ZIP-ből.
- Réginek tűnő kép: a futás által kiírt új almappa megnyitása és a Nézet frissítése.
- Szokatlan tanítási eredmény: állítsd vissza a beállításokat, ellenőrizd a csomagverziókat
  és a kezdősúly-azonosítót. Nem követelmény minden gépen azonos utolsó tizedesjegy.
- Duplán megjelenő agentválasz: nézd meg, egyetlen válasz tartalmaz-e ismételt
  szöveget, vagy az alkalmazás ugyanazt az üzenetet kétszer jeleníti meg. Az utóbbi
  alkalmazásoldali továbbítási/megjelenítési hiba lehet; nem újabb hosszú prompttal javítható.

## Pedagógiai eltérések az eredeti notebookhoz képest

A kisebb, sorok szerint különválasztott adathalmaz a CPU-s rövid futást szolgálja.
A normál validáció tisztább összehasonlítás a normál tanítási görbéhez. A külön,
vegyes gyakorlóhalmazt sokszor nézzük és azon állítjuk a küszöböt, ezért nem
állítunk független teszteredményt vagy klinikai használhatóságot.
Az önálló G03/G04 és a rögzített referencia az óra folytathatóságát szolgálja;
az agent ezt minden ilyen új program előtt egyértelműen elmondja.


## 1.1 – rövid futásmappák és összehasonlítás

A sorszám programonként nő, a mentés nem ír felül régi mappát. A pontos időpont
az eredmeny.json része. Az új csomagot tiszta munkamappába ajánlott kicsomagolni;
a korábbi hosszú nevű mappákat a program nem törli és nem nevezi át.
Az új 10 → 30 epochás menetet ellenőrizd az osszehasonlitas.png képpel is.
A 30-as futás önmagában továbbra is működik, de megfelelő saját 10-es előzmény
nélkül nem készül összehasonlítás. Opcionális 16-os bottleneck nem hasonlítható
észrevétlenül egy 8-as bottleneckkel készült előzményhez.
A frissítési szabály az agent utasításai közt és a programkiírásban is szerepel;
a tényleges betartását élő agentpróbával ellenőrizd.
