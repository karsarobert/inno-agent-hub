"""Kész CPU-beállítás és adagszervezés; nem hallgatói feladat."""
import os
import sys
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
os.environ['KERAS_BACKEND'] = 'tensorflow'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_NUM_INTRAOP_THREADS'] = '1'
os.environ['TF_NUM_INTEROP_THREADS'] = '1'
try:
    import tensorflow as tf
    from tensorflow import keras
    from tensorflow.keras import layers
except (ImportError, OSError) as hiba:
    raise SystemExit(f'A TensorFlow nem tölthető be: {hiba}\nÉrtelmező: {sys.executable}\nKérd az oktató segítségét!') from hiba
try:
    tf.config.set_visible_devices([], 'GPU')
    tf.config.threading.set_intra_op_parallelism_threads(1)
    tf.config.threading.set_inter_op_parallelism_threads(1)
except RuntimeError as hiba:
    raise SystemExit('Új Python-folyamatban, a Run gombbal futtass! Ha ismétlődik a hiba, kérd az oktató segítségét.') from hiba


def uj_tanitas(mag=42):
    keras.backend.clear_session()
    keras.utils.set_random_seed(mag)
    tf.config.experimental.enable_op_determinism()


def adatcsomag(bemenet, cel, keveres=False):
    """(x, y) párok 32-es batch-ekben, korlátozott CPU-s szálhasználattal."""
    csomag = tf.data.Dataset.from_tensor_slices((bemenet, cel))
    if keveres:
        csomag = csomag.shuffle(len(bemenet), seed=42, reshuffle_each_iteration=True)
    opciok = tf.data.Options()
    opciok.threading.private_threadpool_size = 1
    opciok.threading.max_intra_op_parallelism = 1
    return csomag.batch(32).with_options(opciok)


class RovidJelzes(keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs=None):
        if epoch == 0 or (epoch + 1) % 10 == 0 or epoch + 1 == self.params['epochs']:
            print(f"Epocha: {epoch + 1}/{self.params['epochs']}", flush=True)
