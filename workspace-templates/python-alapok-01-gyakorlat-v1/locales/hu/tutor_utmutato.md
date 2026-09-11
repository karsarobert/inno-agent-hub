# EP_01 2.1 — a tutor tanítási terve

A megfelelő blokk előtt olvasd ezt és az aktuális forrást. Az alábbi tanítási példák a közös magyarázat részei; megoldásuk megmutatható. A későbbi önálló kérdés válaszát azonban várd meg. A tanulói szövegben ne hivatkozz erre az utasításfájlra. Ne olvasd fel mereven a mintamondatokat: az adott tanuló előzményeihez igazítsd őket.

## E0 — mi történik, amikor elindítunk egy programot?

**Magyarázd el:** a szerkesztőben a program szövegét módosítjuk; mentéskor ez a fájlba kerül; a terminálban a Python-értelmezőt indítjuk a fájlnévvel. A `python3 hello.py` két részét nevezd meg. A `print()` a megadott értéket írja ki, az idézőjel a szöveg határa, nem jelenik meg a kimeneten.

Az első Hello-futás vezetett bemutatás. Nem kell előtte bizonytalan technikai környezetben vizsgáztatni. Ellenőrizd a helyet, majd segítesz megnyitni, menteni és futtatni. A másik köszönésre módosított futás után közösen magyarázd el a kapcsolatot a mentett szöveg és a megjelenés között.

**Átvezetés:** most már el tudjuk indítani a fájlt; nézzük meg, mit tekint szövegnek és mit számításnak a Python. A Hello visszaállítását ne követeld közvetlenül egy azt teljesen felülíró E1-sorcsere előtt. E1 végén elég rendezni a kezdőállapotot.

## E1 — szöveg, számítás, sorrend és megjegyzés

**Első közös példa:** `print("3 + 1")` az idézőjelek közötti jeleket írja ki, míg `print(3 + 1)` előbb kiszámolja a kifejezést, és 4-et ír. Mutasd meg az okot: ugyanazok a jelek más szerepet kaptak az idézőjelek miatt. Ezután a munkalap 2 + 2 példája már rövid tanulói alkalmazás; egy jóslatot kérj, és várd meg.

**Sorrend:** ebben az egyszerű, elágazás és ciklus nélküli programban egymás után hajtódnak végre a kiírások. A kiírt „Első” szó nem ad utasítást a Pythonnak. Ne általánosítsd korlátlanul minden későbbi Python-programra a felülről lefelé végrehajtást.

**Megjegyzés:** a szövegen kívüli # után az adott sor hátralévő része megjegyzés. A megjegyzés az olvasónak szól. Előbb tanítsd meg ezt, aztán kérdezd, mi történik a kiíró sor elé tett # után. Ne írd oda a várt üres kimenetet a jóslatkérésbe. Ha már közösen megbeszéltétek, kérj eltérő helyzetet: a # idézőjeleken belül jelenik meg.

**Visszajelzés:** „szia” válasznál a kiírás lényegét fogadd el; a pontos `Szia!` alakot egy mondatban tedd hozzá, ne nevezd fogalmi hibának a kisbetűt. A végén a hello.py az eredeti Hello-sorra álljon vissza.

## B1 — rövid kapcsolat a büfés feladathoz

Az E1 alapján már ismert print-et új témában használjuk. Mondd el: „Ebből az egyszerű köszönésből lépésenként egy rendelést összesítő program lesz.” Mutasd meg az első sort, és kérj egy köszönésmódosítást. Ha magabiztosan érti, nem kell ugyanazt a print-fogalmat újra több körben vizsgálni.

A „melyik változtatás miatt lett más?” helyett konkrétan kérdezd: „Az idézőjelek közötti szöveget cserélted, vagy a print műveletét?” Ha a tanuló azt kérdezi, „mire gondolsz?”, magyarázd el a két rész eltérő szerepét, és térj tovább az érthető célra. Ne büntesd a homályos kérdésedet újabb kötelező futással.

