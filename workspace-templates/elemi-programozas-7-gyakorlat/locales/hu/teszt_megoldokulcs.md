# EP_07 – A két záró teszt értékelési kulcsa

Oktatói/tutori segéd, első válaszadás előtt nem mutatandó meg. A fájl a munkatérben technikailag hozzáférhető a hallgatónak: ez tanulási önellenőrző teszt, nem titkos vizsga.

## Pontozás és önállóság

- T1: 10 × 1 pont, az alábbi részpontokkal; helyes saját megfogalmazás elfogadható.
- T2 KÓD1–KÓD5: 0,5 pont a teljes kimenetért, 0,5 a kért magyarázatért.
- T2 KÓD6–KÓD10: 0,5 pont a hiba/ok, 0,5 a helyes javítás. Nem kell az egész programot újra megírnia; az érintett működő sorok/behúzás elegendők. A lent látható teljes javított rövid tesztkódok az értékelést segítik, nem a fő programozási feladatok megoldásai.
- Nincs negatív pont vagy automatikus érdemjegy. T1 x/10, T2 y/10, összesen z/20.
- Az első, segítség és előzetes futtatás nélküli válasz adja az önálló pontot. Az érdemi segítséggel vagy futtatás után kialakult helyes válasz külön támogatott teljesítmény; a megfelelő önálló pontrész abból nem következtethető. Szükség esetén jelezd az összes helyesen megválaszolt pontot is külön a támogatott pontokkal, de ne keverd az önálló eredménnyel.
- A hiányzó, még várt válasz részleges teszt. Kimondott kihagyás befejezéskor 0 pont, és nem azonos egy hibás próbálkozással. A későbbi javítás nem írja felül az első eredményt.
- Egyenértékű kód, saját változónév és idézőjeltípus elfogadható; a típus, jelentés és tényleges viselkedés számít.

## E1

Tuple, három mezővel: terméknév tea, darabszám 2, egységár 350 Ft.

Pontozás: 0,5 pont a tuple típusért, 0,5 a mezők helyes jelentéséért.

## E2

Az (5) int; az (5,) egyelemű tuple. A vessző hozza létre a tuple-t, a zárójel önmagában csak csoportosít.

Pontozás: 0,5 pont a két típusért, 0,5 a vessző szerepéért.

## E3

Az eredeti elemsorrend és az ismétlődések/gyakoriság.

Pontozás: 0,5 pont információnként.

## E4

A halmaznak nincs pozíció alapú indexelése; iterációval mégis elkérhetők az elemei. A sorted új listát ad.

Pontozás: 0,5 pont az indexelés/bejárás megkülönböztetéséért, 0,5 az új listáért.

## E5

A meglévő elem újabb addja nem növeli az elemszámot. A remove hiánynál hibát okoz, a discard nem.

Pontozás: 0,5 pont az ismételt addért, 0,5 a törlések eltéréséért.

## E6

A különbségben az első halmaz másodikból hiányzó elemei vannak. A szimmetrikus különbségben pontosan az egyik halmaz elemei, mindkét oldalról, a közösek nélkül.

Pontozás: 0,5 pont műveletenként.

## E7

Minden elsőbeli elem szerepel-e a másodikban; nem puszta elemszámvizsgálat. Üres bal oldalon nincs ellenpéldát adó elem, ezért True.

Pontozás: 0,5 pont a tartalmi részhalmazért, 0,5 az üres eset indoklásáért.

## E8

len: minden tétel; len(set): különböző termékfajták; count: a megadott keresett termék előfordulásai.

Pontozás: 0,5 pont a két len szerepének helyes megkülönböztetéséért, 0,5 a count jelentéséért.

## E9

list/dict/set módosítható; int/str/tuple nem. Minden esetben a kapott objektumhoz kötődik a helyi paraméternév; a típus módosíthatósága és a végzett művelet magyarázza az eltérő hatást.

Pontozás: 0,5 pont a besorolásért, 0,5 az egységes átadás és a művelet kapcsolatának magyarázatáért. A tuple belső listájának külön esetére helyes utalás elfogadható.

## E10

Az értékadás új listához köti a helyi paraméternevet; a hívó eredeti listája nem változik. Az append a közösen elért eredeti listát bővíti, ez a hívónál látható.

