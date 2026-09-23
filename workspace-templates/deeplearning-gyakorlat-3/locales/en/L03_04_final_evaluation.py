"""Final test of the already trained network chosen on the basis of validation.

There is no retraining. You must give the reason for your choice before the test.
The program asks for the SHORT LABEL of the run (R1, R2, R3, R4) - you do not have
to copy a long folder name. Without a choice only the comparison table of the runs
appears and no test starts; and if you do not choose the run with the lowest
validation loss, the program stops until you deliberately override this (OVERRIDE).
"""
from helpers import (ROOT, check_packages, np, save_json,
                     classification_figures, refresh_view, run_records,
                     run_table, resolve_run, rule_winner)
import json
import shutil

# THE STUDENT FILLS IN THESE THREE LINES after comparing the four spiral runs.
# 1) The short label of the chosen run: "R1", "R2", "R3" or "R4".
# 2) The reason in your own words: which number decided, what you compared.
# 3) OVERRIDE gets a YES only if the program tells you that you did not choose
#    the run with the lowest validation loss, and you can also justify this.
CHOICE = ""
CHOICE_REASON = ""
OVERRIDE = ""

runs = run_records()
if not runs:
    raise SystemExit('There is no finished trained run in the results folder yet. '
                     'Run the L03_02 and L03_03 programs first!')

# 1) Without a choice only the table appears - the test does not start.
#    The table is deliberately neutral: it does not mark the winner, you have to
#    establish that yourself by comparing the data.
if not CHOICE.strip():
    print('NO CHOICE YET - here is the comparison of the runs, without any test.')
    # Neutral table: the winner is deliberately NOT marked here.
    print(run_table(runs, show_winner=False))
    raise SystemExit('Compare the validation loss values, and write the LABEL of the '
                     'chosen run (R1, R2, R3 or R4) into the CHOICE line, the reason '
                     'into the CHOICE_REASON line, then run it again.')

name, message = resolve_run(CHOICE, runs)
if message:
    print(message)
if name is None:
    print(run_table(runs))
    raise SystemExit('I cannot find this label. Write the short label of the run '
                     '(R1..R4), or its folder name exactly.')

selected = next(r for r in runs if r['run_dir'] == name)
winner = rule_winner(runs)

# 2) Comparing the choice with the rule - still before the test.
print('CHOICE CHECK')
print(run_table(runs, selected=name))
print('Selected run:', selected['run_dir'])
print('Choice reason:', CHOICE_REASON)
if selected['val_loss'] is None:
    raise SystemExit('The chosen run has no recorded validation loss; '
                     'it cannot be used for the comparison by the rule.')
if winner and selected['run_dir'] == winner['run_dir']:
    print('By the rule, this is the winning run: the lowest validation loss '
          f"({selected['val_loss']:.5f}) of the {len(runs)} runs.")
elif OVERRIDE.strip().upper() == 'YES':
    print('NOTE: deliberate choice against the rule. The lowest validation loss '
          f"belongs to run {winner['label']} ({winner['val_loss']:.5f}), the chosen run "
          f"has {selected['val_loss']:.5f}. The reason should be consistent with this.")
else:
    print(f"This is NOT the lowest validation loss run: run {winner['label']} has "
          f"{winner['val_loss']:.5f}, the chosen run has {selected['val_loss']:.5f}.")
    raise SystemExit('Think again about which model learned better on the validation '
                     'set! If you deliberately want to test the other one, write YES '
                     'into the OVERRIDE line, and justify it in the program too.')

if not CHOICE_REASON.strip():
    raise SystemExit('The reason for the choice is missing: write it into the '
                     'CHOICE_REASON line, in your own words.')

run_dir = (ROOT / 'results' / selected['run_dir']).resolve()
if run_dir.parent != (ROOT / 'results').resolve():
    raise SystemExit('Give only the name of a direct run subfolder of the results '
                     'folder!')
if not all((run_dir / filename).is_file() for filename in
           ['model.keras', 'test_data.npz', 'settings.json']):
    raise SystemExit('The chosen run is incomplete or cannot be found. Check the '
                     'folder name!')
output_dir = run_dir / 'final_test'
if (output_dir / 'result.json').is_file():
    raise SystemExit('You have already tested this model. Open the existing result; '
                     'do not tune further on the basis of the test result!')
check_packages(['tensorflow'])
from tensorflow import keras
output_dir.mkdir(exist_ok=True)
save_json(output_dir / 'choice.json', {
    'selected_run': selected['run_dir'],
    'run_label': selected['label'],
    'val_loss': selected['val_loss'],
    'parameter_count': selected['parameters'],
    'rule_winner': winner['run_dir'] if winner else None,
    'rule_winner_loss': winner['val_loss'] if winner else None,
    'override': OVERRIDE.strip().upper() == 'YES',
    'reason': CHOICE_REASON})
shutil.copyfile(__file__, output_dir / 'evaluator_source.py')

# We load the saved weights: no fit(), no retraining.
model = keras.models.load_model(run_dir / 'model.keras')
with np.load(run_dir / 'test_data.npz') as data:
    test_x = data['features']
    test_labels = data['labels']
test_target = keras.utils.to_categorical(test_labels, num_classes=3)
result = model.evaluate(test_x, test_target, verbose=0, return_dict=True)
classification_figures(output_dir, model, test_x, test_labels, 'Final test')
save_json(output_dir / 'result.json', result)
print('FINAL TEST - the previously saved model, 120 held-out samples.')
print('Selected run:', selected['run_dir'], '| label:', selected['label'])
print('Choice reason:', CHOICE_REASON)
print('Validation loss at the time of the choice:', round(selected['val_loss'], 5),
      '| parameters:', selected['parameters'])
print('Test loss:', round(result['loss'], 4))
print('Test accuracy:', round(result['accuracy'], 4))
refresh_view(output_dir, training=False)
print('There is no new loss.png here: no training happened. Open the figures of '
      'the test.')
print('First interpret the figures with Inno: which true class did the model predict '
      'as which?')
print('If there is no mistake, explain the diagonal and which points the 100% '
      'refers to.')
print('After discussing the figures comes the 10-question code comprehension test.')
