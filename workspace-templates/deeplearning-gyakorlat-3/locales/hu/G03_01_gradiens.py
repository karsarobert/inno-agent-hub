"""Egy lineáris neuron tanítása: tanulási időből szintetikus pontszám.
A súly és a bias gradienslépéseit NumPy-val számoljuk. Az ábrázolás kész.
"""
from segedletek import (np, regresszios_adatok, uj_mappa, gorbek_mentese,
                       regresszio_abra, json_mentes, nezet_frissites)

TANULASI_RATA = 0.02
EPOCHOK = 120
suly = 1.0
bias = 1.0

tanito_x, validacios_x, tanito_y, validacios_y = regresszios_adatok()
tortenet = {'loss': [], 'val_loss': []}
print('Egy bemenet → egy lineáris neuron: becslés = súly × idő + bias.')
print('80 tanítóminta, 20 validációs minta; mesterséges oktatási adatok.')

# A HALLGATÓ EZT A RÉSZT ÉRTELMEZI: egy epoch itt egy teljes batch.
for epoch in range(EPOCHOK):
    becsles = suly * tanito_x + bias
    hiba = becsles - tanito_y
    suly_gradiense = np.mean(hiba * tanito_x)
    bias_gradiense = np.mean(hiba)
    suly = suly - TANULASI_RATA * suly_gradiense
    bias = bias - TANULASI_RATA * bias_gradiense
    # L = MSE / 2, ezért a gradiensben nincs külön 2-es szorzó.
    tanito_loss = np.mean((suly * tanito_x + bias - tanito_y) ** 2) / 2
    validacios_loss = np.mean((suly * validacios_x + bias - validacios_y) ** 2) / 2
    if not np.isfinite(tanito_loss) or not np.isfinite(validacios_loss):
        raise SystemExit('A veszteség nem véges. Ellenőrizd a tanulási rátát Inno segítségével!')
    tortenet['loss'].append(float(tanito_loss))
    tortenet['val_loss'].append(float(validacios_loss))

# ELŐKÉSZÍTETT ÉRTÉKELÉS – nem kell megírni vagy módosítani.
mappa = uj_mappa(__file__)
gorbek_mentese(mappa, tortenet)
regresszio_abra(mappa, tanito_x, tanito_y, validacios_x, validacios_y, suly, bias)
json_mentes(mappa / 'beallitasok.json', {
    'tanulasi_rata': TANULASI_RATA, 'epochok': EPOCHOK,
    'suly': float(suly), 'bias': float(bias),
    'loss_tipusa': 'MSE / 2', 'validacios_loss': tortenet['val_loss'][-1]})
print(f'Súly: {suly:.4f}; bias: {bias:.4f}; validációs MSE/2: {tortenet["val_loss"][-1]:.4f}')
print(f'Tanulási ráta: {TANULASI_RATA}; epoch: {EPOCHOK}')
nezet_frissites(mappa)
