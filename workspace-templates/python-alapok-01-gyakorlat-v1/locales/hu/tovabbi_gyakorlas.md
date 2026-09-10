# Választható további gyakorlás – K1–K5

Ezek a fő gyakorlat utáni kiegészítők. Nem kell mindet megoldanod. Az előkészített fájlok a `python_gyakorlat/` mappában vannak; a parancsokat ebből a mappából add ki. Másik helyről a `futtatas.sh` segéd is használható.

## K1. Dobozok és maradék – doboz.py

Pozitív egész darabszámoknál a `//` megadja, hány teljes csoport készül, a `%` pedig a kimaradó darabszámot. Például 17 tárgyból, 5 darabos csoportokkal: `17 // 5` értéke 3, `17 % 5` értéke 2. A `/` szokásos osztás: itt 3.4.

Olvasd el a `doboz.py` programot: 29 tárgy és 6-os kapacitás szerepel benne. Jósolj mindkét kiírásra, majd futtasd: `python3 doboz.py`. Változtasd a darabszámot 30-ra. Jósolj, ments, futtass. Magyarázd meg a maradék változását. Végül állítsd vissza 29-re.

Kitekintés: a // általánosan lefelé kerekít, ezért negatív számnál nem egyszerűen a tizedesrész elhagyása. A részletes HTML például a `-7 // 3` esetet is elmagyarázza.

## K2. Beszédes változónevek – valtozok.py

A jó név megmutatja, mit jelent az adat. A `jegy_egysegar` többet mond, mint az `x`. Ha egy nevet módosítasz, minden hozzá tartozó hivatkozást következetesen módosíts; egy szöveges kiírás tartalma ettől nem változik automatikusan.

A `valtozok.py` kódjában nevezd át az `a`, `b`, `c` változókat a kávé egységárát, darabszámát és a fizetendő összeget leíró nevekre. A számértékeken ne változtass. Jósolj: változik-e a kimenet? Ments és futtass: `python3 valtozok.py`. Ha NameError jelenik meg, vesd össze a bevezetett nevet a felhasználási helyeivel.

## K3. Összegzés beolvasott egész számokkal – osszeg.py

Az `input()` szöveget ad. Az `int()` megfelelő egész számot leíró szövegből egész számot készít. Például `int("12") + 1` értéke 13; `"12" + "1"` viszont `"121"`.

Az `osszeg.py` futásakor adj meg előbb 8-at, majd 5-öt. Jósolj előre, utána ellenőrizd: `python3 osszeg.py`. A két szám átalakítása közül a másodikat ideiglenesen hagyd el: `masodik = masodik_szoveg`. Miért nem számösszeget kapsz? A hibaüzenet után állítsd vissza az eredeti sort, és próbáld ki a -2, 7 bemenetet.

## K4. Mérés és formázás – teglalap.py

A `float()` tizedes számot leíró szöveget is átalakít: `float("2.5")` értéke 2.5. Pontot használj tizedesjelként. A kerület `2 * (szelesseg + magassag)`, a terület `szelesseg * magassag`. Az f-stringben a `:.2f` két tizedesjegyes megjelenítést kér; a tárolt számot nem módosítja.

Futtasd a `teglalap.py` fájlt 2.5 és 4 bemenettel. Jósolj a két kiírásra. Ezután mindkét kiírásban módosítsd a `:.2f` részt `:.1f`-re. Mi változik, és mi marad ugyanaz? Ments és futtass újra, majd állítsd vissza a két tizedesjegyet. E feladatban pozitív, ponttal írt számokat várunk; hibás bevitelt kezelő programot most nem kell írnod.

## K5. Ugyanaz a fájl két munkafelületen

Ezt csak akkor válaszd, ha az első szerkesztő–terminál munkamenet már biztosan megy, és a második felület is elérhető.

Nyisd meg ugyanazt a `hello.py` fájlt a másik szerkesztőben is. Ellenőrizd a teljes elérési utat; az azonos fájlnév önmagában nem bizonyítja, hogy ugyanazt a fájlt látod. Egyszerre egy szerkesztőben módosíts, ments, és a másikban szükség esetén töltsd újra a fájlt.

A második terminálban ellenőrizd: `pwd`, `ls`, `python3 --version`. Navigálj a fájl tényleges mappájába, és futtasd: `python3 hello.py`. Hasonlítsd össze az eredményeket. A két felület nem feltétlenül osztozik ugyanazon munkamappán; ezt ellenőrizni kell, nem feltételezni.
