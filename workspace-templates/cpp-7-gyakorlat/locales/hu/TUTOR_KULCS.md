# CPP_07 – Tutori és oktatói ellenőrzési kulcs

Nem felolvasandó hallgatói lecke. A tutor a tényleges kód és követelmények alapján ellenőriz, a teljes kulcsot nem adja oda a feladatok előtt.

## Az alapozás ellenőrzése

| Rész | Várt lényeg |
|---|---|
| G07_01 A | Típus mellett konkrét objektum is készült: 101, 23.5, igaz. |
| G07_01 B | Másolat átírása után 23.5 és 30; külön értékadás után 23.5 és 23.5. |
| G07_02 A | Érték szerint kapott paraméter és struktúra visszaadása; eredeti 10.5, új 12.5. |
| G07_02 B | Az eredeti címe és nyilas mezőelérés; eredeti 12, másolat 12.5. |
| G07_03 A/B | Egész 7, majd tört 2.5; a jelző frissül, csak az aktív mezőt olvassa. |
| G07_04 A/B | Belső 20, külső helyi 10, globális 5; a függvény a globális 5-öt látja. |
| G07_04 C | Összeg 6; a ciklusindex kívül nem látható; a végső kód ismét fordítható. |


## Projektellenőrzés

| Ellenőrzési pont | Eredeti adatok | P6 után |
|---|---:|---:|
| Első rekord értéke | 18.5 | 20.5 |
| Érvényes darabszám | 5 | 5 |
| Érvényes összeg az átlag ellenőrzéséhez | 89 | 91 |
| Érvényes átlag | 17.8 | 18.2 |
| Érvényes és 20 feletti | 3 | 4 |
| Érvényes és 21 feletti | 1 | 1 |

A P2 mind a hat rekordot kiírja. A P4 az érvénytelen 26.0-t kizárja, az érvényes
-2.0-t megtartja. Az átlagfüggvényt csak pozitív érvényes darabszámnál hívjuk.
A minden-jelző-hamis próbánál nincs átlaghívás és nullával osztás. Utána az
eredeti adatokat vissza kell állítani.

A P6 az első rekordot közvetlenül változtatja meg. Az azonosító, dátum, logikai
mező és a többi rekord változatlan. A korábbi függvények újra felhasználhatók.
Az 1/0 és igen/nem, valamint a 17.8 és 17.80 egyaránt jó. A 17-re csonkított
átlag hibás. A feliratok és a szóközök eltérhetnek.


## T1 megoldókulcs

### T1/1 – B

A mezőknek nevük van, és típusuk eltérő is lehet.

Témacímke: struktúra és tömb.

### T1/2 – C

A típusdefiníció az adatszerkezetet írja le; a konkrét változót külön hozzuk létre.

Témacímke: típus és objektum.

### T1/3 – A

A másolat külön objektum, amely az eredeti mezőértékeiből inicializálódik.

Témacímke: másolás és inicializálás.

### T1/4 – D

A nyíl a mutató által megmutatott struktúra mezőjét választja ki.

Témacímke: mutató és mezőelérés.

### T1/5 – B

A const az ezen az elérési úton végzett módosítást tiltja; az elemszám külön paraméter.

Témacímke: const és tömbparaméter.

### T1/6 – A

Az inaktív mező olvasása a bemutatott esetben nem definiált viselkedés lenne.

Témacímke: unió aktív mezője.

### T1/7 – C

A jelző kézi megállapodás része; a nyelv nem ellenőrzi automatikusan az összhangot.

Témacímke: jelzővel követett unió.

### T1/8 – D

A fejlécben deklarált változó hatóköre a ciklushoz tartozik.

Témacímke: ciklusváltozó hatóköre.

### T1/9 – B

A hívás nem terjeszti ki a hívó lokális neveinek láthatóságát.

Témacímke: függvények és névkeresés.

### T1/10 – C

Az elrejtés a névkeresést változtatja meg, nem semmisíti meg a külső objektumot.

Témacímke: névelrejtés és élettartam.

## T2 megoldókulcs

### T2/1

```text
8 11
```

Külön objektumokat használunk; a másolat átírása nem változtatja meg az eredetit.

Témacímke: struktúra másolása.

### T2/2

```text
13 14
```

Az emelt külön másolatot ad vissza; később a mutató az eredeti objektumot módosítja.

Témacímke: érték szerinti átadás és mutató.

### T2/3

```text
10
```

A 100-as értéket kihagyjuk; a két érvényes mérés átlaga (8+12)/2.

Témacímke: érvényes adatok szűrése.

### T2/4

```text
4 1.5
```

Mindkét kiolvasáskor az akkor aktív mezőt olvassuk; a régi mezőt a váltás után nem használjuk.

Témacímke: unió aktív mezője.

### T2/5

```text
20 5 10
```

A belső név 20-at jelöl, a kiir a globális 5-öt látja, a blokk után a main helyi értéke 10.

Témacímke: névelrejtés és névkeresés.

### T2/6

A struktúra definícióját lezáró kapcsos zárójel után hiányzik a pontosvessző.

Fordítási hiba. Legkisebb javítás: a struktúra záró kapcsos zárójele után pontosvessző.

Témacímke: struktúradefiníció szintaxisa.

### T2/7

A mutato mutató, ezért a mutato.ertek hibás.

Fordítási hiba. Javítás: mutato->ertek vagy (*mutato).ertek.

Témacímke: mutató és mezőelérés.

### T2/8

A tort aktív, de az egesz mezőt olvassa.

Nem definiált viselkedés, akkor is, ha a program lefordul. A beállított érték kiírásához adat.tort olvasása a legkisebb javítás. Ha egész érték a cél, előbb az egész mezőt kell megfelelően beállítani. Nem várunk számszerű kimenetet.

Témacímke: inaktív uniómező olvasása.

### T2/9

A darab neve a belső blokkon kívül nem látható.

Fordítási hiba. A kiírás belső blokkba helyezése jó javítás. Ha kívül kell az érték, a változót a külső blokkban deklaráljuk, és belül értékadással töltjük fel; ne új belső változót hozzunk létre.

Témacímke: lokális hatókör.

### T2/10

A ciklus i == meret esetén már a tömbön kívülre lép.

A feltétel i < meret legyen. Az adatok[meret] nem létező elem; a hibás kódot javítás előtt ne futtassuk. A sikeres fordítás önmagában nem bizonyít helyességet.

Témacímke: ciklushatár és tömb.

## Pontozás és lezárás

Minden kérdés 1 pont. T1: 10, T2: 10, összesen 20 pont.
A hibakeresésben az ok és egy működő, legkisebb javítás együttes megfogalmazása
ér 1 pontot. Szakmailag egyenértékű javítás elfogadható.
A kimenetnél a lényegi sorrendet ellenőrizd; a végső sortörés elhagyásáért ne vonj le pontot.

Az első érdemi válasz számít. Utána tanító visszajelzés jár. Az ismétlendő témákat
csak a tényleges hibákból válaszd. Nincs osztályzat, százalékos minősítés, házi
feladat vagy automatikusan bejelentett következő ZH.

