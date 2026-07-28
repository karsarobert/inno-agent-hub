---
name: ian-xiaohei-illustrations
category: Tartalomkészítés
description: Ian stílusú magyar nyelvű cikkillusztrációk készítése. Akkor használd, ha a felhasználó magyar nyelvű cikkhez, bejegyzéshez, bloghoz, Notion dokumentumhoz, munkafolyamat-leíráshoz, módszertanhoz, folyamathoz, struktúrához, állapothoz, metaforához vagy nézőponthoz kér „bizarr”, „kisFekete”, „kézrajzolt”, „cikkillusztráció”, „cikkbeli kép”, „illusztrációs javaslat”, „shot list”, „címtelenítés/képjavítás” feladatot; alapértelmezés szerint a KisFekete IP-t használja, tiszta fehér háttér, kézrajzolt vonalak, kevés piros/narancs/kék megjegyzés, letisztult, de szabadon szárnyaló vizuális stílus.
---

# Ian KisFekete bizarr cikkillusztrációk

## Alapvető célkitűzés

Magyar nyelvű cikkekhez 16:9 fekvő tájolású szöveges illusztrációk tervezése és generálása. A cél nem kereskedelmi illusztráció, PPT infografika vagy aranyos rajzfilmkarakter készítése, hanem a cikkben szereplő kulcsítéletek, folyamatok, struktúrák, állapotok vagy metaforák letisztult, bizarr, kreatív, olvasható, de nem „útmutató” jellegű kézrajzolt magyarázó ábrává alakítása.

Az alapértelmezett vizuális IP a „KisFekete”: tömör fekete figura, fehér pontszemű, vékony lábú, üres arckifejezésű komolyan végez egy bizarr, de logikusan létező cselekvést. A KisFekete a kép magját képező cselekvésnek résztvevője, nem lehet, hogy csak díszként álljon oldalt.

## Először ezeket a referenciákat olvasd

A feladat igényeinek megfelelően olvasd be, ne töltsd meg egyszerre a kontextust:

- `references/style-dna.md`: stílus DNS, színek, szövegek, tilalmak.
- `references/xiaohei-ip.md`: a KisFekete IP megjelenése, személyisége, mozgáskincse és tilalmai.
- `references/composition-patterns.md`: szerkezeti típusok, eredeti metafora-alkotási módszerek és ismétlődési szabályok.
- `references/prompt-template.md`: egyképes generálási prompt-sablon.
- `references/qa-checklist.md`: generálás utáni ellenőrzés és iterációs szabályok.
- `assets/examples/`: csak alacsony frekvenciájú vizuális kalibrációra szolgál, nem lép be az alapértelmezett generálási útvonalba. Ne másold egy az egyben ezeknek a példáknak a kompozícióját, tárgyait vagy megjegyzéseit.

## Munkafolyamat

### 1. A szöveg feldolgozása

Először olvasd be a felhasználó által megadott szöveget, hivatkozásokat, Notion oldalakat, Markdown fájlokat vagy képernyőmentések tartalmát. Vond le belőlük:

- Mi a fő gondolat
- Mely bekezdések hordozzák a kognitív fordulópontokat
- Milyen tartalmakat érdemes ábrával elmagyarázni
- Mely helyeken csak szöveg szerepel, nem kell kép

Ne egyenletesen osszd el a képeket. Előnyben részesítsd a „kognitív horgonyokat”, például: alapvető ítélet, két töréspont, bemenet-kimenet zárt köre, elágazás, előtte-utána összehasonlítás, egy anyag többfelhasználása, továbbítási útvonal, gyakori buktatók, szereplő állapotváltozása.

### 2. Először illusztrációs stratégia

Ha a felhasználó csak azt kéri, hogy „elemezd, hogyan illusztráljuk / gondold át, hol kell kép”, először adj egy shot listet. Minden képnél tüntesd fel:

- Mely bekezdés után kerül
- A kép témája
- A fő gondolat
- Szerkezeti típus
- Mit csinál a KisFekete a képen
- Javasolt elemek
- Javasolt magyar megjegyzés-szavak

Alapértelmezés szerint 4-8 kép. Rövid cikknél 1-3 kép; hosszú cikknél se lépj túl könnyen a 9 képen. Ami elegendő, az elég, kerüld el, hogy a cikkből képes album legyen.

### 3. Egyedi generálás

Ha a felhasználó egyértelműen „generálj / készíts / rajzolj / segíts legenerálni” kérést fogalmaz meg, ne állj meg megerősítésre várva; a beépített `image_gen` segítségével generáld egyenként a képeket. Ne fűzz több képet egyetlen képpé.

Minden kép csak egyetlen alapvető szerkezetet mutasson be. A promptnak tartalmaznia kell:

- 16:9 fekvő tájolású magyar cikkillusztráció
- Tiszta fehér háttér
- Fekete kézrajzolt vonalrajz
- Kevés piros/narancs/kék magyar kézzel írt megjegyzés
- Sok üresen hagyott tér
- A KisFekete mint a központi cselekvő szereplő
- Tiltott: PPT, kereskedelmi illusztráció, gyerekes-aranyos, bonyolult architektúra, bal felső sarokban típuscím

Ne másold a korábbi példákat. A példák csak a stílusűrítést és a KisFekete részvételi módját adják meg, nem lehet egy az egyben újrahasználni a „szállítószalag-töréspont / KisFekete húzza a madzagot / hal-alkatrészek / bélyegzőszerszámosláda / gyakori buktatók útvonala” és más már létező kompozíciókat, hacsak a felhasználó nem kéri egyértelműen egy adott kép újraalkotását. Minden alkalommal az aktuális cikkből indulva találj ki egy új, bizarr, de logikus metaforát.

### 4. Ellenőrzés és iteráció

Generálás után vizsgáld át a `references/qa-checklist.md` szerint. Ha az alábbi problémák valamelyike jelentkezik, előnyben részesítsd az újragenerálást vagy a helyi szerkesztést:

- A KisFekete csak díszít
- A kép túl zsúfolt
- Túl hasonlít egy folyamatábrára/PPT-re
- Túl sok a magyar szöveg, vagy sok a hibás írásmód
- A bal felső sarokban „gyakori buktatók / folyamatábra / rendszerarchitektúra-diagram” stb. cím jelenik meg
- A stílus túl aranyos, gyerekes, merev
- A háttér nem tiszta fehér

### 5. Mentés és átadás

Ha a felhasználó a workspace-en belül dolgozik, másold a végleges képeket ide:

```text
assets/<article-slug>-illustrations/
```

Számozás szerinti elnevezés:

```text
01-topic-name.png
02-topic-name.png
```

Őrizd meg az eredeti generált fájlokat, ne írd felül a meglévő eszközöket, hacsak a felhasználó nem kéri egyértelműen a cserét.

## Kimeneti szabályok

A generálás előtti stratégia-kimenet legyen rövid és pontos. A generálás utáni átadás tartalmazza:

- Hány kép készült
- Minden kép felhasználási célja
- Mentési útvonal
- Mely képek a legstabilabbak, melyek opcionálisak

Ne adj hosszú elméleti stíluszű magyarázatot; hagyd, hogy a képek magukért beszéljenek.
