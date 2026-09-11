# EP_01 2.1 – az első Python-gyakorlat

**Fő útvonal, körülbelül 90 perc.** Kész kódot olvasol, egy-egy részét módosítod, mented és futtatod. A büfés sorozat öt önálló fájlból áll. Nem kell minden HTML-fejezetet egyetlen órán végigvenned.

| Lépés | Feladat | Fájl |
|---|---|---|
| E0 | Munkakörnyezet, mentés és futtatás | hello.py |
| E1 | Kiírás, idézőjelek, sorrend, megjegyzés | hello.py |
| B1 | Üdvözlés | bufe1.py |
| B2 | Változók és értékek | bufe2.py |
| B3 | Számítás és a darabszám módosítása | bufe3.py |
| B4 | Formázott kiírás | bufe4.py |
| B5 | Adatbekérés és számmá alakítás | bufe5.py |
| Z1–Z3 | Önálló ellenőrzés és lezárás | zaro_feladatok.md |

Új fogalomnál először **magyarázat és közösen értelmezett példa** következik. A tutor bemutatja az új műveletet, és megmutatja, hogyan kapcsolódik az eddigiekhez. Ezután egy hasonló kis változtatásban már te próbálkozol: **jóslat → módosítás → mentés → futtatás → megbeszélés**. A jóslatot a futtatás előtt mondd vagy írd le. Nem baj, ha téves: a különbségből tanulunk.

A közösen végigvezetett példát nem kell önálló megoldásként bemutatnod. Az önálló próbáknál sem maradsz segítség nélkül, ha elakadsz. A tutor a válaszod alapján magyaráz tovább; nem minden lépésnél kell a teljes terminálkimenetet bemásolnod. Pontos kimenet elsősorban hibánál, eltérésnél és a formázás vizsgálatakor kell.

Ha a tutort éppen nem éred el, az alábbi magyarázatok és a részletes HTML alapján is haladhatsz. A jegyzetben látott mintaválasz és a saját, segítség nélküli alkalmazás különböző tanulási lépés.

## E0. Először legyen egy működő futás

A szerkesztőben a Python-kódot írod. A bash-terminálban parancsot adsz ki, amely elindítja a Python-értelmezőt. A böngésző a jegyzethez és a bemutatókhoz kell.

1. Válassz egy szerkesztőt: az órán telepített Notepad++/Nextpad++ változatot vagy az Inno Agent fájlszerkesztőjét. A pontos mentésműveletet az oktató mutatja meg. Kezdetben egyféle szerkesztőt és egy terminált használj.
2. A terminálban ellenőrizd a helyed és a Python elérhetőségét:

```bash
pwd
ls
python3 --version
```

Ha az `ls` a `python_gyakorlat` mappát mutatja a csomag többi fájljával, lépj bele: `cd python_gyakorlat`. Ha már a `hello.py` és a `bufe1.py` fájlokat látod, ne lépj még egyszer ugyanilyen nevű almappába. Más könyvtárból az oktató által megmutatott tényleges munkamappába lépj. A `~` a saját felhasználói könyvtáradat jelenti; a telepítés helyét nem helyettesíti.

3. Nyisd meg a meglévő `hello.py` fájlt. Kezdetben ez áll benne:

```python
print("Hello, világ!")
```

4. A gyakorlómappában álló terminálba ezt írd:

```bash
python3 hello.py
```

5. A szerkesztőben cseréld a szöveget `Szia, Python!`-ra. Ments, majd ugyanazzal a paranccsal futtass újra. Az új szöveg megjelenése igazolja, hogy a mentett fájlt futtatod. Ha rögtön az E1-gyakorlattal folytatod, annak új sorára válthatsz; nem kell közben külön visszaállítanod a Hello-szöveget. Az E1 végén visszatérünk a kezdőállapothoz.

Ha `python: command not found` jelenik meg, ellenőrizd a futtatóparancsot: ezen a gyakorlaton `python3` kell. Ha `python3` sincs, szólj az oktatónak. Ha a fájl hiányzik, előbb `pwd` és `ls`, utána a megfelelő útvonal. A Run gomb beállítását az oktató ellenőrzi; a fenti kézi parancsot használjuk a közös munkában.

## E1. Az első kiírás négy rövid próbája

**Előbb értsük meg.** A `print()` kiírja a neki átadott értéket. A `print("3 + 1")` az idézőjelek közti szöveget, vagyis a `3 + 1` jeleket írja ki. A `print(3 + 1)` viszont a kiszámított eredményt, a 4-et írja ki. Az idézőjelek azt jelzik, hogy a köztük álló részt szövegként kezeljük.

Ebben az egyszerű programban a kiíró sorok egymás után hajtódnak végre. A szövegen kívüli `#` után az adott sor további része megjegyzés: az olvasónak szól. A tutor ezeket a fogalmakat az adott részfeladat előtt is bemutatja; a következő próbák a megértést segítik.

**E1.a – szöveg és számítás.** A `hello.py` egyetlen kiíró sorát cseréld erre:

```python
print("2 + 2")
```

