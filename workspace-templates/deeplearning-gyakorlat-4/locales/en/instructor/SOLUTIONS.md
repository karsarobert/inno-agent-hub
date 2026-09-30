# Instructor solutions and interpretation notes

Student files are working starting versions. A solution consists of changing
the specified setting, rerunning and interpreting the actual result. Do not
present all the following values as one large block. The tutor supports only
the current experiment at each step.

## 1. Learning rate

| Run | learning_rate | number_of_steps | Comparison |
|---|---:|---:|---|
| R1 | 0.1 | 8 | Initial state |
| R2 | 0.8 | 8 | R1 |
| R3 | 1.1 | 8 | R1/R2 |
| R4 | 0.1 | 25 | R1, at the same rate |

R1 approaches from one side. In R2, the error alternates sign but shrinks in
magnitude. R3 has growing oscillations. R4 shows that more updates with the
original small steps get closer to the target.

Instructor check: `w_t - 3 = (w_0 - 3) * (1 - 2*eta)**t`. This holds for this
specific quadratic function, not arbitrary network training. It can verify
the program's results and the first worked update.

## 2. Momentum

The initial setting is `momentum = 0.9`; change it to `0.0`. Rate 0.1 and 40
steps stay fixed. At zero momentum, both paths, endpoints and losses coincide
because the two update rules become identical. At 0.9, the path can cross to
the other side of the minimum. Oscillation alone does not imply an incorrect
algorithm, and momentum is not guaranteed to be better in every situation.

## 3. Activations

| Run | Activation | Outer inputs | Negative slope |
|---|---|---|---:|
| A1 | `sigmoid` | −6 and 6 | unused |
| A2 | `sigmoid` | −8 and 8 | unused |
| A3 | `relu` | restored to −6 and 6 | unused |
| A4 | `leaky_relu` | −6 and 6 | 0.1 |
| A5 | `leaky_relu` | −6 and 6 | 0.2 |

The middle inputs remain −1, 0 and 1. At zero, sigmoid outputs 0.5 with derivative
0.25; incoming gradient 2 therefore gives returned gradient 0.5. At input 6, the
derivative is approximately 0.00247; at 8, about 0.000335. In saturation, the
backward signal is attenuated. The output gets closer to 1 while the derivative
shrinks; these are different quantities.

At −1, ReLU gives output 0 and derivative 0. Leaky ReLU with slope 0.1 gives
output −0.1, derivative 0.1 and returned gradient 0.2. With slope 0.2, these become
−0.2, 0.2 and 0.4. Briefly mention the convention at the kink at zero, but do not
examine subgradient theory.

## 4. Small network

```python
# H1: initial settings
HIDDEN_UNITS = 8
EPOCHS = 120

# H2: only hidden-unit count changes relative to H1
HIDDEN_UNITS = 64
EPOCHS = 120

# H3: only training duration changes relative to H2
HIDDEN_UNITS = 64
EPOCHS = 400
```

These are settings for separate runs, not a block to paste into the program.
Rate 0.01, batch size 16 and seed 42 stay fixed. The noise-free curve is a
reference; the model receives noisy training targets.

Compare both final MAEs and the curves. The 64-unit model has 193 parameters,
versus 25 for eight units, but validation performance need not improve. Lower
training error and higher validation error after longer training may indicate
overfitting. Do not turn one small difference into a general rule.

Training epoch averages can differ from training MAE reevaluated with the final
weights. The minimum of the validation curve is not the retained model state:
there is no early stopping or best-weight restoration.

## 5. L2

| Run | L2_STRENGTH | Hidden units | Epochs |
|---|---:|---:|---:|
| REG0 – no penalty | 0.0 | 64 | 120 |
| REG1 – mild penalty | 0.001 | 64 | 120 |
| REG2 – strong penalty | 0.05 | 64 | 120 |

This does not continue the 400-epoch H3 model. Each run starts from the same
initial weights; H2/H3/REG0/REG1/REG2 have matching initial weight IDs.
REG0 reproduces H2 when data handling and environment are identical.

Both Dense kernels receive `kernel_regularizer=regularizers.l2(L2_STRENGTH)`.
Biases are not regularized. The penalty equals λ times the printed kernel sum
of squares. `final_validation_loss = final_validation_mae + l2_penalty`.
At λ=0, total validation loss and validation MAE coincide.

Larger λ can reduce weight magnitude but overly restrict the model. Total losses
with different λ are not a common measure of prediction quality; use MAE on the
same data. A larger gap due to the penalty and an improved MAE can occur together.

## 6. Dropout

| Run | dropout_rate | random_seed | training_mode |
|---|---:|---:|---|
| D1 | 0.5 | 42 | `True` |
| D2 | 0.25 | 42 | `True` |
| D3 | 0.25 | 43 | `True` |
| D4 | 0.25 | 43 | `False` |

D1 doubles retained values; D2/D3 multiply them by 4/3. D2 applies a lower
threshold to the same random numbers: previously retained values stay retained,
and additional values may survive. D3 creates a new sample; a fixed probability
does not specify identical dropped positions or counts. D4 passes every input
through unchanged. Masking is not deleting weights.

One mask need not preserve the actual input average. Inverted dropout preserves
the expected value of each activation. A fixed seed makes repeated program runs
reproducible in the same environment; it does not represent resetting a real
training generator to the same state before every batch.

## Optional files

Softmax of [2,1,0] is approximately [0.665241,0.244728,0.090031]. With
`common_shift = 1000.0`, the probabilities are unchanged and the stable calculation
does not overflow. Outputs sum to 1. Changing one logit generally changes all probabilities.

For BN, [1,2,3,4] has mean 2.5 and variance 1.25 using the 1/m convention.
With epsilon=0.001, normalized values are approximately
[−1.3411,−0.4470,0.4470,1.3411]. Gamma=2 and beta=1 scale and shift these values.
Epsilon means normalized variance is not exactly 1. Evaluation mode retains the
stored statistics even if inputs change to [2,3,4,5]. These statistics are illustrative.

## Evaluating student understanding

“It did not improve”, “it barely changed” and “it is unclear” are acceptable
when supported by the student's output. Do not demand exact instructor reference
numbers or steer towards a predetermined winner. The detailed quiz key is in ANSWER_KEY.md.
