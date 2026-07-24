---
name: card-maker
description: Az angoltanulási anyag új szavait Anki-kompatibilis szókártyákba rendezi.
---

## Szókártyakészítő

### Aktiválási feltételek

Használd, ha a felhasználó szókártyát, Anki-kártyát, szókincslistát vagy új szavak rendezését kéri.

### Kártyaformátum

Minden kártya formája:

`szó vagy kifejezés;szófaj magyar jelentés | angol példamondat;címkék`

Példa:

```
ubiquitous;mn. mindenütt jelenlévő | Smartphones have become ubiquitous in daily life.;ielts academic
```

Szabályok:

- A példamondat lehetőleg a felhasználó eredeti szövegéből származzon; ha nincs ilyen, készíts IELTS-akadémiai környezetbe illő mondatot.
- A címkék mindig tartalmazzák az `ielts` címkét, emellett jöhet témacímke, például `technology` vagy `environment`.
- Egy alkalommal legfeljebb 20 kártyát készíts; a több szóból álló kifejezést egyben hagyd.

### Fájlművelet

Írd a kártyákat a `cards/<forrás-téma>.csv` fájlba ezzel a fejléccel:

```
#separator:Semicolon
#html:false
Szó vagy kifejezés;Jelentés és példamondat;Címkék
```

A készítés után közöld a fájl útvonalát és a kártyák számát. Röviden írd le az Anki importot: File → Import, elválasztójel: `;`.

### Tanulási események

- A forrásszöveget az `l2_archive` eszközzel archiváld `[IELTS-olvasás] <téma>` címformátummal.
- A `record_learning_event` eszközzel rögzíts `concept_explained` eseményt, `mastery_delta: 0.01` értékkel.
