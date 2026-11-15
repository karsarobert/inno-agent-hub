# CPP_10 – Rögzített záróteszt

20 kérdés. T1: 10 választás; T2: 5 pontos kimenet és 5 hibajavítás. Az első érdemi válasz számít. A kódok különálló programok, sikeres fájlhozzáférést feltételeznek, kivéve ahol a kérdés hiányzó fájlt jelöl. Kérdéskódot válasz előtt ne futtass. Javításnál okot és legkisebb helyes módosítást is kérünk.

## T1/1

Miért van TICKETS 1 fejléc?

A. Az 1 azt jelenti, hogy csak egy jegy lehet.
B. Azonosítja a fájlformátumot és a verzióját.
C. Automatikusan megnyitja a fájlt.
D. Megadja az első jegy árát.

## T1/2

Sikeres írás és close() után mi igaz?

A. A bool-konverzió mindig hamis.
B. Az eof() kötelezően igaz.
C. is_open() hamis, de a bool-konverzió igaz lehet.
D. Az objektum azonnal megszűnik.

## T1/3

Mit jelenthet eof=true és fail=false számolvasás után?

A. Az utolsó szám sikeresen kiolvasható volt a fájl végén.
B. A szám kötelezően hibás.
C. Még biztosan van újabb szám.
D. A fájl nem nyílt meg.

## T1/4

Melyik állítás igaz a projekt üres állapotára?

A. Mindkét üresfájl-változat hibás.
B. A teljesen üres fájl helyes, a fejléc hibás.
C. Az üres fájl a régi naplóhoz hozzáfűz nullát.
D. A csak fejlécet tartalmazó fájl helyes; a teljesen üres fájl hibás.

## T1/5

Melyik két rekord ismételt helyfoglalás?

A. 1 2 és 1 3
B. 2 4 és 2 4
C. 1 2 és 2 2
D. 2 1 és 3 1

## T1/6

Miért olvasunk előbb getline-nal, majd istringstream-mel?

A. Így egy rekordot külön szövegfolyamban ellenőrzünk, nem lépünk át a következő sorba.
B. Így nincs szükség hibakezelésre.
C. Így minden fájl automatikusan érvényes.
D. Az ifstream egyáltalán nem tud számot olvasni.

## T1/7

Mit ad vissza az ostringstream str() művelete?

A. A megnyitott fájl nevét.
B. A folyam pointerét.
C. A felépített szöveget string értékként.
D. A sikeres mentés bool értékét.

## T1/8

Miért hibás a teljes jegypénztár ismételt ios::app mentése?

A. Mert az app csak olvasásra jó.
B. Mert int nem írható vele.
C. Mert close() nem használható.
D. Mert újabb fejlécet és ismételt rekordokat fűzhet a fájlhoz.

## T1/9

Melyik fejléc kell a két szövegfolyamtípushoz?

A. <cmath>
B. <sstream>
C. <iomanip>
D. <limits>

## T1/10

Az ok.txt nem nyitható meg RUN-nal, de látszik a munkamappában. Mi legyen az első vizsgálat?

A. Töröljük a fejléc ellenőrzését.
B. Mindig adjunk vissza true-t.
C. A futó program aktuális munkakönyvtárát.
D. A szék árát változtassuk meg.

## T2/1

Mi a pontos kimenet?

```cpp
#include <iostream>
#include <fstream>
using namespace std;

int main() {
    { ofstream fajl("q01.txt"); if (!fajl) return 1;
      fajl << "3\n5\n"; fajl.close(); if (!fajl) return 1; }
    ifstream bemeno("q01.txt"); if (!bemeno) return 1;
    int ertek, darab = 0, osszeg = 0;
    while (bemeno >> ertek) { ++darab; osszeg += ertek; }
    cout << darab << ' ' << osszeg << '\n';
}
```

## T2/2

Mi a pontos kimenet?

```cpp
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main() {
    ostringstream szoveg;
    szoveg << "N=" << 7;
    string eredmeny = szoveg.str();
    eredmeny += "!";
    cout << szoveg.str() << '\n' << eredmeny << '\n';
}
```

## T2/3

Mi a pontos kimenet?

```cpp
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main() {
    istringstream adatok("16");
    int szam = 0;
    adatok >> szam;
    cout << adatok.eof() << ' ' << adatok.fail() << ' '
         << static_cast<bool>(adatok) << '\n';
}
```

## T2/4

Mi a pontos kimenet?

```cpp
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main() {
    istringstream adatok("4x");
    int szam = 0; char maradek = '?';
    bool siker = static_cast<bool>(adatok >> szam);
    bool maradt = static_cast<bool>(adatok >> maradek);
    cout << siker << ' ' << maradt << '\n';
}
```

## T2/5

Mi a pontos kimenet?

```cpp
#include <iostream>
using namespace std;

class Szint {
private:
    int ertek;
public:
    Szint(int szam) : ertek(szam) {}
    bool beallit(int szam) {
        if (szam < 0 || szam > 10) return false;
        ertek = szam; return true;
    }
    int leker() const { return ertek; }
};
int main() {
    Szint eredeti(8), ideiglenes(1);
    ideiglenes.beallit(6);
    bool siker = ideiglenes.beallit(-1);
    if (siker) eredeti = ideiglenes;
    cout << eredeti.leker() << ' ' << ideiglenes.leker() << '\n';
}
```

## T2/6

Miért nem fordul le? Javítsd a visszatérést úgy, hogy a mentés sikerességét adja.

```cpp
#include <iostream>
#include <fstream>
using namespace std;

bool mentes() {
    ofstream fajl("q06.txt");
    if (!fajl) return false;
    fajl << "READY\n";
    fajl.close();
    return fajl;
}
int main() { cout << mentes() << '\n'; }
```

## T2/7

Miért jelenik meg a szám kétszer? A sikeres kiolvasásokhoz kösd a feldolgozást.

```cpp
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main() {
    istringstream bemeno("6\n");
    int ertek = 0;
    while (!bemeno.eof()) {
        bemeno >> ertek;
        cout << ertek << '\n';
    }
}
```

## T2/8

Miért ERROR a kimenet, holott a 25-öt sikerült olvasni? Javítsd a sikeresség vizsgálatát.

```cpp
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main() {
    istringstream adatok("25");
    int ertek = 0;
    adatok >> ertek;
    if (adatok.good()) cout << "OK\n";
    else cout << "ERROR\n";
}
```

## T2/9

Az absent_q09.txt nem létezik. A korábbi 9-et meg kellene őrizni. Hol sérül ez, és mi a legkisebb javítás?

```cpp
#include <iostream>
#include <fstream>
using namespace std;

int main() {
    int eredeti = 9;
    eredeti = 0;
    ifstream fajl("absent_q09.txt");
    if (!fajl) {
        cout << eredeti << '\n';
        return 0;
    }
}
```

## T2/10

Kétszer mentjük ugyanazt a teljes pillanatképet, de hat sor lesz. Hogyan maradjon csak három?

```cpp
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    { ofstream fajl("q10.txt"); if (!fajl) return 1;
      fajl.close(); if (!fajl) return 1; }
    for (int i = 0; i < 2; ++i) {
        ofstream fajl("q10.txt", ios::app);
        if (!fajl) return 1;
        fajl << "TICKETS 1\n1 2\n2 3\n";
        fajl.close(); if (!fajl) return 1;
    }
    ifstream bemeno("q10.txt"); if (!bemeno) return 1;
    string sorAdat; int darab = 0;
    while (getline(bemeno,sorAdat)) ++darab;
    cout << darab << '\n';
}
```