Pontozás: 0,5 pont hatásonként.

# T2 – Kódismeret

## KÓD1

Az eredeti kód kimenete:

```text
tea: 600 Ft
```

A darab és az egységár szorzata: 3 × 200.

## KÓD2

Az eredeti kód kimenete:

```text
5
3
2
```

Öt tétel, három termékfajta, két keksz.

## KÓD3

Az eredeti kód kimenete:

```text
['alma', 'szilva']
False
True
```

Az alma hiányzik a másodikból; az üres halmaznak nincs hiányzó eleme. A körte közös, így kimarad a szimmetrikus különbségből.

## KÓD4

Az eredeti kód kimenete:

```text
11
10
```

A paraméter helyi név; a függvény az új számértékhez rendeli. A hívó nem rendeli újra a külső szam nevet.

## KÓD5

Az eredeti kód kimenete:

```text
['kávé', 'tea']
None
```

Az append a közösen elért listát módosítja. A végrehajtott return nélkül befejeződő függvény None-t ad.

## KÓD6

Az eredeti kód hibával áll le: TypeError. A név ismerete önmagában nem feltétel, a hiba okának felismerése számít.

A halmaz nem indexelhető. A sorted új listáját bejárva minden elem megjelenik, meghatározott sorrendben.

Egy helyes javítás:

```python
termekfajtak = {"tea", "keksz"}
for termek in sorted(termekfajtak):
    print(termek)
```

Javítás utáni kimenet:

```text
keksz
tea
```

## KÓD7

Az eredeti kód hibával áll le: AttributeError. A név ismerete önmagában nem feltétel, a hiba okának felismerése számít.

A {} szótár, amelynek nincs add metódusa. Üres halmazhoz set() kell.

Egy helyes javítás:

```python
termekfajtak = set()
termekfajtak.add("tea")
print(sorted(termekfajtak))
```

Javítás utáni kimenet:

```text
['tea']
```

## KÓD8

Az eredeti kód kimenete:

```text
2
```

A kosar nevet halmazhoz rendeltük, így azon az ismétlődő teák egy elemre csökkentek. Az eredeti listát megtartjuk; külön névhez kerülhet a halmaz.

Egy helyes javítás:

```python
kosar = ["tea", "tea", "keksz"]
termekfajtak = set(kosar)
print(len(kosar))
```

Javítás utáni kimenet:

```text
3
```

## KÓD9

Az eredeti kód kimenete:

```text
['kávé', 'tea']
['kávé', 'tea']
```

Az uj = kosar ugyanahhoz a listához rendel másik nevet. A copy új listát készít; a példabeli szöveges elemeknél a sekély másolat elég.

Egy helyes javítás:

```python
def bovitett_kosar(kosar):
    uj = kosar.copy()
    uj.append("tea")
    return uj

kosar = ["kávé"]
masik = bovitett_kosar(kosar)
print(kosar)
print(masik)
```

Javítás utáni kimenet:

```text
['kávé']
['kávé', 'tea']
```

## KÓD10

Az eredeti kód kimenete:

```text
{'tea': 1}
None
```

A return a ciklusban az első menet után befejezi a hívást; üres listánál el sem érjük. A for utáni return a teljes eredményt adja, üres esetben is.

Egy helyes javítás:

```python
def darabszamokat_ad(kosar):
    eredmeny = {}
    for termek in kosar:
        eredmeny[termek] = kosar.count(termek)
    return eredmeny

print(darabszamokat_ad(["tea", "keksz"]))
print(darabszamokat_ad([]))
```

Javítás utáni kimenet:

```text
{'tea': 1, 'keksz': 1}
{}
```

## Visszajelzés és lezárás

A teljes T2 válaszadás után értékelj. A hibás/részleges válasz konkrét félreértését magyarázd meg, kérj rövid javítást; ekkor a tanuló már futtathat. A helyes válaszokat ne elemezd újra hosszan. Adj legfeljebb két konkrét gyakorlási célt.

A programozási feladatok állapota, az önálló tesztpont és a segítség utáni javítás külön maradjon. A /20 önmagában nem mastery és nem teljes programozási önállóság. Nagyobb pótlás pontos folytatási ponttal kerül későbbre.
