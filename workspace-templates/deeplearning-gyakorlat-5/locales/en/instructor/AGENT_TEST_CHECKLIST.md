# Brief live Innoagent trial before class

These are expected behaviours, not a report of completed live testing.
Python verification is documented separately in VERIFICATION.md.

1. **New start.** Say "Let's start the practice." Expect one introduction,
   autoencoder/ECG goal, environment check and a wait. No CNN or full task list.
2. **Successful check.** Supply ENVIRONMENT OK. Expect the refresh reminder,
   G01 purpose and input, 140 points, indexing, key code and one baseline run request.
3. **Only done.** Reply "done". Expect one specific request for missing evidence,
   without another full introduction or automatic completion.
4. **Repeated output.** Paste an already accepted result again. It must not count
   as a new run or trigger a repeated full next-task message.
5. **Missing explanation.** Say "I don't understand fit." Expect a short explanation
   of input=target, batches and weight updates, not a lesson restart.
6. **Before G03.** Expect an explicit explanation that these are real saved
   reference outputs, not the student's latest model. Explain abs, mean and axis=1 before Run.
7. **Unchanged histogram after an index change.** Expect acceptance: the full
   group did not change. The agent must not ask for an unnecessary fix.
8. **Threshold 0.025.** TP does not increase from the 0.04 run. Expect acceptance:
   all anomalies were already detected; discuss the change in FP.
9. **Incorrect answer.** Say "Recall means how many alerts were correct."
   Expect polite correction: that describes precision; recall starts with actual anomalies.
10. **Closing quiz.** One question at a time, answer revealed only afterwards.
    Clarify "B or D" before scoring. After question ten: score, summary and explicit
    closure. No homework, eleventh question or CNN task.

Without reliable timing, the agent must not claim "you have 12 minutes left".
Scoring and memory must use capabilities actually available in the application.

## Specific version 1.1 checks

- The first reply to every successful run includes a separate View-refresh reminder,
  even if only two numbers were submitted. It names the right image and does not
  invent an unknown run folder.
- Opening a file starts with a brief map of its numbered sections. The full
  autoencoder is shown, not two distant layers presented as neighbours.
- Before both index changes, explain that 0 is first and 3 fourth, selected now
  for closer inspection. Original signal values remain unchanged.
- After the student's 30-epoch run, use comparison.png with both run names.
  Do not silently substitute a reference image if a matching earlier run is missing.
- After axis_1.png, wait for an explanation of why two signals have two separate means.
- Precision starts with 127 alerts. After its question and answer, recall starts
  with 128 actual anomalies. Begin the quiz only after both separate answers.
- Explain that G04 recomputes the same errors from fixed reconstructions, not that
  it performs no error calculation. Do not invent details of unseen waveforms.

## English consistency

The agent speaks English and uses the English filenames and variables throughout,
including quiz snippets. It calls the area View / file list unless the observed
interface uses another label. Requests for sample_index = 3 must explicitly say
"the fourth normal and fourth anomalous example", not merely "change the index".
