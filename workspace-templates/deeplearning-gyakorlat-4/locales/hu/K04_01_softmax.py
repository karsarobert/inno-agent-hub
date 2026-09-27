"""Opcionális: három pontszámból közösen normalizált valószínűségek."""
from segedletek import np, plt, uj_mappa, adatok_mentese, kep_mentese, kesz

logitok = np.array([2.0, 1.0, 0.0])
kozos_eltolas = 0.0

# A maximum kivonása nem változtatja meg a softmax arányait.
eltolt_logitok = logitok + kozos_eltolas
exponencialisak = np.exp(eltolt_logitok - np.max(eltolt_logitok))
valoszinusegek = exponencialisak / np.sum(exponencialisak)
print("Logitok:", eltolt_logitok)
print("Valószínűségek:", np.round(valoszinusegek, 6))
print("Összeg:", np.sum(valoszinusegek))
mappa = uj_mappa(__file__)
adatok_mentese(mappa, {"logitok": logitok.tolist(), "kozos_eltolas": kozos_eltolas},
               ["logit", "valoszinuseg"], zip(eltolt_logitok, valoszinusegek))
abra, t = plt.subplots()
t.bar([1, 2, 3], valoszinusegek, color="#075ac8")
t.set(xlabel="Osztály sorszáma", ylabel="Becsült valószínűség", ylim=(0, 1), xticks=[1, 2, 3])
kep_mentese(abra, mappa, "softmax.png")
kesz(mappa)
