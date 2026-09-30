# Deep Learning 2026 – Lab 4

**English innoagent package · 2 × 45 minutes · CPU · Version 1.1 EN**

Before each new example, the tutor explains its purpose, important code and
output. You run a working example, change one setting and examine the effect
using numbers and figures. You do not need to write a program from an empty file.
The six main topics are learning rate, momentum, activations, a small neural
network, L2 regularization and dropout. The lab ends with ten fixed quiz questions.

## Getting started

1. The package is already prepared as a workspace: `agent.md` and the `G04_...py`
   files sit directly in the workspace folder. Nothing to extract.
2. In Innoagent, select the workspace and its tutor instructions using your usual
   workflow. This package uses the existing application; it does not install one.
3. Start a new conversation: **“Let's start Deep Learning Lab 4!”**
4. Inno introduces the lesson and asks you to run the environment check.

**You edit, save and use Run.** Run handles the working directory; no `cd` is
required. Ask your instructor if a package is missing. Student programs install
nothing and download no data.

## Programs

| File | What we investigate | Main figure |
|---|---|---|
| `environment_check.py` | Local Python, CPU computation and figure saving | `check.png` |
| `G04_01_learning_rate.py` | One weight approaching a minimum | `learning_steps.png` |
| `G04_02_momentum.py` | Paths of two update rules | `trajectories.png` |
| `G04_03_activations.py` | Activation output and local derivative | `activation_and_derivative.png` |
| `G04_04_small_network.py` | Hidden-unit count and training duration | `prediction.png`, `learning_curves.png` |
| `G04_05_l2_regularization.py` | Weight penalty, loss and MAE | `loss_and_mae.png`, `prediction.png` |
| `G04_06_dropout.py` | Random masks and the two modes | `dropout.png` |

`K04_01_softmax.py` and `K04_02_batch_normalization.py` are **optional** supplements,
outside the required 90 minutes and final quiz. No initialization exercise is
included. You do not implement AdaGrad or Adam manually; the small network uses
the supplied Adam optimizer.

## Where are the results?

Each run creates a timestamped subfolder under `view`, whose full path is printed
at the end. Earlier results remain available. **Refresh the View folder / file
list after each run**, then open the image in the new folder. Images do not open
automatically. Numerical results are saved as `values.csv`; settings and summaries
are saved as `result.json`.

## The small network's task

We predict a noisy continuous y value from a synthetic x value. Every run uses
the same 64 training and 128 validation samples. Data generation follows
`y = sin(1.5*x) + 0.3*x + noise`. This is illustrative regression, not Spotify
prediction or classification. The target has arbitrary numerical units; MAE is
not multiplied by 100.

We experiment using validation data. **There is no independent final test-set
measurement**, so the results do not establish final generalization performance.
The Spotify notebook is a separate, more complex application and is not needed
to execute these examples. The theory HTML is also not a runtime dependency.

## Guides

- `START-HERE.md`: student startup and troubleshooting.
- `agent.md`: tutor behavior and progress handling.
- `LESSON_INSTRUCTIONS.md`: step-by-step lesson plan.
- `PROGRAM_WALKTHROUGHS.md`: introductions and key-code explanations.
- `CODE_UNDERSTANDING_TEST.md`: ten fixed single-answer questions.
- `CONCEPTS_AND_CODE.md`: brief concept reference.
- `instructor/`: setup, solutions, answer key and verified reference outputs.

The tutor tracks progress in conversation state or available application memory.
It does not write progress files or repeatedly open the file tree. The closing
sentence is **“Deep Learning Lab 4 is now complete.”** There is no homework.

## Requirements and language

In a prepared environment, the example programs run locally without internet or
GPU. Network-training programs explicitly disable GPU use. NumPy examples need
NumPy and Matplotlib. The environment check and the two network programs also
need TensorFlow/Keras. Innoagent's own model connection is a separate requirement;
this package does not make the agent service work offline.

This is the English edition of the Hungarian 1.1 package. Program filenames,
identifiers, comments, console messages, output paths, figure labels and guides
are in English. The conventional `agent.md` filename is retained. Use a separate
workspace for this edition rather than mixing English and Hungarian modules.
Instructor solutions are readable in the `instructor/` folder: this is guided
learning and self-assessment, not a technically locked examination system.
