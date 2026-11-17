# Ellenőrzési jelentés

Ellenőrzés: 2026. november 17.; Python 3, külső csomag nélkül.

## Sikeres ellenőrzések

- 25 gyökérszintű fájl; ép ZIP és pontos UTF-8 tartalom.
- A JSON-fájlok és az összes Python-fájl szintaktikailag érvényes.
- A Python-azonosítók magyar, ékezet nélküli nevek.
- Az időkeret 90 perc; 10 elméleti és 10 kódos zárókérdés.
- A kódos kérdések közül 5 értelmezési, 5 hibakeresési feladat.
- A kezdő osztály helykitöltőket tartalmaz, szándékosan nem kész megoldás.
- A közöslistás hibapélda a várt, hibásan közös állapotot mutatja.
- Külön tárolt referenciamegoldással az A1, A2, A3, B1, Z1 és mind
  ellenőrzések tényleges futása sikeres.
- A négy tényleges mellékelt adatfájl összesítése a leírt eredményt adja.
  A vegyes fájl hibás sorai: 2, 5, 7, 8; üres sora: 3.
- Az ures.txt 0 bájtos; a vegyes fájl utolsó sora nem zárul sortöréssel.
- A beolvasott források a feldolgozás után változatlanok.
- Üres és csak hibás adat, hiányzó és megnyithatatlan bemenet,
  ismételt mentés és írási hiba ellenőrizve.
- Az elutasított kérések állapotváltozatlansága, külön példányok,
  az objektummegosztás, a 0 Ft-os értékesítés és a __str__ ellenőrizve.
- Mind a 10 kódos kérdés tényleges kimenete vagy kivétele egyezik a kulccsal.
- Szándékosan elrontott referenciaváltozatokon az ellenőrzők felismerték
  az árlistamegosztást, az osztályszintű közös listát, a kihagyott ingyenes
  értékesítést és az ellenőrzés előtti hibás állapotmódosítást.

## Határok

A referenciamegoldás és az ellenőrzéshez használt változatai nem részei
a hallgatói ZIP-nek. A csomag nem tartalmaz kész Bufe-megoldást.
A kezdőkódok funkcionális próbái hallgatói munka előtt szándékosan hibát jeleznek.

Az InnoAgent alkalmazásba történő import és az alkalmazásban zajló
teljes tutorbeszélgetés ebben az ellenőrzésben nem történt meg.
A preset.json alapmetaadat; a feladatok.json helyi tartalomjegyzék.
A kódolási szerkezet és a hallgatói magyarázat vizsgálata a tutor feladata.
