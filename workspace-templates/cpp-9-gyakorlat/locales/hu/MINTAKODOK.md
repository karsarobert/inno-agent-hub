# CPP_09 – Magyarázott analóg minták

Minden program önállóan futtatható. Inno a szükséges mintát a beszélgetésben is bemutatja, megmagyarázza, majd megnevezi az eltérést a saját feladattól. Ezek nem a célprogram részekre osztott megoldásai. Már megértett mintát nem kell minden későbbi lépésnél újraelemezni.

## M1 – Szakasz háromféle létrehozással

```cpp
#include <iostream>
using namespace std;


class Szakasz {
private:
    int kezdet;
    int veg;
public:
    Szakasz() : kezdet(0), veg(0) {}
    Szakasz(int hossz) : kezdet(0), veg(hossz) {}
    Szakasz(int ujKezdet, int ujVeg) : kezdet(ujKezdet), veg(ujVeg) {}
    int hossz() const { return veg - kezdet; }
};
int main() {
    const Szakasz kezdeti;
    const Szakasz egyAdattal(6);
    const Szakasz teljes(3, 11);
    cout << kezdeti.hossz() << ' ' << egyAdattal.hossz() << ' ' << teljes.hossz() << '\n';
    return 0;
}
```

Kimenet:

```text
0 6 8
```

Az argumentum nélküli szakasz 0/0 végponttal, az egyparaméteres 0-tól a kapott hosszig, a kétparaméteres a kapott két végponttal indul. A hossz különbségből számolt lekérdezés; nem tároljuk újabb tagként. A három létrehozás három paraméterlistát választ. A hallgatói versenyzőnél két tárolt mezőt kell lekérdezni, nem végpontkülönbséget számolni.

## M2 – Irány kiválasztása feltételes kifejezéssel

```cpp
#include <iostream>
using namespace std;


class Irany {
private:
    int jel;
public:
    Irany(int bemenet) : jel(bemenet < 0 ? -1 : 1) {}
    int jelLeker() const { return jel; }
};
int main() {
    const Irany bal(-4);
    const Irany jobb(7);
    const Irany kezdeti(0);
    cout << bal.jelLeker() << ' ' << jobb.jelLeker() << ' ' << kezdeti.jelLeker() << '\n';
    return 0;
}
```

Kimenet:

```text
-1 1 1
```

A bemenet < 0 feltétel dönti el a kezdőjelet. Igaz esetben -1, egyébként 1 az eredmény; itt a 0 szándékosan az 1 ágat választja. Csak a kiválasztott ág értékelődik ki. Az eredmény a jel(...) inicializálóba kerül a konstruktor törzse előtt. A fényerőfeladatban más a döntés: teljes tartományt kell vizsgálni, és hibás bemenethez 50-et választunk. A konkrét tartományfeltételt a hallgató írja.

## M3 – Irat és nyomtató együttműködése

```cpp
#include <iostream>
using namespace std;


class Irat {
private:
    int oldalak;
    bool szines;
public:
    Irat(int ujOldalak, bool ujSzines) : oldalak(ujOldalak), szines(ujSzines) {}
    int oldalakLeker() const { return oldalak; }
    bool szinesE() const { return szines; }
};
class Nyomtato {
private:
    int oldalankent;
    int szinesFelAr;
public:
    Nyomtato(int ertek, int felar) : oldalankent(ertek), szinesFelAr(felar) {}
    int koltseg(Irat irat) const {
        int egysegar = oldalankent;
        if (irat.szinesE()) { egysegar += szinesFelAr; }
        return irat.oldalakLeker() * egysegar;
    }
};
int main() {
    const Irat irat(3, true);
    const Nyomtato nyomtato(10, 30);
    cout << nyomtato.koltseg(irat) << '\n';
    return 0;
}
```

Kimenet:

```text
120
```

Az Irat az oldalszámot és a színességet tárolja. A Nyomtato az oldaldíjat és a színes oldalankénti felárat tárolja; koltseg művelete az irat lekérdezőivel dolgozik. A paraméter érték szerinti másolat. A 3 színes oldal ára 3 × (10 + 30) = 120. A postai feladat ettől eltér: alapdíj, megkezdett 500 grammos egységek és küldeményenkénti sürgősségi felár szerepel benne. Ezt nem elég átnevezni.

