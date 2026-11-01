# CPP_08 v2 – Alapozó feladatok

| Blokk | Tartalom | Irányadó idő |
|---|---|---:|
| 1. | G08_01: 11, G08_02: 11, G08_03: 11, G08_04: 12 perc | 45 perc |
| 2. | Könyvtári projekt, P1–P6 | 45 perc |
| 3. | T1: 15, T2: 25, visszajelzés: 5 perc | 45 perc |

A szünetek ezen felül értendők. Az idők támpontok, nem teljesítési bizonyítékok.
Minden rész: nagy kép → analóg program → kulcssorok → eltérés megnevezése → egy hallgatói teendő → mentés/RUN → ellenőrzés.
A forrásfájlban csak kezdőadatok vannak. Ne írd be a kért osztályt, függvényfejléceket, feltételeket vagy ciklusokat a hallgató helyett.

## G08_01 – Időtartam: tárolás és számítás

**Fájl:** G08_01_idotartam.cpp. **Minta:** M1.

### A – az összes perc tárolása

Készíts Idotartam struktúrát egy int percek = 0; adattaggal.
Legyen void hozzaad(int mennyiseg) tagfüggvénye, amely növeli a saját percek adattagját.
A feladatban nemnegatív, kis egész percekkel dolgozunk; itt még nem kell hibakezelés.
Készíts int orak() és int maradekPercek() lekérdezőt.
A teljes órákhoz egész osztás, a megmaradó percekhez 60-nal vett maradék kell. Egész operandusoknál a / egész hányadost, a % maradékot ad.
A main hozzaad hívással töltse fel a 90 perces kezdőértéket, és a két lekérdezővel írja ki az órát és percet.
Ellenőrzés: 1 óra 30 perc. Az eredményt ne előre beírt számokkal írja ki.

### B – újabb hívás ugyanazon objektumon

Adj hozzá 45 percet ugyanahhoz az objektumhoz; a két lekérdező számolja az új megjelenítést.
Ellenőrzés: 2 óra 15 perc.
Átviteli próba: további 45 perc után 3 óra 0 perc.
Röviden tisztázzátok, miért nem elég 60-at kivonni egyszer.
A záró const részletes vizsgálata a következő feladatban jön.

## G08_02 – Téglalap és const pillanatkép

**Fájl:** G08_02_teglalap.cpp. **Minta:** M2.

### A – két külön képlet

Készíts Teglalap struktúrát double szelesseg = 1.0; és double magassag = 1.0; adattagokkal.
Készíts void meretez(double ujSzelesseg, double ujMagassag), double terulet() const és double kerulet() const tagfüggvényeket.
A feladatban pozitív, véges oldalak adottak; most nem kell tartományellenőrzés.
A main hozzon létre 3×2-es alakzatot és róla const Teglalap alap = alakzat; másolatot.
A módosítható alakzatot méretezze 4×3-ra. Írja ki mindkét objektum területét és kerületét.
Ellenőrzés: alap 6 és 10; módosított 12 és 14; az alap továbbra is 6 és 10.

### B – szándékos fordítási hiba

Egyszer próbáljon meretez hívást végezni az alap konstans objektumon.
Az első lényeges fordítási üzenet alapján magyarázza meg a tiltást.
Távolítsa el a hibás hívást, majd újra fordítson és futtasson. A végleges kód helyes legyen.
Ne a const eltávolításával kerülje meg a feladat célját.
Átviteli próba: egy új 2×2-es konstans alakzat lekérdezése legyen 4 és 8.

## G08_03 – Lámpák: privát állapot és másolás

**Fájl:** G08_03_lampa.cpp. **Minta:** M3.

### A – egy lekérdező két adattagra támaszkodik

Készíts Lampa osztályt: private bool bekapcsolt = false; és int fenyero = 0;.
Nyilvános műveletei: void bekapcsol(), void kikapcsol(), void fenyeroBeallit(int ujFenyero), bool vilagitE() const.
A vilagitE csak akkor igaz, ha a lámpa be van kapcsolva ÉS a fényereje pozitív.
A feladatban 0–100 közötti fényerők adottak; itt még nem kell ellenőrző setter.
Két objektum mindegyikén állíts 50-es fényerőt, de csak az elsőt kapcsold be.
Ellenőrzés: igaz/hamis. Az első kikapcsolása után hamis/hamis.
Egyszer próbálj közvetlenül írni az elso.fenyero mezőbe; a fordítási hibát a nyilvános művelettel helyettesítve javítsd.

### B – a másolat független

Az elsőt kapcsold vissza, majd másoló inicializálással készíts masolat nevű példányt.
A másolat fényerejét állítsd 0-ra. Az eredeti világítson, a másolat ne.
Utána add az elsőt a már létező másolatnak; az ismét világítson.
Átviteli próba: a bekapcsolt, de 0 fényerejű állapot önmagában is maradjon hamis.
A private nem tiltja az egész egyszerű objektum másolását.

## G08_04 – Tartály töltése és ürítése

**Fájl:** G08_04_tartaly.cpp. **Minta:** M4.

### A – töltés a szabad hely függvényében

Készíts Tartaly osztályt private int kapacitas = 10; és int tartalom = 0; adattagokkal.
A main kapacitas konstansa csak kezdőadat; az osztály saját adattagját külön kell definiálni.
A bool betolt(int mennyiseg) pozitív, szabad helyet meg nem haladó mennyiséget fogadjon el.
Siker esetén növelje a tartalmat; hibánál hamis eredmény és változatlan állapot szükséges.
Az int aktualis() const tárolt tartalmat, az int szabadHely() const kiszámított szabad helyet adjon.
6 egység betöltése sikeres: tartalom 6, szabad 4. Újabb 5 egység hibás, tartalom marad 6.

### B – ürítés másik feltétellel

A bool urit(int mennyiseg) pozitív, bent lévő tartalmat meg nem haladó mennyiséget fogadjon el.
A main minden bool eredményt használjon fel, például írja ki a tárolt állapottal együtt.
2 egység ürítése után tartalom 4, szabad 6. Az 5 egységes ürítés hibás, marad 4.
A 0 mennyiséget mindkét művelet utasítsa el.
Átviteli próbák: 6 egység még pontosan betölthető; ekkor tele van. Mind a 10 kiüríthető; ekkor üres.
Ezeket az elvégzett műveletek után ellenőrizzük, nem előzetes kimenetjóslásként.

## Folytatás

A PROJEKT hat lépése következik. Az ottani kölcsönzés/visszavétel feltételeit a hallgató fogalmazza meg; ne kapja meg a tartály kódját átnevezve kész könyvtári megoldásként.
