# CPP_08 v2 – Rögzített záróteszt

20 kérdés, egyenként. Az első érdemi válasz számít. A T2 első öt programját válasz előtt ne futtasd. Hibakeresésnél az ok és a legkisebb, a célt megőrző javítás is kell. A kérdésekhez nem tartozik hallgatói megoldókulcs.

# T1 – 10 feleletválasztós kérdés

## T1/1

Melyik információt érdemes a két másik adattagból kiszámolni a könyvtári feladatban?

A) Az azonosítót a darabszámból.

B) A kölcsönzött darabot az azonosítóból.

C) A szabad darabot az összes és kölcsönzött különbségéből.

D) Minden lekérdezésnél véletlen új darabszámot.

## T1/2

Melyik állapot felel meg a 0 <= kölcsönzött <= összes szabálynak?

A) Összes 4, kölcsönzött 4.

B) Összes 2, kölcsönzött 3.

C) Összes -1, kölcsönzött 0.

D) Összes 5, kölcsönzött -1.

## T1/3

Miért kell a betöltés és módosítás sikerét a hívónak is kezelnie?

A) Mert a bool csak kiírás után létezik.

B) Mert a false automatikusan leállítja a main-t.

C) Mert a cout minden hibát kijavít.

D) Mert elutasítás után nem szabad a kért változást megtörténtnek tekinteni.

## T1/4

Mikor térjen vissza hamissal egy állapotot megőrző elutasító művelet?

A) Mindig a módosítás után.

B) Az adattagok átírása előtt.

C) Csak a kiírás után.

D) Csak a main végén.

## T1/5

Miért lehet területet számoló const tagfüggvényt hívni egy konstans alakzaton?

A) Mert a const számolást enged, ha közben nem írjuk át a szokásos adattagokat.

B) Mert a const csak int-re vonatkozik.

C) Mert minden double mező szabadon írható.

D) Mert a const megszünteti az adattagokat.

## T1/6

A private adattag mellett melyik állítás helyes?

A) A saját tagfüggvény sem olvashatja.

B) Az objektum biztosan másolhatatlan.

C) A main közvetlenül nem érheti el, de a public tagfüggvény dolgozhat vele.

D) A mező értéke mindig 0.

## T1/7

Mit jelent a const objektumról érték szerint létrehozott, nem const másolat?

A) Egy másik név ugyanarra az objektumra.

B) Külön objektum, amely önállóan módosítható.

C) Mindig fordítási hiba.

D) Automatikusan dinamikusan foglalt mutató.

## T1/8

A class és struct tagjainak hozzáféréséről melyik állítás helyes?

A) A struct soha nem tartalmazhat tagfüggvényt.

B) A class nem tartalmazhat adattagot.

C) Mindkettőnél private az alapértelmezés.

D) A class alapértelmezése private, a struct-é public; mindkettőben használhatók címkék.

## T1/9

Mit kell még átadni egy tömböt olvasó const Konyv* paraméter mellé?

A) A teljes osztálydefiníció szövegét minden hívásban.

B) Az elemszámot, mert a mutató azt nem tárolja.

C) Mindig egy konstruktor nevét.

D) Csak az első rekord darabszámát; abból minden más kiderül.

## T1/10

Egy érték szerint kapott objektumparaméter módosítása önmagában mit változtat meg?

A) A függvény saját paraméterobjektumát.

B) A hívó összes objektumát.

C) A típus összes későbbi példányát.

D) Mindig az eredeti tömb első elemét.

# T2 – 5 kimenet és 5 hibakeresés

## T2/1 – kimenet

Mi a pontos kimenet?

~~~cpp
#include <iostream>
using namespace std;

struct Utvonal {
    int oda = 4;
    int vissza = 6;
    int osszes() const {
        return oda + vissza;
    }
};
int main() {
    Utvonal elso;
    const Utvonal pillanatkep = elso;
    elso.vissza = 9;
    cout << elso.osszes() << ' ' << pillanatkep.osszes() << '\n';
    return 0;
}
~~~

## T2/2 – kimenet

Mi a pontos kimenet?

~~~cpp
#include <iostream>
using namespace std;

struct Kapcsolo {
    bool engedelyezett = false;
    void atvalt() {
        engedelyezett = !engedelyezett;
    }
    bool allapot() const {
        return engedelyezett;
    }
};
int main() {
    Kapcsolo kapcsolo;
    const Kapcsolo alap = kapcsolo;
    kapcsolo.atvalt();
    cout << kapcsolo.allapot() << ' ' << alap.allapot() << '\n';
    return 0;
}
~~~

## T2/3 – kimenet

Mi a pontos kimenet?

~~~cpp
#include <iostream>
using namespace std;

