# Analóg minták – a feladatok előtt

Ezek eltérő problémájú, teljes programok. Egyenként, külön próbaállományban futtathatók; ne másold őket a célforrás kész megoldásaként.

## M1 – Szöveg fájlba írása

```cpp
#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ofstream fajl("status_demo.txt");
    if (!fajl) return 1;
    fajl << "READY\n";
    fajl.close();
    cout << static_cast<bool>(fajl) << '\n';
}
```

Várt kimenet:

```text
1
```

Az iostream a cout, az fstream az ofstream miatt kell. Az ofstream konstruktor megnyitja a fájlt; a !fajl a hibás állapotot vizsgálja. A << karaktereket ír. A close befejezi a pufferelt írást, és az utána kapott bool nem a nyitottság, hanem a hibamentesség. A static_cast<bool> kifejezetten ezt az átalakítást kéri.

G10_01-ben egy állapotszó helyett két kétszámos rekordot és azok elválasztóit kell megírnod.

## M2 – Hozzáfűzés és soronkénti olvasás

```cpp
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    { ofstream fajl("events_demo.txt"); if (!fajl) return 1;
      fajl << "OPEN\n"; fajl.close(); if (!fajl) return 1; }
    { ofstream fajl("events_demo.txt", ios::app); if (!fajl) return 1;
      fajl << "CLOSE\n"; fajl.close(); if (!fajl) return 1; }
    ifstream bemeno("events_demo.txt"); if (!bemeno) return 1;
    string sorAdat;
    while (getline(bemeno,sorAdat)) cout << sorAdat << '\n';
    if (bemeno.bad() || !bemeno.eof()) return 1;
}
```

Várt kimenet:

```text
OPEN
CLOSE
```

Az első blokk létrehozza az alapot, a második ios::app-pal a végére ír. Mindkettő után ellenőrizzük a lezárást. A string és getline a string fejlécből kell: a getline egy teljes sor karaktereit veszi át. A while a művelet sikerességét vizsgálja, a törzsben már van használható sor.

G10_02-ben a fájlban számok lesznek; olvasás közben darabszámot és összeget kell képezned.

## M3 – Utolsó szám és fájlvég

```cpp
#include <iostream>
#include <fstream>
using namespace std;

int main() {
    { ofstream fajl("number_demo.txt"); if (!fajl) return 1;
      fajl << "8"; fajl.close(); if (!fajl) return 1; }
    ifstream bemeno("number_demo.txt"); if (!bemeno) return 1;
    int szam = 0;
    bemeno >> szam;
    cout << szam << ' ' << bemeno.eof() << ' ' << bemeno.fail() << '\n';
    bemeno >> szam;
    cout << bemeno.eof() << ' ' << bemeno.fail() << '\n';
}
```

Várt kimenet:

```text
8 1 0
1 1
```

Az ofstream pontosan egy számot ír, újsor nélkül. Az első számolvasás sikeres, miközben észleli a fájlvéget: eof igaz, fail hamis. A második kérés már nem kap új számot: eof és fail is igaz. A sikertelen második olvasás után nem írjuk ki a számot.

G10_03-ban két mezőt kérsz, hibás szöveget és hiányzó mezőt is vizsgálsz. A jelzők nem kizárják egymást.

## M4 – Token és teljes számellenőrzés

```cpp
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main() {
    const string sorAdat = "MODE 2x";
    istringstream mezo(sorAdat);
    string jelszo, szoveg, plusz;
    if (!(mezo >> jelszo >> szoveg) || (mezo >> plusz)) return 1;
    istringstream adatok(szoveg);
    int szam = 0; char maradek;
    bool siker = static_cast<bool>(adatok >> szam);
    bool teljes = siker && !(adatok >> maradek);
    cout << (jelszo == "MODE") << ' ' << teljes << '\n';
}
```

Várt kimenet:

```text
1 0
```

A string tárolja a sort, az sstream az istringstream típust adja. A mezo két külön stringet olvas, és megpróbál egy harmadikat: ha van, hibás a formátum. Az adatok csak a második token szövegét vizsgálja. A 2 kiolvasható, de az x maradék, így a teljes hamis. A && rövidzár: ha a számolvasás sikertelen, nem vizsgáljuk tovább.

A célban mindkét token szám, és tartományt is ellenőrzöl; a projektben a meglévő felvételi szabályokat kell meghívnod. A MODE név ellenőrzése nem ezt oldja meg.

## M5 – Ideiglenes állapot

```cpp
#include <iostream>
using namespace std;

class Szint {
private:
    int ertek;
public:
    Szint() : ertek(5) {}
    int leker() const { return ertek; }
    bool beallit(int szam) {
        if (szam < 0 || szam > 10) return false;
        ertek = szam; return true;
    }
};
int main() {
    Szint eredeti, ideiglenes;
    bool elso = ideiglenes.beallit(8);
    bool masodik = ideiglenes.beallit(12);
    if (elso && masodik) eredeti = ideiglenes;
    cout << eredeti.leker() << '\n';
}
```

Várt kimenet:

```text
5
```

Két külön Szint objektumunk van. A 8 beállítása sikerül az ideiglenesen, a 12 nem. Az eredeti csak két siker után kapna új értéket, ezért 5 marad. A false önmagában nem von vissza változtatást: az eredetit az védi, hogy addig hozzá sem nyúltunk.

A projektben nem két ismert kérés, hanem ismeretlen számú fájlsor lehet. Bármelyik rekord hibája megakadályozza a végső objektumcserét.

## M6 – Kimeneti szövegfolyam

```cpp
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main() {
    ostringstream szoveg;
    int ertek = 9;
    szoveg << "LEVEL=" << ertek << ";READY=" << (ertek >= 5);
    string eredmeny = szoveg.str();
    cout << eredmeny << '\n';
}
```

Várt kimenet:

```text
LEVEL=9;READY=1
```

Az ostringstream egy memóriabeli kimenet, az sstream fejlécből. A << a számot karakterekké alakítja, a str() string értéket ad vissza. Csak a cout sor nyomtat. A szöveg építése nem nyit fájlt.

P5-ben az aktuális pénztár két lekérdezőjéből készítesz jelentést, amelyet a tagfüggvény visszaad.

## M7 – Fejléc külön ellenőrzése

```cpp
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    { ofstream fajl("header_demo.txt"); if (!fajl) return 1;
      fajl << "COLORS 2\nblue\n"; fajl.close(); if (!fajl) return 1; }
    ifstream bemeno("header_demo.txt"); if (!bemeno) return 1;
    string fejlec;
    if (!getline(bemeno,fejlec) || fejlec != "COLORS 2") return 1;
    string sorAdat;
    while (getline(bemeno,sorAdat)) cout << sorAdat << '\n';
    if (bemeno.bad() || !bemeno.eof()) return 1;
}
```

Várt kimenet:

```text
blue
```

Az első getline a fejlécé, nem adatrekordé. A || rövidzár miatt sikertelen olvasás után rögtön hiba lesz. Az egyenlőség a teljes szöveget vizsgálja, ezért más verzió vagy plusz szóköz eltérés. A következő getline már az első adatot veszi.

A projekt fejlécét nem COLORS 2-nek, hanem TICKETS 1-nek kell tekinteni; a további sorok két egész helykoordinátát adnak, nem színneveket.
