# Ítéletkalkulus — gyakorlófeladatok

> Gyakorlatsor a Diszkrét matematika 1. – 1. óra (ítéletkalkulus) anyagához.
> A feladatok a `theory.md` jegyzetre épülnek. A megoldókulcs a lap VÉGÉN van —
> csak a saját megoldásod után nézd meg!

---

## Alap szint

**1. Feladat.** Döntsd el az alábbi mondatokról, hogy ítéletek-e vagy sem!

(a) „Budapest Magyarország fővárosa."

(b) „Milyen idő lesz holnap?"

(c) „$x + 3 = 7$."

(d) „Ez a mondat hamis."

**2. Feladat.** Fogalmazd meg az alábbi ítélet **negációját** magyarul:

> „Minden diák szereti a logikát."

**3. Feladat.** Legyen $A = \mathrm{i}$ (igaz) és $B = \mathrm{h}$ (hamis). Számítsd ki az alábbi összetett ítéletek igazságértékét!

(a) $\neg A$

(b) $A \wedge B$

(c) $A \vee B$

(d) $A \rightarrow B$

(e) $A \leftrightarrow B$

**4. Feladat.** Készítsd el a $\neg(A \wedge B)$ formula igazságtáblázatát!

---

## Fejlesztő szint

**5. Feladat.** Formalizáld (írd fel ítéletváltozókkal) a következő ítéletet:

> „Ha esik az eső, akkor viszek esernyőt."

