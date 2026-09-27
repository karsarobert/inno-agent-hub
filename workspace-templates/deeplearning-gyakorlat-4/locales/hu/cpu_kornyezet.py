"""Kizárólag CPU-s TensorFlow. Ezt importáljuk a TensorFlow előtt."""
import os
import sys

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
os.environ["KERAS_BACKEND"] = "tensorflow"
os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "2")
os.environ.setdefault("TF_NUM_INTRAOP_THREADS", "1")
os.environ.setdefault("TF_NUM_INTEROP_THREADS", "1")

try:
    import tensorflow as tf
    from tensorflow import keras
    from tensorflow.keras import layers, regularizers
except (ImportError, OSError) as hiba:
    raise SystemExit(
        f"A TensorFlow nem tölthető be: {hiba}\n"
        f"Értelmező: {sys.executable}\nKérd az oktató segítségét!"
    ) from hiba

try:
    tf.config.set_visible_devices([], "GPU")
    tf.config.threading.set_intra_op_parallelism_threads(1)
    tf.config.threading.set_inter_op_parallelism_threads(1)
except RuntimeError as hiba:
    raise SystemExit("Új Python-folyamatban futtasd a fájlt a Run gombbal! "
                     "Ha a hiba ismétlődik, kérd az oktató segítségét.") from hiba


def uj_tanitas(mag=42):
    keras.backend.clear_session()
    keras.utils.set_random_seed(mag)
    tf.config.experimental.enable_op_determinism()


def adatcsomagok(tanito_x, tanito_y, validacios_x, validacios_y, batch_meret, mag):
    """Kész adagszervezés: egyetlen CPU-s háttérszál, azonos keverési szabály."""
    opciok = tf.data.Options()
    opciok.threading.private_threadpool_size = 1
    opciok.threading.max_intra_op_parallelism = 1
    tanito = tf.data.Dataset.from_tensor_slices((tanito_x, tanito_y))
    tanito = tanito.shuffle(len(tanito_x), seed=mag, reshuffle_each_iteration=True)
    tanito = tanito.batch(batch_meret).with_options(opciok)
    validacios = tf.data.Dataset.from_tensor_slices((validacios_x, validacios_y))
    validacios = validacios.batch(len(validacios_x)).with_options(opciok)
    return tanito, validacios


class RovidJelzes(keras.callbacks.Callback):
    """Legfeljebb néhány állapotjelzés, hosszú epochonkénti napló nélkül."""
    def __init__(self, epochok):
        super().__init__()
        self.epochok = epochok

    def on_epoch_end(self, epoch, logs=None):
        if epoch == 0 or (epoch+1) % 100 == 0 or epoch+1 == self.epochok:
            print(f"Epocha: {epoch+1}/{self.epochok}", flush=True)
