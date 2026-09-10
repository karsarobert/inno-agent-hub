# Ítéletkalkulus — hallgatói jegyzet

**Diszkrét matematika I. · 1. gyakorlat · programtervező informatikus BSc**

Az első gyakorlaton megtanuljuk felismerni az ítéleteket, használni a „nem”, „és”, „vagy” műveletét, valamint értelmezni a „ha…, akkor…” állításokat. A feladatok megoldásához nem szükséges programozási előismeret.

## 1. Miért tanulunk logikát?

A logika segít pontosan megfogalmazni és ellenőrizni az állításainkat. Például a „Ha esik az eső, viszek esernyőt” és a „Ha nincs meg a fájl, hibaüzenet jelenik meg” más helyzetről szól, de ugyanazt a logikai szerkezetet követi.

Először megértjük a mondat jelentését és rögzítjük a helyzetet. Ezután a logikai szerkezetét vizsgáljuk: milyen állításokból áll, és hogyan függ az egész igazságértéke a részek igazságértékétől? A formalizálás során nem szabad elveszíteni vagy önkényesen hozzátenni feltételeket.

A számítógépes rendszerekben is szerepelnek ilyen feltételek: van-e jogosultság, létezik-e egy fájl, teljesül-e legalább az egyik követelmény. Most ezeket szavakkal és egyszerű jelekkel vizsgáljuk.

## 2. Ítélet és igazságérték

**Ítélet** az olyan kijelentő mondattal kifejezett állítás, amelynek a rögzített értelmezésben egyértelmű igazságértéke van: igaz vagy hamis. A klasszikus, kétértékű logikában pontosan az egyik igazságérték tartozik hozzá.

Jelöléseink: **i = igaz**, **h = hamis**.

| Mondat | Ítélet? | Magyarázat |
|---|---|---|
| „A 250 osztható 5-tel.” | Igen, igaz. | Ellenőrizhető számtani állítás. |
| „A 7 páros.” | Igen, hamis. | A hamis állítás is ítélet. |
| „A lezárt dobozban pontosan három ceruza van.” | Igen, ha egy konkrét dobozról beszélünk. | Attól még van igazságértéke, hogy most nem nézhetünk bele. |
| „Hány ceruza van a dobozban?” | Nem. | Kérdés: választ vár, nem állít valamit. |
| „Tegyél három ceruzát a dobozba!” | Nem. | Felszólítás. |
| „n páros.” | Önmagában nem. | Nem rögzítettük, melyik egész számot jelöli n. |

**Fontos:** az igazságérték létezése és az igazságérték ismerete két külön dolog. A doboz tartalmát nem ismerjük, de a mondat egy konkrét helyzetről szól. Az „n páros” esetében viszont még nem jelöltünk ki egy számot. Ez **nyitott állítás**; n = 4 helyettesítéssel igaz, n = 5 helyettesítéssel hamis állítást kapunk.

Ugyanezért a „program 10 másodperc alatt lefut” mondatnál rögzíteni kell, melyik programról, milyen bemenetről és futtatási környezetről beszélünk. Az „ezen a gépen, ezzel a bemenettel elindított konkrét futás 10 másodpercen belül befejeződött” már kellően körülhatárolt állítás.

### Prímítélet és összetett ítélet

Az ítéletkalkulusban logikai műveletekkel kapcsolunk össze ítéleteket. Az adott felbontásban tovább nem bontott építőelemeket **prímítéleteknek** vagy atomoknak nevezzük, és például A, B, C betűkkel jelöljük.

Legyen A: „Nyitva van az ablak”, B: „Ég a lámpa”. Az „Nyitva van az ablak, és ég a lámpa” összetett ítélet. A jelölések bevezetésekor mindig írd le, melyik betű mit jelent!

## 3. Negáció: az állítás tagadása

**¬A** olvasata: „nem A”. Akkor igaz, amikor A hamis, és akkor hamis, amikor A igaz.

| A | ¬A |
|---|---|
| i | h |
| h | i |

