"""Prepared data handling, figures and saving. You do not need to rewrite it in class."""
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
os.environ.setdefault('TF_CPP_MIN_LOG_LEVEL', '2')
os.environ.setdefault('TF_NUM_INTRAOP_THREADS', '2')
os.environ.setdefault('TF_NUM_INTEROP_THREADS', '2')
from pathlib import Path
from datetime import datetime
import importlib
import json
import shutil
import csv

ROOT = Path(__file__).resolve().parent


def check_packages(names):
    for name in names:
        try:
            importlib.import_module(name)
        except (ImportError, OSError) as error:
            print(f'The {name} Python package is missing or cannot be loaded.')
            print('Ask the instructor for help! Do not start an installation on your own.')
            print(f'Show the instructor this error: {error}')
            raise SystemExit(1)


check_packages(['numpy', 'matplotlib', 'sklearn'])
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

COLORS = ['#2764ce', '#de7133', '#37865b']
CMAP = ListedColormap(COLORS)


def _label_from_layers(pairs, learning_rate):
    """The run label from the layer pairs: R1..R4 for the four mandatory runs, otherwise X.

    pairs: [(neurons, activation), ...] the Dense layers of the network in order.
    """
    if pairs == [(3, 'softmax')]:
        structure, index = 'baseline', 'R1'
    elif pairs == [(16, 'relu'), (3, 'softmax')]:
        structure = '16n'
        index = 'R2' if abs(learning_rate - 0.01) < 1e-12 else 'X'
    elif pairs == [(50, 'relu'), (50, 'relu'), (3, 'softmax')]:
        structure = '50x2'
        if abs(learning_rate - 0.01) < 1e-12:
            index = 'R3'
        elif abs(learning_rate - 0.001) < 1e-12:
            index = 'R4'
        else:
            index = 'X'
    else:
        structure = '-'.join(f'{u}{a[:1]}' for u, a in pairs) or 'unknown'
        index = 'X'
    return f'{index}_{structure}_lr{learning_rate:g}'


def run_label(model, learning_rate):
    """The short, readable label of the run, from the ACTUAL model and the learning rate.

    This goes into the name of the results folder, so the learner never has to copy a
    long folder name later: it is enough to type the R1..R4 label.
    """
    pairs = [(layer.units, layer.activation.__name__)
             for layer in model.layers if hasattr(layer, 'units')]
    return _label_from_layers(pairs, learning_rate)


def new_run_dir(source, label=None):
    """A new results folder. The label goes to the front of the name, for example: R3_50x2_lr0.01_0921-174027.

    Without a label the old, long name is produced (backward compatible).
    """
    if label:
        name = f'{label}_{datetime.now().strftime("%m%d-%H%M%S")}'
        run_dir = ROOT / 'results' / name
        attempt = 2
        while run_dir.exists():
            run_dir = ROOT / 'results' / f'{name}_r{attempt}'
            attempt += 1
    else:
        name = Path(source).stem + '_' + datetime.now().strftime('%Y%m%d_%H%M%S_%f')
        run_dir = ROOT / 'results' / name
    run_dir.mkdir(parents=True, exist_ok=False)
    shutil.copyfile(source, run_dir / 'source_snapshot.py')
    shutil.copyfile(__file__, run_dir / 'helpers_copy.py')
    return run_dir


def save_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')


def _label_from_dirname(name):
    """The short label from the front of the folder name (e.g. R3_50x2_lr0.01_0921-174027 -> R3_50x2_lr0.01)."""
    import re
    hit = re.match(r'^(R[1-4]|X_[^_]+|G01_gradient)(_.*?)?_\d{4}-\d{6}(_r\d+)?$', name)
    if hit:
        return (hit.group(1) + (hit.group(2) or '')).strip('_')
    return None


def run_records():
    """Every trained (testable) run in the results folder, in chronological order."""
    results_root = ROOT / 'results'
    if not results_root.is_dir():
        return []
    records = []
    for run_dir in sorted(p for p in results_root.glob('*') if p.is_dir()):
        if not (run_dir / 'model.keras').is_file():
            continue                      # the L03_01 gradient run has no saved model
        data = {}
        if (run_dir / 'settings.json').is_file():
            try:
                data = json.loads((run_dir / 'settings.json').read_text(encoding='utf-8'))
            except json.JSONDecodeError:
                data = {}
        validation = data.get('validation') or {}
        layers = data.get('model_layers')
        label = (data.get('run_label') or _label_from_dirname(run_dir.name)
                 or (_label_from_layers([(r['neurons'], r['activation']) for r in layers],
                                        data.get('learning_rate') or 0) if layers else run_dir.name[:6]))
        records.append({
            'run_dir': run_dir.name,
            'label': label,
            'layers': layers,
            'parameters': data.get('parameter_count'),
            'learning_rate': data.get('learning_rate'),
            'val_loss': validation.get('loss', data.get('val_loss')),
            'tested': (run_dir / 'final_test' / 'result.json').is_file(),
        })
    return records


