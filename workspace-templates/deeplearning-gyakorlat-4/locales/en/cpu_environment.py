"""CPU-only TensorFlow. Import this before importing TensorFlow."""
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
except (ImportError, OSError) as error:
    raise SystemExit(
        f"TensorFlow could not be loaded: {error}\n"
        f"Interpreter: {sys.executable}\nAsk your instructor for help!"
    ) from error

try:
    tf.config.set_visible_devices([], "GPU")
    tf.config.threading.set_intra_op_parallelism_threads(1)
    tf.config.threading.set_inter_op_parallelism_threads(1)
except RuntimeError as error:
    raise SystemExit("Use Run to start the file in a fresh Python process! "
                     "If the error occurs again, ask your instructor for help.") from error


def new_training_run(seed=42):
    keras.backend.clear_session()
    keras.utils.set_random_seed(seed)
    tf.config.experimental.enable_op_determinism()


def make_datasets(train_x, train_y, val_x, val_y, batch_size, seed):
    """Prepared batching: one CPU worker thread and the same shuffling rule."""
    options = tf.data.Options()
    options.threading.private_threadpool_size = 1
    options.threading.max_intra_op_parallelism = 1
    training = tf.data.Dataset.from_tensor_slices((train_x, train_y))
    training = training.shuffle(len(train_x), seed=seed, reshuffle_each_iteration=True)
    training = training.batch(batch_size).with_options(options)
    validation = tf.data.Dataset.from_tensor_slices((val_x, val_y))
    validation = validation.batch(len(val_x)).with_options(options)
    return training, validation


class BriefProgress(keras.callbacks.Callback):
    """Only a few progress messages, without a long per-epoch log."""
    def __init__(self, epochs):
        super().__init__()
        self.epochs = epochs

    def on_epoch_end(self, epoch, logs=None):
        if epoch == 0 or (epoch+1) % 100 == 0 or epoch+1 == self.epochs:
            print(f"Epoch: {epoch+1}/{self.epochs}", flush=True)
