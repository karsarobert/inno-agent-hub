# Mérési adatok elemzése

## Tanulási cél

`std::vector<int>` bejárása, minimum- és maximumkeresés, valamint a cím és az érték megkülönböztetése.

## Előfeltétel

Feltételek és ciklusok biztos használata.

## Feladat

Olvass be pontosan 8 egész mérési értéket egy `std::vector<int>`-be. Határozd meg és írd ki a minimumot, maximumot és az átlagot.

Ezután készíts egy rövid kódrészletet, amely egy `int` változó címét (`&ertek`) és értékét kiírja, majd mutatón keresztül eggyel növeli az értékét.

## Bemenet és kimenet

- Bemenet: 8 egész szám.
- Kimenet: minimum, maximum és lebegőpontos átlag.

## Utalások

- A minimum és maximum kezdetben legyen az első elem.
- Az átlaghoz az összeg legyen elegendően nagy típusú, az osztás pedig lebegőpontos.
- A mutató csak addig legyen használatban, amíg egy valóban létező változóra mutat.

## Ellenőrzési szempontok

- A program nyolc beolvasott értéket dolgoz fel.
- Negatív értékek esetén is helyes a minimum és maximum.
- A mutatós példában az érték tényleg megváltozik.
- A hallgató elmagyarázza, mi a különbség `ertek`, `&ertek` és `*mutato` között.

## Lehetséges bővítés

Rendezd a vektort növekvő sorrendbe `std::sort` használatával, majd hasonlítsd össze a megoldást a buborékrendezés működésével.
