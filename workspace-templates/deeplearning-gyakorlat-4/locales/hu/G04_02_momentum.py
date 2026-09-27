"""Két frissítési szabály ugyanazon L(x,y)=x²/20+y² függvényen."""
from segedletek import np, uj_mappa, adatok_mentese, momentum_abra, kesz

# BEÁLLÍTÁSOK – a kötelező kísérletben csak a momentum változik.
momentum = 0.9
tanulasi_rata = 0.1
lepesek_szama = 40

if not 0 <= momentum < 1 or not 0 < tanulasi_rata <= 0.8 or not 1 <= lepesek_szama <= 500:
    raise SystemExit("Megengedett: 0 <= momentum < 1, 0 < ráta <= 0.8, 1–500 lépés.")

def utvonal(beta):
    hely = np.array([-7.0, 2.0])
    sebesseg = np.zeros(2)
    pontok = [hely.copy()]
    for _ in range(lepesek_szama):
        gradiens = np.array([hely[0] / 10, 2 * hely[1]])
        sebesseg = beta * sebesseg - tanulasi_rata * gradiens
        hely = hely + sebesseg
        pontok.append(hely.copy())
    return np.array(pontok)

# beta=0 esetén a korábbi sebesség hatása eltűnik.
utak = {"Egyszerű gradiensmódszer": utvonal(0.0),
        f"Momentum (β={momentum})": utvonal(momentum)}
sorok = []
for nev, pontok in utak.items():
    x, y = pontok[-1]
    print(f"{nev}: végpont=({x:.4f}, {y:.4f}), veszteség={x*x/20+y*y:.6f}")
    sorok.extend([nev, i, float(p[0]), float(p[1]), float(p[0]**2/20+p[1]**2)]
                 for i, p in enumerate(pontok))
mappa = uj_mappa(__file__)
adatok_mentese(mappa, {"momentum": momentum, "tanulasi_rata": tanulasi_rata,
                       "lepesek_szama": lepesek_szama, "pontos_gradiens": True},
               ["modszer", "lepes", "x", "y", "veszteseg"], sorok)
momentum_abra(mappa, utak)
kesz(mappa)
