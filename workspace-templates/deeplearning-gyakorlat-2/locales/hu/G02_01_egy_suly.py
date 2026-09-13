"""Egyetlen súly egy tanulási lépése.

Ismert adat: x = 1, y = 3. A becslés a w súly és x szorzata.
A program összehasonlítja a becslést a céllal, majd egyszer módosítja w-t.
A kisebb tanulási ráta ugyanennél a gradiensnél kisebb lépést jelent.
Részletes kódbemutatás: PROGRAM_BEMUTATOK.md.
Szemléltetés: szemlelteto.html (böngészőben megnyitható).
"""

print('Egyetlen súly egy tanulási lépése.')
print('Ismert adat: x = 1, y = 3. A becslés a w súly és x szorzata.\nA program összehasonlítja a becslést a céllal, majd egyszer módosítja w-t.\nA kisebb tanulási ráta ugyanennél a gradiensnél kisebb lépést jelent.')

bemenet = 1.0
celertek = 3.0
suly = -1.0
TANULASI_RATA = 0.2

# A modellben most nincs tanulható bias: becslés = súly * bemenet.
becsles = suly * bemenet
veszteseg = (becsles - celertek) ** 2

# Ez a képlet más bemenet esetén is figyelembe veszi a láncszabályt.
gradiens = 2 * (becsles - celertek) * bemenet
uj_suly = suly - TANULASI_RATA * gradiens
uj_becsles = uj_suly * bemenet
uj_veszteseg = (uj_becsles - celertek) ** 2

print(f"Rogzitett bemenet x: {bemenet:.4f}")
print(f"Ismert cel y: {celertek:.4f}")
print(f"Kezdo suly w: {suly:.4f}")
print(f"Becsles y-kalap: {becsles:.4f}")
print(f"Veszteseg a lepes elott: {veszteseg:.4f}")
print(f"Gradiens: {gradiens:.4f}")
print(f"Tanulasi rata: {TANULASI_RATA:.4f}")
print(f"Uj suly: {uj_suly:.4f}")
print(f"Uj becsles: {uj_becsles:.4f}")
print(f"Veszteseg a lepes utan: {uj_veszteseg:.4f}")