## B2 — mi a változó és az értékadás?

**Kapcsolódás:** az ár és a darabszám később több helyen is kell; ezért nevet adunk nekik.

**Tanítási minta:**

```python
tea_darabszam = 4
print(tea_darabszam)
```

Az első sor a jobb oldali 4 értéket a bal oldali névhez rendeli. Az = itt értékadás. A következő sor idézőjelek nélkül használja a nevet, ezért annak értékét írja ki. A `print("tea_darabszam")` ezzel szemben magát a nevet írná ki szövegként. Magyarázd el ezt a különbséget; a változó fogalmát ne merítsd ki annyiban, hogy „két adatot tárol”.

Most mutasd meg a bufe2.py tényleges négy sorát, beleértve a két print-et is. Csak az értékadásokból nem lehet megjósolni a kiírás pontos feliratait. Magyarázd el a vesszőkkel elválasztott kiírást: a szöveg és a változó értéke egymás mellé kerül, alapból szóközzel.

**Tanulói alkalmazás:** a kávé darabszámát 2-ről 3-ra változtatva melyik adat módosul a kiírásban? Előbb válasz, majd szerkesztés, mentés, futás. Megbeszélés: az egységárhoz nem nyúltunk. B2-ben még nincs végösszeg-számítás. Ezután állítsa vissza a 2-t.

## B3 — hogyan vezet az adat a számítás eredményéhez?

**Kapcsolódás:** az előző program megjelenítette az adatokat; most felhasználjuk őket egy számításhoz.

A bufe3.py tényleges sorain vezesd végig a kávé részösszegét, a szendvics részösszegét és a kettő összegét. A * itt szorzás, a + számok összeadása. Az = jobb oldalát kiszámoljuk, és az eredményt a bal oldali névhez rendeljük. Az első rendelés számítását közösen megmutathatod; ez tanítás, nem önálló jóslat.

**Új próba:** 2 helyett 3 kávé esetén mennyivel változik a fizetendő összeg? A választ ne közöld a kérdésben. Várj, majd kérj futtatást. Utána az indoklásban kösd össze az egy plusz kávét az egységárral és a változatlan szendvicsrendeléssel.

**Fontos határ:** amikor a fájl elején módosítjuk az értéket és újra elindítjuk a programot, a számító sorok is újra lefutnak. Az értékadás nem élő táblázatképlet. Ha a tanuló erre rákérdez, külön kis példán mutasd meg: egy már eltárolt eredmény nem frissül pusztán egy másik név új értékadásától. Ez nem új kötelező kitérő.

## B4 — a számítás eredményéből olvasható szöveg

**Kapcsolódás:** a számítás már működik, most részletes rendelésösszesítőt jelenítünk meg.

**Közös mikropélda:**

```python
nev = "Dóra"
print(f"Szia, {nev}!")
```

Mutasd meg a kimenetet és annak eredetét: az f a formázott szöveget jelzi; a kapcsos zárójelben álló kifejezés értéke kerül a megfelelő helyre; a többi szöveg megmarad. A mostani példában a kapcsos zárójelben egy változónév szerepel.

Olvassátok el a bufe4.py három kiíró sorát, az első futás lehet közös ellenőrzés. Ne kérj három sorra jóslatot úgy, hogy már leírtad a három kész eredményt.

**Tanulói próba:** csak az utolsó sor f előtagjának eltávolítása után mi fog megjelenni? Várd meg a választ. A futás után magyarázd meg: a számítás változatlan, a szövegbe helyettesítés maradt el. Végül állítsa vissza az f-et. Egyetlen ilyen érdemi kísérlet többet ér több azonos kimenet bemásolásánál.

## B5 — adatbekérés, szöveg és számkonverzió

Ez két új összefüggés: előbb beolvasunk egy szöveget, utána abból számot készítünk. A futtatás előtt tanítsd meg őket.

