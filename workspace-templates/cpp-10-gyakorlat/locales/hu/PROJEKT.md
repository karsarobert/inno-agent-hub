# CPP_10 – A jegypénztár tartós tárolása

**Forrás:** P10_jegypenztar.cpp. **45 perc, P1–P6.** Az alap osztályok adottak; az új fájlkezelést te írod. Nincs öröklődés, override, polimorfizmus, dinamikus memória vagy referencia-paraméter. A saját módszerek stringet érték szerint kapnak. A szabványos numeric_limits használatára sincs szükség: itt csak egész adatok vannak.

## A modell és a közös fájlformátum

3 sor × 4 szék; első sor ára 4000, másik két soré 3000. A tároló kapacitása 4 jegy. Egy hely csak egyszer szerepelhet. A bevétel az aktuális jegyek árösszege. Az alap `felvesz()` minden állapotváltoztatás előtt vizsgálja a tartományt, kapacitást és ismétlést.

A fájl első sora **pontosan** `TICKETS 1`, azután soronként két egész: sor és szék. Ez a fejléc mindkét nyelvi csomagban ugyanaz, nem fordítjuk le. Az 1 a formátum verziója, nem a jegyek száma. A fájl nem tárolja az árat vagy a darabszámot: ezek a rekordokból meghatározhatók.

```text
TICKETS 1
1 2
2 3
```

A fenti fájl két jegyet jelent, bevétel 7000. Az adatmezők között legalább egy szóköz/tabulátor; az adatsor szélein whitespace megengedett. A fejlécnél nincs plusz szóköz, BOM vagy extra mező. A csomag LF sorvéget használ. Az utolsó sor záró újsora nem kötelező. Üres adatsor hibás. A teljesen üres fájl hibás, mert nincs fejléc. A **csak fejlécet** tartalmazó fájl helyes, üres pénztárat jelent. Ez eltér a HTML mérési naplójától.

## P1 – Az alap és a formátum megértése, 4 perc

Futtasd az adott alapot: az első két felvétel sikeres, az ismétlés nem; 2 jegy, 7000 bevétel. Keresd meg az aktív elemszámot, a feltételeket és a const lekérdezőket. Végezz saját második próbát: 3/4 felvétele igaz, a bevétel 10000. Ezután térj vissza az első két jegyes állapothoz a következő lépéshez. P1 csak az önálló második próba és a szabályok megértése után kész; a starter futása önmagában nem elég.

Az adott alap nem teljes 9. leckebeli projekt: a most nem használt visszaváltást elhagytuk. Ha saját korábbi osztályt használsz, csak a szükséges neveket/interfészt egyeztesd, a saját működő megoldást ne írd felül automatikusan.

## P2 – Fejléces mentés, 8 perc

**Minta:** M1 + M7 fejlécgondolata. Írd meg a `bool mentes(string fajlnev) const` tagfüggvényt. Alapértelmezett ofstream: megnyitás ellenőrzése → fejléc → csak az aktív jegyek sor/szék lekérdezőkből → close → állapotból bool visszatérés. A private adattagokat ne tedd nyilvánossá.

Két jegy mentése után a tickets.txt tartalma a fenti három sor. Ugyanazt a pénztárt másodszor is mentsd: továbbra is három sor legyen, ne két fejléc vagy négy jegy. Üres const pénztár mentése külön fájlba csak fejlécet adjon. Nem kell lebegőpontos pontosságbeállítás, mert két int-et írunk.

A folyam bool-konverziója a hibákról szól, nem arról, hogy nyitva maradt-e. A return static_cast<bool>(fajl) és az egyenértékű return !fajl.fail() is elfogadható. A közvetlen felülíró mentés íráshibánál nem állítja vissza a korábbi fájlt; a memória megőrzése a betöltés külön feladata.

## P3 – Egy helyfoglalási sor feldolgozása, 10 perc

**Minta:** M4 és a saját G10_04. Írd meg a nyilvános `bool sorbolFelvesz(string sorAdat)` tagfüggvényt. Pontosan két külön token, mindkettő teljes int legyen. Csak ezután hívd a meglévő felvesz(sor, szek) műveletet. Ennek eredményét add vissza; a kapacitás-, tartomány- és ismétlésellenőrzést ne másold újra.

Egymás után, friss pénztárból: `1 2` igaz; ismét `1 2` hamis; `2.3` hamis; `2 4x` hamis; `2 4` igaz. Végül 2 jegy és 7000 bevétel. Külön próbák: hiányzó szék, harmadik token, `4 1`, `1 0`, túl nagy egész szám: elutasítás. Hibánál nem változhat a pénztár.