class Lepesszamlalo {
private:
    int ertek = 2;
public:
    bool leptet(int mennyiseg) {
        if (mennyiseg <= 0 || mennyiseg > 3) {
            return false;
        }
        ertek += mennyiseg;
        return true;
    }
    int leker() const {
        return ertek;
    }
};
int main() {
    Lepesszamlalo aktualis;
    cout << aktualis.leptet(3) << ' ' << aktualis.leptet(4) << ' ' << aktualis.leker() << '\n';
    return 0;
}
~~~

## T2/4 – kimenet

Mi a pontos kimenet?

~~~cpp
#include <iostream>
using namespace std;

class Eredmeny {
private:
    int ar = 0;
    bool aktiv = false;
public:
    void beallit(int ujAr, bool ujAktiv) {
        ar = ujAr;
        aktiv = ujAktiv;
    }
    int beszamit() const {
        if (!aktiv) {
            return 0;
        }
        return ar;
    }
};
int main() {
    Eredmeny eredmenyek[3];
    eredmenyek[0].beallit(7, true);
    eredmenyek[1].beallit(20, false);
    eredmenyek[2].beallit(3, true);
    int osszeg = 0;
    for (int i = 0; i < 3; ++i) {
        osszeg += eredmenyek[i].beszamit();
    }
    cout << osszeg << '\n';
    return 0;
}
~~~

## T2/5 – kimenet

Mi a pontos kimenet?

~~~cpp
#include <iostream>
using namespace std;

class Irany {
private:
    bool negativ = false;
public:
    void megfordit() {
        negativ = !negativ;
    }
    int elojel() const {
        if (negativ) {
            return -1;
        }
        return 1;
    }
};
Irany forditottMasolat(Irany irany) {
    irany.megfordit();
    return irany;
}
int main() {
    Irany eredeti;
    Irany masolat = forditottMasolat(eredeti);
    cout << eredeti.elojel() << ' ' << masolat.elojel() << '\n';
    Irany* mutato = &eredeti;
    mutato->megfordit();
    cout << eredeti.elojel() << ' ' << masolat.elojel() << '\n';
    return 0;
}
~~~

## T2/6 – hibakeresés

A cél a hangerő 1-ről 2-re emelése a nyilvános művelettel, a mező elrejtésének megtartásával. Mi a fő hiba és a legkisebb helyes javítás?

~~~cpp
#include <iostream>
using namespace std;

class Hangero {
private:
    int szint = 1;
public:
    bool emel() {
        if (szint >= 3) {
            return false;
        }
        ++szint;
        return true;
    }
    int leker() const {
        return szint;
    }
};
int main() {
    Hangero hangero;
    hangero.szint = 2;
    cout << hangero.leker() << '\n';
    return 0;
}
~~~

## T2/7 – hibakeresés

A konstans vizsgálati adatból szeretnénk lekérdezni, páros-e a szám. Mi a fő hiba és a legkisebb helyes javítás?

~~~cpp
#include <iostream>
using namespace std;

struct Vizsgalat {
    int szam = 2;
    bool parosE() {
        return szam % 2 == 0;
    }
};
int main() {
    const Vizsgalat vizsgalat;
    cout << vizsgalat.parosE() << '\n';
    return 0;
}
~~~

## T2/8 – hibakeresés

Az újraindítás szándékosan módosító művelet: az ütemszámot nullázza. Mi a fő hiba és a legkisebb helyes javítás?

~~~cpp
#include <iostream>
using namespace std;

struct Varakozas {
    int utem = 3;
    void ujraindit() const {
        utem = 0;
    }
};
int main() {
    Varakozas varakozas;
    varakozas.ujraindit();
    cout << varakozas.utem << '\n';
    return 0;
}
~~~

## T2/9 – hibakeresés

Csak pozitív, az aktuális százalékot meg nem haladó csökkentés engedélyezett. Elutasításkor az állapot nem változhat. Mi a fő hiba és a legkisebb helyes javítás?

~~~cpp
#include <iostream>
using namespace std;

class Szazalek {
private:
    int szazalek = 100;
public:
    bool csokkent(int csokkentes) {
        szazalek -= csokkentes;
        if (csokkentes <= 0 || szazalek < 0) {
            return false;
        }
        return true;
    }
    int leker() const {
        return szazalek;
    }
};
int main() {
    Szazalek szazalek;
    cout << szazalek.csokkent(120) << ' ' << szazalek.leker() << '\n';
    return 0;
}
~~~

## T2/10 – hibakeresés

A végén a megállóban ténylegesen várakozók aktuális számát kell kiírni, nem a kezdeti bemenetet. Mi a fő hiba és a legkisebb helyes javítás?

~~~cpp
#include <iostream>
using namespace std;

class Megallo {
private:
    int varakozo = 0;
public:
    void erkezik(int mennyiseg) {
        varakozo += mennyiseg;
    }
    int leker() const {
        return varakozo;
    }
};
int main() {
    const int forrasDarab = 2;
    Megallo megallo;
    megallo.erkezik(forrasDarab);
    megallo.erkezik(3);
    cout << forrasDarab << '\n';
    return 0;
}
~~~
