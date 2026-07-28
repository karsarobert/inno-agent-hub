---
name: example-skill
description: >-
  Egy mondatban írd le, mit csinál ez a készség és mikor aktiválódik. Az Agent a description alapján dönti el,
  hogy meghívja-e a készséget, ezért egyértelműen írd le: „használd, amikor a felhasználónak XXX-ra van szüksége”.
  Támogatott az egysoros forma, valamint a több soros YAML behajtott blokkérték (>- vagy |) is.
---

# Példakészség

<!--
  Ez egy „munkaterület-privát készség” példa. Helyezd ide: <sablon>/.skills/<készségneve>/SKILL.md.
  Az ehhez a munkaterülethez kötött munkamenetek automatikusan betöltik (az inno-agent injektálja).
  - A frontmatter tetején levő name értékének egyeznie kell a könyvtár nevével.
  - A törzsszövegben egyértelműen add meg: aktiválási feltételek, munkafolyamat, kimeneti formátum, alapelvek.
  - Ha sablonokat/szkripteket/referenciaanyagokat is mellékelsz, tedd őket e készség könyvtárába, és a szövegben relatív útvonalon hivatkozz rájuk.
  Beküldés előtt töröld ezeket a megjegyzéseket.
-->

Alakítsd át a(z) <bemenet> elemet <kimenet> formátumba.

## Aktiválási feltételek

Használd, amikor a felhasználónak „<forgatókönyv-kulcsszó>” szükséges.

## Munkafolyamat

1. <Első lépés>
2. <Második lépés>
3. **Exportálás a munkaterületre**: az eredményt írd a jelenlegi munkaterület egyik fájljába, ne csak a beszélgetésben add meg.

## Kimeneti formátum

```text
<Adj meg konkrét kimeneti mintát, amelyet az Agent követhet>
```

## Alapelvek

- <Első alapelv>
- <Második alapelv>
