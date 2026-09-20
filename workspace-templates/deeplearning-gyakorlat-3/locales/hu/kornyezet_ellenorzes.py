"""Run gombbal indítható környezetellenőrzés. Nem telepít semmit."""
import importlib
import os
import sys
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
os.environ.setdefault('TF_CPP_MIN_LOG_LEVEL', '2')
os.environ.setdefault('TF_NUM_INTRAOP_THREADS', '2')
os.environ.setdefault('TF_NUM_INTEROP_THREADS', '2')
print('Python:', sys.version.split()[0])
print('Értelmező:', sys.executable)
hibas = []
for nev in ['numpy', 'matplotlib', 'sklearn', 'tensorflow']:
    try:
        modul = importlib.import_module(nev)
        print(nev, getattr(modul, '__version__', 'betöltve'))
    except (ImportError, OSError) as hiba:
        hibas.append(nev)
        print(nev, ':', hiba)
if hibas:
    print('Hiányzó vagy nem betölthető Python-csomag:', ', '.join(hibas))
    raise SystemExit('Kérd az oktató segítségét! Ne telepíts önállóan Python-csomagot.')
import tensorflow as tf
print('TensorFlow próbaszámítás:', float(tf.reduce_sum([1.0, 2.0, 3.0])))
print('A környezetellenőrzés sikeres. Folytathatod a gyakorlatot Inno segítségével.')
