"""Ezt futtasd először. Nem telepít és nem tölt le semmit."""
import sys
from segedletek import np, plt, matplotlib, betolt_adatok, betolt_referencia, uj_mappa, kep_mentese, befejezes
print(f'Python: {sys.version.split()[0]} | Értelmező: {sys.executable}')
print(f'NumPy: {np.__version__} | Matplotlib: {matplotlib.__version__}')
adatok = betolt_adatok()
referencia = betolt_referencia()
for kulcs, alak in [('tanito_jelek', (512, 140)), ('validacios_jelek', (128, 140)),
                    ('normal_jelek', (128, 140)), ('rendellenes_jelek', (128, 140))]:
    if adatok[kulcs].shape != alak or not np.isfinite(adatok[kulcs]).all():
        raise SystemExit(f'Sérült adatfájl: {kulcs}. Kérd az oktató segítségét!')
for kulcs in ['normal_vissza', 'rendellenes_vissza']:
    if referencia[kulcs].shape != (128, 140) or not np.isfinite(referencia[kulcs]).all():
        raise SystemExit(f'Sérült referencia: {kulcs}. Kérd az oktató segítségét!')
mappa = uj_mappa(__file__)
abra, t = plt.subplots()
t.plot(adatok['normal_jelek'][0]); t.set(title='Az adatbetöltés és az ábramentés működik', xlabel='Mintapont indexe', ylabel='Skálázott jelérték')
kep_mentese(abra, mappa, 'ellenorzes.png')
try:
    from cpu_kornyezet import tf, keras
except SystemExit as hiba:
    print(hiba)
    print('RÉSZLEGES KÖRNYEZET – az 1., 3. és 4. példa futtatható; a 2. példához oktatói segítség kell.')
    befejezes(mappa, {'allapot': 'reszleges', 'tensorflow': False})
    raise SystemExit(1)
print(f'TensorFlow: {tf.__version__} | Keras: {keras.__version__}')
print(f'Látható GPU-k: {tf.config.get_visible_devices("GPU")}')
ellenorzes = tf.reduce_sum(tf.constant([1., 2., 3.])).numpy()
if float(ellenorzes) != 6.0:
    raise SystemExit('A CPU-s számítás ellenőrzése sikertelen.')
print('\nKÖRNYEZET RENDBEN – helyi adatok, CPU-s számítás és ábramentés ellenőrizve.')
befejezes(mappa, {'allapot': 'rendben', 'tensorflow': tf.__version__, 'numpy': np.__version__, 'eszkoz': 'CPU'})
