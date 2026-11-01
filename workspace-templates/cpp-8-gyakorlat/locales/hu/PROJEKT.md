# CPP_08 v2 – Könyvtári kölcsönzési projekt

**Egyetlen munkafájl:** P08_konyvtar.cpp. Nem a HTML mérési projektjét írjuk újra.
Egy Konyv objektum egy könyvtípus több példányát kezeli; az azonosítók kis pozitív egészek, a darabszámok kis egész értékek.
A három privát adattag: int azonosito = 0; int osszes = 0; int kolcsonzott = 0;.
Mindig teljesüljön: 0 <= kolcsonzott <= osszes.
A szabad darabszámot nem tároljuk negyedik mezőben: a két mennyiségből számoljuk.

Szerkezet: osztály → szabad függvények prototípusai → main → szabad függvények definíciói.
A tagfüggvényeket az osztályon belül definiáljuk. Nincs saját konstruktor, referencia-paraméter vagy dinamikus memória.
A tutor minden részt kis lépésekben vezet; a hallgató készíti a kódot.

## P1 – Könyvtípus azonosítása és állománya

**Minta:** M5; szükség szerint az ismert M3 hozzáférési elve. **Idő:** 7 perc.

Készítsd el a Konyv osztályt a fenti adattagokkal.
Nyilvános műveletek:

- void azonosit(int ujAzonosito): tárolja az azonosítót. A feladat helyes, pozitív azonosítókat ad.
- bool allomanyBeallit(int ujOsszes): a teljes példányszámot állítja; negatív vagy a már kölcsönzöttnél kisebb új összest elutasít. A kölcsönzött darabot nem nullázhatja le.
- int azonositoLeker() const és int osszesDarab() const.

Egy új objektumot állíts 501-esre, összesen 5 példánnyal. A main ellenőrizze a bool eredményt.
Próbálj -1 teljes darabszámot: sikertelen, az 5 maradjon meg.
A képernyőre írt állapot a lekérdezőkből származzon, ne a forráskonstansokból.

## P2 – Számított lekérdezés és konstans pillanatkép

**Minta:** M2, csak a másolat/const elve. **Idő:** 6 perc.

Add hozzá az int kolcsonzottDarab() const, int szabadDarab() const és void kiir() const műveleteket.
A szabadDarab a teljes és kölcsönzött mennyiség különbségét adja, nem külön tárolt értéket.
A kiir egy sorban jelenítse meg: azonosító, összes, kölcsönzött, szabad.
Ellenőrzés: 501 5 0 5.
Készíts const Konyv pillanatkep = konyv; másolatot, és hívd meg a kiir és szabadDarab műveleteket rajta.
A pillanatképen egyszer szándékosan próbálj allomanyBeallit hívást; a hibát eltávolítva fordíts újra.

## P3 – Kölcsönzés: van-e elég szabad példány?

**Minta:** M4, az előzetes ellenőrzés elve. **Idő:** 7 perc.

Készíts bool kolcsonoz(int mennyiseg) tagfüggvényt.
Csak pozitív és a szabad mennyiséget meg nem haladó kérés sikerülhet.
Siker esetén a kölcsönzött darab nő; az összes példányszám nem változik.
Elutasításkor egyik adattag sem változhat. A main használja fel az eredményt és írja ki a tényleges állapotot.

5 összesből 3 kölcsönzése sikeres: 501 5 3 2.
Ezután 4 kölcsönzése hibás; maradjon 501 5 3 2.
A 0 és -1 kérés is legyen hibás. Ezek után 3 kölcsönzött és 2 szabad példánnyal folytass.

## P4 – Visszavétel és az adattagok kapcsolatának megőrzése

**Minta:** M5 kapcsolati feltétele; csak az eltérést magyarázd újra. **Idő:** 7 perc.

