# CPP_08 v2 – Analóg minták

A tutor csak az aktuális mintát mutassa és magyarázza el. Ezek nem a hallgatói feladatok megoldásai. A minta és az alkalmazás közötti eltérést mindig nevezze meg. Minden program külön fordítható.

## M1 – Tagfüggvény és tartós állapot

~~~cpp
#include <iostream>
using namespace std;

struct Jelzes {
    int ertek = 2;
    int lepes = 3;

    void leptet() {
        // Csak ez az objektum valtozik.
        ertek += lepes;
    }

    int kovetkezoErtek() {
        return ertek + lepes;
    }
};

int main() {
    Jelzes jelzes;
    cout << jelzes.kovetkezoErtek() << '\n';
    jelzes.leptet();
    cout << jelzes.kovetkezoErtek() << '\n';
    return 0;
}
~~~

Várt kimenet:

~~~text
5
8
~~~

A lekérdezés itt a következő értéket számolja, a leptet viszont eltárol egy új állapotot. Az időtartamnál más számítás kell: osztás és maradékképzés.

## M2 – Konstans összesítés és külön másolat

~~~cpp
#include <iostream>
using namespace std;

struct Szallitas {
    int aru = 4;
    int csomagolas = 1;

    void aruBeallit(int ujAru) {
        aru = ujAru;
    }

    int bruttoTomeg() const {
        // Az adattagokat olvassuk, egyik sem valtozik.
        return aru + csomagolas;
    }
};

int main() {
    Szallitas szallitas;
    const Szallitas alap = szallitas;
    szallitas.aruBeallit(8);
    cout << alap.bruttoTomeg() << ' ' << szallitas.bruttoTomeg() << '\n';
    return 0;
}
~~~

Várt kimenet:

~~~text
5 9
~~~

A rögzített másolat összesítése változatlan, az eredetié változik. A téglalap feladatban két másik képletet kell megalkotni, nem tömegeket összegezni.

## M3 – Privát koordináták és objektummásolás

~~~cpp
#include <iostream>
using namespace std;

class Pozicio {
private:
    int x = 0;
    int y = 0;

public:
    void elhelyez(int ujX, int ujY) {
        x = ujX;
        y = ujY;
    }

    bool origobanE() const {
        return x == 0 && y == 0;
    }
};

int main() {
    Pozicio elso;
    Pozicio masodik;
    masodik.elhelyez(2, 3);
    Pozicio masolat = elso;
    masolat.elhelyez(1, 0);
    cout << elso.origobanE() << ' ' << masodik.origobanE() << ' ' << masolat.origobanE() << '\n';
    masolat = elso;
    cout << masolat.origobanE() << '\n';
    return 0;
}
~~~

Várt kimenet:

~~~text
1 0 0
1
~~~

A main műveleteken át dolgozik, nem a koordinátamezőkbe ír. A lámpánál más állapot és más logikai feltétel lesz szükséges.

## M4 – Elutasítás állapotváltoztatás előtt

~~~cpp
#include <iostream>
using namespace std;

class PalyaPozicio {
private:
    int x = 1;
    int y = 2;

public:
    bool lep(int dx, int dy) {
        const int ujX = x + dx;
        const int ujY = y + dy;
        // Ellenorzes mindket adattag modositasa elott.
        if (ujX < 0 || ujY < 0) {
            return false;
        }
        x = ujX;
        y = ujY;
        return true;
    }

    void kiir() const {
        cout << x << ' ' << y << '\n';
    }
};

int main() {
    PalyaPozicio hely;
    cout << hely.lep(-2, 0) << '\n';
    hely.kiir();
    cout << hely.lep(2, 1) << '\n';
    hely.kiir();
    return 0;
}
~~~

Várt kimenet:

~~~text
0
1 2
1
3 3
~~~

A jelölt új koordináták kiszámítása még nem írja át az objektumot. A tartályhoz kapacitástól és aktuális tartalomtól függő, a kölcsönzéshez szabad darabszámtól függő feltételt kell készíteni.

## M5 – Két összetartozó érték ellenőrzése

~~~cpp
#include <iostream>
using namespace std;

class Idokoz {
private:
    int kezdet = 0;
    int veg = 0;

public:
    bool rogzit(int ujKezdet, int ujVeg) {
        if (ujKezdet < 0 || ujVeg < ujKezdet) {
            return false;
        }
        kezdet = ujKezdet;
        veg = ujVeg;
        return true;
    }

    int hossz() const {
        return veg - kezdet;
    }
};

int main() {
    Idokoz idokoz;
    cout << idokoz.rogzit(3, 8) << ' ' << idokoz.hossz() << '\n';
    cout << idokoz.rogzit(9, 4) << ' ' << idokoz.hossz() << '\n';
    return 0;
}
~~~

Várt kimenet:

~~~text
1 5
0 5
~~~

A szabály a két érték viszonyát vizsgálja, nem csak külön-külön az előjelüket. A könyvállománynál más kapcsolatot kell megőrizni: a kölcsönzött darab nem haladhatja meg az összeset.

