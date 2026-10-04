"""Ready-made CPU setup and batching; not a student programming task."""
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
except (ImportError, OSError) as error:
    raise SystemExit(f'Cannot load TensorFlow: {error}\nInterpreter: {sys.executable}\nAsk your instructor for help.') from error
try:
    tf.config.set_visible_devices([], 'GPU')
    tf.config.threading.set_intra_op_parallelism_threads(1)
    tf.config.threading.set_inter_op_parallelism_threads(1)
except RuntimeError as error:
    raise SystemExit('Use Run to start a fresh Python process. If the error persists, ask your instructor for help.') from error


def start_training(seed=42):
    keras.backend.clear_session()
    keras.utils.set_random_seed(seed)
    tf.config.experimental.enable_op_determinism()


def make_batches(inputs, targets, shuffle=False):
    """Input-target pairs in batches of 32, with limited CPU thread usage."""
    dataset = tf.data.Dataset.from_tensor_slices((inputs, targets))
    if shuffle:
        dataset = dataset.shuffle(len(inputs), seed=42, reshuffle_each_iteration=True)
    options = tf.data.Options()
    options.threading.private_threadpool_size = 1
    options.threading.max_intra_op_parallelism = 1
    return dataset.batch(32).with_options(options)


class BriefProgress(keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs=None):
        if epoch == 0 or (epoch + 1) % 10 == 0 or epoch + 1 == self.params['epochs']:
            print(f"Epoch: {epoch + 1}/{self.params['epochs']}", flush=True)
