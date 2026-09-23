# Changes - 1.1 and 1.2

## 1.2 - simpler run identification and checked model choice

Based on the group test of 21 September 2026: the learners had to copy long,
timestamped folder names into the code, and the two 50-50 neuron runs (R3, R4)
differed only in the learning rate and the name, so it was hard to
identify which run was which. Because of this, in 6 cases out of 24 learners
the final test did not run on the best model according to the rule, and the
tutor did not report this back.

| Observation | Fix |
|---|---|
| The folder names are long and differ only in the timestamp, the student cannot identify them. | Every run gets a short label from its actual model and rate: R1_baseline_lr0.01, R2_16n_lr0.01, R3_50x2_lr0.01, R4_50x2_lr0.001, the gradient program's one is G01_gradient. The label goes to the start of the folder name, so it appears in the tree in alphabetical order (R1, R2, R3, R4). |
| The full folder name had to be pasted into the code. | L03_04 expects the short run label ("R3"); the full folder name still works, but is not mandatory. |
| It did not become clear whether the selected run really had the lowest validation loss. | Before the test L03_04 prints the "CHOICE CHECK" part, and if the chosen run does not have the lowest validation loss, it stops. For a deliberate deviation "YES" must go into the OVERRIDE line. |
| The learner did not have the data of the four runs in one place. | Without filling it in (empty CHOICE) the program prints only the comparison table of the runs, without a test. The table is deliberately neutral: it does not mark the winner, the learner has to establish that. |
| The tutor said in their text that the choice was good, while the folder entered belonged to another run. | agent.md and LESSON_INSTRUCTIONS.md prescribe: the choice is spoken in the form of a short label + the decisive number, and the verdict of L03_04 must be read back; after a rejected choice no progress is allowed. |
| The settings and the folder name could drift apart. | The program computes the label from the actual network and the learning rate, and also writes it into the "run_label" field of settings.json; the end-of-run summary prints it. |

The ten code-comprehension questions, the training schedule and the choice rule
are unchanged. For the verification see: VERIFICATION.md, "Verification of
version 1.2".

## 1.1 - teaching methodology fixes

Based on the test conversation of 20 September 2026 and the approved comments.

| Observation | Fix |
|---|---|
| The learner only looked at the training settings. | Mandatory fourth spiral run: on the 50-50 network the rate 0.01 -> 0.001; everything else identical. |
| The detailed demonstration of the two gradients, fit and predict/argmax was missing. | Concrete code blocks and pre-run demonstration conditions in the agent and the scenario. |
| The categorical/sparse difference only came up after the wrong test answer. | A label-shape/loss table and an example before the first spiral run. |
| Inno gave the answer of the comparison in advance. | Neutral data -> learner interpretation -> feedback; no pre-highlighted winner. |
| The choice rule was only stated after the results. | Smaller validation loss, on an exact tie fewer parameters: to be stated BEFORE the first spiral run. |
| The choice reason could be copied ready-made. | The learner chooses their own run and writes their own reason; the tutor only helps with the pasting afterwards. |
| The larger model's smaller loss and lower accuracy were lost. | A separate interpretation point and teaching example about the two metrics ranking differently. |
| The figures got general yes/no questions. | Separate training and validation observation, the interpretation of one concrete matrix cell. |
| The quiz started immediately after the final test. | Mandatory waiting for the interpretation of the test figures; the program's closing message asks for this too. |
| The 100% could seem generally valid. | A result valid for the given 120 points, not a guarantee for new points. |
| The closing summary asserted certain knowledge. | "Based on your answers..." wording; separation of running, editing, interpreting and recognizing. |
| The new mandatory run needs time. | New 45+45 minute schedule; no extra mandatory batch or regression experiment. |

The ten code-comprehension questions and the correct answers are unchanged;
the teaching preceding the questions became more complete. Inno still introduces
itself, asks for a run with Run, directs to the instructor when a package is
missing, warns about refreshing the View, and clearly closes the lesson.

## Update

Unpack the package ZIP into a new folder, open this as the workspace, and
start a new conversation with the new agent.md. Keep the earlier learner
modifications and results in the old folder. The earlier preset does not
update by itself just because you downloaded the new package. On machines
already opened, the old (timestamped) folder names remain; the short labels
only appear on a new run. L03_04 also recognizes the 1.1 long folder names,
so the update does not break the earlier results.

## Display

For the learner text we ask for simple code blocks and regular tables.
The teaching material does not switch off the application's automatic tool
panel and export formatting. Live interface retesting of the new tutoring
behaviour is an instructor task; the details of the technical run verification
are in VERIFICATION.md.
