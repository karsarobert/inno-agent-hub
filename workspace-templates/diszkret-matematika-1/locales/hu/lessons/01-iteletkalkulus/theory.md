# Diszkrét matematika I. – 1. előadás: Ítéletkalkulus

> Részletes jegyzet az előadás alapján (Kátai-Urbán Kamilla, SZTE)
> Forrás: [[diszkr-t-matematika-i-1-el-ad-s-t-letkalkulus-k-ta-fdc354]]

---

## Tartalomjegyzék

1. [Tárgyi tudnivalók](#1-tárgyi-tudnivalók)
2. [Miről szól a matematikai logika?](#2-miről-szól-a-matematikai-logika)
3. [Ítéletek](#3-ítéletek)
4. [Összetett ítéletek és a logikai műveletek](#4-összetett-ítéletek-és-a-logikai-műveletek)
5. [Az igazságtáblázatok](#5-az-igazságtáblázatok)
6. [A logikai műveletek a hétköznapi nyelvben](#6-a-logikai-műveletek-a-hétköznapi-nyelvben)
7. [Az ítéletkalkulus formulái](#7-az-ítéletkalkulus-formulái)
8. [Részformulák](#8-részformulák)
9. [Ítéletek formalizálása](#9-ítéletek-formalizálása)
10. [Formula igazságtáblázata](#10-formula-igazságtáblázata)
11. [Logikai ekvivalencia és tautológia](#11-logikai-ekvivalencia-és-tautológia)
12. [Az alapvető logikai ekvivalenciák (tételgyűjtemény)](#12-az-alapvető-logikai-ekvivalenciák-tételgyűjtemény)
13. [Helyettesítési tételek](#13-helyettesítési-tételek)
14. [Teljes diszjunktív normálforma (TDNF)](#14-teljes-diszjunktív-normálforma-tdnf)
15. [E-teszt feladatok megoldásokkal](#15-e-teszt-feladatok-megoldásokkal)
16. [Összefoglaló táblázatok](#16-összefoglaló-táblázatok)
17. [Források és irodalom](#17-források-és-irodalom)

---

## 1. Tárgyi tudnivalók

**Előadó:** Kátai-Urbán Kamilla – e-mail: `katai@math.u-szeged.hu`
**Honlap:** `https://www.math.u-szeged.hu/~katai/dimat1_24/dm1ea24.html`

**Követelmények – vizsga** (120 pontos vizsgadolgozat):

| Pont | Érdemjegy |
|------|-----------|
| [0, 47] | elégtelen (1) |
| [48, 65] | elégséges (2) |
| [66, 83] | közepes (3) |
| [84, 101] | jó (4) |
| [102, 120] | jeles (5) |

**Követelmények – gyakorlat** (120 pont):
- **28 pont** elektronikus tesztekből – **minimum 11 pont** kötelező;
- **72 pont (36 + 36)** két zárthelyi dolgozatból;
- **20 pont** gyakorlati munka (a gyakorlatvezető által meghatározott módon);
- Legalább 4 hiányzás → „nem értékelhető”;
- Az egyik ZH javítható/pótolható, ha a teszteken legalább 11 pontot elértél;
- A gyakorlati jegy (≥ 2) vizsgajegyként is elfogadható (csak az adott félévben).

**Elektronikus tesztek:** `https://www.math.u-szeged.hu/~mmaroti/tests/` (az első teszt a 2. hét végén indul).

---

## 2. Miről szól a matematikai logika?

A **matematikai logika** (más néven **szimbolikus logika**) a gondolkodás *formális* szabályaival foglalkozik.

A „formális" itt azt jelenti, hogy **nem az állítások tényleges jelentése** érdekel bennünket, hanem:

- a **szerkezete**,
- az **igazságértéke**,
- a **gondolatmenet helyessége**.

A matematikai logika így a **matematika megalapozását** szolgálja. A logikai műveleteket a legtöbb programozási nyelv is tartalmazza.

---

## 3. Ítéletek

> **Definíció (ítélet, logikai érték / igazságérték).**
> **Ítéletnek** nevezünk egy olyan állítást (kijelentő mondatot), amely **vagy igaz, vagy hamis**, de a kettő egyidejűleg nem teljesülhet.
> Ha az ítélet igaz (vagy hamis), akkor azt mondjuk, hogy az ítélet **logikai értéke** (vagy **igazságértéke**) igaz (vagy hamis).
>
> Az ítélet tehát olyan állítás, **aminek igazságértéke van**.

**Példák:**

| Jel | Állítás | Ítélet? |
|-----|---------|---------|
| A | A Naprendszer harmadik bolygóján intelligens élet található. | ✅ igen (igazságértéke van, ha nem is tudjuk) |
| B | A $22^5 + 1$ természetes szám prímszám. | ✅ igen |
| C | Miért tanulunk logikát? | ❌ nem (kérdés, nincs igazságértéke) |
| D | Már most imádom a Diszkrét matematikát. | ✅ igen (lehet hamis 😉) |
| E | Most nem mondok igazat. | ❌ nem (önellentmondó: ha igaz, akkor hamis és fordítva) |

---

## 4. Összetett ítéletek és a logikai műveletek

A köznapi nyelvben és a matematikában is **kötőszavak** segítségével képezhetünk ítéletekből újabb ítéleteket.

**Példa.** Legyen „Süt a nap." és „Kimegyek az uszodába." két ítélet. Ekkor:

- **F:** Ha süt a nap, akkor kimegyek az uszodába.
- **G:** Kimegyek az uszodába, és süt a nap.
- **H:** Nem süt a nap.
- **I:** Csak akkor megyek ki az uszodába, ha süt a nap.
- **J:** Kimegyek az uszodába, vagy süt a nap.
- **K:** Akkor és csak akkor süt a nap, ha kimegyek az uszodába.

> **Definíció (összetett ítélet, prímítélet).**
> Tetszőleges $A$ és $B$ ítéletre definiáljuk az alábbi **összetett ítéleteket**:
>
> (a) $A$ **negációja** a „nem $A$" ítélet, jele: $\neg A$;
>
> (b) $A$, $B$ **konjunkciója** az „$A$ és $B$" ítélet, jele: $A \wedge B$;
>
> (c) $A$, $B$ **diszjunkciója** az „$A$ vagy $B$" ítélet, jele: $A \vee B$;
>
> (d) $A$, $B$ **implikációja** a „ha $A$, akkor $B$" ítélet, jele: $A \rightarrow B$;
>
> (e) $A$, $B$ **ekvivalenciája** az „akkor és csak akkor $A$, ha $B$" ítélet, jele: $A \leftrightarrow B$.
>
> Ha egy ítélet **nem összetett**, akkor **prímítételnek** nevezzük.

**Megjegyzések:**
- Az ítéletkalkulusban a prímítélet a *tovább nem bontható építőkő*, az **atom**.
- Az igaz és hamis logikai értéket a továbbiakban **i**, illetve **h** jelöli (sok helyen – pl. programozási nyelvekben – **1** és **0**).

---

## 5. Az igazságtáblázatok

> **Definíció.** Az öt logikai művelet igazságtáblázatai:

| $A$ | $\neg A$ |
|-----|----------|
| i | h |
| h | i |

| $A$ | $B$ | $A \wedge B$ | $A \vee B$ | $A \rightarrow B$ | $A \leftrightarrow B$ |
|-----|-----|--------------|------------|-------------------|------------------------|
| i | i | i | i | i | i |
| i | h | h | i | h | h |
| h | i | h | i | i | h |
| h | h | h | h | i | i |

**Kulcsgondolatok (érdemes megjegyezni):**

| Művelet | Mikor igaz? |
|---------|-------------|
| $\neg A$ | akkor és csak akkor, ha $A$ hamis |
| $A \wedge B$ | **akkor és csak akkor, ha mindkét tag igaz** |
| $A \vee B$ | **akkor és csak akkor hamis, ha mindkét tag hamis** (egyébként igaz) |
| $A \rightarrow B$ | **akkor és csak akkor hamis, ha az előtag ($A$) igaz és az utótag ($B$) hamis** (egyébként igaz) |
| $A \leftrightarrow B$ | akkor és csak akkor, ha $A$ és $B$ **azonos** igazságértékű |

---

## 6. A logikai műveletek a hétköznapi nyelvben

### 6.1. A konjunkció és a hétköznapi nyelv

A köznapi nyelvben az „és" **nem mindig** fejez ki konjunkciót, és a konjunkciót **nem csak az „és"** fejezheti ki.

| Mondat | Konjunkció? | Miért? |
|--------|-------------|--------|
| **L:** Péter és Pál szomszédok. | ❌ | Külön-külön nem mondhatjuk, hogy „Péter szomszéd" – nem bontható szét |
| **M:** Péter és Pál haragtartó. | ✅ | Csak rövidítése ennek: „Péter haragtartó **és** Pál haragtartó." |
| **N:** Péter elmegy a sarokig és balra fordul. | ❌ | **Időrendiséget** fejez ki, nem logikai és-t |
| **O:** Szeretem a csokoládét, de utálom a kelkáposztát. | ✅ | A „de" helyettesíthető „és"-sel |

### 6.2. A diszjunkció és a hétköznapi nyelv (megengedő vs. kizáró vagy)

A matematikában a „vagy" kötőszót **mindig megengedő** értelemben használjuk: *akár mind a kettő is megtörténhet*.

- **P:** Kávét hoz, **vagy** álmos. → *Megengedő vagy*: akár mindkettő is igaz lehet.
- **Q:** Gyalog megy, **vagy** biciklizik. → *Kizáró vagy*: csak az egyik történhet meg.

> **Fontos!** A **kizáró vagy** (XOR) nem új logikai művelet. Az „$A$ kizáró vagy $B$" ítélet alatt igazából ezt értjük:
>
> $$(A \vee B) \wedge \bigl(\neg(A \wedge B)\bigr)$$

### 6.3. Az implikáció szöveges változatai

A következő ítéletek **mind ugyanazt jelentik**:

- „ha $A$, akkor $B$";
- „csak akkor $A$, ha $B$";
- „$B$ szükséges feltétele $A$-nak";
- „$A$-ból következik $B$".

**Példa** („uszodába megyek" = A, „süt a Nap" = B):

| Jel | Mondat | Jelentés |
|-----|--------|----------|
| R | Ha uszodába megyek, akkor süt a Nap. | $A \rightarrow B$ |
| S | Csak akkor megyek az uszodába, ha süt a Nap. | $A \rightarrow B$ |
| T | A napsütés szükséges feltétele az uszodába menésnek. | $A \rightarrow B$ |
| U | Uszodába megyek, ebből az következik, hogy süt a Nap. | $A \rightarrow B$ |

### 6.4. Az ekvivalencia szöveges változatai

A következő ítéletek **mind ugyanazt jelentik**:

- „akkor és csak akkor $A$, ha $B$";
- „pontosan akkor $A$, ha $B$";
- „$A$-nak szükséges és elegendő feltétele $B$";
- „$A$ ekvivalens $B$-vel".

**Példa** (párosság ↔ 2-vel való oszthatóság):

- **V:** Egy egész szám akkor és csak akkor páros, ha osztható 2-vel.
- **W:** Egy egész szám pontosan akkor páros, ha osztható 2-vel.
- **X:** Egy egész szám párosságának szükséges és elegendő feltétele a 2-vel való oszthatóság.
- **Y:** Egy egész szám párossága ekvivalens a 2-vel való oszthatóságával.

---

## 7. Az ítéletkalkulus formulái

> **Definíció (formula).** **Ítéletváltozónak** nevezzük az olyan változókat, amelyek prímítéleteket jelölnek ($A_1, A_2, \dots, A_n, \dots$).
> Az ítéletkalkulus **formulái** a következők:
>
> (a) az $A_1, \dots, A_n, \dots$ ítéletváltozók **mindegyike formula**;
>
> (b) ha $F$ és $G$ formula, akkor $(\neg F)$, $(F \wedge G)$, $(F \vee G)$, $(F \rightarrow G)$, $(F \leftrightarrow G)$ **mindegyike formula**;
>
> (c) **minden** ítéletkalkulusbeli formula az (a) és (b) **véges számú alkalmazásával** kapható meg.

**Megjegyzés.** Ez a definíció egy **rekurzív definíció** (vö. Fibonacci-sorozat): a legegyszerűbb esetből indulunk, és a már megépített formulákból építünk nagyobbakat.

---

## 8. Részformulák

> **Definíció (részformula).** Legyenek $F$ és $G$ formulák. Azt mondjuk, hogy **$G$ részformulája $F$-nek**, ha $G$ fellép az $F$ formula előállítása (a rekurzív definíció szerinti felépítése) során.

**Példa.** Az $F = (\neg A) \wedge ((\neg B) \leftrightarrow C)$ formula részformulái:

1. $A$
2. $B$
3. $C$
4. $(\neg A)$
5. $(\neg B)$
6. $((\neg B) \leftrightarrow C)$
7. $(\neg A) \wedge ((\neg B) \leftrightarrow C)$ ← maga a teljes formula

Összesen **7 részformulája** van.

**Megjegyzés.** Adott formulában előforduló ítéletváltozók mindig részformulái a formulának, és a teljes formula is mindig részformulája **önmagának**.

---

## 9. Ítéletek formalizálása

Minden ítélet formalizálható egy ítéletkalkulusbeli formulával, amelyben az ítéletváltozók prímítéleteket jelölnek.

**Példa.** Legyen
- $A$: „Kimegyek az uszodába."
- $B$: „Süt a nap."

| Mondat | Formalizálás |
|--------|--------------|
| **S:** Csak akkor megyek ki az uszodába, ha süt a nap. | $A \rightarrow B$ |
| **T:** Ha nem süt a nap, nem megyek ki az uszodába. | $(\neg B) \rightarrow (\neg A)$ |
| **Z:** Nem fordulhat elő, hogy kimegyek az uszodába és nem süt a nap. | $\neg\bigl(A \wedge (\neg B)\bigr)$ |

**Példa (bonyolultabb).** Formalizáljuk a következő ítéletet:

> „Ha sáros vagy törött a reflektor, és aznap földrengés volt, az operatőr pontosan akkor kap prémiumot, ha időben érkezik, de nincs napfogyatkozás."

Vezessük be a prímítéleteket:
- $A$: „Sáros a reflektor."
- $B$: „Törött a reflektor."
- $C$: „Aznap földrengés volt."
- $D$: „Az operatőr prémiumot kap."
- $E$: „Az operatőr időben érkezik."
- $F$: „Napfogyatkozás van."

**Megoldás:**

$$\bigl((A \vee B) \wedge C\bigr) \rightarrow \bigl(D \leftrightarrow (E \wedge \neg F)\bigr)$$

*Értelmezés:* „Ha sáros **vagy** törött a reflektor **és** aznap földrengés volt, (akkor) az operatőr pontosan akkor kap prémiumot, ha időben érkezik, **de** (= és) nincs napfogyatkozás."

**Gyakorló feladat (az előadáson volt).** Formalizáld a következő ítéletet:

> „Ha taxival megyek, és nem érem el a vonatot, akkor pontosan abban az esetben téved el a taxis, ha taxival megyek."

*Segítség:* Prímítéletek: $A$: „Taxival megyek.", $B$: „Elérem a vonatot.", $C$: „A taxis eltéved."

<details>
<summary><b>Megoldás (kattints)</b></summary>

$$(A \wedge \neg B) \rightarrow (C \leftrightarrow A)$$

*Értelmezés:* Ha taxival megyek **és nem** érem el a vonatot, akkor a taxis pontosan akkor téved el, ha taxival megyek.

</details>

---

## 10. Formula igazságtáblázata

> **Definíció.** Ha adott az ítéletváltozók igazságértéke, akkor a formula igazságértéke a formula felépítése alapján, a logikai műveletek segítségével **mindig kiszámítható**. Ha az ítéletváltozók **minden lehetséges értékére** kiszámoljuk a formula igazságértékét, megkapjuk a formula **igazságtáblázatát**.

**Megjegyzés.** Ha az $F$ formula az $A_1, \dots, A_n$ ítéletváltozókból épül fel, akkor a formula igazságtáblázata **$2^n$ sort** tartalmaz (2 változó → 4 sor, 3 változó → 8 sor).

**Példa.** A $\neg\bigl(A \wedge (\neg B)\bigr)$ formula igazságtáblázata (a táblázat **utolsó oszlopa** a keresett érték):

| $A$ | $B$ | $\neg B$ | $A \wedge (\neg B)$ | $\neg\bigl(A \wedge (\neg B)\bigr)$ |
|-----|-----|----------|---------------------|-------------------------------------|
| i | i | h | h | **i** |
| i | h | i | i | **h** |
| h | i | h | h | **i** |
| h | h | i | h | **i** |

*Olvasat:* a formula pontosan akkor hamis, ha $A$ igaz és $B$ hamis.

---

## 11. Logikai ekvivalencia és tautológia

> **Definíció (logikai ekvivalencia).** Az $F$ és $G$ formulák **logikailag ekvivalensek**, ha a bennük szereplő ítéletváltozók tetszőleges igazságértékére a formulák igazságértéke megegyezik (azaz az igazságtáblázataik megegyeznek). Jelölés:
>
> $$F \equiv G$$

> **Definíció (tautológia).** Az $F$ formulát **tautológiának** nevezzük, ha igazságértéke **mindig igaz**, azaz $F \equiv \mathrm{i}$.

**Példák:** $A \vee \neg A$ (a „kizárt harmadik" törvénye) tautológia; $A \wedge \neg A$ (ellentmondás) sohasem igaz.

> **Tétel.** Az ítéletkalkulus tetszőleges $F$ és $G$ formulájára:
>
> $$F \equiv G \quad \text{pontosan akkor teljesül, ha} \quad F \leftrightarrow G \ \text{tautológia.}$$

---

## 12. Az alapvető logikai ekvivalenciák (tételgyűjtemény)

> **Tétel.** Igazak a következő logikai ekvivalenciák.

### (1) Az implikáció kifejezése

$$A \rightarrow B \ \equiv \ (\neg A) \vee B$$

### (2) A negáció alaptulajdonsága (dupla negáció)

$$\neg(\neg A) \equiv A$$

### (3) De Morgan-azonosságok

$$\neg(A \wedge B) \equiv (\neg A) \vee (\neg B), \qquad \neg(A \vee B) \equiv (\neg A) \wedge (\neg B)$$

### (4) A $\wedge$ és $\vee$ alaptulajdonságai

| Név | Azonosság |
|-----|-----------|
| **Idempotencia** | $A \wedge A \equiv A$, $\quad A \vee A \equiv A$ |
| **Kommutativitás** | $A \wedge B \equiv B \wedge A$, $\quad A \vee B \equiv B \vee A$ |
| **Asszociativitás** | $(A \wedge B) \wedge C \equiv A \wedge (B \wedge C)$, $\quad (A \vee B) \vee C \equiv A \vee (B \vee C)$ |
| **Abszorptivitás** | $A \wedge (A \vee B) \equiv A$, $\quad A \vee (A \wedge B) \equiv A$ |
| **Disztributivitás** | $A \wedge (B \vee C) \equiv (A \wedge B) \vee (A \wedge C)$, $\quad A \vee (B \wedge C) \equiv (A \vee B) \wedge (A \vee C)$ |

### (5) A $\rightarrow$ és $\leftrightarrow$ alaptulajdonságai

$$A \leftrightarrow B \equiv (A \rightarrow B) \wedge (B \rightarrow A)$$

$$A \rightarrow B \equiv (\neg B) \rightarrow (\neg A) \quad \text{(kontrapozíció)}$$

$$A \rightarrow (B \rightarrow C) \equiv (A \wedge B) \rightarrow C$$

$$(A \vee B) \rightarrow C \equiv (A \rightarrow C) \wedge (B \rightarrow C)$$

$$A \rightarrow (B \wedge C) \equiv (A \rightarrow B) \wedge (A \rightarrow C)$$

$$A \leftrightarrow B \equiv B \leftrightarrow A \quad \text{(kommutativitás)}$$

$$(A \leftrightarrow B) \leftrightarrow C \equiv A \leftrightarrow (B \leftrightarrow C) \quad \text{(asszociativitás)}$$

### (6) Az $\mathrm{i}$ és $\mathrm{h}$ alaptulajdonságai

$$A \wedge (\neg A) \equiv \mathrm{h}, \qquad A \vee (\neg A) \equiv \mathrm{i}$$

$$A \wedge \mathrm{i} \equiv A, \qquad A \vee \mathrm{i} \equiv \mathrm{i}$$

$$A \wedge \mathrm{h} \equiv \mathrm{h}, \qquad A \vee \mathrm{h} \equiv A$$

$$\mathrm{i} \rightarrow A \equiv A, \qquad \mathrm{h} \rightarrow A \equiv \mathrm{i}$$

$$A \rightarrow \mathrm{i} \equiv \mathrm{i}, \qquad A \rightarrow \mathrm{h} \equiv \neg A$$

---

## 13. Helyettesítési tételek

> **1. Tétel (részformula-helyettesítés).** Ha egy formula valamely részformulája helyébe **vele logikailag ekvivalens** formulát írunk, akkor az eredetivel logikailag ekvivalens formulát kapunk.

**Példa:**
$$(A \rightarrow B) \wedge C \ \equiv \ (\neg A \vee B) \wedge C$$
mert $A \rightarrow B \equiv \neg A \vee B$ (az implikáció kifejezése).

> **2. Tétel (változó-helyettesítés).** Ha két formula logikailag ekvivalens, akkor a bennük szereplő ítéletváltozókat **tetszőleges formulákkal helyettesítve** (a változók minden előfordulásánál) újra logikailag ekvivalens formulákat kapunk.

**Példa:**
$$((C \wedge \neg D) \rightarrow B) \vee C \ \equiv \ (\neg(C \wedge \neg D) \vee B) \vee C$$
mert $(A \rightarrow B) \vee C \equiv (\neg A \vee B) \vee C$, és itt $A \rightsquigarrow C \wedge \neg D$ helyettesítést végeztünk.

**Kidolgozott példa (a két tétel kombinációja).** Igazoljuk, hogy az alábbi két formula ekvivalens:
$$F = ((A \wedge B) \rightarrow C) \vee D, \qquad G = \neg\bigl(\neg((A \wedge B) \rightarrow C) \wedge \neg D\bigr)$$

*Megoldás, lépésről lépésre:*

1. Alkalmazzuk a **De Morgan-azonosságot** a $G$-re: $\neg(X \wedge Y) \equiv \neg X \vee \neg Y$, az $X \rightsquigarrow \neg((A \wedge B) \rightarrow C)$, $Y \rightsquigarrow \neg D$ helyettesítéssel:
$$G \equiv \neg\bigl(\neg((A \wedge B) \rightarrow C)\bigr) \vee \neg(\neg D)$$
2. Alkalmazzuk a **dupla negációt** ($\neg(\neg X) \equiv X$) a részformulákra:
$$G \equiv ((A \wedge B) \rightarrow C) \vee D = F.$$

Tehát $F \equiv G$. ✔

---

## 14. Teljes diszjunktív normálforma (TDNF)

> **Definíció (dnf és tdnf).** Az $F$ formulát **diszjunktív normálformának (dnf)** nevezzük, ha
>
> $$F = K_1 \vee K_2 \vee \dots \vee K_t$$
>
> alakú, ahol a $K_1, \dots, K_t$ formulák mindegyike **változóknak vagy változók negáltjainak konjunkciója**, és minden $K_i$-ben minden változó legfeljebb egyszer szerepel.
>
> Ha az $A_1, \dots, A_n$ változókból felépített $K_1 \vee \dots \vee K_t$ dnf esetén a $K_1, \dots, K_t$ formulák **páronként különböző $n$-tagú konjunkciók**, amelyekben az $A_1, \dots, A_n$ ítéletváltozók **mindegyike** szerepel (negálva vagy negálatlanul), akkor **teljes diszjunktív normálformáról (TDNF)** beszélünk.

**Példák:**

| Formula | Típus |
|---------|-------|
| $(A \wedge B) \vee ((\neg B) \wedge C)$ | dnf, de **nem** TDNF (a tagok nem 3-tagúak) |
| $(A \wedge B \wedge (\neg C)) \vee ((\neg A) \wedge (\neg B) \wedge C)$ | **TDNF** |
| $A \wedge (\neg B)$ | dnf, de nem TDNF |
| $A \wedge (\neg B) \wedge C$ | **TDNF** |
| $A \vee B \vee C$ | dnf, de nem TDNF |
| $(A \wedge (\neg B)) \vee (B \wedge C)$ | dnf, de nem TDNF |
| $(A \wedge (\neg B) \wedge C) \vee (A \wedge B \wedge C)$ | **TDNF** |
| *(üres diszjunkció, $t = 0$)* | **TDNF** (üres TDNF) |

> **Tétel.** Minden formulához létezik vele logikailag ekvivalens **teljes diszjunktív normálforma**, amely a tagok sorrendjétől eltekintve **egyértelműen meghatározott**.

> **Megjegyzés (a TDNF megkeresése az igazságtáblázatból).** Az $F$ formula TDNF-jében a tagok ($t$) száma = az igazságtáblázat azon sorainak száma, ahol $F$ az **i** értéket veszi fel. Minden ilyen sorhoz a megfelelő $K_j$ tagot úgy kapjuk, hogy **pontosan azokat a változókat negáljuk, amelyek az adott sorban h értéket vesznek fel**, majd az összes változó konjunkcióját képezzük.

**Kidolgozott példa.** Legyen $F = A \wedge \neg(B \rightarrow C) \vee (\neg B \wedge \neg C)$. Számoljuk ki az igazságtáblázatot lépésről lépésre:

| $A$ | $B$ | $C$ | $\neg B$ | $\neg C$ | $\neg B \wedge \neg C$ | $B \rightarrow C$ | $\neg(B \rightarrow C)$ | $\neg(B \rightarrow C) \vee (\neg B \wedge \neg C)$ | $F$ |
|-----|-----|-----|----------|----------|------------------------|-------------------|--------------------------|-----------------------------------------------------|-----|
| i | i | i | h | h | h | i | h | h | **h** |
| i | i | h | h | i | h | h | i | i | **i** |
| i | h | i | i | h | h | i | h | h | **h** |
| i | h | h | i | i | i | i | h | i | **i** |
| h | i | i | h | h | h | i | h | h | **h** |
| h | i | h | h | i | h | h | i | i | **h** |
| h | h | i | i | h | h | i | h | h | **h** |
| h | h | h | i | i | i | i | h | i | **h** |

$F$ pontosan két sorban igaz:
- $A = \mathrm{i}, B = \mathrm{i}, C = \mathrm{h}$ → tag: $A \wedge B \wedge (\neg C)$
- $A = \mathrm{i}, B = \mathrm{h}, C = \mathrm{h}$ → tag: $A \wedge (\neg B) \wedge (\neg C)$

Tehát az $F$ formula **TDNF-je**:

$$F \equiv \bigl(A \wedge B \wedge (\neg C)\bigr) \vee \bigl(A \wedge (\neg B) \wedge (\neg C)\bigr)$$

*Olvasat:* $F$ pontosan akkor igaz, ha „$A$ igaz, $B$ igaz és $C$ hamis" **vagy** „$A$ igaz, $B$ hamis és $C$ hamis".

**Alkalmazás.** A diszjunktív normálformák egyik fontos alkalmazása a **logikai áramkörök tervezése**: az igazságtáblázatból közvetlenül felírható az áramkör logikai kapukkal megvalósítható képlete.

---

## 15. E-teszt feladatok megoldásokkal

### 15.1. Formalizálás és kiértékelés

**Feladat.** Formalizáld a következő mondatot, és döntsd el, hogy a prímítéletek megadott értéke mellett az ítélet igaz vagy hamis! (A prímítéleteket a mondatban való előfordulásuk sorrendje szerint jelöljük $A, B, C, \dots$ betűkkel.)

> „Ha esik az eső, és nincs rossz kedvem, akkor pontosan akkor megyek dimat gyakorlatra, ha röpdolgozatot írunk."

Adott: $A = \mathrm{i}$, $B = \mathrm{h}$, $C = \mathrm{h}$, $D = \mathrm{h}$.

**Megoldás.** A prímítéletek:
- $A$: „Esik az eső."
- $B$: „Rossz kedvem van."
- $C$: „Megyek dimat gyakorlatra."
- $D$: „Röpdolgozatot írunk."

A formula:
$$(A \wedge (\neg B)) \rightarrow (C \leftrightarrow D)$$

Kiértékelés: $( \mathrm{i} \wedge \neg\mathrm{h} ) \rightarrow (\mathrm{h} \leftrightarrow \mathrm{h}) = ( \mathrm{i} \wedge \mathrm{i} ) \rightarrow \mathrm{i} = \mathrm{i} \rightarrow \mathrm{i} = \mathbf{i}$.

**Az ítélet igaz.** ✔

### 15.2. Igaz/hamis állítások

**Feladat.** Döntsd el, hogy az alábbi állítások igazak-e!

**(a)** Az $(A \wedge B) \vee (\neg C)$ formula részformuláinak száma 7.

**Megoldás.** A részformulák a rekurzív definíció szerint: $A$, $B$, $C$, $(\neg C)$, $(A \wedge B)$, $(A \wedge B) \vee (\neg C)$ → **6 részformula**. Az állítás **hamis**. ✘

**(b)** $B \vee (\neg B) \equiv A \leftrightarrow (\neg A)$.

**Megoldás.** A bal oldal **mindig igaz** (tautológia: $B \vee \neg B \equiv \mathrm{i}$), a jobb oldal **mindig hamis** ($A \leftrightarrow \neg A$ sohasem teljesül). Az állítás **hamis**. ✘

**(c)** A $(\neg B \leftrightarrow A) \vee B$ formula teljes diszjunktív normálformájában 2 darab diszjunkciójel van.

**Megoldás.** Igazságtáblázat:

| $A$ | $B$ | $\neg B$ | $\neg B \leftrightarrow A$ | $(\neg B \leftrightarrow A) \vee B$ |
|-----|-----|----------|----------------------------|-------------------------------------|
| i | i | h | h | i |
| i | h | i | i | i |
| h | i | h | i | i |
| h | h | i | h | h |

A formula 3 sorban igaz, 1 sorban hamis (amikor $A$ és $B$ is hamis), így a TDNF 3 tagú: $(A \wedge B) \vee (A \wedge \neg B) \vee (\neg A \wedge B)$ → **2 darab diszjunkciójel**. Az állítás **igaz**. ✔

### 15.3. Elméleti kérdések

Minden elektronikus teszt 3. feladata az **elméleti részhez** kapcsolódó igaz/hamis kérdéseket tartalmaz – ezekhez a fenti definíciók és tételek pontos ismerete szükséges.

---

## 16. Összefoglaló táblázatok

### 16.1. Az öt logikai művelet "egy sorban"

| Művelet | Jele | Olvasata | Hamis, ha… |
|---------|------|----------|------------|
| Negáció | $\neg A$ | „nem A" | $A$ igaz |
| Konjunkció | $A \wedge B$ | „A és B" | legalább az egyik tag hamis |
| Diszjunkció | $A \vee B$ | „A vagy B" (megengedő) | mindkét tag hamis |
| Implikáció | $A \rightarrow B$ | „ha A, akkor B" | $A$ igaz és $B$ hamis |
| Ekvivalencia | $A \leftrightarrow B$ | „A akkor és csak akkor, ha B" | $A$ és $B$ különböző |

### 16.2. Gyakran használt ekvivalenciák („puska")

$$A \rightarrow B \equiv \neg A \vee B$$
$$\neg(A \wedge B) \equiv \neg A \vee \neg B, \qquad \neg(A \vee B) \equiv \neg A \wedge \neg B \quad \text{(De Morgan)}$$
$$\neg(\neg A) \equiv A$$
$$A \leftrightarrow B \equiv (A \rightarrow B) \wedge (B \rightarrow A)$$
$$A \rightarrow B \equiv \neg B \rightarrow \neg A \quad \text{(kontrapozíció)}$$

### 16.3. Formalizálási tippek

- „**de**" → konjunkció ($\wedge$);
- „**vagy**" → megengedő diszjunkció ($\vee$), kivéve ha kizáró értelmet kell kifejezni → $(A \vee B) \wedge \neg(A \wedge B)$;
- „**ha A, akkor B**" / „**csak akkor A, ha B**" / „**B szükséges feltétele A-nak**" → $A \rightarrow B$;
- „**akkor és csak akkor**" / „**pontosan akkor**" / „**szükséges és elegendő**" → $\leftrightarrow$;
- A TDNF tagjai az igazságtáblázat **i-soraihoz** tartoznak; a h értékű változókat negáljuk.

---

## 17. Források és irodalom

- **Előadás diái:** Kátai-Urbán Kamilla: *Diszkrét matematika I., 1. előadás – Ítéletkalkulus* (2024/25. tanév) → [[diszkr-t-matematika-i-1-el-ad-s-t-letkalkulus-k-ta-fdc354]]
- **Jegyzet:** Dormán Miklós, Kátai-Urbán Kamilla: *Előadásvázlat* – `https://www.math.u-szeged.hu/~katai/dimat1_jegyzet/DisMatInf1-Elm.pdf`
- **E-tesztek:** `https://www.math.u-szeged.hu/~mmaroti/tests/`
- Az előadások diáinál felhasznált irodalom: Czédli Gábor (2005–2019), Dormán Miklós (2022–2023), Maróti Miklós (*Diszkrét matematika – előadásvázlat*), Szendrei Ágnes (*Diszkrét matematika*, Polygon jegyzet)

---

*Készült a Diszkrét matematika I. tárgy 1. előadásának anyaga alapján. A gyakorlati feladatok (teljes indukció, halmazok) a [[diszkr-t-matematika-i-gyakorlati-feladatok-teljes--f4d235]] anyagban találhatók.*
