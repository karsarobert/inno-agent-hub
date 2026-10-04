# Rögzített záróteszt – 10 kérdés

Az agent egyesével adja fel. Minden kérdésnél egy helyes válasz van.
Az első egyértelmű választ pontozza; utána a kulcs szerint magyaráz.
A kérdések fogalmi és kódértési kérdések, nem előzetes futásjóslási feladatok.

## 1. Mi a tanítás célja az autoencoderben?

A. Minden bemenethez egy normál/rendellenes címkét kiadni.
B. A bemeneti jelet a saját kimenetén visszaállítani.
C. Minden bemenetet nullává alakítani.
D. A 140 mintapontot véletlen sorrendbe tenni.

## 2. Mit jelent a 140 az EKG-példában?

A. A tanítás epocháinak számát.
B. A felismerendő betegségek számát.
C. A normál jelek százalékos arányát.
D. Az egy jelszakaszhoz tartozó bemeneti értékek számát.

## 3. Miért szerepel ugyanaz a jelhalmaz kétszer?

```python
tanito_csomag = adatcsomag(tanito_jelek, tanito_jelek, keveres=True)
```

A. Az első a bemenet, a második a kívánt kimenet.
B. Véletlenül kétszer töltöttük le ugyanazt a fájlt.
C. Így kétszer annyi osztálya lesz a modellnek.
D. Az egyik normál, a másik rendellenes címkéket tartalmaz.

## 4. Mi a nyolcértékű szűk keresztmetszet szerepe?

A. Nyolc előre rögzített betegséget nevez meg.
B. Kiválasztja a nyolc legnagyobb eredeti mintapontot.
C. Korlátozott méretű, tanult belső reprezentációt továbbít.
D. Garantálja a hibátlan, veszteségmentes visszaállítást.

## 5. Mit jelentenek a 140 kimeneti szigmoid értékei?

A. A 140 osztály valószínűségét, amelyek összege egy.
B. A visszaállított jel 0 és 1 közötti amplitúdóit.
C. A tanítójelek sorszámait.
D. Az Adam által használt tanulási rátákat.

## 6. Mi az `axis=1` szerepe ebben a számításban?

```python
hibak = np.mean(np.abs(jelek - visszaallitott_jelek), axis=1)
```

A. Kiválasztja az első jelet, és a többit eldobja.
B. Az összes jel összes pontját egyetlen közös hibává átlagolja.
C. Csak a pozitív előjelű eltéréseket használja.
D. Jelenként átlagolja a mintapontok abszolút eltéréseit.

## 7. Melyik állítás igaz a G05_03 és G05_04 programra?

A. Minden futtatáskor új autoencodert tanítanak.
B. Automatikusan a hallgató legutolsó G05_02 modelljét használják.
C. A csomaghoz mellékelt, rögzített referencia rekonstrukcióit használják.
D. Véletlen számokat neveznek rekonstrukciónak.

## 8. Mi a téves riasztás ebben a gyakorlatban?

A. Valóban normál jelet rendellenesnek jelzünk.
B. Valóban rendellenes jelet helyesen jelzünk.
C. A tanítási veszteség csökken.
D. Egy normál jel normál besorolást kap.

## 9. Mit jelent az anomália-recall?

A. A riasztások közül valóban rendellenes jelek arányát.
B. A valóban rendellenes jelek közül észlelt jelek arányát.
C. A hibátlanul visszaállított mintapontok arányát.
D. Az összes normál tanítójel számát.

## 10. Mi változik a G05_04-ben, ha csak a küszöböt módosítjuk?

A. A tanult súlyok automatikusan újratanulnak.
B. Minden rekonstruált jel más lesz.
C. A valódi címkék a küszöbhöz igazodnak.
D. A rögzített hibaértékek alapján hozott döntések változhatnak.
