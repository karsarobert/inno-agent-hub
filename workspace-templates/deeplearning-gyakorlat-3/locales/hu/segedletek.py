"""Előkészített adatkezelés, ábrák és mentés. Órán nem kell átírni."""
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
os.environ.setdefault('TF_CPP_MIN_LOG_LEVEL', '2')
os.environ.setdefault('TF_NUM_INTRAOP_THREADS', '2')
os.environ.setdefault('TF_NUM_INTEROP_THREADS', '2')
from pathlib import Path
from datetime import datetime
import importlib
import json
import shutil
import csv

GYOKER = Path(__file__).resolve().parent


def csomagok_ellenorzese(nevek):
    for nev in nevek:
        try:
            importlib.import_module(nev)
        except (ImportError, OSError) as hiba:
            print(f'A(z) {nev} Python-csomag hiányzik vagy nem tölthető be.')
            print('Kérd az oktató segítségét! Ne kezdj önálló telepítésbe.')
            print(f'Az oktatónak mutasd meg ezt a hibát: {hiba}')
            raise SystemExit(1)


csomagok_ellenorzese(['numpy', 'matplotlib', 'sklearn'])
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

SZINEK = ['#2764ce', '#de7133', '#37865b']
SZINTERKEP = ListedColormap(SZINEK)


def uj_mappa(forras):
    nev = Path(forras).stem + '_' + datetime.now().strftime('%Y%m%d_%H%M%S_%f')
    mappa = GYOKER / 'eredmenyek' / nev
    mappa.mkdir(parents=True, exist_ok=False)
    shutil.copyfile(forras, mappa / 'futtatott_forras.py')
    shutil.copyfile(__file__, mappa / 'segedletek_masolata.py')
    return mappa


def json_mentes(ut, adat):
    ut.write_text(json.dumps(adat, ensure_ascii=False, indent=2), encoding='utf-8')


def nezet_frissites(mappa, tanitas=True):
    print('\nEredménymappa:', mappa)
    print('FRISSÍTSD a Nézet mappát / fájllistát az Innoagentben!')
    pelda = 'loss.png' if tanitas else 'dontesi_tartomanyok.png'
    print(f'Ezután nyisd meg ennek az ÚJ futásnak a képeit, például a {pelda} fájlt.')
    print('Ha korábbi kép maradt nyitva, zárd be, és nyisd meg az új mappa képét.')


def regresszios_adatok():
    # Szintetikus oktatási adatok, nem valódi hallgatói teljesítménymérés.
    veletlen = np.random.default_rng(42)
    orak = np.linspace(0, 10, 100).astype('float32')
    pontok = (20 + 6 * orak + veletlen.normal(0, 4, 100)).astype('float32')
    indexek = np.arange(100)
    tanito, validacios = train_test_split(indexek, test_size=0.2, random_state=42)
    return orak[tanito], orak[validacios], pontok[tanito], pontok[validacios]


def spiral_adatok():
    veletlen = np.random.default_rng(42)
    jellemzok = np.zeros((600, 2), dtype='float32')
    cimkek = np.zeros(600, dtype='int64')
    for osztaly in range(3):
        hely = slice(200 * osztaly, 200 * (osztaly + 1))
        sugar = np.linspace(0, 1, 200)
        szog = np.linspace(osztaly * 4, (osztaly + 1) * 4, 200)
        szog += veletlen.normal(0, 0.2, 200)
        jellemzok[hely] = np.column_stack([sugar * np.sin(szog), sugar * np.cos(szog)])
        cimkek[hely] = osztaly
    # Minden felosztás ugyanazokkal az indexekkel történik minden futásban.
    indexek = np.arange(600)
    fejlesztes, teszt = train_test_split(indexek, test_size=0.2,
                                        random_state=42, stratify=cimkek)
    tanito, validacio = train_test_split(fejlesztes, test_size=0.25,
                                        random_state=42, stratify=cimkek[fejlesztes])
    return (jellemzok[tanito], jellemzok[validacio], jellemzok[teszt],
            cimkek[tanito], cimkek[validacio], cimkek[teszt])


def gorbek_mentese(mappa, tortenet):
    adatok = tortenet.history if hasattr(tortenet, 'history') else tortenet
    epochok = np.arange(1, len(adatok['loss']) + 1)
    with (mappa / 'tanulasi_gorbek.csv').open('w', newline='', encoding='utf-8') as fajl:
        iro = csv.writer(fajl)
        iro.writerow(['epoch'] + list(adatok))
        iro.writerows(zip(epochok, *adatok.values()))
    for kulcs, felirat in [('loss', 'Veszteség'), ('accuracy', 'Pontosság')]:
        if kulcs not in adatok:
            continue
        abra, tengely = plt.subplots(figsize=(8, 4.8))
        tengely.plot(epochok, adatok[kulcs], label='Tanítás')
        if 'val_' + kulcs in adatok:
            tengely.plot(epochok, adatok['val_' + kulcs], label='Validáció', linestyle='--')
        tengely.set(xlabel='Epoch / teljes tanítóhalmaz bejárása', ylabel=felirat,
                    title=felirat + ' a tanítás során')
        if kulcs == 'accuracy':
            tengely.set_ylim(0, 1.02)
        tengely.legend()
        tengely.grid(alpha=0.2)
        abra.tight_layout()
        abra.savefig(mappa / (kulcs + '.png'), dpi=135)
        plt.close(abra)