## M4 – Tagobjektumok közvetlen inicializálása

```cpp
#include <iostream>
using namespace std;


class Pont {
private:
    int x;
    int y;
public:
    Pont(int ujX, int ujY) : x(ujX), y(ujY) {}
    int xLeker() const { return x; }
    int yLeker() const { return y; }
};
class Terulet {
private:
    Pont bal;
    Pont jobb;
public:
    Terulet(int kezdet, int veg) : bal(kezdet, 0), jobb(veg, 0) {}
    int xOsszeg() const { return bal.xLeker() + jobb.xLeker(); }
};
int main() {
    const Terulet terulet(2, 8);
    cout << terulet.xOsszeg() << '\n';
    return 0;
}
```

Kimenet:

```text
10
```

A Terulet két Pont objektumot tartalmaz. A bal(kezdet, 0) és jobb(veg, 0) taginicializálók a Pont konstruktorát hívják. Ez azért is fontos, mert a Pontnak nincs argumentum nélküli konstruktora: a törzsben adott értékadás már túl késő lenne az első létrehozásához. Az eredménylapnál ezzel szemben van alapértelmezett konstruktor, ezért létrejöhet a tömb, amelyet a törzsben később feltöltünk. A példában az xOsszeg csak a két x összege, nem geometriai terület.

## M5 – Dobás érvényessége

```cpp
#include <iostream>
using namespace std;


class Dobas {
private:
    int lapErtek;
public:
    Dobas() : lapErtek(0) {}
    Dobas(int ujLapErtek) : lapErtek(0) {
        if (ujLapErtek >= 1 && ujLapErtek <= 6) { lapErtek = ujLapErtek; }
    }
    bool ervenyesE() const { return lapErtek >= 1 && lapErtek <= 6; }
    bool parosE() const { return ervenyesE() && lapErtek % 2 == 0; }
};
int main() {
    const Dobas elso(4);
    const Dobas masodik(9);
    cout << elso.ervenyesE() << ' ' << elso.parosE() << '\n';
    cout << masodik.ervenyesE() << ' ' << masodik.parosE() << '\n';
    return 0;
}
```

Kimenet:

```text
1 1
0 0
```

A 0 még nem dobott állapot; csak 1–6 tekinthető érvényesnek. A konstruktor inicializálja a mezőt 0-ra, majd helyes bemenetnél értékadással módosítja. A parosE egyszerre ellenőrzi az érvényességet és a kettővel vett maradékot, így a 0 nem lesz érvényes páros dobás. A Jegy két egymáshoz tartozó mezőt és sorfüggő árat kezel; a dobáspélda ezt nem oldja meg helyette.

## M6 – Objektumtömb a jelzőpanelen

```cpp
#include <iostream>
using namespace std;


class Jelzo {
private:
    bool bekapcsolt;
public:
    Jelzo() : bekapcsolt(false) {}
    void bekapcsol() { bekapcsolt = true; }
    bool bekapcsoltE() const { return bekapcsolt; }
};
class Jelzopanel {
private:
    Jelzo lampak[2];
public:
    bool bekapcsol(int index) {
        if (index < 0 || index >= 2) { return false; }
        lampak[index].bekapcsol();
        return true;
    }
    void lista() const {
        for (int i = 0; i < 2; ++i) { cout << lampak[i].bekapcsoltE() << ' '; }
        cout << '\n';
    }
};
int main() {
    Jelzopanel panel;
    panel.lista();
    cout << panel.bekapcsol(1) << '\n';
    panel.lista();
    cout << panel.bekapcsol(2) << '\n';
    return 0;
}
```

Kimenet:

```text
0 0 
1
0 1 
0
```

A panel létrehozásakor mindkét Jelzo alapértelmezett konstruktora lefut, és mindkettő kikapcsolt. Az indexet ellenőrizzük, mielőtt a tömböt elérjük. A panel mindig két lámpát használ, ezért listázáskor kettőt jár be. A projekt pénztárában ezzel szemben a tényleges darabszám kezdetben 0, és csak az aktív előtagot szabad bejárni. A panel nem tartalmaz hozzáadási vagy jegykeresési megoldást.

## M7 – Keresés és találati index

