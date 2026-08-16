# Önellenőrzés — Bevezetés a C programozásba

**BSc bevezető kurzus · programozás**

> Mielőtt nekiállsz: olvasd át a **theory.md** jegyzetet, és oldd meg a **gyakorlatok.md** legalább alap szintjét! Ezután válaszolj a kérdésekre **önállóan, jegyzet nélkül** (a C-kódos feladatokat lehet papíron is válaszolni). A megoldókulcs a lap végén van — előbb minden kérdést válaszolj meg, csak utána javítsd ki magad!

---

## A) Rövid kérdések (6 pont)

Válaszolj 1–2 mondattal!

1. Mi a **ciklusinvariáns**, és mire használjuk?
2. Miért kell `&` a `scanf("%d", &n)` hívásban?
3. Mi a különbség az `=` és a `==` között?
4. Miért végződik a C-karakterlánc `\0` karakterrel?
5. Mi az a **nem definiált működés**, és miért nem elegendő, ha „a program a mintabemenetre működik"?
6. Milyen különbség a `for` és a `do`–`while` ciklus futási viselkedében? (Ha a feltétel eleve hamis, mi történik mindkettőnél?)

## B) Igaz vagy hamis? (5 pont)

Írd az állítás mellé, hogy **IGAZ** vagy **HAMIS** — és ha hamis, **javítsd is ki**!

1. `scanf("%s", szo)`-ban egy `char szo[20]` tömbhöz nem kell `&`, mert a tömb neve mutatóvá alakul.
2. `s == "hello"` azt vizsgálja, hogy a `s` lánc tartalmilag egyenlő-e a „hello" sztringgel.
3. `9 / 5` kifejezés egész típusú operandusokkal 1.8-at ad.
4. A `do`–`while` ciklus legalább egyszer lefut, még akkor is, ha a feltétel eleve hamis.
5. A `malloc`-kal foglalt memóriát a C fordító automatikusan felszabadítja a `main` végén, ezért soha nem szivárog.

## C) Hiba a kódban! (3 pont)

Mindegyik kódrészletben **egy hiba** van. Találd meg, magyarázd el mi a probléma, és írd meg a javítást!

**C1.**
```c
int n = 0;
scanf("%d", n);
printf("n = %d\n", n);
```

**C2.**
```c
int i = 1;
while (i < 5) {
    printf("%d\n", i);
}
```
*(Mi fog történni, ha lefuttatod?)*

**C3.**
```c
char nev[10];
gets(nev);
```

## D) Kézi programozás (2 pont)

**D1.** Írd meg a `szamjegy_osszeg(int n)` függvényt, amely egy nemnegatív egész szám számjegyainak összegét adja vissza. (Például `szamjegy_osszeg(305) = 8`, `szamjegy_osszeg(0) = 0`.) Tipp: `do`–`while` + `% 10` + `/ 10`!

**D2.** Írd le a *nyomkövetési táblázatot* a `szamjegy_osszeg(305)` híváshoz!

---

## Értékelés

**Maximális pontszám: 16 pont** (A: 6, B: 5, C: 3, D: 2)

| Pontszám | Hol tartasz? | Mit csinálj legközelebb? |
|---|---|---|
| **13–16** | 🏆 Kiváló! Az alapanyagot biztosan tudod. | Nézd meg a gyakorlatok **bővítő szintjét** (pénzváltás, vízkimérés, logikai paradoxon kódolva)! |
| **9–12** | 👍 Jó alap! A lényeg megvan, de akadnak bizonytalanságok. | Gyakorold a **fejlesztő szint** feladatait, főleg a mutatós csere és az osztópárok feladatát! |
| **5–8** | 📖 Még dolgoznod kell rajta. | Olvasd újra a theory.md **8–9. részét** (mutatók, tömbök és karakterláncok) és a **11. részét** (gyakori hibák), majd oldd meg újra az **alap szint** feladatait! |
| **0–4** | 🤝 Kérj segítséget! | Beszéld át az anyagot a tanárral vagy egy társaddal, és példakódon végigfuttatva dolgozd fel újra a jegyzetet! |

> 💡 **Ha elakadtál:** A → theory.md 6. (ciklusok) és 9. (karakterláncok) része; B → 5., 11. rész; C → 11. rész (hibatáblázat); D → 3. és 6. rész (nyomkövetés, ciklusok).

---

## Megoldókulcs

> ⚠️ Csak az önellenőrzés **kitöltése után** használd!

### A) Rövid kérdések

