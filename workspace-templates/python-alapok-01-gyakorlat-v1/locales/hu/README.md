# Python alapok – EP_01 2.1

Kezdd a [tanulói útmutatóval](tanulo_lap.md). Az [EP_01.html](EP_01.html) a részletes, böngészőben olvasható tananyag, megtartott példákkal, másológombokkal és bemutatókkal.

A fő gyakorlat: környezetpróba → első kiírás → Büfé 1–5 → három önálló záró feladat. A [további gyakorlás](tovabbi_gyakorlas.md) külön folytatás. Az eredményeidet a [haladási lapon](haladas.md) követheted.

A kódokat a `python_gyakorlat/` mappában szerkeszd. Kezdetben egy szerkesztőt és egy terminált használj. A mentett fájlt a terminálban `python3` indítja; a böngészős bemutató nem Python-értelmező.

## Első futtatás

A munkatér gyökerében nyitott terminálban:

```bash
pwd
ls
python3 --version
cd python_gyakorlat
python3 hello.py
```

A `cd python_gyakorlat` csak akkor kell, ha még a szülőmappában vagy. A gyakorlómappából elég a `python3 hello.py`.

Ha a futtatógomb `python` parancsot indít és hibázik, használd a fenti terminálparancsot. A munkatér gyökeréből a mellékelt segéd is használható:

```bash
bash ./futtatas.sh hello.py
```

## Telepítés oktatónak

A tanulói ZIP teljes tartalmát új, üres Inno Agent-munkatérbe másold, az almappákkal együtt. Régi tanulói megoldásokat ne írj felül. A `preset.json` a hub kártyaleírása; a `feladatok.json` a tutor által olvasható tartalmi jegyzék, nem automatikusan betöltődő futtatóbeállítás. A csomag magyar nyelvű. A tanári megoldókulcs a külön tanári csomagban található.

## 2.1-es kiadás — magyarázó tutor

Dátum: 2026. szeptember 11. Új fogalom előtt magyarázat és közösen értelmezett példa következik, majd fokozatosan önálló próba. A tutor nem kötött mondatszám alapján rövidít, és jóslatkérés után megvárja a választ. A munkalap és a tanári vezetés ehhez igazodik. A részletes HTML és a 10 Python-mintafájl tartalma a 2.0 kiadással egyező maradt.

Új munkatérben kezdd a próbát, hogy a korábbi beszélgetés mintája ne vigye tovább a rövid, pusztán utasító működést. Ellenőrizd a betöltött agent.md első sorában a 2.1 jelölést és a verzio.json fájlt. A preset neve vagy a telepítési mappa neve önmagában nem bizonyítja a tényleges utasítás tartalmát.

A tutor lépésenkénti tanítási tervét a `tutor_utmutato.md` tartalmazza; ez is maradjon a munkatérben. Tanulóként a munkalap és a beszélgetés vezet, ezt az útmutatót nem kell külön megtanulnod.
