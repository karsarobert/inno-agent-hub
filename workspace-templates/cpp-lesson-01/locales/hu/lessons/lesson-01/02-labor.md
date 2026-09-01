# 1. alkalom – Hallgatói labor
## C++ alapok gyakorlatban

**Alapelv:** előbb értsd meg és jósolj, utána futtasd.

Javasolt fordítás:

```bash
g++ -std=c++20 -Wall -Wextra -Wpedantic main.cpp -o program
./program
```

## Időkeret

A labor előtt kb. 10–12 perc elméleti visszaidézés történik.

**Kötelező magfeladatok:** 1–6., 8–9.  
**Bővítő feladatok, ha marad idő:** 7. és 10.

---

## 1. Kódolvasás — kötelező

```cpp
#include <iostream>

int main() {
    double distanceKm = 210.0;
    double consumption = 6.4;
    double fuelPrice = 618.9;

    double usedFuel = distanceKm / 100.0 * consumption;
    double cost = usedFuel * fuelPrice;

    std::cout << cost << " Ft\n";
}
```

Futtatás nélkül:

1. Melyik három változó tartalmazza a kiinduló adatokat?
2. Melyik két változó számított érték?
3. Hol történik a kiírás?
4. Milyen nagyságrendű eredményt vársz?
5. Számítsd ki kézzel a várt értéket, majd futtasd.

---

## 2. Változóértékek követése — kötelező

```cpp
double distanceKm = 120.0;
distanceKm = 150.0;
distanceKm = distanceKm + 20.0;
distanceKm = distanceKm * 2.0;
```

| sor után | `distanceKm` |
|---|---:|
| 1. | |
| 2. | |
| 3. | |
| 4. | |

Előbb papíron töltsd ki, csak utána ellenőrizd futtatással.

---

## 3. Deklaráció / inicializálás / értékadás — kötelező

Jelölések:

- **D** = deklaráció
- **I** = inicializálás
- **É** = értékadás

```cpp
double price;
int passengers = 4;
price = 620.5;
double total = price * 10.0;
passengers = 5;
```

Egy sor több kategóriába is tartozhat.

---

## 4. Típusválasztás — kötelező

Választható: `int`, `double`, `bool`, `char`, `std::string`.

| adat | javasolt típus | rövid indoklás |
|---|---|---|
| csoport létszáma | | |
| átlaghőmérséklet | | |
| sikeres-e egy művelet | | |
| egy karakteres kategóriakód | | |
| település neve | | |
| hálózati késleltetés, törtrész is lehet | | |

Legalább két választást indokolj.

---

## 5. Fordítási hibák — kötelező

Mentsd ezt külön `.cpp` fájlba:

```cpp
#include <iostream>

int main() {
    distanceKm = 200.0;
    double fuelPrice = 620.0
    std::cout << distanceKM * fuelPrice << "\n";
}
```

1. Fordítsd le változtatás nélkül.
2. Olvasd el a legelső hibaüzenetet.
3. Saját szavaiddal mondd el, mire panaszkodik a fordító.
4. Javíts **egyetlen** hibát.
5. Fordíts újra.
6. Ismételd, amíg a program lefordul.

Ne próbáld az összes hibát egyszerre javítani.

---

## 6. Utazási költség kalkulátor — kötelező

Nyisd meg:

`starter/trip_cost.cpp`

A program kérje be:

- az út hosszát km-ben;
- az átlagfogyasztást l/100 km-ben;
- az üzemanyag árát Ft/l-ben.

Képlet:

```text
felhasznált üzemanyag = távolság / 100 × fogyasztás
költség = felhasznált üzemanyag × üzemanyagár
```

Mielőtt futtatod, készíts egy olyan tesztesetet, amelynek eredményét kézzel is
könnyen ki tudod számítani.

**P-A-K-T:** P → A → K → T

---

## 7. Oda-vissza út — bővítő

A felhasználó egyirányú távolságot ad meg. Módosítsd az előző programot úgy,
hogy az oda-vissza út költségét számolja.

Feltétel:
- ne másold kétszer a teljes számítást;
- indokold egy mondatban, hogyan módosítottad a programot.

---

## 8. Mini-projekt: villamosenergia-költség — kötelező

Készíts programot, amely bekéri:

- egy eszköz teljesítményét wattban;
- napi használati időt órában;
- az energia árát Ft/kWh-ban.

Számítsd ki a 30 napos energiafogyasztást és költséget:

```text
energia_kWh = teljesítmény_W / 1000 × napi_óra × 30
költség = energia_kWh × ár
```

Kódolás előtt írd le:

1. a szükséges változókat;
2. a típusukat;
3. a két fő számítást.

---

## 9. Teszttervezés — kötelező

A villamosenergia-programhoz tervezz legalább három tesztesetet:

1. könnyen kézzel ellenőrizhető eset;
2. nulla használati idő;
3. törtszámokat is tartalmazó eset.

| teljesítmény | óra/nap | Ft/kWh | várt energia | várt költség | tényleges |
|---:|---:|---:|---:|---:|---:|
| | | | | | |
| | | | | | |
| | | | | | |

A várt eredményt a program futtatása **előtt** számítsd ki.

---

## 10. Logikai hibakeresés — bővítő

```cpp
double distanceKm = 200.0;
double consumption = 6.0;
double fuelPrice = 600.0;

double cost = distanceKm * consumption * fuelPrice;
```

A program lefordulhat, de a képlet hibás.

1. Mi a probléma a mértékegységekkel?
2. Írd fel először matematikailag a helyes számítást.
3. Utána javítsd a C++ kifejezést.
4. Válassz olyan tesztadatot, amelyen a hiba könnyen észrevehető.

**P-A-K-T:** A → K → T
