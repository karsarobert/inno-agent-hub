# Instructor setup

## Environment

The package targets Linux x86-64, Python 3.12, NumPy, Matplotlib and CPU-only
TensorFlow/Keras. VALIDATION.md records the tested versions and measurements.
`requirements.txt` pins tested direct dependencies, not every transitive dependency.

The following is **instructor preparation**, not a student exercise:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python environment_check.py
```

Run these commands from the extracted workspace if a new environment is needed.
An existing suitable TensorFlow environment can also be used after testing;
do not unnecessarily install another TensorFlow distribution over it. Configure
Innoagent's Run feature to use the same appropriate interpreter using the actual
application settings. This package does not assume unverified menu commands.

`cpu_environment.py` disables GPU visibility before importing TensorFlow, then
sets TensorFlow to CPU-only operation. Compute and data-loading thread counts
are small. Networks have 25 or 193 parameters. No CUDA or GPU installation is
needed. Run each file in a fresh Python process; importing it into an existing
notebook kernel is not the intended classroom workflow.

## Before-class checks

1. Extract into a new workspace and use Run to execute the environment check.
2. Run G04_04's starting version. Check eight units, 120 epochs, 64/128 samples,
   CPU execution and saved figures.
3. Try the 64-unit, 400-epoch version and measure total runtime. Restore eight
   units and 120 epochs before giving the package to students.
4. Try L2 strengths 0, 0.001 and 0.05. The supplied starting value is 0.
5. Check that every first Run request follows a meaningful introduction:
   purpose, input–computation–output relationship and key code with explanations.
   A statement of purpose alone is not enough. The tutor should then request
   one run, wait for the result and follow the planned changes. Prompt files
   alone do not prove how a particular Innoagent version behaves.

Keep instructor checks separate from student `view` folders. No completed student
runs are included. Reference images live separately under `instructor/sample_outputs`.

## Why is the problem so small?

The goal is to connect code with its output. A synthetic one-input task avoids
the additional complexity of Spotify preprocessing, genre encoding and large
datasets. Data is generated locally, so there is no download or CSV preparation.
The known generating function makes the prediction curve directly interpretable.

Network programs perform real TensorFlow/Keras training. Activation, momentum,
dropout, softmax and BN examples are mathematical demonstrations, not fabricated
training results. The required network does not include dropout: we first study
its mechanism separately. Applied dropout and early stopping comparisons remain
in the related notebook.

## Deliberate simplifications

- The network uses Adam and MAE, as in the related notebook, but here the rate
  is 0.01 and the task and sample count are different.
- L2 applies to both Dense kernels. This directly links the full kernel sum of
  squares to the penalty. The HTML/Spotify example regularizes hidden kernels
  only; the tutor briefly identifies the difference.
- No early stopping or best-weight restoration occurs. Every run evaluates the
  last epoch's model consistently.
- There is no final test-set evaluation. Repeated illustrative comparisons using
  validation are not independent performance assessment. The final quiz tests
  conceptual understanding, not the model's generalization.
- H1 and H2 differ in architecture and cannot have identical weight matrices.
  H2/H3 and L2 runs share an initial weight ID and shuffling rule.
- Fixed seeds reduce random variation but do not promise bitwise identical
  results across machines and package versions.

## Timing and instructor decisions

Block 1 reaches the first network run. Block 2 compares network size, training
duration and L2, followed by dropout and the quiz. Most edits change one value.
The tutor must allow students to answer observation questions themselves.

If local computers are slower, establish a shorter common training schedule
before class. H2 and L2 runs must still use the same epoch count, with H3 as the
longer-training experiment. Recheck the curves; do not guarantee visible
overfitting. Optional softmax/BN must not automatically consume required lesson time.

## Using the English edition

This edition translates the Hungarian 1.1 package, including filenames, code
identifiers, comments, messages, figures and instructor documents. Use the
English files together in a separate folder: mixing translated and untranslated
helper modules will break imports. Keep the conventional filename `agent.md`.
Load the English tutor instructions using the application's usual method.
Begin with “Let's start Deep Learning Lab 4!”

The enhanced pre-run explanations are retained. On resumption, if an introduction
was missed, supply it before the next modification without repeating a successful
run or restarting the lab. For an existing conversation, do not assume that
changed instruction files are automatically reloaded. If a fresh conversation
is needed, provide the current stage, current settings and latest output.

The earlier Hungarian trial reported verbatim duplication of entire replies.
Its cause was not established from the transcript. This translation does not
claim to repair application streaming, display or response-generation behavior.
During the live check, verify that each explanation appears once and that the
tutor waits for the student's response. If duplication persists, distinguish
what the model returned from what the application displayed or exported.

The original pre-run explanation update moves the first code explanation before
execution; it is not an additional full lecture after every run. Adjust pacing
based on the local trial.

## Source and use

The package accompanies DL_04 theory and follows the tutoring structure of the
DL_03 package. Prepared Python examples run locally offline; Innoagent's model
connection is separate. Instructor keys are readable in the package. This is
guided learning, not a closed examination interface.
