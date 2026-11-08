# Concept guide and observation support

## Updated demonstrations and English access

The supplied `forrasok/Batch_Normalization_HU.html` and `forrasok/Skip_Connection_ResNet_HU.html` are unchanged Hungarian originals. The notebook, tutor, questions and this guide are English. The following glossary and self-contained examples make both observation checkpoints possible without Hungarian proficiency or a working HTML/CDN connection.

| Hungarian screen label | English meaning / action |
|---|---|
| Hol vannak az x₁…x₆értékek? | Locate the six weighted values for one selected neuron. |
| Mini-Batch(Sorok) vs.Neuronok(Oszlopok) | Mini-batch samples are rows; neurons are columns. |
| Vizsgált neuron; N₁/N₂/N₃ | Selected neuron; click another neuron and inspect its column. |
| Bemenet / Eltolás / Skálázás / Tanulható | Input / centering / normalization / learned scale and shift. |
| Következő lépés / Előző lépés | Next step / previous step. |
| Identitás / Finomhangolás / Jellemző-kiemelés | Identity / small correction / feature enhancement presets. |
| Skip Connection: BEKAPCSOLVA | Skip connection enabled; toggle to compare. |
| Bemenet / Korrekció / Összeg / Kimenet | Input x / correction F(x) / sum H=x+F / output y=ReLU(H). |
| Tanítási hiba / Teszt hiba | Training error / test error. |

For B01, inspect the topology/matrix panel and switch N1 to N2. A selected column contains one neuron’s weighted values across samples. Then inspect the four BN stages and change one input. Self-contained alternative: [[2,10],[4,18],[6,20],[8,40]], one sample per row and one neuron per column. Column means are 5 and 22. Use this matrix to identify which values contribute to one neuron’s statistic. The notebook’s data and probes are separate from the HTML’s six-sample house illustration.

For R00, select identity(F=0) and inspect the live vector panel. Self-contained alternative: x=[2,4,−1,3],F=[0,0,0,0],H=x+F=x,y=ReLU(H)=[2,4,0,3]. Identify where the negative input survives. The sum preserves it; post-activation does not. Toggle the skip to inspect its contribution if the HTML is available. Degradation curves and landscape animation are prescribed illustrations rather than a measurement from your run. Higher training error can indicate optimization difficulty; overfitting does not require training error near 0.

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

Use FOLYTATAS.md for recovery. There is no automatic homework or submission.