Jósolj, ments és futtass. Ezután csak az idézőjeleket távolítsd el: `print(2 + 2)`. Jósolj és ellenőrizz újra. Miért változott a kimenet?

**E1.b – sorrend.** Most a teljes kód helyére ez a két sor kerüljön:

```python
print("Első sor")
print("Második sor")
```

Jósold meg a sorrendet. Cseréld fel a két teljes sort, ments és futtass. A szövegben álló „első” szó vagy a kódbeli sorrend határozza meg a végrehajtást?

**E1.c – megjegyzés.** Cseréld a fájl tartalmát erre:

```python
# Ez a sor az olvasónak szól.
print("Szia!")
```

Tegyél `#` jelet a kiíró sor elejére is. Jósolj, ments és futtass. Jegyezd fel, megjelent-e bármilyen szöveg, és a megjegyzés szerepével magyarázd meg a megfigyelést. Távolítsd el az imént hozzáadott `#` jelet a kiíró sor elől.

**E1.d – a jel helye.** Próbáld ki: `print("# Ez szöveg.")`. Miért jelenik meg most a `#`? Végül állítsd vissza a fájl egyetlen sorát `print("Hello, világ!")` alakra, és ments.

## B1. Büfé 1/5 – csak üdvözlés

A következő öt kis fájl egy büfés rendelés feldolgozását építi fel. Először köszönünk, aztán elnevezett adatokkal számolunk, végül a vásárlótól kérjük be a rendelést.

Nyisd meg a `bufe1.py`-t. A `print()` a neki átadott értéket írja ki; az idézőjelek a szöveget határolják.

Jósold meg a kimenetet, majd futtasd: `python3 bufe1.py`. Cseréld az üdvözlést erre: `Jó reggelt a büfében!`. Ments, futtass, és nevezd meg: a print műveletét változtattad meg, vagy az idézőjelek közötti szöveget? Ha ez az E1 alapján már biztosan megy, ez a rész rövid átvezetés lehet. Ebben a fájlban még nincs szorzás vagy változó.

## B2. Büfé 2/5 – változó és érték

Eddig közvetlenül megadtuk a kiírandó szöveget. Az árnak és a darabszámnak most nevet adunk, hogy később hivatkozhassunk rájuk.

```python
tea_darabszam = 4
print(tea_darabszam)
```

**Közös magyarázó példa, nem kell külön fájlba bemásolni.** Az első sor az `=` jobb oldalán álló 4 értéket a bal oldali névhez rendeli. Ez az értékadás. A következő sor a névhez tartozó értéket, a 4-et írja ki. A `print("tea_darabszam")` ezzel szemben magát a `tea_darabszam` szöveget írná ki, mert az idézőjelek közé került.

Nyisd meg a `bufe2.py`-t, és nézd meg a teljes négy sort, a kiírásokat is. A `print("Kávé egységára:", kave_egysegar, "Ft")` a feliratot, az értéket és az egységet írja egymás mellé; a vesszővel elválasztott részek közé alapból szóköz kerül. A változó nevét idézőjel nélkül használjuk, ha az értékét szeretnénk kiírni.

Milyen két sort vársz? Futtasd: `python3 bufe2.py`. Módosítsd a `kave_darabszam = 2` sort `kave_darabszam = 3`-ra. Melyik kiírt adat változik? Itt csak megjelenítjük az adatokat; a teljes árat még nem számítjuk ki. A próba végén állítsd vissza a darabszámot 2-re, és ments.

## B3. Büfé 3/5 – számítás és darabszám

Nyisd meg a `bufe3.py`-t. A kávé egységára 450 Ft, a szendvicsé 890 Ft. Kezdetben 2 kávé és 1 szendvics szerepel. A `*` szorzás, a `+` itt összeadás.

A tutor az első rendelést közösen végigvezeti veled a tényleges kódon: előbb a két részösszeg készül el, utána ezekből a végösszeg. Egy értékadásnál a jobb oldali kifejezést kiszámoljuk, majd az eredményt a bal oldali névhez rendeljük. Például `tea_osszeg = 4 * 200` esetén a `tea_osszeg` értéke 800. Ezt egy későbbi sorban már a nevével használhatjuk.

A darabszám forrásbeli módosítása után újraindítjuk a programot, így a számító sorok is újra végrehajtódnak. A tárolt összeg nem folyamatosan frissülő táblázatképlet.

1. Kövesd a tutorral a két részösszeget és a végösszeget. Ez a közös bemutatás. Futtasd: `python3 bufe3.py`, és hasonlítsátok össze a számítással.
2. Most előbb jósolj: ha csak a `kave_darabszam = 2` sort cseréled `kave_darabszam = 3`-ra, mennyivel fog változni az összeg? Mondd el az okát, mielőtt futtatnál.
3. Végezd el a cserét, ments és futtass. A próba után állítsd vissza a 2 kávét, és ments. A B4 külön fájl, ezért annak kódját ez a változtatás nem módosítja.

## B4. Büfé 4/5 – f-string

A számítást most olvasható összesítőként szeretnénk megjeleníteni. Előbb nézzünk meg egy kisebb példát:

