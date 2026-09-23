# Sources and processing decisions

## Teaching materials provided by the user

- Dl_02(1).zip: the role of the Hungarian Inno tutor, mandatory introduction of new
  programs, 2 x 45 minute structure, learner editing and independent running,
  explanation -> action -> interpretation order, separate experiment results.
- DL_03(1).html: loss, gradient, learning rate, batch/epoch,
  optimization, spiral classification, softmax, output interpretation, notebook refinements.
- PTE_DL3_1_ipynb_masolata(2).ipynb: linear regression, MSE/2 loss,
  weight and bias gradient, custom gradient method.
- PTE_DL3_spiral(2).ipynb: 600 spiral points, three classes, one-hot target,
  Dense 50 -> Dense 50 -> Dense 3, ReLU/softmax, Adam, training and evaluation.

We did not modify the source files. The package is the practical counterpart of the
theoretical material, not a further examination of all the theoretical derivations.
There is no separate manual backpropagation or numerical gradient problem set.

## Important differences in the local processing

1. Instead of notebooks, standalone .py programs run with the Inno Agent Run button.
2. Instead of the regression notebook's data read from the network, we generate
   our own documented synthetic data: 100 time values between 0 and 10, score
   20 + 6 x time + normal noise with standard deviation 4, seed=42. This is not the
   original data file, and not a real learner study. MSE/2 and its gradient are kept.
   The rate and epoch are matched to this differently scaled example.
3. We keep the spiral data construction, but use a fixed random generator
   and a train/validation/test split that preserves the class ratio.
   Sizes: 360/120/120, that is 60/20/20 percent.
4. Instead of the notebook's X_test set, which was also used for validation, we keep
   a genuinely separate test set. We measure on the test only after the choice.
5. For the colouring we pass the class index, not the full softmax vector.
6. We do not carry on the notebook's model/model2 name confusion. Every program
   configures, trains and evaluates its own model. We do not compare a trained
   and an accidentally untrained network as an activation-function effect.
7. The mandatory models use a softmax output; the flawed comparison with a ReLU
   output is left out. A logit output does not burden the lesson even as a separate
   optional topic.
8. We build the notebook's two 50-neuron hidden layers step by step:
   baseline without a hidden layer -> 16 hidden neurons -> 50 and 50 neurons.
   We work with Keras's default Dense initialization; we do not claim to
   reproduce a bit-identical run of the notebook's glorot_normal initialization.
9. The figures come from ready helper code. For the new files, both the programs
   and the tutor remind about refreshing the View folder. The final test does not
   draw a training curve.
10. The ten new code-comprehension questions build on the operations processed by
    the learner.

## Official technical background

- [Keras: model configuration, training, measurement and estimation](https://keras.io/api/models/model_training_apis/).
  compile configures, fit trains, evaluate measures, predict estimates; validation_data
  serves verification, without a direct weight update.
- [Keras: probabilistic losses](https://keras.io/api/losses/probabilistic_losses/).
  categorical_crossentropy can be used for one-hot targets; the sparse variant
  expects integer labels. The from_logits setting determines the interpretation of the output.

We verified the technical API references when preparing the package.


## Methodological source of versions 1.1-1.2

Version 1.2 only touches run identification and the program-side check of the model
choice; no new professional source belongs to it.

The user's test conversation of 20 September 2026: "markdown(9).md pasted in".
The fixes react to the skipped code explanations, the pre-given comparison
answers, the missing rate experiment and the omitted final figure interpretation
observed in it. The content of the ten questions and the answer key is unchanged,
the advance teaching and the independent decision task were strengthened.