Ez a művelet itt nyilvános, mert önállóan is ellenőrzött felvételt kínál; nem fér hozzá közvetlenül kívülről a tömbhöz. A teljes fájl betöltésénél ugyanazt a műveletet egy ideiglenes pénztáron hívjuk.

## P4 – Teljes betöltés vagy változatlan régi állapot, 12 perc

**Minta:** M5 ideiglenes állapot + M7 fejléc; a sort már saját P3 műveleted dolgozza fel. Írd meg a `bool betoltes(string fajlnev)` tagfüggvényt:

1. Nyisd meg ifstream-mel; sikertelen megnyitáskor hamis, régi állapot marad.
2. Az első getline olvassa a fejlécet. Hiányzó vagy eltérő fejléc: hamis, régi állapot marad.
3. Hozz létre üres ideiglenes Jegypenztar objektumot.
4. Minden további getline után annak sorbolFelvesz műveletét hívd. Bármelyik hibája az egész betöltés hibája.
5. A ciklus után vizsgáld a bad() állapotot és a fájlvégi leállást. Csak teljes siker után másold az ideiglenes állapotot az aktuális objektumba; igaz visszatérés.

A this mutató az aktuális objektumot jelöli; a *this ennek az objektumnak az elérése. A teljes objektumértékadás itt a rögzített tömböt és a darabszámot is másolja. Ne ürítsd előre az eredetit, és ne az eredetin dolgozz a ciklusban.

Próbák: először az eredetiben 1/4 (1 jegy, 4000). Az ok.txt betöltése után 2 jegy, 7000; ez csere, nem hozzáfűzés. Ezután a duplicate.txt és a missing.txt betöltése is hamis; továbbra is 2/7000 és az eredeti két hely marad. A további kötelező határeseteket P6 összegzi.

## P5 – Jelentés szövegként, 6 perc

**Minta:** M6. Írd meg a `string jelentes() const` tagfüggvényt ostringstream használatával. A visszaadott szöveg: `TICKETS=2;REVENUE=7000` a kétjegyes pénztárra; üres const pénztárra `TICKETS=0;REVENUE=0`. A két számot a jelenlegi állapotból kérdezd le. A jelentés maga ne cout-ra írjon és ne módosítsa a tickets.txt fájlt; a main nyomtassa ki a visszaadott stringet.

Magyarázat: az ostringstream a memóriában épít karaktereket, str() adja a kész stringet. A jelentés címkéi közösek HU/EN-ben; a kód azonosítói a csomag nyelvét követik.

## P6 – Új futás és hibás fájlok, 5 perc

A main kérjen egyetlen karaktert: `S` vagy `L`. S-nél vegye fel az 1/2 és 2/3 jegyet, majd mentse tickets.txt-be; L-nél egy frissen létrejött üres pénztárba töltse be a fájlt. Ezután írja ki a művelet sikerességét és a saját jelentését. Hibás mód vagy beolvasás esetén kiléphet 1-gyel; teljes menü nem feladat.

RUN → S → program vége; új RUN → L. Mindkettőnél siker és TICKETS=2;REVENUE=7000. A betöltési ág ne hozza újra létre a fájlt és ne vegye fel kézzel a két jegyet: az adatoknak valóban az előző futásból kell származniuk.

A tutor a már elkészült műveleten, rövid ellenőrző hívásokkal végigmegy a mellékelt fájlokon (nincs új feldolgozó kód):

| Fájl | Eredmény |
|---|---|
| full.txt | siker, 4 jegy, 14000 |
| no_newline.txt | siker, 1 jegy (3/4), 3000 |
| header_only.txt | siker, üres pénztár |
| empty.txt, wrong_header.txt | hiba; korábbi állapot marad |
| duplicate.txt, overflow.txt | hiba; korábbi állapot marad |
| missing.txt, extra.txt, joined.txt, suffix.txt, range.txt, blank.txt | hiba; korábbi állapot marad |
| nem létező absent.txt | hiba; korábbi állapot marad |

Minden hibapróba előtt állíts be ismert, nem üres eredetit, és utána a darabszámot, bevételt és helyeket is ellenőrizd. Nem elég csak a false kiírása. Ne nevezd át a programban szereplő tickets.txt-t egy hibás próbafájlra úgy, hogy az S ág azt felülírhassa; a betoltes paraméterével, külön hívásban tesztelj.