Készíts bool visszavesz(int mennyiseg) műveletet.
Csak pozitív, ténylegesen kölcsönzött mennyiséget meg nem haladó visszavétel sikerülhet.
Siker esetén a kölcsönzött darab csökken, az összes változatlan.
A 3 kölcsönzöttből 1 visszavétele után: 501 5 2 3.
Újabb 3 visszavétele hibás, mert már csak 2 van kölcsönben. A 0 és -1 is hibás.
Próbálj ekkor 1-re csökkenteni az összes darabot: az allomanyBeallit utasítsa el, mert 2 példány kölcsönben van.
Határpróba: mind a 2 visszavehető; utána 0 kölcsönzött és 5 szabad. A további egyobjektumos próbákhoz ismét 2-t kölcsönözz ki.

## P5 – Hat könyvtípus és összesítés

**Minták:** M6 bejárás, M7 feldolgozó függvény. **Idő:** 10 perc.

A P1–P4 egyobjektumos próbái után a main a starter forrásaiból töltsön fel egy tömböt; ne legyen párhuzamos második projekt.

| Azonosító | Összes | Kezdeti kölcsönzés |
|---|---:|---:|
| 501 | 5 | 3 |
| 502 | 3 | 3 |
| 503 | 0 | 0 |
| 504 | 7 | 2 |
| 505 | 4 | 0 |
| 506 | 2 | 1 |

A main-ben hozz létre 6 Konyv objektumot tartalmazó tömböt. A tömb elemeit ciklusban állítsd be: azonosítás, ellenőrzött állománybeállítás, majd a pozitív kezdeti kölcsönzés végrehajtása.
A 0 kezdeti kölcsönzés azt jelenti, hogy nincs ilyen művelet; ne hívd a pozitív kérést elváró kolcsonoz(0)-t.
Bármely hibás forrásműveletnél jelezz hibát, és ne számolj sikeresen betöltöttnek hibás rekordot.
Készíts szabad függvényeket const Konyv* és külön meret paraméterrel:

- void osszesKiirasa(...): minden rekord kiir műveletét meghívja.
- int osszSzabad(...): a számított szabad darabszámok összege.
- int elfogyottCimek(...): hány könyvtípusnál 0 a szabad darabszám.

Ellenőrzés: 12 szabad példány és 2 olyan cím, amelyből nem kölcsönözhető példány. Az 503-as nulla állományú cím is ebbe a kettőbe számít.
A szabad függvények nem érhetik el közvetlenül a privát adatokat.
Kiegészítő próba, új feladat nélkül: 0 elemszámra az összeg és a darabszám 0 legyen, a mutatóból ne olvass.

## P6 – Próbakölcsönzés másolaton és eredeti példányon

**Minta:** M8. **Idő:** 8 perc.

### P6_A – a paraméterobjektum önálló

Készíts Konyv probakolcsonzes(Konyv konyv, int mennyiseg) szabad függvényt.
A saját paraméterobjektumon próbáljon kölcsönözni, a bool eredményt jelenítse meg, és térjen vissza a teljes objektummal.
Az első tömbelemről készíts külön másolatot 2 példány kölcsönzésével.
Ellenőrzés: eredeti 501 5 3 2, másolat 501 5 5 0; a tömb összesítése továbbra is 12 és 2.

### P6_B – az eredeti módosul

Készíts bool eredetinKolcsonoz(Konyv* konyv, int mennyiseg) függvényt.
A mutatón át nyilvános tagfüggvényt hívjon, és adja vissza a művelet sikerét.
Az első eredeti elemen 1 példány kölcsönzése sikeres: 501 5 4 1.
Az új összesítés 11 szabad példány, továbbra is 2 elfogyott cím.
Újabb 2 kölcsönzése hibás; a rekord és a 11/2 összesítés változatlan maradjon.

Végül röviden magyarázd el: miért külön művelet a kölcsönzés és a visszavétel, és miért nem kell külön tárolni a szabad darabszámot?
