# Concept guide and observation support

## The English interactive masterclass

Open `sources/deep_learning_masterclass_en.html` in a browser. All three modules, including their controls, diagrams and dynamic labels, are in English. Use the top tabs to switch modules.

| Checkpoint | Module and section | What to inspect |
|---|---|---|
| B01 | 1 Batch Normalization → 1.1, topology and mini-batch matrix | Select N₁, then N₂. Rows are samples; each column is one neuron's pre-activation values across the batch. |
| B02–B03 support | 1 Batch Normalization → 1.2, the four-step pipeline | Step through centering, normalization and learned scaling/shifting. Change gamma or beta and observe the output. |
| R00 | 2 Skip Connections (ResNet) → 2.2, residual block and live vector | Select Identity Mapping (F=0). Compare the negative input entry in Input, Sum H and Out ReLU(H). Toggle the shortcut. |
| R01–R03 support | 2 Skip Connections (ResNet) → 2.2–2.3 | Locate the residual branch, identity path, addition and final ReLU. Distinguish an identity contribution from the full gradient. |
| G01–G02 support | 3 Dropout & L2 Regularization → 3.2–3.3 | Inspect training versus inference and the penalty example. These support the existing probes; no new checkpoint or extra assignment is added. |

For B01, change one input or select another neuron and describe which values determine the selected column's mean. The HTML's six-house illustration is a demonstration; the notebook uses different four-sample, two-feature data.

For R00, use the live feature-vector table. The negative entry distinguishes the sum H=x+F from the final output y=ReLU(H). Preserving x at the addition node does not mean preserving every negative value after ReLU.

## If the HTML cannot be opened

Keep the observation discussion using these English examples. For BN use [[2,10],[4,18],[6,20],[8,40]], with one sample per row and one neuron per column. The column means are 5 and 22. Ask which entries contribute to one neuron's statistic.

For the skip use x=[2,4,−1,3], F=[0,0,0,0], H=x+F=x and y=ReLU(H)=[2,4,0,3]. Ask where the negative input survives. These alternatives preserve the intended discussion without requiring a particular browser or external styling connection.

The masterclass is supplied by the instructor. Its curve animations and loss landscapes are illustrations, not measurements from the student's model. Apply the precise interpretations below when a visual explanation simplifies BN, gradients, overfitting or weight decay.

## Precise interpretations

| Concept | Meaning in this practice |
|---|---|
| BN axes | For Dense inputs, normalize each feature across batch samples; convolutional BN also includes spatial positions per channel. This is not merging RGB channels. |
| Gamma/beta | Learned feature scales/shifts. Gamma can be negative; the HTML slider range is not a general constraint. BN is not min–max scaling or a forced Gaussian distribution. |
| Running state | Moving mean and moving variance, not a moving standard deviation. Inference uses stored state. |
| BN benefits | BN can aid optimization but does not guarantee higher accuracy or removal of every vanishing gradient. Internal covariate shift is a historical motivation, not a single settled explanation. |
| Activation slope | Sigmoid is approximately linear near 0, not exactly linear. Local activation derivatives are not a measurement of an entire network’s learning. |
| H=x+F | F=0 gives identity at the sum; a subsequent ReLU clips negative values. A projection skip can have weights. |
| Gradient path | dH/dx contains an identity contribution (an identity matrix in multiple dimensions). Other branches, cancellation, projections and activations affect the full gradient. R03 measures examples automatically. |
| Loss landscape | The HTML draws prescribed surfaces and trajectories. Neither BN nor skips universally guarantee a convex loss or global minimum. This notebook does not reproduce the historical 20/56-layer experiment. |
| GAP/1×1Conv | GAP averages spatial positions per channel;1×1Conv learns channel mixing. Input shapes can impose other size restrictions. |
| L2 | A loss penalty; not universally equivalent to decoupled weight decay with every optimizer. |

## Code-reading glossary

axis=0 reduces rows separately per column in our 2Dexample; axis=1 works across columns within each row. Broadcasting applies a feature vector to every sample row. get_layer selects by name; get_weights/set_weights read/restore arrays. Functional API layer calls produce tensors, allowing branches. Add sums equally shaped tensors elementwise. GradientTape records operations for automatic differentiation; no manual differentiation task is set. iter creates an iterator and next retrieves one item, here a whole images–labels batch. argmax(axis=1) selects the maximum-probability column index per row.

## Controlled CIFAR comparison

Shared8000/2000/2000 split, fixed order, batch 64,6 epochs, separate Adam(1e-3) optimizers. Conv16–optionalBN–ReLU–MaxPool–Conv32–optionalBN–ReLU–GAP–Dense10. Rescaling1/255 once inside each model. No Dropout/L2/skip/augmentation in the two models. Common Conv/Dense starting weights are checked. Restore best val_loss, select on validation, then test. BN improvement is not required. Few epochs and fixed batch order are educational controls, not a universal training recipe. Two90-minute sessions are a planning estimate; discussion may take longer.

Use RECOVERY.md for recovery. There is no automatic homework or submission.