1. A ciklusinvariáns olyan állítás, amely a ciklus **minden iterációjában** igaz egy meghatározott ponton (pl. az iteráció elején). Használatával kézi ellenőrzésen túl a ciklus *helyességét* is érveléssel igazolhatjuk, és leállásáról meggyőződhetünk.
2. Mert a `scanf` **a hívó változójába** kell írnia, és ehhez a változó **memóriacímét** kell kapnia. A `%d` konverzió egy `int *` argumentumot vár, ezért `&n` (a tömbnéveknél — pl. `%s` + `char[]` — a tömb neve már „mutatóvá alakul", ott nem kell).
3. Az `=` **értékadás** (bal oldalra ír), a `==` **összehasonlítás** (0 vagy 1-et ad). `if (x = 5)`-nél a feltétel mindig igaz lesz, és `x` értéke mellékhatásként 5 lesz.
4. Mert a C-ben a karakterláncok *tömbök*, és a `strlen`, `printf("%s")` stb. függvényeknek valamiért meg kell állniuk — a `\0` jelöli a lánc végét. A tömb mérete önmagában nem tartalmazza a láncrendszer hosszát.
5. Nem definiált működés = olyan viselkedés, amelyet a C szabvány **nem ír elő**: a program összeomolthat, hibás eredményt adhat, vagy látszólag működik. Pont emiatt nem elég, ha a mintabemenetre működik — a szélső- és hibaeseteket is tesztelni kell (a „működik" lehet csak véletlen).
6. A `for` ciklus a feltételt a ciklusmag **előtt** vizsgálja: ha eleve hamis, a ciklus **egyszer sem** fut le. A `do`–`while` a feltételt **után** vizsgálja: a ciklusmag **mindig legalább egyszer** lefut, még hamis eleve feltételnél is.

### B) Igaz vagy hamis?

1. **IGAZ** — a tömb neve a legtöbb kifejezésben az első elem címére mutató mutatóvá alakul (de a `sizeof(szamok)` és a `&szamok` kivétel! A kettő *típusa* más).
2. **HAMIS** — a `==` a **címeket** hasonlítja össze, nem a tartalmat. Tartalmi összehasonlítás: `strcmp(s, "hello") == 0`.
3. **HAMIS** — egész osztásnál a törtpart **levágódik**: `9 / 5 == 1`. Lebegőpontos osztáshoz: `9.0 / 5.0 == 1.8`.
4. **IGAZ** — a `do`–`while` a feltételt a ciklusmag végén ellenőrzi, ezért a mag garantáltan egyszer lefut. (Ezt használjuk például a „0 számjegye 1" feladatban.)
5. **HAMIS** — a C **nem** felszabadítja automatikusan a dinamikusan foglalt memóriát; a programozó felelőssége a `free`. (A processz kilépésekor az OS visszaigényli a teljes memóriát, de *futás közben* a nem felszabadított terület szivárgás, és több lefoglalásnál kimerülhet a program memóriája.)

### C) Hiba a kódban!

**C1.** A `scanf("%d", n)` helyett `scanf("%d", &n)` kell: a `%d` konverzió egy `int *` argumentumot vár (hová írja a beolvasott számot). Cím nélkül nem definiált működés — a program összeomolhat vagy a memória tetszőleges helyét írhatja felül. (És érdemes a visszatérési értéket is ellenőrizni.)

**C2.** **Végtelen ciklus**: az `i` soha nem változik, így ha `i = 1`-el indul, az `i < 5` feltétel örökké igaz marad — a program végtelenig írja ki az 1-et. Javítás: a ciklusmagba kell az állapotfrissítés: `while (i < 5) { printf("%d\n", i); ++i; }` (vagy `for (int i = 1; i < 5; ++i)`).

**C3.** A `gets` **nem korlátozza** a beolvasott adatok hosszát — egy 10 bájnál hosszabb bemenet puffertúlcsordulást (biztonsági hibát!) okoz. A `gets` a C11 szabványból is kikerült: helyette `fgets(nev, 10, stdin)` (vagy `scanf("%9s", nev)`).

### D) Kézi programozás

**D1.**

```c
int szamjegy_osszeg(int n) {
    int osszeg = 0;
    int x = n;
    do {
        osszeg += x % 10;
        x /= 10;
    } while (x != 0);
    return osszeg;
}
```

(A `do`–`while` miatt `n = 0` esetén is pontosan 0-t ad: egy lépésben `0 % 10 = 0` adódik.)

**D2.**

| Lépés | `x` a lépés elején | `x % 10` | `osszeg` a lépés után | `x` a lépés után | `x != 0`? |
| --- | --- | --- | --- | --- | --- |
| 1 | 305 | 5 | 5 | 30 | igaz |
| 2 | 30 | 0 | 5 | 3 | igaz |
| 3 | 3 | 3 | 8 | 0 | hamis → vége |

Eredmény: **8** (3 + 0 + 5 = 8 ✓).

---

*Készült a „Bevezetés a C programozásba — BSc-kurzushoz" oktatóanyag tanulóiváltozataként. Elmélet: **theory.md** · Feladatok: **gyakorlatok.md**.*
