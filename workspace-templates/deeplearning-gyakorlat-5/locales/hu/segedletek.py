"""Kész helyi adatbetöltés, ábrázolás és mentés. Nincs hálózati művelet."""
from pathlib import Path
from datetime import datetime
import json
import sys
import hashlib
try:
    import numpy as np
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
except (ImportError, OSError) as hiba:
    raise SystemExit(f'Hiányzó vagy nem betölthető csomag: {hiba}\nÉrtelmező: {sys.executable}\nKérd az oktató segítségét!') from hiba
GYOKER = Path(__file__).resolve().parent
KEK, NARANCS = '#1764aa', '#bc4b22'
plt.rcParams.update({'figure.figsize': (10, 5), 'font.size': 11})


def betolt_adatok():
    ut = GYOKER / 'adatok' / 'ekg_adatok.npz'
    if not ut.exists():
        raise SystemExit('Hiányzik az adatok/ekg_adatok.npz. Csomagold ki a teljes csomagot; kérd az oktató segítségét!')
    with np.load(ut, allow_pickle=False) as tar:
        return {kulcs: tar[kulcs].copy() for kulcs in tar.files}


def betolt_referencia():
    ut = GYOKER / 'adatok' / 'referencia_rekonstrukciok.npz'
    if not ut.exists():
        raise SystemExit('Hiányzik a mellékelt referencia_rekonstrukciok.npz. Ez nem az első feladat futási hibája: a csomaghoz mellékelt fájl szükséges.')
    meta = json.loads((GYOKER / 'adatok' / 'referencia_leiras.json').read_text(encoding='utf-8'))
    ellenorzo = hashlib.sha256((GYOKER / 'adatok' / 'ekg_adatok.npz').read_bytes()).hexdigest()
    if ellenorzo != meta['adathalmaz_sha256']:
        raise SystemExit('Az adatok és a referencia nem tartoznak össze. Állítsd vissza az eredeti adatok mappát!')
    with np.load(ut, allow_pickle=False) as tar:
        adatok = {k: tar[k].copy() for k in tar.files}
    print('ADATFORRÁS: mellékelt, valódi CPU-s tanításból mentett referencia; 30 epocha, bottleneck=8.')
    print('Ez a program nem tanít új modellt, és nem a saját legutóbbi G05_02 futásodat olvassa.')
    return adatok


def index_ellenorzes(index, darab):
    if not isinstance(index, int) or isinstance(index, bool) or not 0 <= index < darab:
        raise SystemExit(f'A minta_index 0 és {darab - 1} közötti egész szám legyen!')


def uj_mappa(program):
    """Rövid, példánként növekvő sorszám. Meglévő futást nem ír felül."""
    rovid = {'kornyezet_ellenorzes': '00_ellenorzes', 'G05_01_ekg_adatok': '01_adatok',
             'G05_02_autoencoder': '02_halo', 'G05_03_rekonstrukcios_hiba': '03_hiba',
             'G05_04_kuszob': '04_kuszob'}[Path(program).stem]
    alap = GYOKER / 'nezet'
    alap.mkdir(exist_ok=True)
    szamok = [int(p.name[len(rovid)+1:]) for p in alap.glob(rovid + '_*')
              if p.name[len(rovid)+1:].isdigit()]
    szam = max(szamok, default=0) + 1
    while True:
        mappa = alap / f'{rovid}_{szam:02d}'
        try:
            mappa.mkdir(exist_ok=False)
            return mappa
        except FileExistsError:
            szam += 1


def kep_mentese(abra, mappa, nev):
    abra.tight_layout()
    abra.savefig(mappa / nev, dpi=140, bbox_inches='tight')
    plt.close(abra)


def befejezes(mappa, eredmeny):
    eredmeny.update({'futas': mappa.name, 'mentes_ideje': datetime.now().astimezone().isoformat()})
    (mappa / 'eredmeny.json').write_text(json.dumps(eredmeny, ensure_ascii=False, indent=2), encoding='utf-8')
    print('\nFUTÁS KÉSZ. Az ábrák és számadatok helye:')
    print(mappa)
    print(f'Rövid mappanév: {mappa.name}')
    print('Képek: ' + ', '.join(p.name for p in sorted(mappa.glob('*.png'))))
    print(f'Frissítsd a Nézet mappát / fájllistát, majd nyisd meg a {mappa.name} mappát!')


