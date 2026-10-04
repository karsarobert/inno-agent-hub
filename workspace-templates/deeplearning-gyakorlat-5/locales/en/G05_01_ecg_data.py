"""Observe ECG signals: this program does not use a neural network yet.
Input: locally stored normal and anomalous signal segments.
Output: two curves in ecg_signals.png.
Change sample_index to select another example, without changing signal values.
"""
from helpers import load_data, check_index, new_run_folder, plot_signal_pair, finish_run

# 1. SETTING: which example will we examine?
# 0 = first, 1 = second, 2 = third, 3 = fourth example.
# Run with 0 first, then change to 3. Valid indices range from 0 to 127.
sample_index = 0

# 2. LOAD DATA: normal and anomalous signals are in separate groups.
# Each group contains 128 rows. Each row is one signal with 140 sample points.
data = load_data()
normal_signals = data['normal_signals']
anomalous_signals = data['anomalous_signals']
check_index(sample_index, len(normal_signals))

# 3. SELECT ONE SIGNAL FROM EACH GROUP: square brackets select a row.
# The same index in two groups does not identify two readings from one person.
normal_signal = normal_signals[sample_index]
anomalous_signal = anomalous_signals[sample_index]

# 4. FIGURE AND SUMMARY: the helper saves the image without opening a window.
folder = new_run_folder(__file__)
plot_signal_pair(folder, normal_signal, anomalous_signal, sample_index)
print('\nRUN SUMMARY')
print(f'Selected example: {sample_index + 1} | Sample index: {sample_index}')
print(f'One signal contains 140 sample points; array shape: {normal_signal.shape}')
print('Normal / anomalous examples: 128 / 128. The figure shows scaled signal values.')
finish_run(folder, {'sample_index': sample_index, 'signal_length': len(normal_signal)})