**6. Feladat.** Formalizáld a következő ítéletet! (Figyelj: a „csak akkor … ha" az implikáció irányát adja meg.)

> „Csak akkor megyek strandra, ha süt a nap."

**7. Feladat.** Írd fel a De Morgan-azonosságokat, és alkalmazd őket: írd fel az alábbi formulák ekvivalens alakját negáció nélküli kötőszóval a zárójelen belül!

(a) $\neg(A \vee B)$

(b) $\neg(A \wedge B)$

**8. Feladat.** Igazságtáblázattal igazold, hogy

$$A \rightarrow B \ \equiv \ \neg A \vee B.$$

**9. Feladat.** Döntsd el az alábbi formulákról, hogy **tautológiák**, **ellentmondások**, vagy egyik sem!

(a) $A \vee \neg A$

(b) $A \wedge \neg A$

(c) $(A \rightarrow B) \leftrightarrow (\neg B \rightarrow \neg A)$

---

## Bővítő szint

**10. Feladat.** Formalizáld a következő (bonyolultabb) ítéletet! Vezesd be a prímítéleteket, és írd fel a formulát!

> „Ha a vizsga nehéz, és nem tanultam, akkor pontosan akkor megyek át, ha a pótvizsga könnyű."

**11. Feladat.** Írd fel az $F = A \rightarrow B$ formula **teljes diszjunktív normálformáját (TDNF-jét)** az igazságtáblázata alapján!

**12. Feladat.** Igazold (igazságtáblázattal vagy ekvivalenciákkal), hogy a *modus ponens* séma tautológia:

$$\bigl(A \wedge (A \rightarrow B)\bigr) \rightarrow B.$$

---

# Megoldókulcs

## 1. Feladat

- (a) **Igen**, ítélet (igaz, és ez eldönthető).
- (b) **Nem**, kérdő mondat — nincs igazságértéke.
- (c) **Nem**, mert $x$-től függ, nincs meghatározott igazságértéke (ítéletváltozó lenne).
- (d) **Nem**, önellentmondó (ha igaz, akkor hamis, és fordítva).

## 2. Feladat

> „Van olyan diák, aki **nem** szereti a logikát."
(Illetve: „Nem minden diák szereti a logikát.")

## 3. Feladat

(a) $\neg A = \mathrm{h}$ (b) $A \wedge B = \mathrm{h}$ (c) $A \vee B = \mathrm{i}$
(d) $A \rightarrow B = \mathrm{h}$ (csak akkor hamis, ha $A$ igaz és $B$ hamis)
(e) $A \leftrightarrow B = \mathrm{h}$ (különböző igazságértékűek)

## 4. Feladat

| $A$ | $B$ | $A \wedge B$ | $\neg(A \wedge B)$ |
|-----|-----|--------------|---------------------|
| i | i | i | **h** |
| i | h | h | **i** |
| h | i | h | **i** |
| h | h | h | **i** |

## 5. Feladat

Legyen $A$: „Esik az eső.", $B$: „Visek esernyőt." A formula:

$$A \rightarrow B.$$

## 6. Feladat

Legyen $A$: „Megyek strandra.", $B$: „Süt a nap." A „csak akkor $A$, ha $B$" jelentése „ha $A$, akkor $B$", tehát:

$$A \rightarrow B.$$

(Fontos: **nem** $B \rightarrow A$!)

## 7. Feladat

$$\neg(A \wedge B) \equiv \neg A \vee \neg B, \qquad \neg(A \vee B) \equiv \neg A \wedge \neg B.$$

(a) $\neg(A \vee B) \equiv \neg A \wedge \neg B$

(b) $\neg(A \wedge B) \equiv \neg A \vee \neg B$

## 8. Feladat

| $A$ | $B$ | $A \rightarrow B$ | $\neg A$ | $\neg A \vee B$ |
|-----|-----|--------------------|-----------|------------------|
| i | i | i | h | i |
| i | h | h | h | h |
| h | i | i | i | i |
| h | h | i | i | i |

A két oszlop megegyezik, tehát $A \rightarrow B \equiv \neg A \vee B$. ✔

## 9. Feladat

- (a) $A \vee \neg A$: **tautológia** (a „kizárt harmadik" törvénye — mindig igaz).
- (b) $A \wedge \neg A$: **ellentmondás** (sohasem igaz).
- (c) $(A \rightarrow B) \leftrightarrow (\neg B \rightarrow \neg A)$: **tautológia** — a kontrapozíció, a két oldal mindig azonos igazságértékű.

## 10. Feladat

Prímítéletek:

- $A$: „A vizsga nehéz."
- $B$: „Tanultam."
- $C$: „Átmegyek."
- $D$: „A pótvizsga könnyű."

A formula („ha … és …, akkor pontosan akkor …, ha …"):

$$\bigl(A \wedge \neg B\bigr) \rightarrow \bigl(C \leftrightarrow D\bigr).$$

## 11. Feladat

Az $A \rightarrow B$ igazságtáblázata:

| $A$ | $B$ | $A \rightarrow B$ |
|-----|-----|--------------------|
| i | i | i |
| i | h | h |
| h | i | i |
| h | h | i |

A formula három sorban igaz: $(i,i)$, $(h,i)$, $(h,h)$. Minden i-sorhoz egy tag tart,
amelyben a $h$ értékű változókat negáljuk:

- $(i,i)$ → $A \wedge B$
- $(h,i)$ → $\neg A \wedge B$
- $(h,h)$ → $\neg A \wedge \neg B$

Tehát a TDNF:

$$A \rightarrow B \ \equiv\ (A \wedge B) \vee (\neg A \wedge B) \vee (\neg A \wedge \neg B).$$

## 12. Feladat

Ekvivalenciákkal:

$$A \wedge (A \rightarrow B) \ \equiv\ A \wedge (\neg A \vee B)\ \equiv\ (A \wedge \neg A) \vee (A \wedge B)\ \equiv\ A \wedge B.$$

Így $\bigl(A \wedge (A \rightarrow B)\bigr) \rightarrow B \equiv (A \wedge B) \rightarrow B$, és ez
**tautológia**: az implikáció csak akkor lenne hamis, ha az előtag igaz és az utótag
hamis, de ha $A \wedge B$ igaz, akkor $B$ is igaz. ✔
