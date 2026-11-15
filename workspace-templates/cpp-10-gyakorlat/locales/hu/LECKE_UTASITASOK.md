# CPP_10 – Alapozás, 45 perc

Indítás 3 perc; G10_01: 8, G10_02: 9, G10_03: 10, G10_04: 15 perc. A tutor egyszerre egy részlépést ad. A konzolkimenet mellett a létrejött fájl valódi tartalma is bizonyíték.

## G10_01 – Raktári pillanatkép

**Forrás:** G10_01_mentes.cpp. **Analógia:** M1, amely egy állapotszót ír, nem rekordokat.

**G10_01_A:** Hozd létre a stock.txt fájlt ofstream-mel. Írd ki ezt a két rekordot, külön sorokba: `215 7`, `309 12`. Az első mező cikkszám, a második darabszám. Ellenőrizd a megnyitást, zárd le a fájlt, majd ellenőrizd a folyam állapotát is. Sikerüzenet csak ezután jelenjen meg. A fájlt nyisd meg a nézetben; a számok közé szóköz, a rekordok közé újsor kell.

**G10_01_B:** A forrásban módosítsd a második készletet 12-ről 5-re, fordítsd és futtasd újra. A fájl két soros maradjon, a második `309 5`. Ezután a fájlt kézzel is módosítsd, és figyeld meg, hogy az újrafuttatás a forrás szerinti tartalmat állítja vissza. Ez a próba a felülírásról szól. A módosításokat ne fontos állományon próbáld.

Magyarázd el a megnyitás és az írás ellenőrzésének külön szerepét. A close() után a fájl nincs nyitva, de a folyam bool-értéke siker esetén igaz lehet.

## G10_02 – Látogatók hozzáfűzése és összegzése

**Forrás:** G10_02_latogatok.cpp. **Analógia:** M2 szöveges eseményeket kezel; itt számokat kell feldolgoznod.

**G10_02_A:** Egy külön blokkban hozd létre a visits.txt állományt a 4 és 6 számokkal, külön sorban, majd zárd és ellenőrizd. Másik blokkban ios::app móddal fűzd hozzá a 3-at külön sorba; ezt az írást is zárd és ellenőrizd. A fájl sorrendje: 4, 6, 3.

**G10_02_B:** ifstream-mel, `while (bemeno >> ertek)` mintájú ciklussal számold meg és összegezd a számokat. A darab 3, az összeg 13 legyen. A ciklus után külön zárd ki a bad() állapotot és azt, hogy fájlvég nélkül állt le az olvasás. Ez egyetlen számot tartalmazó rekordokon gyakorol, helyes bemenettel; nem a projekt szigorú kétszámos olvasója.

Második próba: a forrásban 3 helyett 8-at fűzz hozzá. Új futáskor 3 adat, 18-as összeg kell. Az első blokk minden futás elején újrakezdi a fájlt, ezért az egész program ismételt futása nem gyűjt további sorokat. A 3/13 és 3/18 értéket a változókból számold, ne írd be kész eredményként.

## G10_03 – Hibás fájl és folyamállapot

**Forrás:** G10_03_hibas_adat.cpp. **Analógia:** M3; előbb a sikeres utolsó számot értelmezzétek.

**G10_03_A:** A program írja ki az invalid.txt fájlba a `215 bad` sort, majd lezárás és ellenőrzés után nyissa meg olvasásra. Két egész számot várj. A láncolt kiolvasás eredményét alakítsd bool-lá, és írd ki a sikerességet, eof()-ot és fail()-t. Várt értékek: `0 0 1`. A sikertelenül olvasott második számot ne dolgozd fel. Az érvénytelenség bemutatása itt normál demonstráció: a program befejeződhet 0 kóddal.

**G10_03_B:** A forrásban változtasd meg a generált tartalmat, mindegyiket külön fordítás/futtatás kövesse:

| Teljes tartalom | Siker | eof | fail |
|---|---:|---:|---:|
| 215 bad és újsor | 0 | 0 | 1 |
| 215 7, záró újsor nélkül | 1 | 1 | 0 |
| csak 215, záró újsor nélkül | 0 | 1 | 1 |

A tényleges tagfüggvények eredményét írd ki. Az utolsó két eset mutatja: eof nem egyenlő a hibátlan rekorddal. A `!eof()` önmagában elnézheti a hiányzó második mezőt. Az állapotot az olvasás után vizsgáld, nem előzetes jóslásként.

## G10_04 – Egy sor szigorú ellenőrzése

**Forrás:** G10_04_sor.cpp. **Analógia:** M4 egy MODE szót és egy számot ellenőriz; itt két külön egész mező és két tartomány kell.

**G10_04_A:** Írd meg a `bool ervenyesSor(string sorAdat)` függvényt. Pontosan két whitespace-szel elválasztott token legyen. Az első teljes egész szám 100–999 között, a második teljes egész szám 0–20 között. Hiányzó vagy harmadik token, szám után maradó karakter és int-tartományt meghaladó érték is hiba. Két szöveges tokent válassz le, majd külön istringstream-ekben olvasd és ellenőrizd őket. Ne csak két közvetlen számkiolvasással vizsgálj, mert a `215.7` hibás sor is két számmá eshet szét.

A token egy whitespace-szel elválasztott szövegrész. A számolvasás utáni char-próba azt vizsgálja, maradt-e bármi a tokenből. Sikeres char-próba: elutasítás. Sikertelen próba a token végén: ezúttal az elvárt eredmény.

**G10_04_B:** A mellékelt g04_cases.txt fájlt getline-nal olvasd. Minden sorra hívd meg a saját függvényedet, és írd ki a bool eredményt. Nyolc kimeneti sor: `1, 0, 0, 0, 0, 0, 0, 0`. Külön próbáld a `100 0` és `999 20` sorokat is: mindkettő igaz. Az eredeti nyolcsoros tesztfájlt őrizd meg, a határeseteket külön próbahívásokban ellenőrizheted.

Itt minden sort külön értékelünk, nem egy egész objektumgyűjteményt cserélünk. A projekt új feladata lesz a teljes betöltés sikeréhez kötött állapotcsere.
