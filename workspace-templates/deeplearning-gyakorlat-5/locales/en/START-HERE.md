# Start the autoencoder practice

In the extracted workspace, write to Inno:

> Let's start Deep Learning practice 5!

Inno introduces the goal and asks you to run `environment_check.py`. Before each
new program, it explains the example and important code lines. You edit, save
and click Run; no `cd` command is needed.

Run each example unchanged first. Change only the value currently requested.
Python uses a decimal point: write `0.025`, not `0,025`.

## Images and results

Wait for **RUN COMPLETE**. The program prints the new short numbered folder.
Refresh the View folder / file list, then open the image from that new folder.
Older images remain available for comparison. `result.json` contains settings
and numbers; you do not need to edit it.

## If you get stuck

- For missing packages, ask your instructor and show the last error lines.
- For missing data, check that you extracted the complete package.
- Training may be silent for a few seconds during imports. Do not start several
  copies of the same program.
- If old settings appear, check which file you saved and ran.
- `sample_index` must be an integer from 0 to 127. Index 0 is the first example;
  index 3 is the fourth.
- Programs 3 and 4 use a fixed reference. Changing the epoch count in program 2
  does not change their results. This is intentional.

You do not need medical knowledge to compare waveforms. This is a machine learning
exercise. It ends with ten short questions and a summary. There is no homework.

## The additional images

- `axis_1.png`: two signals → two individual means; an illustration, not real ECG errors.
- `precision_recall.png`: alerts and actual anomalies as separate starting groups.
- `comparison.png`: your own 10- and 30-epoch reconstructions in one figure.
  Run the baseline ten epochs before thirty. The image requires a matching
  earlier run of your own. Interpret numbers and curves together.