```python
nev = "Dóra"
print(f"Szia, {nev}!")
```

Ez `Szia, Dóra!` szöveget ír ki. Az idézőjel előtti `f` jelzi a formázott szöveget: a kapcsos zárójelben lévő kifejezés értékét behelyettesítjük. Itt ez a `nev` változó értéke. A többi szövegrész változatlanul megmarad.

Nyisd meg a `bufe4.py`-t. A tutorral nézzétek meg, mely értékeket helyettesíti a három kiíró sor. A szóközök és az „Ft” felirat is a megjelenítés része.

Az első futás közös bemutatás: `python3 bufe4.py`. Most következik a saját jóslatod: mi jelenne meg, ha az utolsó `print()` sorban csak az idézőjel előtti `f` betűt törölnéd? Előbb válaszolj, majd végezd el a törlést, ments és futtass. Beszéljétek meg, a számítás vagy a megjelenítés változott-e. Ezután írd vissza az `f` betűt, és ments.

## B5. Büfé 5/5 – adatbekérés

Eddig a rendelést a forrásban rögzítettük. Most a felhasználó adja meg, így új rendeléshez nem kell a programot átírni.

Az `input()` kiírja a megadott kérdést, megvár egy Enterrel lezárt sort, majd annak szövegét adja vissza. Ez akkor is szöveg, ha számjegyeket gépeltünk be.

```python
tea_szoveg = input("Hány teát kérsz? ")
tea_darabszam = int(tea_szoveg)
```

**Magyarázó példa.** Ha 4-et gépelsz, az első sor a `"4"` szöveget rendeli a `tea_szoveg` névhez. Az idézőjeleket nem kell beírnod: itt a szövegtípust jelzik. A második sorban az `int()` a szövegből 4 egész számot készít; ezt a `tea_darabszam` névhez rendeljük. A két névhez most különböző típusú érték tartozik. A `tea_szoveg` értéke továbbra is szöveg.

Miért számít ez? A `"4" + "1"` két szöveg összefűzése, eredménye `"41"`. A `4 + 1` számok összeadása, eredménye 5. A névvel nem számolunk, ezért annak nincs szüksége számkonverzióra.

Nyisd meg a `bufe5.py`-t. A tutor előbb megmutatja az adatbekérés és az átalakítás sorait, majd a már ismert számításhoz és kiíráshoz kapcsolja őket.

Az első rendelést közösen próbáljátok: `python3 bufe5.py`. Amikor a program kérdez, külön-külön, Enterrel lezárva add meg: `Anna`, `2`, `1`. A darabszámoknál csak a számjegyet írd, a „db” szót ne. Az adatokat a futó program kérdéseire válaszolva írd be, ne külön shellparancsként.

A tutorral azonosítsátok a bekérés, átalakítás, számítás és kiírás egy-egy sorát. Egy kiválasztott sor szerepét próbáld a saját szavaiddal elmondani.

A második rendelésnél a bemenet sorrendben: `Béla`, `3`, `2`. Előbb számítsd ki a várható végösszeget, és mondd vagy írd le. Ezután futtasd újra a programot, és add meg az adatokat. A jóslat és a tényleges futás eredménye két külön megfigyelés.

Ha véletlenül `3 db` került be, az `input()` az egész szöveget átvette. Az `int()` azonban a betűket tartalmazó szöveget nem tudja egész számmá alakítani, ezért `ValueError` keletkezik. A program itt leáll; újraindítás után 3-at gépelj, mértékegység nélkül. A hiba megértése is a tanulás része. Most nem kell kivételkezelést írnod.

**Rövid típuspróba.** Szöveget egész számmal szorozva ismétlés történik: a `"ha" * 2` eredménye `"haha"`. A HTML Szövegműveletek fejezete ezt szemlélteti. E példa után jósolj: mit csinál a `"2" * 3`, és miért más, mint a `2 * 3`? A tutor várja meg a válaszodat, majd beszéljétek meg. A konverzió hiánya nem mindig okoz hibaüzenetet: előfordulhat, hogy más jelentésű művelet fut le.

A büfés példa egész, nemnegatív darabszámokat vár. A hibás bemenetek kezelése külön későbbi téma; az első órán nem kell kivételkezelést írnod.

## Z1–Z3. Önálló lezárás

Az eddigi út összekapcsolódik: szöveget írtunk ki; adatokat neveztünk el; ezekkel számoltunk; az eredményt formáztuk; végül a felhasználótól kapott szöveget szükség szerint számmá alakítottuk. Most azt próbáljuk ki, hogyan használod ezeket egy új helyzetben.

Nyisd meg a [záró feladatokat](zaro_feladatok.md). Először segítség és a mintaválasz felfedése nélkül próbálkozz. Ha segítséget kérsz, jelöljük, és utána új példán ellenőrzünk. A három feladat után a fő gyakorlat véget ér.

## Ha marad idő

A [további gyakorlásban](tovabbi_gyakorlas.md) a dobozos feladat, a beszédes nevek, az összeadás, a téglalap és a második terminál próbája következhet. Ezek nem a fő gyakorlat rejtett kötelező szintjei.
