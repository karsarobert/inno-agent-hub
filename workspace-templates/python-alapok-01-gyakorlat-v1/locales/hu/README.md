# Python alapok – EP_01 v2

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
