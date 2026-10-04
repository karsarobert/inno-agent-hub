"""Per-signal reconstruction error: compare the original with its reconstruction.
Input: original signals and supplied reconstructions saved from an earlier training run.
Output: axis_1.png, reconstructions.png, error_distribution.png and MAE values.
Change sample_index (0 to 3). No training occurs; TensorFlow is not required.
"""
from helpers import (np, load_data, load_reference, check_index, new_run_folder,
                     plot_reconstructions, plot_errors, illustrate_axis, finish_run)

# 1. SETTING: 0 selects the first and 3 the fourth example from each group.
# Changing the index does not change the network or the full error distribution.
sample_index = 0

# 2. LOAD: always use the supplied 30-epoch reference, not your most recent run.
data = load_data()
reference = load_reference()
normal_signals = data['normal_signals']
anomalous_signals = data['anomalous_signals']
normal_reconstructed = reference['normal_reconstructed']
anomalous_reconstructed = reference['anomalous_reconstructed']
check_index(sample_index, len(normal_signals))

# 3. SMALL WORKED EXAMPLE: illustrative differences, not measured ECG errors.
# Two rows = two separate signals; four numbers per row = four absolute differences.
illustrative_differences = np.array([
    [0.1, 0.1, 0.3, 0.3],  # Mean for the first signal: 0.2.
    [0.4, 0.4, 0.4, 0.4],  # Mean for the second signal: 0.4.
])
individual_means = np.mean(illustrative_differences, axis=1)  # Two results: [0.2, 0.4].
overall_mean = np.mean(illustrative_differences)             # One result: 0.3.

# 4. MAE FOR THE REAL SIGNALS: three clearly separated steps.
# Subtract: compare each original sample point with its reconstructed value.
differences = normal_signals - normal_reconstructed
# Absolute value: positive and negative differences must not cancel each other.
absolute_differences = np.abs(differences)
# axis=1: average the 140 points within each row -> 128 signals, 128 errors.
normal_errors = np.mean(absolute_differences, axis=1)

# Repeat the same three steps for anomalous signals.
anomalous_differences = anomalous_signals - anomalous_reconstructed
anomalous_absolute = np.abs(anomalous_differences)
anomalous_errors = np.mean(anomalous_absolute, axis=1)

# 5. PLOTS: a selected pair and the full error distribution in separate images.
folder = new_run_folder(__file__)
illustrate_axis(folder, illustrative_differences)
plot_reconstructions(folder, [normal_signals[sample_index], anomalous_signals[sample_index]],
                     [normal_reconstructed[sample_index], anomalous_reconstructed[sample_index]],
                     [f'Normal reference · example {sample_index+1} (index {sample_index})',
                      f'Anomalous reference · example {sample_index+1} (index {sample_index})'],
                     'reconstructions.png')
plot_errors(folder, normal_errors, anomalous_errors)

# 6. SUMMARY: keep the illustrative example separate from the real ECG results.
print('\nILLUSTRATIVE EXAMPLE (not an ECG measurement)')
print(f'Per-signal means: {individual_means} | Overall mean: {overall_mean:.1f}')
print('\nRUN SUMMARY')
print(f'Selected example: {sample_index + 1} | Sample index: {sample_index}')
print(f'Normal signal MAE: {normal_errors[sample_index]:.6f}')
print(f'Anomalous signal MAE: {anomalous_errors[sample_index]:.6f}')
print(f'Mean MAE across all normal signals: {np.mean(normal_errors):.6f}')
print(f'Mean MAE across all anomalous signals: {np.mean(anomalous_errors):.6f}')
print('The index changes only the selected pair; the histogram of the full group stays the same.')
np.savetxt(folder / 'errors.csv', np.column_stack([normal_errors, anomalous_errors]),
           delimiter=',', header='normal_mae,anomalous_mae', comments='')
finish_run(folder, {'sample_index': sample_index, 'source': 'supplied_30_epoch_reference',
                   'normal_mae': float(normal_errors[sample_index]),
                   'anomalous_mae': float(anomalous_errors[sample_index])})