## M6 – Objektumtömb olvasása

~~~cpp
#include <iostream>
using namespace std;

class Jelado {
private:
    int frekvencia = 0;
    bool engedelyezett = false;

public:
    void beallit(int ujFrekvencia, bool ujEngedelyezett) {
        frekvencia = ujFrekvencia;
        engedelyezett = ujEngedelyezett;
    }

    int frekvenciaLeker() const {
        return frekvencia;
    }

    bool engedelyezettE() const {
        return engedelyezett;
    }
};

void osszesKiirasa(const Jelado* jeladok, int meret) {
    // Az elemszamot a mutatotol kulon adjuk at.
    for (int i = 0; i < meret; ++i) {
        if (jeladok[i].engedelyezettE()) {
            cout << jeladok[i].frekvenciaLeker() << '\n';
        }
    }
}

int main() {
    Jelado jeladok[3];
    jeladok[0].beallit(10, true);
    jeladok[1].beallit(20, false);
    jeladok[2].beallit(30, true);
    osszesKiirasa(jeladok, 3);
    return 0;
}
~~~

Várt kimenet:

~~~text
10
30
~~~

A const mutatón át csak olvasunk, az elemszám külön paraméter. A könyvtárban minden rekordot ki kell írni, és a betöltés ellenőrzött műveletekből áll.

## M7 – Feldolgozó szabad függvény

~~~cpp
#include <iostream>
using namespace std;

class Feladat {
private:
    int pont = 0;
    bool kesz = false;

public:
    void beallit(int ujPont, bool ujKesz) {
        pont = ujPont;
        kesz = ujKesz;
    }

    int pontLeker() const {
        return pont;
    }

    bool keszE() const {
        return kesz;
    }
};

int legnagyobbKesz(const Feladat* feladatok, int meret) {
    int legjobb = 0;
    for (int i = 0; i < meret; ++i) {
        if (feladatok[i].keszE() && feladatok[i].pontLeker() > legjobb) {
            legjobb = feladatok[i].pontLeker();
        }
    }
    return legjobb;
}

int main() {
    Feladat feladatok[3];
    feladatok[0].beallit(4, true);
    feladatok[1].beallit(20, false);
    feladatok[2].beallit(7, true);
    cout << legnagyobbKesz(feladatok, 3) << '\n';
    return 0;
}
~~~

Várt kimenet:

~~~text
7
~~~

A példa nemnegatív pontokat feltételez, és maximumot keres a kész feladatok között. A könyvtári összesítésben más bejárási művelet kell: összeadás, illetve feltételes számlálás.

## M8 – Értékparaméter és eredeti objektum

~~~cpp
#include <iostream>
using namespace std;

class Jelolo {
private:
    int hely = 0;

public:
    void eltol(int tavolsag) {
        hely += tavolsag;
    }

    int helyLeker() const {
        return hely;
    }
};

Jelolo eltoltMasolat(Jelolo aktualis, int tavolsag) {
    // Ez a parameter onallo masolat.
    aktualis.eltol(tavolsag);
    return aktualis;
}

void eredetitEltol(Jelolo* aktualis, int tavolsag) {
    // Nyilvanos tagfuggvenyt hivunk a mutaton keresztul.
    aktualis->eltol(tavolsag);
}

int main() {
    Jelolo eredeti;
    Jelolo masolat = eltoltMasolat(eredeti, 4);
    eredetitEltol(&eredeti, -2);
    cout << eredeti.helyLeker() << ' ' << masolat.helyLeker() << '\n';
    return 0;
}
~~~

Várt kimenet:

~~~text
-2 4
~~~

Az értékparaméter másolat; a mutató a meglévő objektumot éri el. A könyvkölcsönzésnél ezen felül kezelni kell a művelet logikai eredményét és az elutasított kérést.

## M9 – Keresés visszaadott indexszel

~~~cpp
#include <iostream>
using namespace std;

class Csomag {
private:
    int kod = 0;

public:
    void kodBeallit(int ujKod) {
        kod = ujKod;
    }

    bool egyezikE(int keresett) const {
        return kod == keresett;
    }
};

int indexKeres(const Csomag* csomagok, int meret, int keresett) {
    for (int i = 0; i < meret; ++i) {
        if (csomagok[i].egyezikE(keresett)) {
            return i;
        }
    }
    return -1;
}

int main() {
    Csomag csomagok[2];
    csomagok[0].kodBeallit(41);
    csomagok[1].kodBeallit(72);
    cout << indexKeres(csomagok, 2, 72) << ' ' << indexKeres(csomagok, 2, 99) << '\n';
    return 0;
}
~~~

Várt kimenet:

~~~text
1 -1
~~~

Az index pozíció, nem azonosító. A -1 azt jelzi, hogy nincs megfelelő elem; ilyen indexszel nem szabad a tömböt elérni. Ez csak az opcionális X1-hez szükséges minta.
