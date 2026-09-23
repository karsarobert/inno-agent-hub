# My own experiment notes - Lab 3, 1.2

The rule I learned BEFORE the first spiral run: I choose based on the smaller total validation
cross-entropy; on an exact match fewer parameters decide.
I also interpret the accuracy and the figures. I look at the test only after the decision.
I do not compare the MSE/2 value of the gradient program to the loss of the spiral models.

## Four mandatory spiral runs

| Run | Hidden neurons | Rate | Epoch | Batch | Parameters |
|---|---|---:|---:|---:|---:|
| R1 | none | 0.01 | 150 | 32 | 9 |
| R2 | 16 | 0.01 | 150 | 32 | 99 |
| R3 | 50, 50 | 0.01 | 150 | 32 | 2853 |
| R4 | 50, 50 | 0.001 | 150 | 32 | 2853 |

If the instructor selected a different uniform epoch budget in advance, write in the actual one.

| Run | Short label of the run (from the folder name) | Validation loss | Validation accuracy |
|---|---|---:|---:|
| R1 | | | |
| R2 | | | |
| R3 | | | |
| R4 | | | |

I compare based on the complete printed/saved loss, not only on the rounded number.
I write the data and the interpretation myself; the tutor does not fill it in instead of me.

## My own observations

- R1 -> R2: what changed in the decision boundary and in the validation metrics?
- R2 -> R3: do the loss and the accuracy prefer the same model?
  Why can the ranking by the two metrics differ?
- R3 -> R4: how do the training and the validation loss curve change separately?
  What difference do I see in the initial progress and at the end of the run?
- What stayed identical in the rate experiment, and what changed?
- One validation matrix cell: true label -> predicted label, count.
  If there are values only in the main diagonal, what does that mean?

## Decision - BEFORE looking at the test

- Out of R1-R4 I choose this run:
- The short label of the run (for example R3_50x2_lr0.01):
- The validation values compared:
- The justification in my own words:

Only after this do I fill in the three lines of L03_04: CHOICE (the short label of the run),
CHOICE_REASON (the justification) and - only for a deliberate deviation - OVERRIDE.
Before the test the program prints whether my choice is the run with the lowest validation
loss; if it is not, I review the data first.
The previously saved model can be loaded, I do not have to restore the current code of L03_03 for it.

## Final test and interpreting the figures

- Test accuracy:
- Test loss:
- One mistake: true label -> predicted label and count.
  In a perfect case the meaning of the main diagonal and of the off-diagonal zeros:
- Which data does the measured accuracy refer to, and what does it not guarantee for new points?

I refreshed the View and looked at the final_test folder of the chosen run.
Based on the test result I do not choose a new model any more. After the discussion of the figures
comes Inno's ten multiple-choice questions.
