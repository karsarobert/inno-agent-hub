# Instructor answer key – fixed final quiz

The tutor must not extend the quiz or replace it with improvised questions.
Score the first answer, then explain. Record prior assistance separately;
explanation after an answer is not prior assistance.

| Question | Correct answer |
|---|---|
| 1 | B |
| 2 | D |
| 3 | A |
| 4 | C |
| 5 | B |
| 6 | D |
| 7 | C |
| 8 | A |
| 9 | B |
| 10 | D |

## 1. One weight update

**B.** The gradient is −8. The new weight is −1 − 0.1·(−8) = −0.2.
Subtracting a negative number increases the weight.

## 2. Without momentum

**D.** The `beta * velocity` term becomes zero. The update reduces to
`position = position - learning_rate * gradient`, which is plain gradient descent.

## 3. ReLU output

**A.** The maximum chooses between 0 and each input. Negative values become
zero; positive values pass through unchanged.

## 4. Sigmoid: output and derivative

**C.** Sigmoid outputs 0.5 at z=0. Its local derivative is
0.5·(1−0.5)=0.25. The output and derivative are different numbers.

## 5. The regression network

**B.** `shape=(1,)` specifies one feature per sample. `Dense(64)` is a single
hidden layer. `Dense(1)` without a specified activation produces a linear output.

## 6. How many training updates?

**D.** 64/16=4. Each training batch produces one optimization update.
Validation measurements do not add weight updates.

## 7. L2 and total loss

**C.** The sum of squares is 4+1=5. The penalty is 0.01·5=0.05 and total loss
is 0.12+0.05=0.17. Prediction MAE alone is still 0.12.

## 8. What should we compare?

**A.** MAE on the same targets and validation samples can be compared directly.
Total loss with different regularization terms is not prediction error alone.
This result does not prove superiority on every dataset.

## 9. A retained dropout activation

**B.** The multiplier is 1/(1−0.5)=2, so 0.8·2=1.6.
Output would be zero if the mask were 0.

## 10. Dropout during evaluation

**D.** False selects the else branch. Inverted dropout passes values through
unchanged in evaluation mode, without a new mask or extra scaling. Python does
not evaluate variables in the branch that is not executed.

## Final feedback

Report X/10 with short, concrete conceptual feedback. Do not assign an arbitrary
university grade; this quiz does not prove independent programming ability.
Identify at most two topics to revisit. Report skipped experiments separately
from the quiz score. End with “Deep Learning Lab 4 is now complete.”
Do not automatically assign homework or question 11.
