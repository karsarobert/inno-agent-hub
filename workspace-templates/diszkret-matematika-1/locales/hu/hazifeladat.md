# Ítéletkalkulus — óra utáni gyakorlás

Az alapfeladatokat mindenki oldja meg. A további feladatok közül a tanár ajánlása vagy a saját bizonytalanságod alapján válassz. A válaszok mellé rövid indoklás is kell. A programozási kitekintés választható.

## Alapfeladatok

**H1. Ítélet vagy nem ítélet?**

(a) „A 21 páros.” (b) „Nyisd ki a könyvet!” (c) „m osztható 3-mal.” — m nincs rögzítve. (d) „Ebben a konkrét borítékban két lap van.” — a borítékot most nem bonthatjuk fel.

**H2.** Tagadd: „A fájl mérete 10 MB-nál kisebb.” A fájlnak van meghatározott mérete. Ellenőrizd a tagadást pontosan 10 MB esetén is!

**H3.** Készítsd el `(¬P) ∧ Q` igazságtáblázatát köztes oszloppal! Válassz egy sort, és magyarázd el!

**H4.** „Ha elküldöm az üzenetet, visszaigazolást kapok.” Vezesd be a betűjeleket, írd fel a formulát, és nevezd meg az egyetlen hamis esetet! Mit mond a formula arról az esetről, amikor nem küldöm el az üzenetet?

## További gyakorlás

**H5.** Egy feladatot szöveges vagy szóbeli indoklással lehet beadni, és mindkettő is megengedett. Másik feladatnál a két forma közül pontosan egyet kérnek. Vezesd be a betűjeleket! Az első feltételt írd fel formulával; a másodiknál magyarázd meg a különbséget! A második formula felírása választható.

**H6.** „Csak akkor küldöm el a jelentkezést, ha kitöltöttem az adatlapot.” J: „Elküldöm a jelentkezést”, A: „Kitöltöttem az adatlapot”. Formalizáld! Következik-e belőle, hogy a kitöltött adatlapot biztosan elküldöm?

**H7.** Készítsd el `¬(P ∧ Q)` táblázatát! Hasonlítsd össze H3-mal: melyik sorban térnek el?

## Választható kitekintés

**H8.** Találj egy mondatot, amelyben „és” szerepel, és két önálló állítást kapcsol össze! Írj egy olyat is, amelyben az események sorrendje fontos. Magyarázd el a különbséget!

**H9. Programozási kapcsolat.** Az alábbi C++-részletben a `%` az egész osztás maradékát adja; a `==` egyenlőséget vizsgál; az `if` igaz feltételnél az első, az `else` hamis feltételnél a második ágat választja; a `std::cout` szöveget ír ki. Ez egy program részlete, önmagában nem teljes futtatható program.

```cpp
int number = 7;
if (number % 2 == 0) {
    std::cout << "even";
} else {
    std::cout << "odd";
}
```

Mi a feltétel igazságértéke, és melyik szöveg jelenik meg? Nem szükséges kódot írni vagy futtatni.

## Rövid ismétlés a következő gyakorlat előtt

Jegyzet nélkül válaszolj: mikor hamis a megengedő vagy; mikor hamis az implikáció; mitől függ, mire vonatkozik a tagadás? Ezután ellenőrizd magad a jegyzetben. A bizonytalan pontot hozd magaddal a következő órára.