Például „A 7 prímszám” tagadása: „A 7 nem prímszám”. Az első igaz, a második hamis; a tagadást attól még helyesen fogalmaztuk meg, hogy hamis mondatot kaptunk.

A tagadás nem egyszerűen egy ellentétes jelentésű szó keresése. „A válaszidő 100 ms-nál kisebb” tagadása: **„A válaszidő legalább 100 ms.”** Pontosan 100 ms-nál már hamis az eredeti állítás. A „100 ms-nál nagyobb” ezért nem jó tagadás: kihagyná a határesetet. Itt feltételezzük, hogy van meghatározott, számmal kifejezett válaszidő.

Köznyelvi példán: „A vizsga nehéz volt” tagadása „A vizsga nem volt nehéz”, nem feltétlenül „A vizsga könnyű volt”. Ezt csak a „nehéz” adott helyzetben rögzített értelmezése mellett használjuk.

## 4. Konjunkció: mindkettő

**A ∧ B** olvasata: „A és B”. Pontosan akkor igaz, ha **mindkét tag igaz**.

| A | B | A ∧ B |
|---|---|---|
| i | i | i |
| i | h | h |
| h | i | h |
| h | h | h |

Ha A azt jelenti, hogy nyitva van az ablak, B pedig azt, hogy ég a lámpa, akkor A ∧ B csak akkor igaz, ha mindkettőt megfigyelhetjük. Egyetlen hamis tag elég ahhoz, hogy az egész konjunkció hamis legyen.

## 5. Diszjunkció: legalább az egyik

**A ∨ B** olvasata: „A vagy B”, **megengedő értelemben**. Akkor igaz, ha legalább az egyik tag igaz; abban az esetben is, ha mindkettő igaz.

| A | B | A ∨ B |
|---|---|---|
| i | i | i |
| i | h | i |
| h | i | i |
| h | h | h |

Példa: „A jelentkezéshez angol vagy német nyelvtudás szükséges; mindkettő is elfogadható.” Legyen A: „A jelentkező tud angolul”, B: „A jelentkező tud németül”. Az előírt nyelvi feltételt A ∨ B írja le. Aki mindkét nyelven tud, az is teljesíti ezt a feltételt.

### Megengedő és kizáró „vagy”

A **kizáró vagy** pontosan az egyik tag igazságát engedi meg. Például: „A két választható időpont közül pontosan egyet jelölhetsz meg.” Legyen A: „Bejelölted az első időpontot”, B: „Bejelölted a másodikat”. A megfelelő kitöltés feltétele csak akkor teljesül, ha egy jelölés van; nulla vagy két jelölésnél nem.

| A | B | Legalább az egyik | Pontosan az egyik |
|---|---|---|---|
| i | i | i | h |
| i | h | i | i |
| h | i | i | i |
| h | h | h | h |

**A különbséget a két igaz tag esete mutatja meg.** Egy igaz és egy hamis tag mellett a kétféle „vagy” ugyanazt adja.

A köznyelvi mondat szándéka nem mindig egyértelmű. Ilyenkor érdemes megkérdezni: „Mindkettő megengedett, vagy pontosan az egyiket kell választani?” A feladatban szereplő ∨ jel viszont mindig megengedő vagyot jelent.

**Választható kitekintés:** a kizáró vagy új jel nélkül is kifejezhető: `(A ∨ B) ∧ ¬(A ∧ B)`. Az első rész legalább egy igaz tagot kér, a második kizárja a két igaz tagot. Ennek önálló előállítása nem követelmény az első gyakorlaton.

## 6. Hogyan készítsünk igazságtáblázatot?

Az igazságtáblázat a változók **összes lehetséges igazságérték-kombinációjához** megadja a formula értékét. A formula itt az állítás logikai szerkezetének jelekkel leírt alakja; a formális szintaktikai definíció későbbi téma.

**Kidolgozott példa:** `(¬A) ∧ B`.