def jelpar_rajz(mappa, normal, rendellenes, index):
    abra, tengelyek = plt.subplots(2, 1, figsize=(10, 6), sharex=True, sharey=True)
    for t, jel, nev, szin in zip(tengelyek, [normal, rendellenes], ['Normál', 'Rendellenes'], [KEK, NARANCS]):
        t.plot(jel, color=szin)
        t.set(title=f'{nev} jel · {index + 1}. példa (index: {index}) · 140 érték', ylabel='Skálázott jelérték')
        t.grid(alpha=.2)
    tengelyek[-1].set_xlabel('Mintapont indexe (nem másodperc)')
    kep_mentese(abra, mappa, 'ekg_jelek.png')


def rekonstrukcio_rajz(mappa, jelek, rekonstrukciok, cimek, nev='rekonstrukcio.png'):
    abra, tengelyek = plt.subplots(len(jelek), 1, figsize=(10, 3.8 * len(jelek)), squeeze=False, sharex=True, sharey=True)
    for t, jel, vissza, cim in zip(tengelyek[:, 0], jelek, rekonstrukciok, cimek):
        hiba = float(np.mean(np.abs(jel - vissza)))
        t.plot(jel, color=KEK, label='Eredeti jel')
        t.plot(vissza, color=NARANCS, label='Rekonstrukció')
        t.fill_between(np.arange(140), jel, vissza, color=NARANCS, alpha=.15, label='Eltérés')
        t.set(title=f'{cim} · MAE: {hiba:.6f}', ylabel='Skálázott jelérték')
        t.grid(alpha=.2)
        t.legend(loc='best')
    tengelyek[-1, 0].set_xlabel('Mintapont indexe')
    kep_mentese(abra, mappa, nev)


def tanitas_mentese(mappa, modell, tortenet, adatok, beallitasok, masodperc):
    tanito = adatok['tanito_jelek']
    valid = adatok['validacios_jelek']
    normal = adatok['normal_jelek']
    rendellenes = adatok['rendellenes_jelek']
    tv = modell(tanito, training=False).numpy()
    vv = modell(valid, training=False).numpy()
    nv = modell(normal, training=False).numpy()
    rv = modell(rendellenes, training=False).numpy()
    tanito_mae = float(np.mean(np.abs(tanito - tv)))
    valid_mae = float(np.mean(np.abs(valid - vv)))
    beallitasok = dict(beallitasok, adathalmaz_sha256=hashlib.sha256((GYOKER / 'adatok/ekg_adatok.npz').read_bytes()).hexdigest(),
                       modell_beallitas=hashlib.sha256(json.dumps([modell.get_config(), modell.get_compile_config()], sort_keys=True).encode()).hexdigest())
    eredmeny = dict(beallitasok, tanito_mae=tanito_mae, validacios_mae=valid_mae,
                    normal_0_mae=float(np.mean(np.abs(normal[0] - nv[0]))),
                    tanitas_masodperc=round(masodperc, 3), parameterek=modell.count_params(), eszkoz='CPU')
    np.savez_compressed(mappa / 'rekonstrukciok.npz', normal_vissza=nv, rendellenes_vissza=rv,
                        tanito_hibak=np.mean(np.abs(tanito - tv), axis=1))
    np.savetxt(mappa / 'tanulasi_gorbek.csv', np.column_stack([np.arange(1, len(tortenet.history['loss']) + 1),
               tortenet.history['loss'], tortenet.history['val_loss']]), delimiter=',',
               header='epocha,tanitasi_mae_epochaatlag,validacios_mae_epocha_vegen', comments='')
    abra, t = plt.subplots()
    x = np.arange(1, len(tortenet.history['loss']) + 1)
    t.plot(x, tortenet.history['loss'], color=KEK, label='Tanítási MAE (epochátlag)')
    t.plot(x, tortenet.history['val_loss'], color=NARANCS, label='Normál validációs MAE (epocha végén)')
    t.set(xlabel='Epocha', ylabel='MAE', title='Rekonstrukció tanulása')
    t.legend(); t.grid(alpha=.2)
    kep_mentese(abra, mappa, 'tanulasi_gorbek.png')
    rekonstrukcio_rajz(mappa, [normal[0]], [nv[0]], ['Nem tanított normál gyakorlópélda · index 0'])
    print('\nFUTÁSI ÖSSZEFOGLALÓ')
    print(f"Epochák: {beallitasok['epochok']} | Szűk keresztmetszet: {beallitasok['szuk_keresztmetszet']}")
    print(f'Tanítható paraméterek: {modell.count_params()}')
    print(f'Végső tanítási MAE: {tanito_mae:.6f}')
    print(f'Végső normál validációs MAE: {valid_mae:.6f}')
    print(f"Normál gyakorlópélda (index 0) MAE: {eredmeny['normal_0_mae']:.6f}")
    print(f'Tanítás: {masodperc:.3f} s (import, mérés és rajzolás nélkül)')
    print('Az utolsó epocha súlyaival mérünk; minden Run új modellt tanít.')
    osszehasonlitas_mentese(mappa, normal[0], nv[0], eredmeny)
    befejezes(mappa, eredmeny)


