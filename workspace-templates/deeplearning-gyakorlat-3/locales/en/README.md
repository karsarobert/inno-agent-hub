# Deep Learning 2026 - lab 3

**Corrected 1.2 edition.** English-language Inno Agent package, for **2 x 45 minutes**. Topic: the gradient
method, the structure of a neuron and a neural network, training settings, spiral classification,
validation and the final test. At the end, 10 multiple-choice code-comprehension questions.

## Getting started

1. Unzip the ZIP into a new working folder. The `agent.md` and the
   `L03_...py` files should be directly in the opened working folder.
2. In Inno Agent, select this workspace and its tutoring instruction the same way
   you used before. Start a new conversation.
3. Type: **"Let's start the 3rd Deep Learning lab!"**
4. Inno introduces itself, states the goal of the lab, and guides you through the tasks.

The ZIP contains the course material and the workspace instructions; it uses the
existing Inno Agent application. It does not install or configure an application on its own.

**Run the programs after saving with the Run button.** Run handles the path,
you do not need to issue a `cd` command because of it. You edit the Python files;
Inno explains the code and helps you interpret the result.

**If a Python package is missing, ask the instructor for help!** Do not start
installing anything yourself. The package works locally, we do not use Colab or Jupyter.
In the prepared environment, running the programs needs no internet or GPU.

## Tasks

| File | Task |
|---|---|
| `environment_check.py` | Check the local environment; it installs nothing. |
| `L03_01_gradient.py` | Follow how one weight and one bias learn on synthetic data. |
| `L03_02_spiral_baseline.py` | Examine the baseline model with three classes and no hidden layer. |
| `L03_03_spiral_network.py` | Train a 16-neuron network, build two 50-neuron layers, then in a separate run reduce the rate. |
| `L03_04_final_evaluation.py` | Evaluate the saved model chosen from validation on the test. |
| `CODE_COMPREHENSION_TEST.md` | Answer Inno's 10 multiple-choice questions, asked one by one. |

Among the settings we also work through the meaning of the learning rate, the
epoch and the batch. The **learning-rate experiment is compulsory**: on the 50-50
network you change the rate from 0.01 to 0.001 while everything else stays identical.
The code for the data handling and for all evaluation figures is ready in the `helpers.py` file.
The lab work concentrates on building, configuring and understanding the model.

You compare four spiral runs: the baseline model, 16 hidden neurons,
50-50 hidden neurons with rate 0.01, then the same with rate 0.001. You learn
the choice rule in advance: lower validation loss; on an exact tie,
fewer parameters. **You choose the model and you justify your decision.**
We also interpret the final test figures before the ten questions start.

## Opening the new figures

**After every run, refresh the View folder / file list**, so the new
files appear! Look for the run folder given in the output under
`results`; its name starts with the run's short label (for example
`R3_50x2_lr0.01_...`), so it is identifiable in alphabetical order too. From there open,
for example, the new `loss.png` image.
If an earlier image is still open, close it, and open the right one from the new folder.

| Output | Content |
|---|---|
| `loss.png` | Training and validation loss |
| `accuracy.png` | Training and validation accuracy for the spiral models |
| `regression.png` | Synthetic data points and the learned line in the first task |
| `decision_regions.png` | True and predicted spiral labels, with the model's decision background |
| `confusion_matrix.png` | Correct and wrong classifications per class |
| `settings.json` | The run's settings and validation result |
| `model.keras` | The spiral model's layers and learned parameters |
| `training_curves.csv` | The numeric data of the training curves |

The final test figures are in the chosen run's `final_test` subfolder.
There is no new loss curve there: the program measures the existing network, it does not
retrain it. The old runs remain. The figures do not open automatically.

## Guides

- `START-HERE.md`: short learner start and troubleshooting.
- `agent.md`: the tutor's introduction, operation, test guidance and closing.
- `LESSON_INSTRUCTIONS.md`: detailed lesson plan and learner steps.
- `PROGRAM_GUIDES.md`: program overviews and code explanations.
- `EXPERIMENT_NOTES.md`: your own measurements and the reason for the model choice.
- `CONCEPTS_AND_CODE.md`: a short conceptual support.
- `TEACHER_ANSWER_KEY.md`: test solutions with reasoning, for instructor use.
- `TEACHER_PREPARATION.md`, `requirements.txt`: environment for the instructor.
- `CHANGELOG.md`: the fixes of the 1.1 and 1.2 editions and the update procedure.
- `SOURCES.md`, `VERIFICATION.md`: origin, professional corrections and checks.

The answer key included in the package is not technically hidden; this is a learning
self-check, not a closed examination system. The tutor gives the solution only after the answer.
The theory HTML and the source notebooks are separate materials, not needed for running.
At the end of the lab Inno says: **"The 3rd Deep Learning lab has ended."**
