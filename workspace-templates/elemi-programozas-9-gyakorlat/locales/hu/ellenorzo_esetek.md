# EP_09 – Normatív ellenőrző esetek

Az elvárt eredmények nem elvégzett tanulói futások. A bizonyíték az aktuális kód, az azonosítható kimenet/fájltartalom, illetve külön jelölve a tanulói beszámoló. Már igazolt próbát csak érintő módosítás vagy ellentmondás esetén kérünk újra. Nem kell minden korábbi próbahívást a végső fájlban egyszerre megtartani.

A3.b.5 hiányzó fájlos próbáját a B1.2 ellenőrzése igazolhatja, ha ugyanaz a saját A3-beolvasó van a B1-ben. Nem kell kétszer megismételni ugyanazt a bizonyított viselkedést. Az A2.4 / A3.a.3 / A3.a.4 sorok több rövid esetet foglalnak egy azonosító alá; csak az összes ott felsorolt próba után teljesek.

A kivétel üzenetének pontos szövege nincs beégetve: a típus és a megfelelő, nem üres ok számít. A sorok sorrendje, a fizikai sorszám, a pozitív darab, a nulla ár és a visszatérési típus viszont lényegi.

## A1

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| A1.1 | fizetendo=800; terminálválaszok egymás után: alma, -10, 500, 1000 | Az alma konverziós hiba; -10 és 500 kevés. Az utolsó önálló felajánlás 1000, visszajáró 200 Ft. Nem adódnak össze a felajánlások. |
| A1.2 | fizetendo=800; terminálválasz: 800 | Visszatérés 800, visszajáró 0 Ft; nem kér újra. |
| A1.3 | fizetendo=0; terminálválaszok: -1, 0 | -1 elutasított; 0 elfogadott, visszajáró 0. Csak a paraméter változik. |

## A2

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| A2.1 | termek="kávé", darab=2, alapárjegyzék | 900 egész érték; a főprogram sikerüzenete ezt mutatja. |
| A2.2 | termek="víz", darab=3 | 0 egész érték; nem hiba. |
| A2.3 | termek="kakaó", darab=1 | ValueError, az üzenet az ismeretlen termékre utal. A főprogram közli a hibát, nincs Tételösszeg sikerüzenet. |
| A2.4 | Ismert termék; darab=0, majd külön próbában -2 | Mindkét eset ValueError, pozitív darabszámra utaló üzenettel. |
| A2.5 | A kávé árát a próba előtt 500-ra változtatod; termek="kávé", darab=2 | 1000; a függvény csak a paraméterben kapott szótárat használja, a bemeneteket nem módosítja. |

## A3.a

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| A3.a.1 | sor=" kávé ; 2 ; 450\n" (a \n itt valódi sortörés) | ("kávé", 2, 450): szöveg és két egész, a szélső whitespace eltűnik. |
| A3.a.2 | sor="víz;3;0", végső sortörés nélkül | ("víz", 3, 0); a nulla egységár érvényes. |
| A3.a.3 | Külön próbák: `hibas sor`, `kávé;1;450;extra`, `;1;100` | Mindhárom ValueError: hibás mezőszám vagy üres terméknév; a hívó kezeli a jelzést. |
| A3.a.4 | Külön próbák: `tea;ketto;350`, `tea;0;350`, `tea;1;-50` | Mindhárom ValueError: konverzió, nem pozitív darab, illetve negatív egységár. |

## A3.b

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| A3.b.1 | eladasok_jo.txt | Rekordok sorrendben: (kávé,2,450), (tea,1,350), (víz,3,0), (kávé,1,500); hibák=[]; üres sorok=0. |
| A3.b.2 | eladasok_vegyes.txt | Ugyanaz a 4 jó rekord; hibalista 5 elemmel, sorszámok 2,6,8,9,10 és értelmes ok; üres sorok=1. |
| A3.b.3 | ures.txt | ([], [], 0). Az üres fájl sikeres, üres beolvasás. |
| A3.b.4 | eladasok_hibas.txt | ([], [(1,ok),(2,ok),(3,ok)], 0), az okok nem üresek. Nem keletkezik kitalált 0 árú jó rekord. |
| A3.b.5 | ep09_nincs_naplo.txt (nem létezik) | FileNotFoundError továbbterjed a hívóhoz; nem tér vissza álcázott ([],[],0). Ezt a próbát a B1 főprogramjával fejezzük be, a fájlt nem hozzuk létre. |

## B1

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| B1.1 | A3 saját függvényei; bemenet=eladasok_vegyes.txt, cél=bufe_jelentes.txt | True; 4 érvényes rekord, 7 darab, 1750 Ft, 5 hiba, 1 üres sor, részleges állapot. Mentett jelentés sikerüzenet és végül a finally lezáró üzenete. |
| B1.2 | A B1.1 célját megtartva bemenet=ep09_nincs_naplo.txt | False és hiányzó bemenetet jelző üzenet; a korábbi cél bájtra változatlan, nincs sikerüzenet. A finally lefut. |
| B1.3 | bemenet=ures.txt, cél=bufe_jelentes.txt | True; 0 rekord/darab/bevétel/hiba/üres sor; nincs feldolgozható eladás. A korábbi sorok eltűnnek. |
| B1.4 | bemenet=eladasok_jo.txt, cél=ures.txt/jelentes.txt; az ures.txt változatlanul 0 bájtos fájl | False és mentési OSError-üzenet; nincs sikerüzenet, a finally lefut, az ures.txt és a forrás megmarad. |
| B1.5 | bemenet=eladasok_valtott.txt, rendes külön cél; majd ugyanaz még egyszer | Mindkét futás True; a riport 3 rekord, 6 darab, 2140 Ft. A második mentés nem dupláz. |

## Z1

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| Z1.1 | kosar=[("kávé",2),("víz",3)]; alapárjegyzék | (900, []); a főprogram Fizetendő: 900 Ft üzenetet ad. |
| Z1.2 | kosar=[("víz",3)] | (0, []); a 0 valós fizetendő összeg, nem hibajelzés. |
| Z1.3 | kosar=[("kávé",1),("kakaó",1),("tea",0),("víz",2)] | (None, hibalista), két hiba a 2. és 3. tételhez. Nincs Fizetendő sikerüzenet és nincs 450 Ft-os részfizetés. |
| Z1.4 | kosar=[] | (0, []), hiba nélkül; a főprogram közölheti, hogy nincs rendelés. Nem kér fizetési inputot. |
| Z1.5 | kosar=[("tea",2),("tea",1)]; az árjegyzék tea ára előbb 400 | (1200, []); az ismétlődő tételek mind számítanak. Minden Z1-próbában a kosár és árjegyzék változatlan. |

## C1

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| C1.1 | Új, még nem létező uj_eladasok.txt; kosár [("kávé",2),("víz",3)]; alapárak | True; két rekord: kávé;2;450 és víz;3;0, mindkettő sortöréssel. Második futás után négy sor, a korábbi két sor megmarad. |
| C1.2 | Meglévő cél tartalmát megtartva kosár [("kávé",1),("tea",0)]; utána ugyanez másik, még nem létező célra | False; meglévő cél bájtra változatlan, hiányzó cél nem jön létre. A valid kávé sem kerül részlegesen a naplóba. |
| C1.3 | Üres kosár, még nem létező cél | True, nincs mentendő tétel; a cél nem jön létre. |
| C1.4 | Érvényes kosár, cél=ures.txt/naplo.txt | False és OSError-visszajelzés; nincs sikerüzenet, a források és az ures.txt változatlanok. |