def hibak_rajz(mappa, normal_hibak, rendellenes_hibak, kuszob=None):
    abra, t = plt.subplots()
    szel = np.linspace(0, max(normal_hibak.max(), rendellenes_hibak.max()) * 1.05, 25)
    t.hist(normal_hibak, bins=szel, alpha=.6, color=KEK, label='Normál gyakorlójelek')
    t.hist(rendellenes_hibak, bins=szel, alpha=.6, color=NARANCS, label='Rendellenes gyakorlójelek')
    if kuszob is not None:
        t.axvline(kuszob, color='black', linestyle='--', label=f'Küszöb: {kuszob:.3f}')
        t.set_xlim(0, max(szel[-1], kuszob * 1.05))
    t.set(xlabel='Jelenkénti rekonstrukciós MAE', ylabel='Jelek száma', title='Hibák eloszlása · rögzített referencia')
    t.legend(); t.grid(axis='y', alpha=.2)
    kep_mentese(abra, mappa, 'hibaeloszlas.png')


def dontes_rajz(mappa, tp, fn, fp, tn, kuszob):
    abra, t = plt.subplots(figsize=(7, 5))
    tomb = np.array([[tp, fn], [fp, tn]])
    t.imshow(tomb, cmap='Blues', vmin=0, vmax=128)
    for r in range(2):
        for c in range(2):
            t.text(c, r, f'{[["TP", "FN"], ["FP", "TN"]][r][c]} = {tomb[r,c]}', ha='center', va='center', fontsize=18, color='white' if tomb[r,c] > 70 else 'black')
    t.set(xticks=[0,1], yticks=[0,1], xticklabels=['Rendellenes', 'Normál'], yticklabels=['Rendellenes', 'Normál'],
          xlabel='Becsült osztály', ylabel='Valódi osztály', title=f'Döntések · küszöb: {kuszob:.3f}\nPozitív osztály = rendellenes')
    kep_mentese(abra, mappa, 'dontesek.png')



def osszehasonlitas_mentese(mappa, eredeti, mostani, eredmeny):
    """30 epochánál azonos beállítású, befejezett saját 10 epochás futást keres."""
    if eredmeny['epochok'] != 30:
        return
    egyezo = []
    kulcsok = ['szuk_keresztmetszet', 'kezdeti_sulyok', 'veletlen_mag', 'batch_meret',
               'adathalmaz_sha256', 'modell_beallitas']
    for jelolt in mappa.parent.glob('02_halo_*/eredmeny.json'):
        if jelolt.parent == mappa or not (jelolt.parent / 'rekonstrukciok.npz').exists():
            continue
        try:
            korabbi = json.loads(jelolt.read_text(encoding='utf-8'))
            if korabbi.get('epochok') == 10 and all(korabbi.get(k) == eredmeny[k] for k in kulcsok):
                egyezo.append((int(jelolt.parent.name.rsplit('_', 1)[1]), jelolt.parent))
        except (ValueError, KeyError, OSError):
            continue
    if not egyezo:
        print('Összehasonlító kép még nincs: ehhez előbb azonos beállítású saját 10 epochás futás kell.')
        eredmeny['osszehasonlitas'] = None
        return
    elozo = max(egyezo)[1]
    with np.load(elozo / 'rekonstrukciok.npz', allow_pickle=False) as tar:
        regi = tar['normal_vissza'][0].copy()
    abra, t = plt.subplots(3, 1, figsize=(10, 9), sharex=True)
    for tengely, vissza, nev in [(t[0], regi, '10 epocha · ' + elozo.name),
                               (t[1], mostani, '30 epocha · ' + mappa.name)]:
        tengely.plot(eredeti, color=KEK, label='Eredeti jel')
        tengely.plot(vissza, color=NARANCS, label='Rekonstrukció')
        tengely.set(title=f'{nev} · MAE = {np.mean(np.abs(eredeti-vissza)):.6f}', ylabel='Jelérték')
        tengely.legend(); tengely.grid(alpha=.2)
    also = min(eredeti.min(), regi.min(), mostani.min()) - .04
    felso = max(eredeti.max(), regi.max(), mostani.max()) + .04
    t[0].set_ylim(also, felso); t[1].set_ylim(also, felso)
    t[2].plot(np.abs(eredeti-regi), color=KEK, label='Abszolút eltérés · 10 epocha')
    t[2].plot(np.abs(eredeti-mostani), color=NARANCS, label='Abszolút eltérés · 30 epocha')
    t[2].set(title='Hol változott a rekonstrukció hibája?', xlabel='Mintapont indexe', ylabel='Abszolút eltérés')
    t[2].legend(); t[2].grid(alpha=.2)
    abra.suptitle('Ugyanaz az első normál gyakorlópélda (index 0) · két saját futás', fontsize=13)
    kep_mentese(abra, mappa, 'osszehasonlitas.png')
    eredmeny['osszehasonlitas'] = {'elozo_futas': elozo.name, 'mostani_futas': mappa.name,
                                  'elozo_mae': float(np.mean(np.abs(eredeti-regi)))}
    print(f'Összehasonlító kép: osszehasonlitas.png | {elozo.name} → {mappa.name}')


