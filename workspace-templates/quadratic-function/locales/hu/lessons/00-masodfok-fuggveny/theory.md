# Másodfokú függvény — elméleti jegyzet

**Téma:** az f(x) = x² függvény, grafikonja és jellemzése · **9. évfolyam**

> Ez a jegyzet az órai munkához és az otthoni gyakorláshoz készült. Olvasd el lépésről lépésre, és közben rajzolj is!

---

## 1. Mi az a másodfokú függvény?

A **másodfokú függvény** olyan függvény, amelyben a változó **négyzete** szerepel. Ezen az órán a legegyszerűbb másodfokú függvénnyel ismerkedünk meg:

$$f(x) = x^2$$

**Hol találkozol vele a valóságban?**
- Egy négyzet területe az oldalhossz négyzete: T(a) = a².
- A feldobott labda (vagy vízsugár) röppályája parabola alakú.
- A szabadesés közben megtett út az eltelt idő négyzetével arányos.

> 💡 **Tipp:** ha valami „négyzetesen nő", az azt jelenti, hogy a kétszereséből négyszeres, a háromszorosából kilencszeres lesz. Ezt láthatod az alábbi táblázatban is!

---

## 2. Az értéktáblázat

A függvény ábrázolásához először kiszámoljuk néhány x értékhez a függvényértéket.

| x | −3 | −2 | −1 | 0 | 1 | 2 | 3 |
|---|---|---|---|---|---|---|---|
| **f(x) = x²** | 9 | 4 | 1 | 0 | 1 | 4 | 9 |

📌 **Figyeld meg!** A táblázat **szimmetrikus**: a −3-hoz és a 3-hoz ugyanaz (9) tartozik, a −2-höz és a 2-höz ugyanaz (4), stb. Ez nem véletlen, később visszatérünk rá!

---

## 3. A grafikon megrajzolása (3 lépés)

**1. lépés:** készíts értéktáblázatot (mint fent).

**2. lépés:** a kapott (x; f(x)) pontokat jelöld be a koordináta-rendszerben:
(−3; 9), (−2; 4), (−1; 1), (0; 0), (1; 1), (2; 4), (3; 9).

**3. lépés:** kösd össze a pontokat **sima, kanyargó görbével** — *nem* egyenes szakaszokkal!

```
          y
          │
        9 │        •
          │      •   •
        4 │    •       •
          │  •           •
        1 │ •             •
          │•               •
    ──────┼────────────────────→ x
        −3 −2 −1  0  1  2  3
```

**Miért nem egyenes?** Mert a függvény *nem egyenletesen* nő: 0-tól 1-ig csak 1-et lép, 2-től 3-ig viszont már 5-öt. Nézzük meg közelebbről a 0 és 3 közötti részt fél egységenként:

| x | 0 | 0,5 | 1 | 1,5 | 2 | 2,5 | 3 |
|---|---|---|---|---|---|---|---|
| **f(x) = x²** | 0 | 0,25 | 1 | 2,25 | 4 | 6,25 | 9 |

A lépések egyre nagyobbak (0,25 → 0,75 → 1,25 → 1,75 → 2,25 → 2,75) — ettől lesz a görbe **egyre meredekebb**, és ettől ível a parabola.

📌 **A grafikon neve: PARABOLA.** A legmélyebb pontja (0; 0) a **csúcspont**.

---

## 4. A függvény jellemzése

A jellemzés = a grafikonról leolvasható, pontos megfigyelések összefoglalása. Az f(x) = x² esetén:

| Tulajdonság | Érték | Hogyan olvasod le a rajzról? |
|---|---|---|
| **Értelmezési tartomány** (milyen x-ekhez tartozik pont) | ℝ (minden valós szám) | A grafikon a teljes x-tengely fölött végigfut |
| **Értékkészlet** (milyen f(x) értékek fordulnak elő) | [0; ∞) | A grafikon sosem megy az x-tengely alá |
| **Csúcspont** | (0; 0) | A parabola legalsó pontja |
| **Tengelyes szimmetria** | az y tengelyre | A grafikon az y tengely mentén „összecsukva" fedésbe kerül |
| **Monotonitás** | x < 0 esetén **csökkenő**, x > 0 esetén **növekvő** | Bal oldalon lefelé halad, jobb oldalon felfelé |
| **Szélsőérték** | **minimum** 0, a helye x = 0 | A legkisebb érték a csúcspontban van |

