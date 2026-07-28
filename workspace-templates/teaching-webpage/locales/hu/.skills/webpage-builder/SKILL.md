---
name: webpage-builder
description: Készíts tantermi nagykijelzőhöz illeszkedő, egyfájlos interaktív tanórai weboldalt (tudáselemek bemutatása / órai válaszadás / tanórai kérdezz-felelek / összegzés), beágyazott stílusokkal és szkriptekkel, offline megnyitható index.html kimenetként.
---

# Interaktív tanórai weboldal készítése

Amikor a felhasználó egy tanórához interaktív weboldalt szeretne készíteni, e készség szerint dolgozz.

## Kimenet

- **Egyetlen `index.html` fájl**, teljesen beágyazott CSS-sel és JS-sel, külső erőforrások nélkül (CDN, betűtípus, képhivatkozás: mindet be kell ágyazni vagy el kell hagyni), hogy az osztálytermi hálózat kiesése esetén is dupla kattintással megnyitható legyen.
- **Igazodjon a tantermi nagykijelzőhöz**: nagy alapszövegméret (törzsszöveg ≥ 20px, címek ennél nagyobbak), nagy kontrasztú színpaletta, kellően nagy gombok és kattintható területek, távolról olvasható és érintőképernyővel / egérrel kezelhető kialakítás.

## Oldalszerkezet (alapértelmezés szerint négy modul, igény szerint bővíthető vagy csökkenthető)

1. **Az óra tudáselemeinek bemutatása**: az óra kulcspontjai kártyákon vagy listán; elemenként kattintással kibontás / összecsukás.
2. **Órai interaktív feladatmodul**: több feleletválasztós / igaz-hamis kérdés; választás után azonnali helyes-helytelen kiemelés és rövid magyarázat, pontszám kijelzésével.
3. **Valós idejű tanórai kérdezz-felelek terület**: vitaindító kérdések, véletlen felszólítás, gyorsválasz-időmérő, visszaszámláló és hasonló tanórai segédeszközök (kizárólag frontend megvalósítással).
4. **Órai összegzés modul**: az óra záró kulcspontjai, összekapcsolva a tudáselemek bemutatásával.

## Megvalósítási megállapodások

- A négy modul között felső navigációval vagy szakaszhorgonyokkal lehessen váltani, hogy a tanár könnyen ugorhasson az órán.
- Az interakciók natív JS-sel készüljenek; elég a memóriában tárolt állapot (frissítéskor alaphelyzet), háttérrendszer nem szükséges.
- A feladatok és tudáselemek tartalmához elsőként a munkaterületen meglévő óratervet / magyarázó szöveget használd; ennek hiányában a felhasználó által adott témából készítsd el.
- A vizuális stílus (tipográfia / színvilág / animáció) kövesse a munkaterület `claude-design` készségét: válassz határozott esztétikai irányt, adj változatokat, kerüld a sablonos AI-hatást; közben tartsd meg a fenti „nagykijelzőn olvasható, könnyen kattintható” tantermi korlátokat.
- A strukturált elrendezéshez (diák / táblázatok / folyamatábrák / szakasznavigáció stb.) támaszkodhatsz a munkaterület `visual-explainer` készségének sablonjaira és CSS-mintáira.
- **Offline elsőbbség (szigorú tantermi korlát)**: a `claude-design` React/Babel módja unpkg CDN-t, a `visual-explainer` Mermaid-je jsdelivr CDN-t használ — a tanórai weboldal **alapértelmezés szerint ne használja ezeket a hálózati útvonalakat**, hanem tiszta CSS / HTML / SVG-t alkalmazzon; ha valóban kell könyvtár, a kódját **ágyazd be** az egyfájlos dokumentumba, hogy hálózat nélkül is megnyíljon.

## Interakció és animáció (céllal, nem díszítésként)

Az interakciónak és az animációnak **a megértést kell szolgálnia**, nem pusztán szépnek lennie. Döntési szabály: **ha eltávolítjuk, nehezebben értenék meg a tanulók? Igen → maradjon; nem → töröljük.**

**Javasolt (közvetlenül segíti a tanulást):**
- **Manipulálhatóság**: a tanulók módosíthatnak paramétereket / húzhatnak / választhatnak, és azonnal láthatják az eredményt — tanulás cselekvés közben.
- **Változás és folyamat megjelenítése**: mozgásról, átalakulásról, lépésekről vagy okságról szóló anyagnál animáció mutassa be a folyamatot.
- **Figyelemirányító jelzések**: kiemelés / fókusz vezesse a figyelmet az éppen tárgyalt elemre.
- **Azonnali visszajelzés**: a válasz helyessége vagy a kattintással felfedett megoldás adjon egyértelmű vizuális visszajelzést.

**Kerülendő (növeli a kognitív terhelést, elvonja a figyelmet):**
- Díszítő animációk: belépési effektek, részecskeháttér, értelmetlen átmenetek, puszta látványosság.
- Nem vezérelhető automatikus lejátszás: az animációnak **léptethetőnek / szüneteltethetőnek / újrajátszhatónak** kell lennie; a tanár vagy a tanuló szabályozza a tempót, ne fusson végig magától.

**Tantermi korlátok:**
- Nagykijelzőn olvasható: legyen nagy mozgás, távolról is látható; ne használj apró micro-interaction megoldásokat.
- Tiszta CSS / JS elegendő (illeszkedik az offline egyfájlos formához); gyenge gépeken óvatosan a nehéz WebGL-lel.

## Munkafolyamat

1. Azonosítsd az évfolyamot, a tantárgyat, a témát és az óra tudáselemeit (hiányos információ esetén előbb kérdezz rá).
2. Az `ask_user_question` segítségével adj a felhasználónak **többválasztós modul-listát** (tudáselemek bemutatása / interaktív dinamikus szemléltetés / órai feladatok / órai összegzés / valós idejű tanórai kérdezz-felelek / egyéni), amelyen kiválaszthatja a szükséges elemeket; ajánlhatsz opciókat, de a felhasználó választása a mérvadó. Csak a kijelölt modulokat hozd létre.
3. Készítsd el a teljes `index.html` fájlt, és írd az aktuális munkaterület gyökérkönyvtárába.
4. Közöld a felhasználóval a fájl helyét és a használat módját: „dupla kattintás a böngészőben → kivetítés a nagykijelzőre”.
