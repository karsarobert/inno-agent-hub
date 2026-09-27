"""Kész adatgenerálás, mérés és rajzolás a 4–5. programhoz."""
import hashlib
from time import perf_counter
from segedletek import np, plt, KEK, NARANCS, ZOLD, kep_mentese, adatok_mentese, kesz


def regresszios_adatok():
    """Rögzített 64 tanító- és 128 validációs minta. Nincs tesztmérés."""
    veletlen = np.random.default_rng(2026)
    x = veletlen.uniform(-3, 3, (192, 1)).astype("float32")
    y = (np.sin(1.5*x) + .3*x + veletlen.normal(0, .3, x.shape)).astype("float32")
    return x[:64], y[:64], x[64:], y[64:]


def kezdeti_azonosito(modell):
    tar = b"".join(s.tobytes() for s in modell.get_weights())
    return hashlib.sha256(tar).hexdigest()[:16]


def halo_mentese(mappa, modell, tortenet, adatok, beallitasok, kezdes):
    tanito_x, tanito_y, validacios_x, validacios_y = adatok
    tanito_becsles = modell(tanito_x, training=False).numpy()
    validacios_becsles = modell(validacios_x, training=False).numpy()
    tanito_mae = float(np.mean(np.abs(tanito_y-tanito_becsles)))
    validacios_mae = float(np.mean(np.abs(validacios_y-validacios_becsles)))
    buntetes = sum(float(v.numpy()) for v in modell.losses)
    negyzetosszeg = sum(float(np.sum(r.kernel.numpy()**2)) for r in modell.layers if hasattr(r, "kernel"))
    eredmeny = dict(beallitasok)
    eredmeny.update({"tanito_mae_vegso": tanito_mae, "validacios_mae_vegso": validacios_mae,
                    "l2_buntetes": buntetes, "validacios_loss_vegso": validacios_mae+buntetes,
                    "kernel_negyzetosszeg": negyzetosszeg, "parameterek": modell.count_params(),
                    "tanitas_es_meres_masodperc": round(perf_counter()-kezdes, 3),
                    "eszkoz": "CPU", "tanito_mintak": 64, "validacios_mintak": 128,
                    "adatmag": 2026, "legjobb_val_mae_epocha": int(np.argmin(tortenet.history["val_mae"])+1),
                    "ertekelt_allapot": "utolso epocha; nincs suly-visszaallitas", "teszt_hasznalata": False})
    kulcsok = ["loss", "mae", "val_loss", "val_mae"]
    sorok = [[i+1]+[float(tortenet.history[k][i]) for k in kulcsok]
             for i in range(len(tortenet.history["loss"]))]
    adatok_mentese(mappa, eredmeny, ["epocha"]+kulcsok, sorok)
    # Az epochátlag és az utolsó súlyokkal végzett mérés külön fogalom.
    abra, t = plt.subplots()
    epochak = np.arange(1, len(tortenet.history["mae"])+1)
    t.plot(epochak, tortenet.history["mae"], color=KEK, label="Tanítási MAE (epochátlag)")
    t.plot(epochak, tortenet.history["val_mae"], color=NARANCS, label="Validációs MAE (epocha végén)")
    t.set(xlabel="Epocha", ylabel="MAE", title="Becslési hibák a tanítás során")
    t.legend(); t.grid(alpha=.2)
    kep_mentese(abra, mappa, "tanulasi_gorbek.png")
    racs = np.linspace(-3, 3, 400, dtype="float32").reshape(-1, 1)
    becsles = modell(racs, training=False).numpy()
    abra, t = plt.subplots()
    t.scatter(tanito_x, tanito_y, s=25, color=KEK, label="Tanítóminták")
    t.scatter(validacios_x, validacios_y, s=20, marker="x", color=NARANCS, alpha=.6, label="Validációs minták")
    t.plot(racs, np.sin(1.5*racs)+.3*racs, "--", color="gray", label="Adatgenerátor zaj nélküli görbéje")
    t.plot(racs, becsles, color=ZOLD, linewidth=2, label="Hálózat becslése")
    t.set(xlabel="Bemenet x", ylabel="Folytonos cél / becslés", title="Mit tanult a hálózat?")
    t.legend(fontsize=9)
    kep_mentese(abra, mappa, "becsles.png")
    abra, t = plt.subplots()
    t.plot(epochak, tortenet.history["val_loss"], color=NARANCS, label="Validációs loss: MAE + büntetés")
    t.plot(epochak, tortenet.history["val_mae"], color=KEK, label="Validációs MAE: becslési hiba")
    t.set(xlabel="Epocha", ylabel="Érték", title="Veszteség és becslési hiba")
    t.legend(); t.grid(alpha=.2)
    kep_mentese(abra, mappa, "loss_es_mae.png")
    print("\nFUTÁSI ÖSSZEFOGLALÓ")
    print(f"Eszköz: CPU | Minták: 64 tanító / 128 validációs")
    print(f"Hálózat: 1 → {beallitasok['rejtett_neuronok']} ReLU → 1 lineáris kimenet")
    print(f"Epochák: {beallitasok['epochok']} | L2: {beallitasok['l2_erosseg']}")
    print(f"Tanítható paraméterek: {modell.count_params()}")
    print(f"Végső tanítási MAE: {tanito_mae:.6f}")
    print(f"Végső validációs MAE: {validacios_mae:.6f}")
    print(f"L2-büntetés: {buntetes:.6f} | Validációs teljes loss: {validacios_mae+buntetes:.6f}")
    print(f"Dense súlymátrixok négyzetösszege: {negyzetosszeg:.6f}")
    print(f"Tanítás és mérés: {eredmeny['tanitas_es_meres_masodperc']:.3f} s (import nélkül)")
    print("Az utolsó epocha modelljét mérjük; a validáció alapján nem állítottunk vissza súlyokat.")
    kesz(mappa)