```cpp
#include <iostream>
using namespace std;


int main() {
    const int adatok[4] = {4, 8, 12, 16};
    const int kivalasztott = 12;
    int talalt = -1;
    for (int i = 0; i < 4; ++i) {
        if (adatok[i] == kivalasztott) { talalt = i; break; }
    }
    // Az index nem azonos a tarolt ertekkel.
    cout << talalt << '\n';
    return 0;
}
```

Kimenet:

```text
2
```

A -1 jelzi a sikertelen keresést. Találatkor a ciklus a hely indexét menti, nem a megtalált 12-es értéket; a break kilép a ciklusból. A példában 2 az index. A foglaláskeresésben egy szám helyett két mező együttes egyezését kell vizsgálni, és a teljes kapacitás helyett csak a tényleges jegyeket. A visszaváltásnál az indexet csak sikeres keresés után használjuk.

## M8 – Egy ismert hely törlése tömbből

```cpp
#include <iostream>
using namespace std;


int main() {
    int adatok[5] = {10, 20, 30, 40, 50};
    int meret = 5;
    const int toroltIndex = 2;
    // A talalat utani elemeket balra mozgatjuk.
    for (int i = toroltIndex; i < meret - 1; ++i) { adatok[i] = adatok[i + 1]; }
    --meret;
    for (int i = 0; i < meret; ++i) { cout << adatok[i] << ' '; }
    cout << '\n';
    return 0;
}
```

Kimenet:

```text
10 20 40 50 
```

A 2-es indexen a 30 található. A ciklus a 40-et, majd az 50-et másolja eggyel balra; i + 1 még aktív elem legyen, ezért a feltétel i < meret - 1. A méret csak ezután csökken. Az utolsó fizikai hely régi 50-es tartalma kívül kerül az aktív tartományon. A jegyprojektben neked kell megkeresned a sor–szék párt, kezelni a hiányzó esetet, majd egész Jegy objektumokat mozgatni.

## M9 – Összegzés forrásadatokból

```cpp
#include <iostream>
using namespace std;


int main() {
    const int mennyiseg[3] = {2, 1, 4};
    const int egysegar[3] = {100, 250, 50};
    int osszeg = 0;
    for (int i = 0; i < 3; ++i) { osszeg += mennyiseg[i] * egysegar[i]; }
    cout << osszeg << '\n';
    return 0;
}
```

Kimenet:

```text
650
```

Az összeg 0-ról indul, és minden tételnél a mennyiség × egységár járul hozzá: 200 + 250 + 200 = 650. Nincs előre beírt végeredmény. A pénztárnál a jegy árát a tagfüggvény adja, és csak a darab aktív jegyet kell összesíteni. A mintában a 3 minden elem tényleges használatát jelöli; ezt nem szabad automatikusan a pénztár kapacitásával helyettesíteni.

## M10 – Névjegyből visszaadott szöveg

```cpp
#include <sstream>
#include <string>
#include <iostream>
using namespace std;


class Nevjegy {
private:
    string nev;
    int iranyitoszam;
public:
    Nevjegy(string ujNev, int ujIranyitoszam) : nev(ujNev), iranyitoszam(ujIranyitoszam) {}
    string nevLeker() const { return nev; }
    int iranyitoszamLeker() const { return iranyitoszam; }
};
string cimke(const Nevjegy* nevjegy) {
    // A folyam szoveget epit; a str() string erteket ad.
    ostringstream szoveg;
    szoveg << nevjegy->nevLeker() << " (" << nevjegy->iranyitoszamLeker() << ")";
    return szoveg.str();
}
int main() {
    const Nevjegy nevjegy("Anna", 7624);
    cout << cimke(&nevjegy) << '\n';
    return 0;
}
```

Kimenet:

```text
Anna (7624)
```

A cimke egy létező Nevjegy címét kapja const mutatóként, és a nyíl operátorral hívja a nyilvános lekérdezőket. Az ostringstream helyi folyam szöveget épít a memóriában; a str() eredményét string értékként adjuk vissza, ezért a helyi folyam megszűnése nem teszi használhatatlanná a visszaadott szöveget. A main végzi a cout-ra írást. A pénztári összefoglalóban más típust, más lekérdezéseket és darab/érték tartalmat kell alkalmaznod.