1. Két változónk van: A és B. Mindkettő két értéket vehet fel, ezért négy kombinációt vizsgálunk.
2. Következetesen felsoroljuk ezeket: (i, i), (i, h), (h, i), (h, h).
3. Külön oszlopban kiszámítjuk ¬A értékét.
4. Az utolsó oszlophoz már ¬A és B értékét kapcsoljuk össze „és”-sel.

| A | B | ¬A | (¬A) ∧ B |
|---|---|---|---|
| i | i | h | h |
| i | h | h | h |
| h | i | i | i |
| h | h | i | h |

A harmadik sorban A hamis, ezért ¬A igaz; B is igaz, tehát a konjunkció igaz. A formula azt mondja: **A nem teljesül, B viszont teljesül.**

Más sorrendben is felsorolhatod a sorokat, ha minden kombináció pontosan egyszer szerepel. A közös munka megkönnyítésére ezen az órán a fenti sorrendet használjuk.

### Mire vonatkozik a tagadás?

`(¬A) ∧ B` és `¬(A ∧ B)` különböző állítás:

- `(¬A) ∧ B`: „A nem igaz, B pedig igaz.”
- `¬(A ∧ B)`: „Nem igaz, hogy A és B egyszerre igaz.”

Legyen A = i és B = h. Ekkor `(¬A) ∧ B = h ∧ h = h`, míg `¬(A ∧ B) = ¬h = i`.

**A zárójel jelzi, mire vonatkozik a tagadás.** A példákban szükség esetén kiírjuk a zárójeleket. A ¬A ∧ B szokásos olvasata (¬A) ∧ B, mert a negáció erősebben köt.

## 7. Implikáció: „ha…, akkor…”

**A → B** olvasata: „ha A, akkor B”. A az **előtag**, B az **utótag**. A klasszikus logikában az implikáció **pontosan akkor hamis, ha A igaz, B pedig hamis**.

| A | B | A → B |
|---|---|---|
| i | i | i |
| i | h | h |
| h | i | i |
| h | h | i |

Gondolj erre a vállalásra: „Ha esik az eső, viszek esernyőt.” Egy konkrét alkalmat vizsgálunk.

- Esik, és van nálam esernyő: a vállalásnak megfelel az eset.
- Esik, de nincs nálam esernyő: **ez sérti a vállalást**, a formula hamis.
- Nem esik, de van nálam esernyő: a vállalás ezt nem tiltja, a formula igaz.
- Nem esik, és nincs nálam esernyő: ezt sem tiltja, a formula igaz.

Az ígéret hasonlata az egyetlen hamis eset megjegyzését segíti. A logikai implikáció pontos jelentését az igazságtáblája adja. Nem állítja, hogy A ténylegesen teljesül, és önmagában nem fejez ki oksági kapcsolatot vagy időrendet.

### „Ha” és „csak akkor, ha”

A következő mondatok ugyanazt az A → B formulát fejezik ki:

- „Ha A, akkor B.”
- „A csak akkor teljesül, ha B teljesül.”
- „B szükséges feltétele A-nak.”

Példa: „Csak akkor megyek kirándulni, ha elkészültem a feladattal.” Legyen K: „Kirándulni megyek”, E: „Elkészültem a feladattal”. A formula **K → E**: kizárjuk azt, hogy kirándulni menjek úgy, hogy a feladattal nem készültem el. A feladat elkészülése önmagában még nem jelenti azt, hogy kirándulni is megyek.

Ugyanezt jelenti más szórenddel: „A feladat elkészülése szükséges a kirándulásomhoz.” **A jelentést figyeld, ne a mondatrészek sorrendjét!**

Az első gyakorlat közös minimuma a „ha A, akkor B” értelmezése és hamis esetének indoklása. A „csak akkor” fordulat további gyakorlása az óra utáni feladatok része is lehet.

## 8. A köznyelvi „és” — rövid kitekintés

A kötőszó felismerése önmagában nem elég a formalizáláshoz.