> ⚠️ **Vigyázz!** A függvénynek **minimuma** van (a „völgy" alja), nem maximuma! És az értelmezési tartomány nem a nemnegatív számok halmaza — negatív x-ekre is számolunk értéket!

---

## 5. Kidolgozott mintapéldák

### 1. példa: Ábrázolás és jellemzés
Az ábrázolás és a jellemzés lépéseit a 2–4. részben láttad. Gyakorold te is: milliméterpapírra rajzold meg a parabolát, majd írd mellé a jellemzést!

### 2. példa: Rajta van-e a pont a grafikonon?
*Rajta van-e a (2; 4), a (−3; −9) és az (5; 25) pont a grafikonon?*

**Módszer: helyettesíts be!** Egy (a; b) pont akkor van a grafikonon, ha f(a) = b.

- (2; 4): f(2) = 2² = 4 ✓ → **rajta van**
- (−3; −9): f(−3) = (−3)² = 9, és 9 ≠ −9 ✗ → **nincs rajta** (a −9 nem lehet függvényérték, hiszen az értékkészlet [0; ∞))
- (5; 25): f(5) = 5² = 25 ✓ → **rajta van**

### 3. példa: Mely x-ekre igaz, hogy x² = 4?
Rajzold meg a parabolát, és húzd be az y = 4 egyenest! A metszéspontok x koordinátái a megoldások:

- A vízszintes egyenes két pontban metszi a parabolát: (−2; 4) és (2; 4).
- Tehát x = −2 **vagy** x = 2. (Ellenőrzés: (−2)² = 4 és 2² = 4 ✓)

> 💡 **Tipp:** egy vízszintes egyenes általában **két** helyen metszi a parabolát — ez a szimmetria miatt van!

---

## 6. Vigyázz! A leggyakoribb hibák

| Hiba | Jó megoldás | Miért? |
|---|---|---|
| (−3)² = −9 | (−3)² = **9** | (−3)² = (−3) · (−3) = 9. Két negatív szám szorzata pozitív! |
| x² = 2x | x² ≠ 2x (csak x = 0 és x = 2 esetén egyenlő) | x² a szám *önmagával* szorzott értéke, a 2x a *kétszerese*. Pl. x = 3: 9 ≠ 6. |
| A parabola „V" alakú | Sima görbe, nincs törés a csúcspontnál | A V alak az abszolútérték-függvényre jellemző. A parabolánál nincs éles sarok! |
| Csak a jobb oldalt rajzolom meg | Negatív x-ekre is kell a grafikon! | A függvény az egész ℝ-en értelmezve van, és a szimmetria miatt a bal oldal is fontos. |
| „A legnagyobb érték..." | A függvénynek **minimuma** van: a 0 | A parabola felfelé nyílik, a csúcspont a legalsó pont. |

---

## 7. Kulcsszavak (mini szószedet)

- **Másodfokú függvény:** olyan függvény, amelyben a változó négyzete szerepel (pl. f(x) = x²).
- **Értéktáblázat:** táblázat, amelyben megadott x értékekhez kiszámoljuk az f(x) értékeket.
- **Parabola:** a másodfokú függvény grafikonjának neve („kanyar" alakú görbe).
- **Csúcspont:** a parabola legmélyebb (vagy legmagasabb) pontja; itt: (0; 0).
- **Tengelyes szimmetria:** a grafikon egy egyenes mentén „összecsukva" önmagára illeszkedik; itt: az y tengelyre.
- **Értelmezési tartomány:** azok az x értékek, amelyekre a függvényt értelmezzük (itt: ℝ).
- **Értékkészlet:** azok az f(x) értékek, amelyeket a függvény felvesz (itt: [0; ∞)).
- **Monotonitás:** a függvény növekedésének/csökkenésének leírása (itt: x < 0-nál csökkenő, x > 0-nál növekvő).
- **Szélsőérték (minimum):** a függvény legkisebb értéke (itt: 0, az x = 0 helyen).

---

*Készült a „A másodfokú függvény — bevezető óra" óraterv tanulói változataként.*
