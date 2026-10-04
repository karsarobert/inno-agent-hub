"""Ready-made local data loading, plotting and saving. No network operations."""
from pathlib import Path
from datetime import datetime
import json
import sys
import hashlib
try:
    import numpy as np
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
except (ImportError, OSError) as error:
    raise SystemExit(f'Missing or unloadable package: {error}\nInterpreter: {sys.executable}\nAsk your instructor for help.') from error
ROOT = Path(__file__).resolve().parent
BLUE, ORANGE = '#1764aa', '#bc4b22'
plt.rcParams.update({'figure.figsize': (10, 5), 'font.size': 11})


def load_data():
    path = ROOT / 'data' / 'ecg_data.npz'
    if not path.exists():
        raise SystemExit('Missing data/ecg_data.npz. Extract the complete package; ask your instructor for help.')
    with np.load(path, allow_pickle=False) as archive:
        return {key: archive[key].copy() for key in archive.files}


def load_reference():
    path = ROOT / 'data' / 'reference_reconstructions.npz'
    if not path.exists():
        raise SystemExit('Missing reference_reconstructions.npz. This is a supplied file, not an output you must generate in the first exercise.')
    metadata = json.loads((ROOT / 'data' / 'reference_metadata.json').read_text(encoding='utf-8'))
    checksum = hashlib.sha256((ROOT / 'data' / 'ecg_data.npz').read_bytes()).hexdigest()
    if checksum != metadata['dataset_sha256']:
        raise SystemExit('The data and reference do not match. Restore the original data folder.')
    with np.load(path, allow_pickle=False) as archive:
        data = {k: archive[k].copy() for k in archive.files}
    print('DATA SOURCE: supplied reference saved from real CPU training; 30 epochs, bottleneck=8.')
    print('This program does not train a new model or read your most recent G05_02 run.')
    return data


def check_index(index, count):
    if not isinstance(index, int) or isinstance(index, bool) or not 0 <= index < count:
        raise SystemExit(f'sample_index must be an integer between 0 and {count - 1}.')


def new_run_folder(program):
    """Short names with a separate counter per program. Existing runs are never overwritten."""
    short_name = {'environment_check': '00_check', 'G05_01_ecg_data': '01_data',
             'G05_02_autoencoder': '02_model', 'G05_03_reconstruction_error': '03_error',
             'G05_04_threshold': '04_threshold'}[Path(program).stem]
    base = ROOT / 'view'
    base.mkdir(exist_ok=True)
    numbers = [int(p.name[len(short_name)+1:]) for p in base.glob(short_name + '_*')
              if p.name[len(short_name)+1:].isdigit()]
    number = max(numbers, default=0) + 1
    while True:
        folder = base / f'{short_name}_{number:02d}'
        try:
            folder.mkdir(exist_ok=False)
            return folder
        except FileExistsError:
            number += 1


def save_figure(figure, folder, name):
    figure.tight_layout()
    figure.savefig(folder / name, dpi=140, bbox_inches='tight')
    plt.close(figure)


