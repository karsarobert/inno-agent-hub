"""Egy súly tanulása. A cél a w = 3; minden sor egy frissítés UTÁNI állapot."""
from segedletek import uj_mappa, adatok_mentese, gradiens_abra, kesz

# BEÁLLÍTÁSOK – első alkalommal változtatás nélkül futtasd.
tanulasi_rata = 0.1
lepesek_szama = 8
kezdo_suly = -1.0

if not 0 < tanulasi_rata <= 1.2 or not 1 <= lepesek_szama <= 100:
    raise SystemExit("Ebben a példában: 0 < ráta <= 1.2; 1–100 lépés.")

# A VIZSGÁLT SZÁMÍTÁS
suly = kezdo_suly
sorok = [[0, suly, (suly-3)**2]]
print("Lépés | Súly | Veszteség")
print(f"{0:5d} | {suly: .6f} | {(suly-3)**2:.6f}  (kezdet)")
for lepes in range(lepesek_szama):
    gradiens = 2 * (suly - 3)
    suly = suly - tanulasi_rata * gradiens
    veszteseg = (suly - 3) ** 2
    sorok.append([lepes+1, suly, veszteseg])
    if lepes < 8 or lepes+1 == lepesek_szama:
        print(f"{lepes+1:5d} | {suly: .6f} | {veszteseg:.6f}")

# KÉSZ ÁBRÁZOLÁS – a teljes számsor a CSV-ben is megmarad.
mappa = uj_mappa(__file__)
adatok_mentese(mappa, {"tanulasi_rata": tanulasi_rata, "lepesek_szama": lepesek_szama,
                       "kezdo_suly": kezdo_suly, "vegso_suly": suly, "vegso_veszteseg": veszteseg},
               ["lepes", "suly", "veszteseg"], sorok)
gradiens_abra(mappa, sorok)
kesz(mappa)
