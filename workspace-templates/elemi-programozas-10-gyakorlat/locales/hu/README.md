# EP_10 – Saját büfé objektumokkal

Magyar nyelvű, 2 × 45 perces InnoAgent-gyakorlás.

## Használat

Az agent.md a tutor fő utasítása, a preset.json az alapleírás.
A többi Markdown-fájl a feladatokat és tutorsegédleteket adja.
A feladatok.json helyi tartalomjegyzék, nem alkalmazásimport-séma.

A hallgató egy Bufe osztályt készít, majd előkészített fájlfeldolgozó
programban használja. A csomag a jóváhagyott 90 perces útvonalat adja.

## Fájlok

- bufe.py: a hallgató itt építi a saját osztályát.
- peldanyok.py: a hallgató itt írja a többpéldányos próbát.
- kozos_lista.py: különálló, szándékosan hibás szemléltető.
- feldolgozas.py: működő fájlkezelési keret egy kijelölt hallgatói résszel.
- probak.py: szakaszonként futtatható ellenőrzések.
- eladasok_jo.txt, eladasok_vegyes.txt, eladasok_hibas.txt, ures.txt:
  UTF-8 próbaadatok.
- teszt_elmelet.md és teszt_kodismeret.md: 10 + 10 zárókérdés.
- teszt_megoldokulcs.md: tutorsegédlet; válaszadás előtt nem mutatandó meg.

A pass utasítások helykitöltők. A kezdőkód szándékosan nem teljesíti
az ellenőrzéseket a hallgatói munka előtt. Kész Bufe-megoldás nincs a ZIP-ben.

## Környezet és indítás

Python 3; külső csomag nem szükséges. A munkamappa a kicsomagolt
fájlok könyvtára legyen. A szakasz elkészítése után:

    python3 probak.py A1
    python3 probak.py A2
    python3 probak.py A3
    python3 peldanyok.py
    python3 probak.py B1
    python3 feldolgozas.py
    python3 probak.py Z1

A kész megoldás összes ellenőrzése:

    python3 probak.py mind

A futtatas.sh ugyanazokat az ellenőrzéseket indítja:

    sh futtatas.sh A1

## Elméleti előzmény

Az EP_10.html mérési és bankszámlapéldái után más problémában
alkalmazzuk az osztályok és példányok használatát.
Az elméleti HTML külön tananyag, nem része ennek a ZIP-nek:
https://chatgpt.com/library?file_id=libfile_04406558dfe481919a931b484fe9d547&account_id=personal

## Ellenőrzés

A csomag szintaktikai és funkcionális ellenőrzésének eredményeit
az ellenorzesi_jelentes.md tartalmazza. Az ellenőrzéshez használt
referenciamegoldás nem része a hallgatói csomagnak.
