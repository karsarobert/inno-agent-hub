"""A validáció alapján kiválasztott, már megtanított hálózat végső tesztje.
Nincs újratanítás. A kiválasztás indokát a teszt előtt kell megadni.
"""
from segedletek import (GYOKER, csomagok_ellenorzese, np, json_mentes,
                       osztalyozasi_abrak, nezet_frissites)
import json
import shutil

# A HALLGATÓ EZT A KÉT SORT TÖLTI KI a négy spirálfutás összevetése UTÁN.
# A mappát ő választja, az indokot saját szavaival írja; a tesztet még nem nézi meg.
KIVALASZTOTT_FUTAS = ""
VALASZTAS_INDOKA = ""

if not KIVALASZTOTT_FUTAS or not VALASZTAS_INDOKA.strip():
    raise SystemExit('Előbb válassz a validáció alapján! Írd be a futási mappa nevét '
                     'és a választás indokát a két üres szöveg helyére.')
mappa = (GYOKER / 'eredmenyek' / KIVALASZTOTT_FUTAS).resolve()
if mappa.parent != (GYOKER / 'eredmenyek').resolve():
    raise SystemExit('Csak az eredmenyek mappa közvetlen futási almappájának nevét add meg!')
if not all((mappa / nev).is_file() for nev in ['modell.keras', 'teszt_adatok.npz', 'beallitasok.json']):
    raise SystemExit('A kiválasztott futás hiányos vagy nem található. Ellenőrizd a mappanevet!')
celmappa = mappa / 'vegso_teszt'
if (celmappa / 'eredmeny.json').is_file():
    raise SystemExit('Ezt a modellt már tesztelted. Nyisd meg a meglévő eredményt; '
                     'ne hangolj tovább a teszteredmény alapján!')
csomagok_ellenorzese(['tensorflow'])
from tensorflow import keras
celmappa.mkdir(exist_ok=True)
json_mentes(celmappa / 'valasztas.json', {
    'kivalasztott_futas': KIVALASZTOTT_FUTAS, 'indok': VALASZTAS_INDOKA})
shutil.copyfile(__file__, celmappa / 'ertekelo_forras.py')

# A mentett súlyokat töltjük be: nincs fit(), nincs újratanítás.
modell = keras.models.load_model(mappa / 'modell.keras')
with np.load(mappa / 'teszt_adatok.npz') as adat:
    teszt_x = adat['jellemzok']
    teszt_cimke = adat['cimkek']
teszt_cel = keras.utils.to_categorical(teszt_cimke, num_classes=3)
eredmeny = modell.evaluate(teszt_x, teszt_cel, verbose=0, return_dict=True)
osztalyozasi_abrak(celmappa, modell, teszt_x, teszt_cimke, 'Végső teszt')
json_mentes(celmappa / 'eredmeny.json', eredmeny)
print('VÉGSŐ TESZT – a korábban mentett modell, 120 elkülönített minta.')
print('Kiválasztott futás:', KIVALASZTOTT_FUTAS)
print('Választás indoka:', VALASZTAS_INDOKA)
print('Tesztveszteség:', round(eredmeny['loss'], 4))
print('Tesztpontosság:', round(eredmeny['accuracy'], 4))
nezet_frissites(celmappa, tanitas=False)
print('Itt nincs új loss.png: nem történt tanítás. A teszt ábráit nyisd meg.')
print('Előbb értelmezd az ábrákat Innóval: melyik valódi osztályt melyiknek becsülte a modell?')
print('Ha nincs tévesztés, magyarázd el az átlót és azt, mely pontokra vonatkozik a 100%.')
print('Az ábrák megbeszélése után következik a 10 kérdéses kódértési teszt.')