def regresszio_abra(mappa, tanito_x, tanito_y, validacios_x, validacios_y, suly, bias):
    abra, tengely = plt.subplots(figsize=(7, 4.8))
    tengely.scatter(tanito_x, tanito_y, label='Tanítás', s=20)
    tengely.scatter(validacios_x, validacios_y, label='Validáció', marker='^')
    racs = np.linspace(0, 10, 100)
    tengely.plot(racs, suly * racs + bias, c='black', label='Tanult egyenes')
    tengely.set(xlabel='Tanulási idő (óra)', ylabel='Szintetikus pontszám',
                title='Egy lineáris neuron: becslés = súly × idő + bias')
    tengely.legend()
    abra.tight_layout()
    abra.savefig(mappa / 'regresszio.png', dpi=135)
    plt.close(abra)


def osztalyozasi_abrak(mappa, modell, jellemzok, cimkek, megnevezes):
    # A predict kimenete (minták, 3), az argmax kimenete (minták,).
    valoszinusegek = modell.predict(jellemzok, verbose=0)
    becsult = valoszinusegek.argmax(axis=1)
    tengely = np.linspace(-1.1, 1.1, 150)
    racs_x, racs_y = np.meshgrid(tengely, tengely)
    racs = np.column_stack([racs_x.ravel(), racs_y.ravel()]).astype('float32')
    racs_osztaly = modell.predict(racs, verbose=0).argmax(axis=1).reshape(racs_x.shape)
    abra, tengelyek = plt.subplots(1, 2, figsize=(10, 4.5))
    for ax, szin, cim in zip(tengelyek, [cimkek, becsult], ['Valódi címkék', 'Becsült címkék']):
        ax.contourf(racs_x, racs_y, racs_osztaly, levels=[-0.5, 0.5, 1.5, 2.5],
                    cmap=SZINTERKEP, alpha=0.18)
        ax.scatter(jellemzok[:, 0], jellemzok[:, 1], c=szin, cmap=SZINTERKEP,
                   vmin=0, vmax=2, s=22, edgecolors='white', linewidths=0.3)
        hibas = becsult != cimkek
        ax.scatter(jellemzok[hibas, 0], jellemzok[hibas, 1], s=55,
                   facecolors='none', edgecolors='black', label='Hibás becslés')
        ax.set(title=cim, xlabel='Első koordináta', ylabel='Második koordináta', aspect='equal')
        ax.legend(fontsize=8)
    abra.suptitle(megnevezes + ' – háttér: a modell döntési tartományai')
    abra.tight_layout()
    abra.savefig(mappa / 'dontesi_tartomanyok.png', dpi=135)
    plt.close(abra)
    matrix = confusion_matrix(cimkek, becsult, labels=[0, 1, 2])
    abra, ax = plt.subplots(figsize=(5, 4.5))
    kep = ax.imshow(matrix, cmap='Blues', vmin=0)
    for sor in range(3):
        for oszlop in range(3):
            ax.text(oszlop, sor, str(matrix[sor, oszlop]), ha='center', va='center',
                    color='white' if matrix[sor, oszlop] > matrix.max()/2 else 'black')
    ax.set(xticks=[0, 1, 2], yticks=[0, 1, 2], xlabel='Becsült osztály',
           ylabel='Valódi osztály', title=megnevezes + ' – konfúziós mátrix')
    abra.colorbar(kep, ax=ax)
    abra.tight_layout()
    abra.savefig(mappa / 'konfuzios_matrix.png', dpi=135)
    plt.close(abra)
    np.savetxt(mappa / 'becslesek.csv', np.column_stack([jellemzok, cimkek, becsult, valoszinusegek]),
               delimiter=',', header='x0,x1,valodi,becsult,p0,p1,p2', comments='')
    return valoszinusegek, becsult


def spiral_mentes(mappa, modell, tortenet, beallitasok, validacios_x,
                   validacios_cimke, teszt_x, teszt_cimke):
    gorbek_mentese(mappa, tortenet)
    valoszinusegek, becsult = osztalyozasi_abrak(
        mappa, modell, validacios_x, validacios_cimke, 'Validáció')
    modell.save(mappa / 'modell.keras')
    # A tesztet itt csak archiváljuk, nincs rajta predict vagy evaluate.
    np.savez_compressed(mappa / 'teszt_adatok.npz', jellemzok=teszt_x, cimkek=teszt_cimke)
    beallitasok['parameterek_szama'] = modell.count_params()
    beallitasok['modell_retegei'] = [
        {'neuronok': reteg.units, 'aktivacio': reteg.activation.__name__}
        for reteg in modell.layers if hasattr(reteg, 'units')]
    import tensorflow as tf
    beallitasok['tensorflow_verzio'] = tf.__version__
    json_mentes(mappa / 'beallitasok.json', beallitasok)
    print('\nFUTÁSI ÖSSZEFOGLALÓ')
    print('Hálózat:', beallitasok['modell_retegei'])
    print('Paraméterek:', modell.count_params())
    print('Beállítások:', {k: beallitasok[k] for k in ['tanulasi_rata', 'epochok', 'batch_meret']})
    print('Validáció:', beallitasok['validacio'])
    print('Első öt becsült / valódi címke:', becsult[:5], '/', validacios_cimke[:5])
    print('Első softmax-vektor:', np.round(valoszinusegek[0], 4))
    print('Teszthalmaz: elkülönítve, még nem értékeltük.')
    nezet_frissites(mappa)
