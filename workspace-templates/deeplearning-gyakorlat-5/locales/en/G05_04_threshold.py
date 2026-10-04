"""Threshold decisions: turn reconstruction errors into alerts or acceptance.
Input: original signals and fixed reference reconstructions. No new training.
Output: counts, error_distribution.png, decisions.png, precision_recall.png.
Change threshold (0.04 to 0.025 to 0.06). Positive class = anomalous.
"""
from helpers import (np, load_data, load_reference, new_run_folder,
                     plot_errors, plot_decisions, plot_precision_recall, finish_run)

# 1. SETTING: raise an alert when the error reaches or exceeds the threshold.
# We change only the decision boundary, not the reconstructions.
threshold = 0.04
if not isinstance(threshold, (int, float)) or not np.isfinite(threshold) or threshold < 0:
    raise SystemExit('threshold must be a finite, nonnegative number.')

# 2. DATA AND ERRORS: recompute the same MAEs from the fixed reconstructions.
data = load_data()
reference = load_reference()
normal_differences = np.abs(data['normal_signals'] - reference['normal_reconstructed'])
anomalous_differences = np.abs(data['anomalous_signals'] - reference['anomalous_reconstructed'])
normal_errors = np.mean(normal_differences, axis=1)
anomalous_errors = np.mean(anomalous_differences, axis=1)

# 3. DECISIONS: True means the rule flags this signal as anomalous.
# An alert on a normal signal is false; an alert on an anomalous signal is correct.
normal_alerts = normal_errors >= threshold
anomalous_alerts = anomalous_errors >= threshold

# 4. COUNT THE FOUR CASES: np.sum counts the True values.
# ~ inverts the Boolean array: True now marks signals without an alert.
false_alarms = int(np.sum(normal_alerts))           # FP: normal signal flagged.
correct_normal = int(np.sum(~normal_alerts))       # TN: normal signal accepted.
correct_anomalous = int(np.sum(anomalous_alerts))   # TP: anomaly detected.
missed_anomalous = int(np.sum(~anomalous_alerts))   # FN: anomaly missed.

# 5. PRECISION STARTS WITH THE ALERTS: how many were correct?
# All alerts = correct alerts (TP) + false alarms (FP).
alerts = correct_anomalous + false_alarms
precision = correct_anomalous / alerts if alerts > 0 else None

# 6. RECALL STARTS WITH THE ACTUAL ANOMALIES: how many did we find?
# All actual anomalies = detected (TP) + missed (FN).
actual_anomalies = correct_anomalous + missed_anomalous
recall = correct_anomalous / actual_anomalies

# 7. SUMMARY: first the counts, then two ratios based on different groups.
print('\nRUN SUMMARY')
print(f'Threshold: {threshold:.3f} | Positive class: anomalous')
print(f'Correctly detected anomalies (TP): {correct_anomalous}')
print(f'Missed anomalies (FN): {missed_anomalous}')
print(f'False alarms (FP): {false_alarms}')
print(f'Correctly accepted normal signals (TN): {correct_normal}')
print(f'PRECISION: of {alerts} alerts, {correct_anomalous} are correct and {false_alarms} are false.')
if precision is None:
    print('Precision: undefined because there are no alerts.')
else:
    print(f'Precision = {correct_anomalous}/{alerts} = {precision:.1%}')
print(f'RECALL: of {actual_anomalies} actual anomalies, {correct_anomalous} were detected and {missed_anomalous} were missed.')
print(f'Recall = {correct_anomalous}/{actual_anomalies} = {recall:.1%}')

# 8. SAVE FIGURES: the two bars show the starting group for each ratio.
folder = new_run_folder(__file__)
plot_errors(folder, normal_errors, anomalous_errors, threshold)
plot_decisions(folder, correct_anomalous, missed_anomalous, false_alarms, correct_normal, threshold)
plot_precision_recall(folder, correct_anomalous, missed_anomalous, false_alarms)
finish_run(folder, {'threshold': threshold, 'TP': correct_anomalous, 'FN': missed_anomalous,
                   'FP': false_alarms, 'TN': correct_normal, 'precision': precision, 'recall': recall,
                   'source': 'supplied_30_epoch_reference', 'positive': 'anomalous'})
