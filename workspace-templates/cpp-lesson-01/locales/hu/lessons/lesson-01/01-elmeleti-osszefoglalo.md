# 1. alkalom – Elméleti összefoglaló
## C++ alapok: az első használható program

Ez referenciaanyag az órán elhangzottak felidézéséhez. A Tutor nem olvassa fel
egyben: részenként röviden összefoglalja, majd egy kérdéssel ellenőrzi a megértést.

---

## 1. Probléma → algoritmus → program

A programozás egy megoldandó problémából indul. Az **algoritmus** a megoldás
lépéseinek nyelvfüggetlen leírása, a **program** pedig ennek egy programozási
nyelven – itt C++-ban – megfogalmazott megvalósítása.

Példa: utazási költség esetén először az adatokat és a képletet kell meghatározni,
csak utána írunk C++ kódot.

---

## 2. Forráskód, fordítás és futtatás

```text
main.cpp → C++ fordító → futtatható program → futtatás → kimenet
```

Például:

```bash
g++ -std=c++20 -Wall -Wextra -Wpedantic main.cpp -o program
./program
```

A `.cpp` fájl forráskód. A fordító ellenőrzi a C++ szabályait és – ha nincs
fordítást megakadályozó hiba – létrehozza a futtatható programot.

A **szintaxis** a nyelv formai szabályait jelenti. Egy program azonban akkor is
lehet logikailag hibás, ha lefordul.

---

## 3. `main`, kimenet és bemenet

```cpp
#include <iostream>

int main() {
    std::cout << "C++ program indul.\n";
}
```

- `main()` a program végrehajtásának kezdőpontja.
- `std::cout` adatot ír a standard kimenetre.
- `std::cin` adatot olvas be.

```cpp
double distanceKm;
std::cin >> distanceKm;
```

---

## 4. Változó és adattípus

A változónak neve, típusa és futás közbeni értéke van.

```cpp
int passengers = 4;
double fuelPrice = 618.9;
bool success = true;
char category = 'A';
```

Gyakori alaptípusok:
- `int` – egész szám;
- `double` – lebegőpontos szám;
- `bool` – igaz/hamis;
- `char` – egy karakter;
- `std::string` – szöveg.

A típust az adat természete alapján választjuk.

---

## 5. Deklaráció, inicializálás, értékadás

```cpp
double price;          // deklaráció
double fuelPrice = 620.5; // deklaráció + inicializálás
fuelPrice = 625.0;     // értékadás
```

A deklaráció létrehozza/bejelenti a változót.  
Az inicializálás a létrehozáskor kezdőértéket ad.  
Az értékadás egy már létező változó értékét módosítja.

---

## 6. Kifejezések és az `=`

```cpp
double usedFuel = distanceKm / 100.0 * consumption;
double cost = usedFuel * fuelPrice;
```

A jobb oldali kifejezés először kiértékelődik, majd az eredmény a bal oldali
változóba kerül.

```cpp
distanceKm = distanceKm + 20.0;
```

Ez nem matematikai egyenlet. A régi `distanceKm` értékhez hozzáadunk 20-at,
majd az eredményt visszaírjuk ugyanabba a változóba.

### Fontos pontosítás

Ha `distanceKm` típusa `double`, akkor:

```cpp
distanceKm / 100
```

és

```cpp
distanceKm / 100.0
```

is lebegőpontos osztást végez, mert az egyik operandus már `double`.
A `100.0` itt elsősorban a lebegőpontos számítás szándékát teszi láthatóvá.

Valódi egészosztási példa:

```cpp
int a = 5;
int b = 2;
```

`a / b` eredménye egész osztásnál `2`.

---

## 7. Fordítási és logikai hibák

Fordítást megakadályozó hiba lehet például:

```cpp
double price = 620.0
```

Hiányzik a `;`.

Vagy:

```cpp
distanceKm = 200.0;
```

ha `distanceKm` korábban nincs deklarálva.

Logikai hiba:

```cpp
double cost = distanceKm * consumption * fuelPrice;
```

Ez lefordulhat, de a képlet nem veszi figyelembe, hogy a fogyasztás
liter / 100 km mértékegységű.

### Típusvesztés

```cpp
int consumption = 6.7;
```

Ez lefordulhat, de a törtrész elveszik. A fordítási kapcsolók nem feltétlenül
adnak erre figyelmeztetést, ezért a megfelelő típusválasztás a programozó feladata.

### Inicializálatlan változó

```cpp
double fuelPrice;
```

A változó ekkor még nem kapott használható kezdőértéket. Ne használjuk számításban,
amíg nem inicializáltuk vagy nem olvastunk bele értéket.

---

## 8. Tesztelés

A program futtatása előtt legyen várható eredmény.

Példa:

| távolság | fogyasztás | ár | várt költség |
|---:|---:|---:|---:|
| 100 km | 6 l/100 km | 600 Ft/l | 3600 Ft |
| 200 km | 5 l/100 km | 600 Ft/l | 6000 Ft |
| 0 km | 6 l/100 km | 600 Ft/l | 0 Ft |

A teljes gondolkodási keret:

**P-A-K-T = Probléma → Algoritmus → Kód → Teszt**
