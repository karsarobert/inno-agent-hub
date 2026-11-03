# EP_08 – A két gyakorló teszt megoldókulcsa

Tutori/oktatói értékelési segédlet. Az önálló válaszadás végéig ne mutasd meg. A munkatérben elérhető, ezért a teszt nem titkos vizsga. Ez a fájl nem tartalmaz kész megoldóprogramot az A1–C1 feladatokhoz.

## Pontozás és visszajelzés

T1: kérdésenként 1 pont, legfeljebb 10. Egy helyes betű elfogadott, ha nem mond ellent neki a kísérő magyarázat. Ellentmondás esetén egyszer kérj tisztázást; ne találj ki választ. Több betű nem egyértelmű egyválaszos megoldás. Kihagyás 0.

T2 KÓD1–KÓD5: 1 pont a teljes, helyes értelmezés és a kért rövid ok együtt. A helyes eredmény lényegi indoklás nélkül vagy egyetlen lényegi rész hiánya 0,5 pont; félreértett működés 0. KÓD1-nél a négy érték egyértelmű elkülönítése a lényeg; az idézőjeltípus önmagában nem számít. KÓD3/KÓD5-nél külön indoklás nem kötelező, ha mindhárom eredmény helyes, és a KÓD5 kért eltérését megnevezi.

T2 KÓD6–KÓD10: 0,5 pont az ok (és a kért hibatípus), 0,5 a helyes javítás. Ekvivalens, működő megoldás elfogadott. Teljes új programot nem kell kérni. Kihagyás 0. A részpontok összege legfeljebb 10.

Az első önálló válasz eredményét különítsd el a támogatott választól és a javítástól. Ha a kérdés első válasza előtt segítséget kapott, jelöld támogatottnak, és a /10–/10–/20 eredmény mellé írd oda az érintett azonosítókat. Ne nevezd a támogatott összpontot tisztán önálló eredménynek. A későbbi javítás nem írja felül az eredeti pontot. A kihagyott vagy még fel nem tett kérdés nem teljesített; részleges tesztnél jelezd a megválaszolt kérdések számát is.

A teljes T2 után értékelj: külön T1 /10, T2 /10, összesen /20; majd csak a tényleges tévedéseket beszéljétek meg. A pontszám nem automatikus érdemjegy vagy elsajátítási százalék.

## T1

| Azonosító | Helyes válasz | Indoklás |
| --- | --- | --- |
| E1 | B | A munkamappa a futtatási környezet állapota; a .py helye önmagában nem elég. |
| E2 | D | A with lezárja a fájlt. Nem darabol, nem tisztít, és önmagában nem teker vissza. |
| E3 | A | Az üres sor is tartalmazhat sortöréskaraktert. Fájlvégnél nincs kiolvasott karakter, ezért üres szöveg tér vissza. |
| E4 | C | A szöveges olvasás szöveget ad; a számmá alakítás külön konverzió. A sorok végén a sortörés megmaradhat. |
| E5 | B | Mindkettő szövegrészek listáját adja. Az explicit elválasztóval üres mező is létrejöhet; a számkonverzió külön lépés. |
| E6 | D | Az argumentum karakterkészletként működik; a belső karakterekhez nem nyúl. |
| E7 | A | Az eredmény kulcsait a keresett halmaz határozza meg; a találat hiánya 0 darabot jelent. |
| E8 | C | A csonkítás a megnyitáskor történik, akkor is, ha később semmit sem írunk. |
| E9 | B | Az ismételt futás ismételt eseményt menthet. A sorhatárt a programnak kell megadnia; a napló előző sorának lezárása is számít. |
| E10 | D | A feladat a korábbi eladás ténylegesen eltárolt bevételét vizsgálja, nem a termék mai árát. |

## T2

### KÓD1

```text
'alma\n'
'\n'
'körte'
''
```

Az üres sor sortörést ad; az utolsó sor sortörés nélkül is olvasható; csak a negyedik olvasás fájlvég.

### KÓD2

```text
3
0
'A\n'
```

Az első read a végére jut, a másodiknak nem marad adat. A seek(0) kifejezetten a kezdetre állítja a pozíciót.

### KÓD3

```text
3
2
gyors | gyors | olcsó
```

A tabulátor és az ismételt szóköz whitespace. Három darab, két különböző érték; a join új elválasztókat tesz közéjük.

### KÓD4

```text
'három\n'
```

Az utolsó w megnyitás kiüríti az addigi tartalmat.

### KÓD5

```text
tea
3505
355
```

A szövegek + művelete összefűz. Az int utáni + számtani összeadás.

### KÓD6

ValueError: lezárt fájlból olvas. A read a with blokkon belül legyen; a szöveget ott eltárolhatja, és utána kiírhatja. Külön újranyitás is helyes.

A név a blokk után is létezik, de az általa hivatkozott fájlobjektum már le van zárva.

### KÓD7

A strip az üres sor "\n" értékét ""-vé teszi, így a ciklus ezt fájlvégnek téveszti. Az eredeti readline eredményét kell ""-hez hasonlítani, a tisztítás csak ezután jöjjön; vagy for sor in fajl bejárás használható.

A nyers és tisztított szöveg eltérő szerepű. A while leállásához a valódi fájlvég számít.

### KÓD8

A ciklus minden iterációban w móddal újranyit és töröl. Egyszer kell w módban megnyitni a for ciklus előtt, a for és write a with blokkon belül legyen. A puszta a-ra cserélés nem biztosít friss fájlt.

A megnyitás helye és módja együtt határozza meg, mi marad meg.

### KÓD9

A += során int és str összegzése TypeError. Az ármezőt int-té kell alakítani az összeadás előtt vagy közben, például osszeg += int(ar). Az eredmény 200.

A lista elemei szövegek; a látható számjegy nem automatikus számkonverzió.

### KÓD10

A cikluson belüli return az első elem után lezár. Üres listánál a ciklus és return nem fut, ezért None az implicit eredmény. A return osszeg a ciklus után legyen, a függvényen belül.

A helyes 0 kezdőérték és a teljes bejárás utáni visszatérés minden esetre eredményt ad.
