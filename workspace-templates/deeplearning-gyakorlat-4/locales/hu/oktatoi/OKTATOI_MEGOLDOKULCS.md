# Oktatói megoldókulcs – rögzített záróteszt

A kérdéssor nem bővíthető és nem cserélhető le az agent által rögtönzött kérdésekre.
Az első választ pontozzuk; utána magyarázat jár. A segítséggel adott válasz
ténye külön rögzítendő, a válasz utáni tanári magyarázat nem előzetes segítség.

| Kérdés | Helyes válasz |
|---|---|
| 1 | B |
| 2 | D |
| 3 | A |
| 4 | C |
| 5 | B |
| 6 | D |
| 7 | C |
| 8 | A |
| 9 | B |
| 10 | D |

## 1. Egy súlyfrissítés

**B.** A gradiens −8. Az új súly −1 − 0,1·(−8) = −0,2. Negatív érték kivonása növeli a súlyt.

## 2. Momentum nélkül

**D.** A beta * sebesseg tag nulla. A frissítés így hely = hely − tanulasi_rata * gradiens, vagyis az egyszerű gradiensmódszer.

## 3. A ReLU kimenete

**A.** A maximum elemenként a 0 és a bemenet közül választ. A negatív érték 0 lesz, a pozitív érték változatlan marad.

## 4. Sigmoid: kimenet és derivált

**C.** A sigmoid kimenete z=0 esetén 0,5. A lokális derivált 0,5·(1−0,5)=0,25. A kimenet és a derivált nem ugyanaz a szám.

## 5. A regressziós hálózat

**B.** A shape=(1,) a mintánkénti jellemzőszám. A Dense(64) egyetlen rejtett réteg. A Dense(1) megadott aktiváció nélkül lineáris kimenetet ad.

## 6. Hány tanítási frissítés?

**D.** 64/16=4. Mindegyik tanítási batch után egy optimalizálási frissítés történik. A validációs mérés nem további súlyfrissítés.

## 7. L2 és teljes veszteség

**C.** A négyzetösszeg 4+1=5. A büntetés 0,01·5=0,05, a teljes loss 0,12+0,05=0,17. A tiszta becslési MAE továbbra is 0,12.

## 8. Mit hasonlítsunk össze?

**A.** Az azonos célon és validációs mintákon mért MAE közvetlenül összevethető. Az eltérő regularizációval számolt teljes loss nem tiszta becslési hiba. Ez nem bizonyít minden adaton jobb működést.

## 9. Egy megtartott dropout-aktiváció

**B.** A megtartott aktiváció szorzója 1/(1−0,5)=2, így 0,8·2=1,6. A maszk=0 esetben lenne nulla a kimenet.

## 10. Dropout kiértékeléskor

**D.** A False miatt az else ág fut. Az inverted dropout kiértékeléskor változatlanul továbbít; nincs új maszk vagy külön skálázás. A nem futó ág változóit a Python nem értékeli ki.

## Visszajelzés a végén

Az X/10 pont mellé rövid, konkrét fogalmi visszajelzés jár. Ne adj önkényes
egyetemi érdemjegyet; a teszt nem bizonyít önálló programozási készséget.
A hibás válaszokhoz legfeljebb két ismétlendő témát emelj ki. Ha egy futási rész
kimaradt, a tesztpontszám mellett azt külön jelezd. A zárómondat:
„A 4. Deep Learning-gyakorlat véget ért.” Nincs automatikus házi vagy 11. kérdés.
