# EP_01 – az első Python-gyakorlat

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

Minden kódváltoztatásnál: **olvasd el → tervezd meg a változtatást → jósolj → módosíts → ments → futtass → indokolj**. A jóslat egy rövid várakozás: például „A program ezt a szöveget fogja kiírni.” Nem baj, ha téves; összehasonlítjuk a futással.

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

5. A szerkesztőben cseréld a szöveget `Szia, Python!`-ra. Ments, majd ugyanazzal a paranccsal futtass újra. Az új szöveg megjelenése igazolja, hogy a mentett fájlt futtatod. Utána állítsd vissza az eredeti szöveget, és ments.

Ha `python: command not found` jelenik meg, ellenőrizd a futtatóparancsot: ezen a gyakorlaton `python3` kell. Ha `python3` sincs, szólj az oktatónak. Ha a fájl hiányzik, előbb `pwd` és `ls`, utána a megfelelő útvonal. A Run gomb beállítását az oktató ellenőrzi; a fenti kézi parancsot használjuk a közös munkában.

## E1. Az első kiírás négy rövid próbája

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

Tegyél `#` jelet a kiíró sor elejére is. Jósolj, ments és futtass. Az üres kimenet most lehet helyes eredmény. Távolítsd el az imént hozzáadott `#` jelet a kiíró sor elől.

**E1.d – a jel helye.** Próbáld ki: `print("# Ez szöveg.")`. Miért jelenik meg most a `#`? Végül állítsd vissza a fájl egyetlen sorát `print("Hello, világ!")` alakra, és ments.

## B1. Büfé 1/5 – csak üdvözlés

Nyisd meg a `bufe1.py`-t. A `print()` a neki átadott értéket írja ki; az idézőjelek a szöveget határolják.

Jósold meg a kimenetet, majd futtasd: `python3 bufe1.py`. Cseréld az üdvözlést erre: `Jó reggelt a büfében!`. Ments, futtass és mondd el, melyik változtatás miatt lett más a kimenet. Ebben a fájlban még nincs szorzás vagy változó.

## B2. Büfé 2/5 – változó és érték

Nyisd meg a `bufe2.py`-t. Az `=` jobb oldalán álló értéket a bal oldali névhez rendeljük. A változó nevét idézőjel nélkül írjuk a `print()`-be, ha az értékét akarjuk látni.

Milyen két sort vársz? Futtasd: `python3 bufe2.py`. Módosítsd a `kave_darabszam = 2` sort `kave_darabszam = 3`-ra. Melyik kiírt adat változik? Itt csak megjelenítjük az adatokat; a teljes árat még nem számítjuk ki. A próba végén állítsd vissza a darabszámot 2-re, és ments.

## B3. Büfé 3/5 – számítás és darabszám

Nyisd meg a `bufe3.py`-t. A kávé egységára 450 Ft, a szendvicsé 890 Ft. Kezdetben 2 kávé és 1 szendvics szerepel. A `*` szorzás, a `+` itt összeadás.

1. Kövesd a két részösszeget és a végösszeget. Mennyi lesz a fizetendő összeg? Futtasd: `python3 bufe3.py`.
2. Csak a `kave_darabszam = 2` sort cseréld `kave_darabszam = 3`-ra. Mennyivel fog változni az összeg? Miért?
3. Ments és futtass. A próba után állítsd vissza a 2 kávét, és ments. A B4 külön fájl, ezért annak kódját ez a változtatás nem módosítja.

## B4. Büfé 4/5 – f-string

Nyisd meg a `bufe4.py`-t. Az idézőjel előtti `f` jelzi, hogy a kapcsos zárójelben lévő kifejezés értékét behelyettesítjük a szövegbe. A szóközök és az „Ft” felirat is a megjelenítés része.

Jósold meg a három kiírt sort, majd futtasd: `python3 bufe4.py`. Az utolsó `print()` sorban csak az idézőjel előtti `f` betűt töröld. Mi fog megjelenni a kapcsos zárójelek helyén? Ments és ellenőrizz; utána írd vissza az `f` betűt, és ments. A számítás változott meg, vagy a megjelenítés?

## B5. Büfé 5/5 – adatbekérés

Nyisd meg a `bufe5.py`-t. Az `input()` kérdést ír ki, egy beírt sorra vár, majd szöveget ad vissza. A darabszámokból `int()` készít egész számot. A név szöveg marad.

Futtasd: `python3 bufe5.py`. Amikor a program kérdez, külön-külön, Enterrel lezárva add meg: `Anna`, `2`, `1`. Az adatokat a futó program kérdéseire válaszolva írd be, ne külön shellparancsként.

Mely sorok végzik az adatbekérést, az átalakítást, a számítást és a kiírást? Futtasd újra más adatokkal: `Béla`, `3`, `2`. Előtte számítsd ki a várható végösszeget. Egy jóslat és egy tényleges futás eredménye két külön megfigyelés.

**Rövid típuspróba.** A HTML Szövegműveletek fejezetében nézd meg az ismétlést. Mit csinál a `"2" * 3`? Miért nem ugyanaz, mint a `2 * 3`? A konverzió hiánya nem mindig okoz hibaüzenetet: előfordulhat, hogy más jelentésű művelet fut le.

A büfés példa egész, nemnegatív darabszámokat vár. A hibás bemenetek kezelése külön későbbi téma; az első órán nem kell kivételkezelést írnod.

## Z1–Z3. Önálló lezárás

Nyisd meg a [záró feladatokat](zaro_feladatok.md). Először segítség és a mintaválasz felfedése nélkül próbálkozz. Ha segítséget kérsz, jelöljük, és utána új példán ellenőrzünk. A három feladat után a fő gyakorlat véget ér.

## Ha marad idő

A [további gyakorlásban](tovabbi_gyakorlas.md) a dobozos feladat, a beszédes nevek, az összeadás, a téglalap és a második terminál próbája következhet. Ezek nem a fő gyakorlat rejtett kötelező szintjei.