def axis_szemleltetes(mappa, elteresek):
    """Két rövid szemléltető jel; nem a valódi EKG-hibák."""
    abra, t = plt.subplots(figsize=(11, 4.5))
    t.axis('off')
    sorok = [[f'{i+1}. jel'] + [f'{x:.1f}' for x in sor] + [f'{np.mean(sor):.1f}']
             for i, sor in enumerate(elteresek)]
    tabla = t.table(cellText=sorok, colLabels=['Külön sorok', '1. pont', '2. pont', '3. pont', '4. pont', 'Saját MAE'],
                    cellLoc='center', bbox=[0, .43, 1, .38])
    tabla.auto_set_font_size(False); tabla.set_fontsize(12)
    for r in range(1, 3):
        for c in range(6):
            tabla[(r,c)].set_facecolor('#e4f0fb' if r == 1 else '#fff0df')
    t.text(.5, .93, 'Szemléltető abszolút eltérések: két jel, jelenként négy pont', ha='center', fontsize=14)
    t.text(.5, .30, 'axis=1: minden soron belül átlagolunk → [0.2, 0.4]', ha='center', fontsize=14, weight='bold')
    t.text(.5, .13, 'axis nélkül: az összes nyolc érték közös átlaga → 0.3', ha='center', fontsize=13)
    t.text(.5, .01, 'A valódi (128, 140) tömbnél ugyanígy: 128 külön jel → 128 külön MAE.', ha='center', fontsize=12)
    kep_mentese(abra, mappa, 'axis_1.png')


def precision_recall_rajz(mappa, tp, fn, fp):
    """Ugyanaz a TP, két külön kiinduló csoport: riasztások vs. valódi rendellenességek."""
    abra, tengelyek = plt.subplots(2, 1, figsize=(10, 6))
    veg = max(tp + fp, tp + fn, 1)
    for t, masik, cim, resz, formula in [
        (tengelyek[0], fp, 'PRECISION · A riasztásokból indulunk', 'Téves riasztás (FP)', 'TP / (TP + FP)'),
        (tengelyek[1], fn, 'RECALL · A valódi rendellenességekből indulunk', 'Elnézett rendellenesség (FN)', 'TP / (TP + FN)')]:
        osszes = tp + masik
        t.barh([0], [tp], color=KEK, label=f'Helyesen jelzett (TP): {tp}')
        t.barh([0], [masik], left=[tp], color=NARANCS, label=f'{resz}: {masik}')
        ertek = f'{tp / osszes:.1%}' if osszes else 'nem értelmezhető'
        t.set_title(f'{cim}\n{formula} = {tp}/{osszes} → {ertek}', loc='left', fontsize=12)
        t.set_xlim(0, veg * 1.05); t.set_yticks([])
        t.set_xlabel(f'A kiinduló csoport létszáma: {osszes} jel')
        t.legend(loc='upper center', bbox_to_anchor=(.5, -.38), ncol=2, fontsize=10)
        t.grid(axis='x', alpha=.2)
    abra.subplots_adjust(hspace=1.15)
    kep_mentese(abra, mappa, 'precision_recall.png')