def run_table(runs, selected=None, show_winner=True):
    """The comparison table of the runs: label, structure, parameter, rate, validation loss.

    With show_winner=False a neutral table is produced: the learner makes the decision,
    so the winner is not marked in that case.
    """
    if not runs:
        return 'No trained run found in the results folder yet.'
    winner = rule_winner(runs) if show_winner else None
    rows = [f"{'label':16} {'structure':28} {'params':>7} {'rate':>7} {'val.loss':>11}  tested"]
    for f in runs:
        layers = f['layers'] or []
        structure = '-'.join(f"{r['neurons']}{r['activation'][:4]}" for r in layers) or '?'
        loss = '?' if f['val_loss'] is None else f"{f['val_loss']:.5f}"
        rate = '?' if f['learning_rate'] is None else f"{f['learning_rate']:g}"
        parameters = '?' if f['parameters'] is None else str(f['parameters'])
        marker = ''
        if f['run_dir'] == selected:
            marker += '  <== your choice'
        if winner and f['run_dir'] == winner['run_dir']:
            marker += '  <== lowest validation loss'
        rows.append(f"{f['label']:16} {structure:28} {parameters:>7} {rate:>7} {loss:>11}  "
                    f"{('yes' if f['tested'] else 'no'):8}{marker}")
    return '\n'.join(rows)


def rule_winner(runs):
    """The winner by the rule: the lowest validation loss; on a tie, fewer parameters."""
    candidates = [f for f in runs if f['val_loss'] is not None]
    if not candidates:
        return None
    return min(candidates, key=lambda f: (f['val_loss'], f['parameters'] if f['parameters'] else 10**9))


def resolve_run(choice, runs):
    """Resolve the entered label (R1..R4), number (1..4) or folder name to one run.

    Returns: (folder name or None, explanatory message or '').
    """
    text = str(choice).strip().strip('"\'')
    if not text:
        return None, ''
    if text.isdigit() and 1 <= int(text) <= 4:
        text = f'R{text}'
    matches = [f for f in runs if f['run_dir'] == text or f['label'].lower() == text.lower()]
    if not matches:
        matches = [f for f in runs if f['run_dir'].lower().startswith(text.lower() + '_')]
    if not matches:
        return None, ''
    if len(matches) > 1:
        hit = matches[-1]
        return hit['run_dir'], (f"Several runs belong to this label ({len(matches)} of them); "
                                f"I took the most recent one: {hit['run_dir']}.")
    return matches[0]['run_dir'], ''


def refresh_view(run_dir, training=True):
    label = _label_from_dirname(run_dir.name) or run_dir.name
    print('\nRun folder:', run_dir)
    print('Run label:', label, '- refer to this when you compare the four runs.')
    print('Refresh the View folder / file list in Inno Agent!')
    example = 'loss.png' if training else 'decision_regions.png'
    print(f'Then open the figures of this NEW run, for example the {example} file.')
    print('If an older figure is still open, close it and open the figure of the new folder.')


def regression_data():
    # Synthetic teaching data, not a real measurement of learner performance.
    rng = np.random.default_rng(42)
    hours = np.linspace(0, 10, 100).astype('float32')
    scores = (20 + 6 * hours + rng.normal(0, 4, 100)).astype('float32')
    indices = np.arange(100)
    train, val = train_test_split(indices, test_size=0.2, random_state=42)
    return hours[train], hours[val], scores[train], scores[val]


def spiral_data():
    rng = np.random.default_rng(42)
    features = np.zeros((600, 2), dtype='float32')
    labels = np.zeros(600, dtype='int64')
    for class_index in range(3):
        where = slice(200 * class_index, 200 * (class_index + 1))
        radius = np.linspace(0, 1, 200)
        angle = np.linspace(class_index * 4, (class_index + 1) * 4, 200)
        angle += rng.normal(0, 0.2, 200)
        features[where] = np.column_stack([radius * np.sin(angle), radius * np.cos(angle)])
        labels[where] = class_index
    # Every split uses the same indices in every run.
    indices = np.arange(600)
    dev, test = train_test_split(indices, test_size=0.2,
                                random_state=42, stratify=labels)
    train, val = train_test_split(dev, test_size=0.25,
                                  random_state=42, stratify=labels[dev])
    return (features[train], features[val], features[test],
            labels[train], labels[val], labels[test])


