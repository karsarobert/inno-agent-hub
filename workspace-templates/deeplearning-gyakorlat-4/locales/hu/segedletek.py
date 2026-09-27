"""Kész ábrázolás és mentés. A hallgatói feladatokhoz nem kell módosítani."""
from datetime import datetime
from pathlib import Path
import csv
import json
import sys

try:
    import numpy as np
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
except ImportError as hiba:
    raise SystemExit(
        f"Python-csomag nem tölthető be: {hiba}\n"
        f"Értelmező: {sys.executable}\nKérd az oktató segítségét!"
    ) from hiba

GYOKER = Path(__file__).resolve().parent
plt.rcParams.update({"font.size": 11, "figure.figsize": (10, 4.5),
                     "axes.spines.top": False, "axes.spines.right": False})
KEK, NARANCS, ZOLD = "#075ac8", "#b54a17", "#087e87"


def uj_mappa(program):
    nev = Path(program).stem
    idopont = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    mappa = GYOKER / "nezet" / f"{nev}_{idopont}"
    mappa.mkdir(parents=True, exist_ok=False)
    return mappa


def adatok_mentese(mappa, beallitasok, fejlec, sorok):
    (mappa / "eredmeny.json").write_text(
        json.dumps(beallitasok, ensure_ascii=False, indent=2, allow_nan=False),
        encoding="utf-8")
    with (mappa / "ertekek.csv").open("w", newline="", encoding="utf-8") as fajl:
        iro = csv.writer(fajl)
        iro.writerow(fejlec)
        iro.writerows(sorok)


def kep_mentese(abra, mappa, nev):
    abra.tight_layout()
    abra.savefig(mappa / nev, dpi=145)
    plt.close(abra)


def kesz(mappa):
    print("\nFUTÁS KÉSZ. Az ábrák és a számadatok helye:")
    print(mappa)
    print("Frissítsd a Nézet mappát / fájllistát, majd a MOSTANI mappa képét nyisd meg!")


def gradiens_abra(mappa, sorok):
    ertekek = np.asarray(sorok)
    abra, tengelyek = plt.subplots(1, 2, figsize=(10, 4))
    tengelyek[0].plot(ertekek[:, 0], ertekek[:, 1], "o-", color=KEK)
    tengelyek[0].axhline(3, color=NARANCS, linestyle="--", label="Minimum: w = 3")
    tengelyek[0].set(xlabel="Frissítések száma", ylabel="Súly", title="Hogyan változik a súly?")
    tengelyek[0].legend()
    tengelyek[1].plot(ertekek[:, 0], ertekek[:, 2], "o-", color=NARANCS)
    tengelyek[1].set(xlabel="Frissítések száma", ylabel="L = (w − 3)²", title="Veszteség")
    for t in tengelyek:
        t.grid(alpha=.2)
    kep_mentese(abra, mappa, "tanulasi_lepesek.png")


def momentum_abra(mappa, utak):
    abra, tengelyek = plt.subplots(1, 2, figsize=(11, 4.5))
    hatar_x = max(8, *(np.max(np.abs(u[:, 0])) * 1.05 for u in utak.values()))
    hatar_y = max(3, *(np.max(np.abs(u[:, 1])) * 1.05 for u in utak.values()))
    x, y = np.meshgrid(np.linspace(-hatar_x, hatar_x, 220),
                       np.linspace(-hatar_y, hatar_y, 160))
    for tengely, (nev, ut) in zip(tengelyek, utak.items()):
        tengely.contour(x, y, x*x/20+y*y,
                       levels=[.05, .2, .5, 1, 2, 4, 8, 16, 32], colors="#b7c7d8")
        tengely.plot(ut[:, 0], ut[:, 1], ".-", color=KEK, linewidth=1.2)
        tengely.scatter(*ut[0], color=ZOLD, s=55, label="Kezdőpont")
        tengely.scatter(*ut[-1], color=NARANCS, s=55, label="Utolsó pont", zorder=5)
        tengely.plot(0, 0, "+", color="black", markersize=10)
        tengely.set(title=nev, xlabel="x paraméter", ylabel="y paraméter",
                    xlim=(-hatar_x, hatar_x), ylim=(-hatar_y, hatar_y))
        tengely.legend(fontsize=9)
    kep_mentese(abra, mappa, "utvonalak.png")


def aktivacio_abra(mappa, fuggveny, derivalt, bemenetek):
    x = np.linspace(-8, 8, 801)
    abra, t = plt.subplots(1, 2, figsize=(11, 4.5))
    t[0].plot(x, fuggveny(x), color=KEK)
    t[0].scatter(bemenetek, fuggveny(bemenetek), color=NARANCS, zorder=5)
    t[1].plot(x, derivalt(x), color=ZOLD)
    t[1].scatter(bemenetek, derivalt(bemenetek), color=NARANCS, zorder=5)
    for tengely, cim, felirat in zip(t, ["Aktiváció", "Lokális derivált"], ["f(z)", "f′(z)"]):
        tengely.set(title=cim, xlabel="Bemenet z", ylabel=felirat)
        tengely.axhline(0, color="gray", linewidth=.6)
        tengely.axvline(0, color="gray", linewidth=.6)
        tengely.grid(alpha=.2)
    kep_mentese(abra, mappa, "aktivacio_es_derivalt.png")


def oszlop_abra(mappa, bemenet, kimenet, cim, fajl):
    hely = np.arange(1, len(bemenet)+1)
    abra, t = plt.subplots()
    t.bar(hely-.18, bemenet, width=.36, color=KEK, label="Bemenet")
    t.bar(hely+.18, kimenet, width=.36, color=NARANCS, label="Kimenet")
    t.axhline(0, color="gray", linewidth=.6)
    t.set(xlabel="Elem sorszáma", ylabel="Érték", title=cim, xticks=hely)
    t.legend()
    kep_mentese(abra, mappa, fajl)
