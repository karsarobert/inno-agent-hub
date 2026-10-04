"""Run this first. It does not install packages or download data."""
import sys
from helpers import np, plt, matplotlib, load_data, load_reference, new_run_folder, save_figure, finish_run
print(f'Python: {sys.version.split()[0]} | Interpreter: {sys.executable}')
print(f'NumPy: {np.__version__} | Matplotlib: {matplotlib.__version__}')
data = load_data()
reference = load_reference()
for key, shape in [('training_signals', (512, 140)), ('validation_signals', (128, 140)),
                   ('normal_signals', (128, 140)), ('anomalous_signals', (128, 140))]:
    if data[key].shape != shape or not np.isfinite(data[key]).all():
        raise SystemExit(f'Invalid data file: {key}. Ask your instructor for help.')
for key in ['normal_reconstructed', 'anomalous_reconstructed']:
    if reference[key].shape != (128, 140) or not np.isfinite(reference[key]).all():
        raise SystemExit(f'Invalid reference: {key}. Ask your instructor for help.')
folder = new_run_folder(__file__)
figure, axis = plt.subplots()
axis.plot(data['normal_signals'][0])
axis.set(title='Data loading and figure saving work', xlabel='Sample point index', ylabel='Scaled signal value')
save_figure(figure, folder, 'check.png')
try:
    from cpu_environment import tf, keras
except SystemExit as error:
    print(error)
    print('PARTIAL ENVIRONMENT - examples 1, 3 and 4 can run; ask your instructor for help with example 2.')
    finish_run(folder, {'status': 'partial', 'tensorflow': False})
    raise SystemExit(1)
print(f'TensorFlow: {tf.__version__} | Keras: {keras.__version__}')
print(f'Visible GPUs: {tf.config.get_visible_devices("GPU")}')
check = tf.reduce_sum(tf.constant([1., 2., 3.])).numpy()
if float(check) != 6.0:
    raise SystemExit('CPU computation check failed.')
print('\nENVIRONMENT OK - local data, CPU computation and figure saving verified.')
finish_run(folder, {'status': 'ok', 'tensorflow': tf.__version__, 'numpy': np.__version__, 'device': 'CPU'})