def finish_run(folder, result):
    result.update({'run': folder.name, 'saved_at': datetime.now().astimezone().isoformat()})
    (folder / 'result.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print('\nRUN COMPLETE. Figures and results are saved in:')
    print(folder)
    print(f'Short folder name: {folder.name}')
    print('Images: ' + ', '.join(p.name for p in sorted(folder.glob('*.png'))))
    print(f'Refresh the View folder / file list, then open the {folder.name} folder.')


def plot_signal_pair(folder, normal, anomalous, index):
    figure, axes = plt.subplots(2, 1, figsize=(10, 6), sharex=True, sharey=True)
    for t, signal, name, color in zip(axes, [normal, anomalous], ['Normal', 'Anomalous'], [BLUE, ORANGE]):
        t.plot(signal, color=color)
        t.set(title=f'{name} signal · example {index + 1} (index: {index}) · 140 values', ylabel='Scaled signal value')
        t.grid(alpha=.2)
    axes[-1].set_xlabel('Sample point index (not seconds)')
    save_figure(figure, folder, 'ecg_signals.png')


def plot_reconstructions(folder, signals, reconstructions, titles, name='reconstruction.png'):
    figure, axes = plt.subplots(len(signals), 1, figsize=(10, 3.8 * len(signals)), squeeze=False, sharex=True, sharey=True)
    for t, signal, reconstructed, title in zip(axes[:, 0], signals, reconstructions, titles):
        error = float(np.mean(np.abs(signal - reconstructed)))
        t.plot(signal, color=BLUE, label='Original signal')
        t.plot(reconstructed, color=ORANGE, label='Reconstruction')
        t.fill_between(np.arange(140), signal, reconstructed, color=ORANGE, alpha=.15, label='Difference')
        t.set(title=f'{title} · MAE: {error:.6f}', ylabel='Scaled signal value')
        t.grid(alpha=.2)
        t.legend(loc='best')
    axes[-1, 0].set_xlabel('Sample point index')
    save_figure(figure, folder, name)


def save_training_results(folder, model, history, data, settings, seconds):
    training = data['training_signals']
    validation = data['validation_signals']
    normal = data['normal_signals']
    anomalous = data['anomalous_signals']
    tv = model(training, training=False).numpy()
    vv = model(validation, training=False).numpy()
    nv = model(normal, training=False).numpy()
    rv = model(anomalous, training=False).numpy()
    training_mae = float(np.mean(np.abs(training - tv)))
    valid_mae = float(np.mean(np.abs(validation - vv)))
    settings = dict(settings, dataset_sha256=hashlib.sha256((ROOT / 'data/ecg_data.npz').read_bytes()).hexdigest(),
                       model_configuration=hashlib.sha256(json.dumps([model.get_config(), model.get_compile_config()], sort_keys=True).encode()).hexdigest())
    result = dict(settings, training_mae=training_mae, validation_mae=valid_mae,
                    normal_0_mae=float(np.mean(np.abs(normal[0] - nv[0]))),
                    training_seconds=round(seconds, 3), parameters=model.count_params(), device='CPU')
    np.savez_compressed(folder / 'reconstructions.npz', normal_reconstructed=nv, anomalous_reconstructed=rv,
                        training_errors=np.mean(np.abs(training - tv), axis=1))
    np.savetxt(folder / 'learning_curves.csv', np.column_stack([np.arange(1, len(history.history['loss']) + 1),
               history.history['loss'], history.history['val_loss']]), delimiter=',',
               header='epoch,training_mae_epoch_average,validation_mae_epoch_end', comments='')
    figure, t = plt.subplots()
    x = np.arange(1, len(history.history['loss']) + 1)
    t.plot(x, history.history['loss'], color=BLUE, label='Training MAE (epoch average)')
    t.plot(x, history.history['val_loss'], color=ORANGE, label='Normal validation MAE (epoch end)')
    t.set(xlabel='Epoch', ylabel='MAE', title='Learning to reconstruct')
    t.legend(); t.grid(alpha=.2)
    save_figure(figure, folder, 'learning_curves.png')
    plot_reconstructions(folder, [normal[0]], [nv[0]], ['Normal practice example, not used for training · index 0'])
    print('\nRUN SUMMARY')
    print(f"Epochs: {settings['epochs']} | Bottleneck: {settings['bottleneck_size']}")
    print(f'Trainable parameters: {model.count_params()}')
    print(f'Final training MAE: {training_mae:.6f}')
    print(f'Final normal validation MAE: {valid_mae:.6f}')
    print(f"Normal practice example (index 0) MAE: {result['normal_0_mae']:.6f}")
    print(f'Training: {seconds:.3f} s (excluding imports, evaluation and plotting)')
    print('Evaluation uses the final epoch weights; every Run trains a new model.')
    save_comparison(folder, normal[0], nv[0], result)
    finish_run(folder, result)


def plot_errors(folder, normal_errors, anomalous_errors, threshold=None):
    figure, t = plt.subplots()
    edges = np.linspace(0, max(normal_errors.max(), anomalous_errors.max()) * 1.05, 25)
    t.hist(normal_errors, bins=edges, alpha=.6, color=BLUE, label='Normal practice signals')
    t.hist(anomalous_errors, bins=edges, alpha=.6, color=ORANGE, label='Anomalous practice signals')
    if threshold is not None:
        t.axvline(threshold, color='black', linestyle='--', label=f'Threshold: {threshold:.3f}')
        t.set_xlim(0, max(edges[-1], threshold * 1.05))
    t.set(xlabel='Per-signal reconstruction MAE', ylabel='Number of signals', title='Error distribution · fixed reference')
    t.legend(); t.grid(axis='y', alpha=.2)
    save_figure(figure, folder, 'error_distribution.png')


def plot_decisions(folder, tp, fn, fp, tn, threshold):
    figure, t = plt.subplots(figsize=(7, 5))
    matrix = np.array([[tp, fn], [fp, tn]])
    t.imshow(matrix, cmap='Blues', vmin=0, vmax=128)
    for r in range(2):
        for c in range(2):
            t.text(c, r, f'{[["TP", "FN"], ["FP", "TN"]][r][c]} = {matrix[r,c]}', ha='center', va='center', fontsize=18, color='white' if matrix[r,c] > 70 else 'black')
    t.set(xticks=[0,1], yticks=[0,1], xticklabels=['Anomalous', 'Normal'], yticklabels=['Anomalous', 'Normal'],
          xlabel='Predicted class', ylabel='Actual class', title=f'Decisions · threshold: {threshold:.3f}\nPositive class = anomalous')
    save_figure(figure, folder, 'decisions.png')



def save_comparison(folder, original, current, result):
    """At 30 epochs, find a completed 10-epoch run of your own with matching settings."""
    if result['epochs'] != 30:
        return
    matches = []
    keys = ['bottleneck_size', 'initial_weights', 'random_seed', 'batch_size',
               'dataset_sha256', 'model_configuration']
    for candidate in folder.parent.glob('02_model_*/result.json'):
        if candidate.parent == folder or not (candidate.parent / 'reconstructions.npz').exists():
            continue
        try:
            previous = json.loads(candidate.read_text(encoding='utf-8'))
            if previous.get('epochs') == 10 and all(previous.get(k) == result[k] for k in keys):
                matches.append((int(candidate.parent.name.rsplit('_', 1)[1]), candidate.parent))
        except (ValueError, KeyError, OSError):
            continue
    if not matches:
        print('No comparison image yet: first complete a 10-epoch run of your own with matching settings.')
        result['comparison'] = None
        return
    earlier = max(matches)[1]
    with np.load(earlier / 'reconstructions.npz', allow_pickle=False) as archive:
        old = archive['normal_reconstructed'][0].copy()
    figure, t = plt.subplots(3, 1, figsize=(10, 9), sharex=True)
    for axis, reconstructed, name in [(t[0], old, '10 epochs · ' + earlier.name),
                               (t[1], current, '30 epochs · ' + folder.name)]:
        axis.plot(original, color=BLUE, label='Original signal')
        axis.plot(reconstructed, color=ORANGE, label='Reconstruction')
        axis.set(title=f'{name} · MAE = {np.mean(np.abs(original-reconstructed)):.6f}', ylabel='Signal value')
        axis.legend(); axis.grid(alpha=.2)
    lower = min(original.min(), old.min(), current.min()) - .04
    upper = max(original.max(), old.max(), current.max()) + .04
    t[0].set_ylim(lower, upper); t[1].set_ylim(lower, upper)
    t[2].plot(np.abs(original-old), color=BLUE, label='Absolute difference · 10 epochs')
    t[2].plot(np.abs(original-current), color=ORANGE, label='Absolute difference · 30 epochs')
    t[2].set(title='Where did the reconstruction error change?', xlabel='Sample point index', ylabel='Absolute difference')
    t[2].legend(); t[2].grid(alpha=.2)
    figure.suptitle('Same first normal practice example (index 0) · two runs of your own', fontsize=13)
    save_figure(figure, folder, 'comparison.png')
    result['comparison'] = {'previous_run': earlier.name, 'current_run': folder.name,
                                  'previous_mae': float(np.mean(np.abs(original-old)))}
    print(f'Comparison image: comparison.png | {earlier.name} → {folder.name}')


def illustrate_axis(folder, differences):
    """Two short illustrative signals, not the real ECG errors."""
    figure, t = plt.subplots(figsize=(11, 4.5))
    t.axis('off')
    rows = [[f'Signal {i+1}'] + [f'{x:.1f}' for x in row] + [f'{np.mean(row):.1f}']
             for i, row in enumerate(differences)]
    table = t.table(cellText=rows, colLabels=['Separate rows', 'Point 1', 'Point 2', 'Point 3', 'Point 4', 'Individual MAE'],
                    cellLoc='center', bbox=[0, .43, 1, .38])
    table.auto_set_font_size(False); table.set_fontsize(12)
    for r in range(1, 3):
        for c in range(6):
            table[(r,c)].set_facecolor('#e4f0fb' if r == 1 else '#fff0df')
    t.text(.5, .93, 'Illustrative absolute differences: two signals, four points per signal', ha='center', fontsize=14)
    t.text(.5, .30, 'axis=1: average within each row → [0.2, 0.4]', ha='center', fontsize=14, weight='bold')
    t.text(.5, .13, 'Without axis: one mean across all eight values → 0.3', ha='center', fontsize=13)
    t.text(.5, .01, 'For the real (128, 140) array: 128 separate signals → 128 separate MAEs.', ha='center', fontsize=12)
    save_figure(figure, folder, 'axis_1.png')


def plot_precision_recall(folder, tp, fn, fp):
    """Same TP, two different starting groups: alerts and actual anomalies."""
    figure, axes = plt.subplots(2, 1, figsize=(10, 6))
    end = max(tp + fp, tp + fn, 1)
    for t, other, title, part, formula in [
        (axes[0], fp, 'PRECISION · Start with all alerts', 'False alarms (FP)', 'TP / (TP + FP)'),
        (axes[1], fn, 'RECALL · Start with all actual anomalies', 'Missed anomalies (FN)', 'TP / (TP + FN)')]:
        total = tp + other
        t.barh([0], [tp], color=BLUE, label=f'Correctly detected (TP): {tp}')
        t.barh([0], [other], left=[tp], color=ORANGE, label=f'{part}: {other}')
        value = f'{tp / total:.1%}' if total else 'undefined'
        t.set_title(f'{title}\n{formula} = {tp}/{total} → {value}', loc='left', fontsize=12)
        t.set_xlim(0, end * 1.05); t.set_yticks([])
        t.set_xlabel(f'Size of the starting group: {total} signals')
        t.legend(loc='upper center', bbox_to_anchor=(.5, -.38), ncol=2, fontsize=10)
        t.grid(axis='x', alpha=.2)
    figure.subplots_adjust(hspace=1.15)
    save_figure(figure, folder, 'precision_recall.png')