- „Szeretem a csokoládét, de nem szeretem a kelkáposztát”: a „de” két állítást kapcsol össze, logikai szempontból konjunkciót fejez ki.
- „Péter és Pál szomszédok”: a két ember közötti kapcsolatról szól. Nem kapjuk meg a jelentését a „Péter szomszéd” és „Pál szomszéd” mondatok összekapcsolásával.
- „Elmentettem a dokumentumot, majd bezártam a programot”: két eseményt és a sorrendjüket is közli. A konjunkció kifejezheti, hogy mindkét esemény megtörtént, de **a sorrendet önmagában nem őrzi meg**.

## 9. Gyakori hibák

1. A hamis állítást nem ítéletnek tekintjük. Pedig a hamis is igazságérték.
2. Összekeverjük az ismeretlen igazságértéket a nyitott állítással.
3. A negáció helyett „ellentétes” szót keresünk, vagy kihagyjuk a határesetet.
4. A megengedő vagyot két igaz tag mellett hamisnak vesszük.
5. Nem figyeljük, mire vonatkozik a tagadás.
6. Az implikációt hamis előtag esetén hamisnak vagy értelmetlennek tekintjük.
7. A → B helyett B → A-t vizsgálunk, vagy a szórend alapján választunk irányt.

## 10. Önellenőrzés

Előbb válaszolj saját szavaiddal, majd ellenőrizd a válaszokat!

1. Miért ítélet a „9 páros” mondat?
2. Miben különbözik az „n páros” a konkrét, lezárt doboz tartalmáról szóló állítástól?
3. Mikor igaz A ∧ B? Mikor hamis A ∨ B?
4. Melyik eset különbözteti meg a megengedő és a kizáró vagyot?
5. Mikor hamis A → B?
6. Miért kell figyelni a zárójelekre a tagadásnál?

<details>
<summary>Rövid válaszok — a saját válaszod után nyisd ki</summary>

1. Mert kijelentés és meghatározott igazságértéke van: hamis.
2. Az elsőben nincs kijelölve egy szám. A második konkrét helyzetre vonatkozik, csak mi nem ismerjük az igazságértékét.
3. A ∧ B akkor igaz, ha mindkét tag igaz; A ∨ B akkor hamis, ha mindkét tag hamis.
4. A = i, B = i. A megengedő vagy igaz, a kizáró vagy hamis.
5. Ha A igaz, B hamis.
6. Mert mást jelent egyetlen tagot és az egész összetett állítást tagadni.

</details>

## 11. Választható kitekintések

**Paradoxon:** „Ez a mondat hamis.” A klasszikus kétértékű keretben nem rendelhetünk hozzá következetesen igazságértéket. Az önhivatkozó mondat és egy egyszerűen hamis ítélet nem ugyanaz. A paradoxon részletes elemzése nem az első óra követelménye.

**Programozási kapcsolat:** C++-ban logikai értékeken a tagadás jele `!`, az és jele `&&`, a megengedő vagy jele `||`. Ezek kötési sorrendje nem → és → vagy, a szokásos logikai jelöléshez hasonlóan. A zárójelek mindkét jelölésben segítenek. A beépített C++-operátorok rövidzáras kiértékelése külön programozási sajátosság, amelyre később térünk vissza.

## Források és a gyakorlat határa

- Kátai-Urbán Kamilla: [Diszkrét matematika I., 1. előadás — Ítéletkalkulus](https://www.math.u-szeged.hu/~katai/dimat1_24/DMI1-Ea01-Log1_24.pdf), különösen a 7–14. dia. A jelen jegyzet önálló, gyakorlathoz igazított feldolgozás, további saját példákkal.
- Dormán Miklós, Kátai-Urbán Kamilla: [Előadásvázlat](https://www.math.u-szeged.hu/~katai/dimat1_jegyzet/DisMatInf1-Elm.pdf).
- A programozási kitekintéshez: [C++ logikai ÉS](https://eel.is/c++draft/expr.log.and) és [logikai VAGY](https://eel.is/c++draft/expr.log.or).

A formula formális szintaxisa, részformulák, ekvivalenciák, normálformák, predikátumkalkulus és halmazelmélet későbbi gyakorlatok témái. A kitekintések nem bővítik az első óra kötelező követelményeit.
