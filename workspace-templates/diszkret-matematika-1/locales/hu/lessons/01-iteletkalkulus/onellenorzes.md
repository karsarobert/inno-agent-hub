# Ítéletkalkulus — önellenőrzés

> Ellenőrizd a tudásodat az 1. óra (ítéletkalkulus) anyagából! Válaszolj
> előbb saját magad, és csak utána nézd meg a kulcsot a lap alján.

---

**1. Kérdés.** Definiáld röviden: mi az **ítélet**? Mi a **prímítélet**?

**2. Kérdés.** Pontosan mikor **hamis** az $A \rightarrow B$ implikáció?

**3. Kérdés.** Igaz-e a következő ekvivalencia?

$$A \leftrightarrow B \ \equiv\ (A \rightarrow B) \wedge (B \rightarrow A)$$

**4. Kérdés.** Írd fel a **De Morgan-azonosságokat** (mindkettőt)!

**5. Kérdés.** Az $F = \neg A \vee B$ formula igazságtáblázatának hány sora van, és
hány sorban **igaz** $F$?

**6. Kérdés.** Mi a **kontrapozíciója** az $A \rightarrow B$ formulának?

**7. Kérdés.** Formalizáld a következő ítéletet!

> „A napsütés szükséges feltétele a strandolásnak."

**8. Kérdés.** Tautológia-e az $A \leftrightarrow \neg A$ formula?

---

# Kulcs

**1.** Az ítélet olyan kijelentő mondat, amelynek **igazságértéke van** (vagy igaz,
vagy hamis, de a kettő egyszerre nem). A prímítélet (atom) tovább nem bontható,
nem összetett ítélet.

**2.** Pontosan akkor hamis, ha **$A$ igaz és $B$ hamis** (minden más esetben igaz).

**3.** Igen, ez az ekvivalencia definíció szerint igaz (a „↔" felbontása).

**4.** $\neg(A \wedge B) \equiv \neg A \vee \neg B$ és $\neg(A \vee B) \equiv \neg A \wedge \neg B$.

**5.** Két változó ($A$, $B$) van, ezért $2^2 = 4$ sora van. $F = \neg A \vee B$
(= $A \rightarrow B$) **3 sorban igaz**, és csak akkor hamis, ha $A = \mathrm{i}$ és
$B = \mathrm{h}$.

**6.** $\neg B \rightarrow \neg A$ („ha nem $B$, akkor nem $A$").

**7.** Legyen $S$: „Strandolok.", $N$: „Süt a nap." A „szükséges feltétel" az
implikáció irányát az utótag felől adja meg: $S \rightarrow N$.

**8.** Nem — ez **ellentmondás** (sohasem igaz), mert $A$ és $\neg A$ igazságértéke
mindig ellentétes.
