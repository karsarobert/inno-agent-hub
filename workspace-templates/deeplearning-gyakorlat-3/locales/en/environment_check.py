"""Environment check that can be started with the Run button. It installs nothing."""
import importlib
import os
import sys
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
os.environ.setdefault('TF_CPP_MIN_LOG_LEVEL', '2')
os.environ.setdefault('TF_NUM_INTRAOP_THREADS', '2')
os.environ.setdefault('TF_NUM_INTEROP_THREADS', '2')
print('Python:', sys.version.split()[0])
print('Interpreter:', sys.executable)
broken = []
for name in ['numpy', 'matplotlib', 'sklearn', 'tensorflow']:
    try:
        module = importlib.import_module(name)
        print(name, getattr(module, '__version__', 'loaded'))
    except (ImportError, OSError) as error:
        broken.append(name)
        print(name, ':', error)
if broken:
    print('Missing or not loadable Python package:', ', '.join(broken))
    raise SystemExit('Ask the instructor for help! Do not install a Python package on your own.')
import tensorflow as tf
print('TensorFlow test computation:', float(tf.reduce_sum([1.0, 2.0, 3.0])))
print('The environment check was successful. You can continue the lab with Inno.')
