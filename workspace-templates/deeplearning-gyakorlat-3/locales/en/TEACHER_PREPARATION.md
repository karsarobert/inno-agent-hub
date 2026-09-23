# Teacher preparation

For learners the only environment task is launching the environment check with
Run. If a package is missing, **they ask the instructor for help**.
The tutor does not give an install command and does not attempt an installation
on their own.

## Environment

The package is built for Linux x86-64, Python 3.12 and CPU. The verified
main package versions are in requirements.txt. This is not a complete lock of
every transitive dependency. The programs use the tensorflow.keras API.
No GPU, Colab, Jupyter, pandas or network data download is needed.

The instructor should provide the packages and the right Python interpreter for
the Inno Agent Run in advance, following the institutional procedure. Installation
is not part of the lesson. The teaching material does not change the application
settings.

## Pre-lesson check

1. agent.md and the L03 programs are directly in the workspace root.
2. The local Inno Agent preset uses the new agent.md; a new conversation starts.
3. environment_check.py launched with Run runs successfully.
4. The 16-neuron variant of L03_03, then the 50-50 model with both rate 0.01 and
   0.001 also run. The latter comparison is a mandatory learner experiment.
5. The image files are created under results/; after refreshing the View
   they can be opened in the institutional interface. The exact button for this
   is interface-dependent.
6. L03_04 can load the selected saved model and produces test figures.
7. Learners receive their own experiment copy: do not hand out the teacher's
   trial results and filled-in choice fields as a finished learner solution.

The 150 epochs appear in several separate runs; measure it on the local machine
before the lesson. If justified, the instructor may uniformly reduce the epoch
budget of the four spiral runs; record this in both the scenario and the notes.
Do not take the 15 minutes of the closing test out of the waiting time.
Run one model at a time.

In the package verbose=0 makes training quiet, so the tutor says in advance
that there is a wait until the run summary. The parameters, metrics and output
folder appear together at the end of the run.

## Pedagogical goal

The learner works in the model part: interprets the input and output,
changes the neuron count, inserts a new Dense layer, configures the training,
compares the validation, then justifies their choice. The plotting
and the data preparation are ready infrastructure. Beside the
concrete APIs, the difference between the data roles and the operations matters.

The closing test is the last mandatory task part. After a question Inno waits for
the answer, explains, scores, then moves on. The key is not technically locked away,
so this is formative assessment. The instructor should not treat it as a
supervised exam.


## Short acceptance test for the new tutor version

The new agent.md and lesson plan belong to version 1.2. Use a new workspace and
a new conversation to avoid mixing with the old instructions.
The main checkpoints:

- In L03_01 the tutor actually demonstrates both gradient formulas.
- Before the first spiral run they state the choice rule and demonstrate
  the label shapes, the arguments of fit, and the difference between predict/argmax.
- They lead through four spiral runs, in the mandatory R4 only the rate changes.
- They do not name the winning run in advance and do not dictate a ready-made
  choice reason.
- They ask for a concrete, separate training/validation observation on the figures.
- After the test metrics they also wait for the interpretation of the figures;
  only after that does the quiz start.
- In the closing they name the knowledge proven by the answers and separate the
  earlier help from the usual explanation after the answer.

In the earlier test copy, tool names and broken table formatting were also visible.
agent.md forbids narrating internal tool names in the learner text and asks
for regular simple formatting. The automatic tool panel and the export
display are an application-side question; the teaching material cannot
switch them off. Check live that the table and the code blocks are readable
in the interface too.
