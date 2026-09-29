# EP_04 – opcionális elmélyítés

A K1–K6 feladatok a 90 perces főút után, külön választás esetén következnek. Nem kötelező házi feladatok, a tutor a főút végén nem indítja el őket automatikusan. A tanuló a korábbi megoldását őrizze meg; ha külön próbafájlt használ, azt is maga hozza létre a munkatér gyökerében. Előbb magyarázat, majd saját kód és tényleges próba, jóslás nélkül.

## K1 – Insert, index és clear (8 perc)

A listamuveletek.py saját megoldásából kiindulva szúrj szendvicset a kosár elejére. Az index metódussal keresd meg az első kávé helyét, de csak ha szerepel a listában. Végül ürítsd a kosarat clear()-rel, és írasd ki a hosszát.

Próbák: induló ["kávé", "üdítő"] esetén beszúrás után a kávé indexe 1; clear után 0 a hossz. Kávé nélküli listán ne hívj index("kávé")-t. A beírt kódot a tanuló készíti.

## K2 – Szövegkeresés és rövidítés (10 perc)

A szoveg.py mellett külön függvényt írj: megjegyzest_rovidit(szoveg, hatar). Nemnegatív egész határt feltételezünk. Ha hosszabb a szöveg, az első hatar karakter után három pont álljon, különben az eredetit adja vissza. A három pont a határon felül értendő.

Próbák: "tej nélkül", 3 → "tej..."; "tea", 3 → "tea"; "", 3 → ""; "tea", 0 → "...". További rövid rész: egy megjegyzésben find-del keresd a kávé részszöveget. A nulla index találat; a −1 jelzi a hiányt. Magyarázd el a feltételt a kész futás után.

## K3 – Másolat és beágyazott kosarak (10 perc)

A listamuveletek.py adataiból készíts copy()-val külön kosarat. Csak a másolatba tegyél croissant-t, és írasd ki mindkettőt. Ezután rendelesek néven tárolj három kosarat, köztük egy üreset, és saját for ciklussal írasd ki a tételszámukat.

Próba: [["kávé", "üdítő"], [], ["croissant"]] → 2, 0, 1 tétel. A lista értékadása önmagában nem másolás. A copy csak a külső listát másolja; beágyazott listánál a belső listák továbbra is közösek lehetnek. Ne ígérj mély másolatot.

## K4 – Összeg, átlag és maximum (10 perc)

A feldolgozas.py mellé külön saját próbában egész forintos rendelési összegekkel dolgozz. Ciklussal összegezz és keress maximumot. Üres lista esetén adj tájékoztatást; az indexelés és az osztás csak a nem üres ágban történjen. A számítás után hasonlítsd össze az eredményt a sum és max függvényével.

Próbák: [450, 840, 520] → összeg 1810, maximum 840, átlag két tizedesre 603.33; [450] → 450, 450, 450.00; [] → nincs indexelés vagy nullával osztás. A maximum kezdőértéke valódi listaelem legyen.

## K5 – Résztvevők és sorsolás (12 perc)

Új külön próbában kérj neveket vesszővel elválasztva. Split után minden rész széleit vágd le; az üres részeket új lista építésével hagyd ki. A nevek betűalakját őrizd meg. Nem üres névlistából a random.choice válasszon.

Az import random a standard könyvtár modulját teszi elérhetővé, nem kell pip csomag. A tutor előbb magyarázza el az import és a choice szerepét. Próbák: "Anna, , Béla," → két résztvevő; ", ," → nincs sorsolás; "Anna" → Anna. Több résztvevőnél a pontos véletlen eredményt nem írjuk elő. Két futásban azonos név is előfordulhat.

## K6 – Napi ajánlat a büfében (18 perc)

A működő bufe_04.py-ból a tanuló készítsen saját másolatot. Egy ajánlott termék ára a normál ár 80%-a egész forintra lefelé kerekítve; a diákkedvezmény ezután a csökkentett kosárösszeg // 10 része. A két százalékot nem adjuk egyszerűen össze.

A tanuló írjon ajanlati_ar(termek, napi_ajanlat) függvényt a normál árlekérdezésre építve. A kosar_osszege és a blokkot_mutat is kapja meg ugyanazt a napi ajánlatot, és ezt az árfüggvényt használja. Az ajánlatot egyszer válasszuk ki, ne minden árhívásban sorsoljunk újra.

Először rögzített próba: ajánlat kávé; kosár ["kávé", "üdítő"] → 360 + 390 = 750 Ft. Diáknak 75 Ft kedvezmény, 675 Ft fizetendő, 1000 Ft-ból 325 Ft visszajár. Nem diáknak 750 Ft fizetendő. Csak a számítás igazolása után kerüljön be a random.choice, nem üres kínálaton.

A fő csomag nem tartalmazza készen ezt a bővítést. A kódot itt is a tanuló írja, fokozatos tutorsegítséggel.