**Kapcsolódás:** eddig a forrásban adtuk meg a rendelést. Most a vásárló fogja begépelni, így másik rendeléshez nem kell átírni a programot.

**Közös mikropélda:**

```python
tea_szoveg = input("Hány teát kérsz? ")
tea_darabszam = int(tea_szoveg)
```

Ha a vásárló 4-et ír és Entert nyom, az első sor eredménye a `"4"` szöveg. Az idézőjelek a magyarázatban jelzik a típust; a felhasználó nem gépeli be őket. Az int ebből a 4 egész számot készíti, és a második értékadás egy másik névhez rendeli. A tea_szoveg ettől nem változik számmá. A név szöveg marad, ezért azt nem alakítjuk int-té.

**Típuspróba:** a + két szöveget összefűz, két számot összead. Mutasd meg közösen a `"4" + "1"` és `4 + 1` különbségét. Tanulói alkalmazásként kérdezd a munkalap `"2" * 3` és `2 * 3` példáját, miután a szövegismétlés jelentését egy másik példán (`"ha" * 2`) megmutattad. A konverzió elmaradása nem mindig okoz hibát; néha érvényes, de más értelmű művelet történik.

A bufe5.py négy részét együtt azonosítsátok: rögzített árak; bekérés; átalakítás és számítás; kiírás. Előbb te mutass rá egy-egy jellegzetes sorra. Utána kérdezheted, melyik rész felel például azért, hogy a beírt nevet látjuk a köszönésben. Nem szükséges rögtön minden sort önállóan osztályoztatni.

**Első rendelés:** Anna, 2, 1, külön sorokban, mértékegység nélkül. A terminálban az aktuális programkérdésre válaszolunk. Az első próba vezetett. **Második rendelés:** Béla, 3, 2. A jóslatkérésben csak a számokat add, ne másolható „3 db” bemeneti blokkot. Várd meg a várható végösszeget, csak utána indíttasd a programot.

**Ha mégis 3 db került be:** az input az egész beírt sort átvette, az int a számjegyek mellett a betűket is megkapta, ezért ValueError keletkezett. Mutasd meg a hibában az érintett szöveget. A kapott szöveg ebben a formában nem alakítható int-té; nem igaz általánosan, hogy az int csak már eleve egész számot fogad. A javításhoz 3 kerüljön a válaszba, db nélkül. A program nem automatikusan kérdez újra, újra kell indítani. Kivételkezelést nem kell most íratni. Sikeres javítás után röviden kérdezd, mire kellett a konverzió; ne követelj minden alkalommal teljes rendeléskimenetet.

## Zárás — fokozatosan átadott önállóság

A zárófeladatok előtt a fenti fő fogalmak már szerepeljenek a tanításban. Kérj rövid önálló alkalmazást, egy kérdést egyszerre. A tartalmilag helyes választ ismerd el; a kihagyott másik részt semleges kérdéssel kérd. Az új utalást, magyarázatot vagy kész megoldást az érintett részhez rögzítsd.

Ha a tanuló csak a kimenet számát adja meg, miközben teljes formátumot kértél, mondd: „A számítás helyes. Hogyan jelenik meg ez a print sor alapján?” Ne add meg rögtön a teljes formát, majd nevezz mindent önállónak vagy mindent támogatottnak.

Z3-nál a „szerkesztem” nem bizonyít mentést. Kérdezz rá egy hiányzó lépésre. Ha nem tudja, tanítsd meg, és új, rövid helyzetben ellenőrizd. A python helyett python3 az órai alap, de a helyben igazolt Python 3-alias önmagában nem hibás tudás.

A végén rövid, érthető tanulási összegzést adj, aztán a folytatási pontot. A fő gyakorlat nem nyúlhat végtelen újravizsgáztatássá. A nem ellenőrzött rész maradhat későbbi gyakorlás.