def save_curves(run_dir, history):
    data = history.history if hasattr(history, 'history') else history
    epochs = np.arange(1, len(data['loss']) + 1)
    with (run_dir / 'training_curves.csv').open('w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['epoch'] + list(data))
        writer.writerows(zip(epochs, *data.values()))
    for key, caption in [('loss', 'Loss'), ('accuracy', 'Accuracy')]:
        if key not in data:
            continue
        fig, ax = plt.subplots(figsize=(8, 4.8))
        ax.plot(epochs, data[key], label='Training')
        if 'val_' + key in data:
            ax.plot(epochs, data['val_' + key], label='Validation', linestyle='--')
        ax.set(xlabel='Epoch / one full pass over the training set', ylabel=caption,
               title=caption + ' during training')
        if key == 'accuracy':
            ax.set_ylim(0, 1.02)
        ax.legend()
        ax.grid(alpha=0.2)
        fig.tight_layout()
        fig.savefig(run_dir / (key + '.png'), dpi=135)
        plt.close(fig)


def regression_figure(run_dir, train_x, train_y, val_x, val_y, weight, bias):
    fig, ax = plt.subplots(figsize=(7, 4.8))
    ax.scatter(train_x, train_y, label='Training', s=20)
    ax.scatter(val_x, val_y, label='Validation', marker='^')
    line_x = np.linspace(0, 10, 100)
    ax.plot(line_x, weight * line_x + bias, c='black', label='Learned line')
    ax.set(xlabel='Study time (hours)', ylabel='Synthetic score',
           title='One linear neuron: prediction = weight * time + bias')
    ax.legend()
    fig.tight_layout()
    fig.savefig(run_dir / 'regression.png', dpi=135)
    plt.close(fig)


def classification_figures(run_dir, model, features, labels, name):
    # The output of predict is (samples, 3), the output of argmax is (samples,).
    probabilities = model.predict(features, verbose=0)
    predicted = probabilities.argmax(axis=1)
    axis_range = np.linspace(-1.1, 1.1, 150)
    grid_x, grid_y = np.meshgrid(axis_range, axis_range)
    grid = np.column_stack([grid_x.ravel(), grid_y.ravel()]).astype('float32')
    grid_class = model.predict(grid, verbose=0).argmax(axis=1).reshape(grid_x.shape)
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5))
    for ax, panel_data, panel_title in zip(axes, [labels, predicted], ['True labels', 'Predicted labels']):
        ax.contourf(grid_x, grid_y, grid_class, levels=[-0.5, 0.5, 1.5, 2.5],
                    cmap=CMAP, alpha=0.18)
        ax.scatter(features[:, 0], features[:, 1], c=panel_data, cmap=CMAP,
                   vmin=0, vmax=2, s=22, edgecolors='white', linewidths=0.3)
        wrong = predicted != labels
        ax.scatter(features[wrong, 0], features[wrong, 1], s=55,
                   facecolors='none', edgecolors='black', label='Wrong prediction')
        ax.set(title=panel_title, xlabel='First coordinate', ylabel='Second coordinate', aspect='equal')
        ax.legend(fontsize=8)
    fig.suptitle(name + ' - background: the decision regions of the model')
    fig.tight_layout()
    fig.savefig(run_dir / 'decision_regions.png', dpi=135)
    plt.close(fig)
    matrix = confusion_matrix(labels, predicted, labels=[0, 1, 2])
    fig, ax = plt.subplots(figsize=(5, 4.5))
    image = ax.imshow(matrix, cmap='Blues', vmin=0)
    for row in range(3):
        for column in range(3):
            ax.text(column, row, str(matrix[row, column]), ha='center', va='center',
                    color='white' if matrix[row, column] > matrix.max()/2 else 'black')
    ax.set(xticks=[0, 1, 2], yticks=[0, 1, 2], xlabel='Predicted class',
           ylabel='True class', title=name + ' - confusion matrix')
    fig.colorbar(image, ax=ax)
    fig.tight_layout()
    fig.savefig(run_dir / 'confusion_matrix.png', dpi=135)
    plt.close(fig)
    np.savetxt(run_dir / 'predictions.csv', np.column_stack([features, labels, predicted, probabilities]),
               delimiter=',', header='x0,x1,true,predicted,p0,p1,p2', comments='')
    return probabilities, predicted


def save_spiral_run(run_dir, model, history, settings, val_x,
                    val_labels, test_x, test_labels):
    save_curves(run_dir, history)
    probabilities, predicted = classification_figures(
        run_dir, model, val_x, val_labels, 'Validation')
    model.save(run_dir / 'model.keras')
    # The test set is only archived here, there is no predict or evaluate on it.
    np.savez_compressed(run_dir / 'test_data.npz', features=test_x, labels=test_labels)
    settings['parameter_count'] = model.count_params()
    settings['model_layers'] = [
        {'neurons': layer.units, 'activation': layer.activation.__name__}
        for layer in model.layers if hasattr(layer, 'units')]
    settings['run_label'] = _label_from_layers(
        [(r['neurons'], r['activation']) for r in settings['model_layers']],
        settings['learning_rate'])
    import tensorflow as tf
    settings['tensorflow_version'] = tf.__version__
    save_json(run_dir / 'settings.json', settings)
    print('\nRUN SUMMARY')
    print('Run label (refer to this when you choose):', settings['run_label'])
    print('Network:', settings['model_layers'])
    print('Parameters:', model.count_params())
    print('Settings:', {k: settings[k] for k in ['learning_rate', 'epochs', 'batch_size']})
    print('Validation:', settings['validation'])
    print('First five predicted / true labels:', predicted[:5], '/', val_labels[:5])
    print('First softmax vector:', np.round(probabilities[0], 4))
    print('Test set: kept aside, not evaluated yet.')
    refresh_view(run_dir)
