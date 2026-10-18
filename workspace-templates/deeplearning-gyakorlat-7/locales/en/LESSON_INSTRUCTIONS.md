# Practice 7 · detailed tutor sequence

The agent converses; the student edits and runs cells in Colab. Follow agent.md.
Prepared cells also require the one-cell → evidence → feedback rhythm. Never send the entire sequence
as one student-facing instruction.

## Suggested pacing

Plan initially for two 45-minute blocks: setup, regression and MNIST preparation in the first;
MNIST evaluation, anomalies and closing in the second. Prior knowledge, dialogue and runtime speed
can extend this. If time is short, record an honest stopping point instead of silently omitting
interpretation or claiming completion without evidence.

## Introduce each new task

- Before R01: historical district data, 13 features, one real target in thousand historical USD; regression.
- Before M01: 28×28 images, ten digits, flattening, one-hot labels and softmax; classification.
- Before A01: five artificial transaction features, normal 0/anomaly 1; learn normal reconstruction,
  calibrate an error threshold and evaluate a separate mixed test. This is not a direct binary classifier.

## Cell map

| Cell | Mode | Focus |
|---|---|---|
| E01 | prepared | Environment and working method |
| R01 | prepared | Load the housing data |
| R02 | prepared | Inspect the data |
| R03 | prepared | Training, validation and test sets |
| R04 | independent | Scale without data leakage |
| R05 | independent | Build the regression network |
| R06 | independent | Loss and early stopping |
| R07 | prepared | Train the regression model |
| R08 | prepared | Read the learning curves |
| R09 | prepared | Final test and a baseline |
| R10 | independent | A new input and the same scaler |
| M01 | prepared | MNIST and a smaller training subset |
| M02 | prepared | One image and its true label |
| M03 | independent | Normalize and flatten |
| M04 | independent | One-hot target vectors |
| M05 | independent | Build the digit classifier |
| M06 | independent | Choose a classification loss |
| M07 | prepared | Train the classifier |
| M08 | prepared | Plot loss and accuracy separately |
| M09 | independent | Test performance and one digit prediction |
| M10 | prepared | Inspect classification errors |
| A01 | prepared | Synthetic transactions and labels |
| A02 | prepared | Split before fitting a scaler |
| A03 | independent | Normal training data and separate calibration |
| A04 | independent | Learn the normal input scale |
| A05 | independent | Build an autoencoder with a bottleneck |
| A06 | prepared | Train inputs to reconstruct themselves |
| A07 | independent | One calibration error per sample |
| A08 | independent | Fix the threshold before testing |
| A09 | independent | Mixed test decisions and metrics |
| A10 | prepared | Error distributions and mistakes |
| Z01 | prepared | Save and conclude |

## Per-cell guidance

### [E01] Environment and working method

**Explain before editing/running:** This cell imports the libraries and sets the random seed. It does not train a model. Use Colab to edit and run code; use Innoagent to discuss it. R_, M_ and A_ prefixes keep the three tasks separate.

**Current action only:** Run this cell in Colab. Send the version numbers and the final readiness message.

**Required evidence:** TensorFlow and NumPy versions, plus the E01 readiness message.

**Acceptance criteria — do not recite as the answer before the student responds:** Imports succeed and the readiness message appears. No particular version or GPU is required.

**If stuck:** If TensorFlow cannot be imported, first confirm that this is a Colab Python runtime. Do not start a local installation.

**Then:** wait for the actual output and necessary interpretation. Introduce the next cell only after verification.

### [R01] Load the housing data

**Explain before editing/running:** Each row in the historical Boston dataset describes a district using 13 features. The target is its median home value in thousands of historical US dollars. After loading the official NPZ file, we will create our own split. A manually uploaded NPZ file is only a download fallback.

**Current action only:** Run the loader. Report the feature and target shapes, and explain what the target represents.

**Required evidence:** Both shapes and the meaning of the target in your own words.

**Acceptance criteria — do not recite as the answer before the student responds:** (506, 13) and (506,); district median home value in thousand historical USD. The 13 is a feature count.

**If stuck:** The first dimension counts samples. The target is neither a current price nor the observed selling price of an individual house.

**Then:** wait for the actual output and necessary interpretation. Introduce the next cell only after verification.

### [R02] Inspect the data

**Explain before editing/running:** A DataFrame makes the features readable. Column minima and maxima reveal their different scales. isfinite checks for missing or infinite numeric values.

**Current action only:** Run the cell. Identify two actual column ranges and explain why scaling will be useful.

**Required evidence:** Two column ranges from your output and a brief explanation.

**Acceptance criteria — do not recite as the answer before the student responds:** The observation uses actual output and identifies different input scales. Scaling inputs does not change the target unit.

**If stuck:** TAX and NOX have different orders of magnitude. Ask the student to read their own values rather than supplying invented output.

**Then:** wait for the actual output and necessary interpretation. Introduce the next cell only after verification.

### [R03] Training, validation and test sets

**Explain before editing/running:** We first keep 60% for training and split the remainder in half. Validation guides early stopping; the final test is reserved for evaluation. Integer rounding makes validation and test counts slightly different.

**Current action only:** Run the split. Send the three sample counts and identify the subset used for early stopping.

**Required evidence:** Three sample counts and the role of validation.

**Acceptance criteria — do not recite as the answer before the student responds:** 303 training, 101 validation, 102 test. We monitor validation loss, not final test loss.

**If stuck:** Training samples update weights. Validation influences selection without directly updating weights.

**Then:** wait for the actual output and necessary interpretation. Introduce the next cell only after verification.

### [R04] Scale without data leakage

**Explain before editing/running:** A MinMaxScaler learns a minimum and maximum for each input column. Fit it only on training inputs. Keep target prices in their original unit.

**Current action only:** Create R_scaler as a MinMaxScaler. Produce R_X_train_s, R_X_val_s and R_X_test_s. Use fit_transform only on training inputs and transform on the other two subsets. Print all three shapes and n_samples_seen_.

**Required evidence:** Your scaling code, three shapes and the number of fitting samples.

**Acceptance criteria — do not recite as the answer before the student responds:** (303, 13), (101, 13), (102, 13), with n_samples_seen_=303. Inspect the code to confirm that only training inputs were fitted.

**If stuck:** Apply the workflow in the HTML example to the R_ variables. Fitting a separate scaler on validation data is incorrect.

**Then:** wait for the actual output and necessary interpretation. Introduce the next cell only after verification.

### [R05] Build the regression network

**Explain before editing/running:** The network predicts one real value from 13 features. Hidden layers use ReLU. A linear output does not constrain the predicted price to the interval 0–1.

**Current action only:** Build R_model as a Sequential model. Set its input size from the scaled training feature count, then add 64 and 32 ReLU units and one linear output. Display the model summary.

**Required evidence:** Model code, the final output shape and why one output is sufficient.

**Acceptance criteria — do not recite as the answer before the student responds:** 13→64→32→1, final shape (None, 1), linear activation. The target is a number rather than a class.

**If stuck:** First show a small Dense example with a different unit count if needed. Let the student assemble their own network.

**Then:** wait for the actual output and necessary interpretation. Introduce the next cell only after verification.

### [R06] Loss and early stopping

**Explain before editing/running:** compile configures learning; it does not train. MAE averages absolute errors. Early stopping selects an appropriate training state using validation loss.

**Current action only:** Compile R_model with adam and mae. Create R_stop using EarlyStopping: monitor val_loss, min_delta=0.001, patience=12, and restore the best weights. Print the loss and monitor names.

**Required evidence:** Compile and callback code, plus what 12 epochs without improvement means.

**Acceptance criteria — do not recite as the answer before the student responds:** MAE, val_loss, patience=12 and restore_best_weights=True. Training may stop after 12 consecutive epochs without sufficient improvement.

**If stuck:** Patience is not the total epoch budget. min_delta defines the size of an improvement that counts.

**Then:** wait for the actual output and necessary interpretation. Introduce the next cell only after verification.

### [R07] Train the regression model

**Explain before editing/running:** fit updates weights using training features and their target values. Validation does not directly update weights. The 150-epoch budget is an upper limit.

**Current action only:** Run training and wait for completion. Report the completed epoch count and the lowest validation loss.

**Required evidence:** The two final summary values after training finishes.

**Acceptance criteria — do not recite as the answer before the student responds:** Between 1 and 150 epochs and a finite validation MAE. No fixed error threshold or early-stop event is required.

**If stuck:** Do not start another fit while training is running. A fresh experiment requires rebuilding the model from R05.

**Then:** wait for the actual output and necessary interpretation. Introduce the next cell only after verification.

### [R08] Read the learning curves

**Explain before editing/running:** The plot shows training and validation MAE. Joint improvement and a persistent separation suggest different learning situations. Focus on directions and relationships rather than an exact epoch number.

**Current action only:** Run the plot. Describe one specific relationship between the two curves.

**Required evidence:** A screenshot or a specific description of the actual curves.

**Acceptance criteria — do not recite as the answer before the student responds:** Both curves are identified and the observation is grounded in the supplied evidence. Never invent the trend of an unseen plot.

**If stuck:** If the student only says the plot is good, ask whether the curves fall together or diverge. Do not repeat an adequate explanation.

**Then:** wait for the actual output and necessary interpretation. Introduce the next cell only after verification.

### [R09] Final test and a baseline

**Explain before editing/running:** We now evaluate the reserved test set. Compare the network with a constant prediction equal to the median training target, a natural MAE baseline.

**Current action only:** Run the cell. Report both MAEs and explain the network error in the correct unit.

**Required evidence:** Network MAE, baseline MAE and an interpretation of the network value.

**Acceptance criteria — do not recite as the answer before the student responds:** Average absolute error in thousand historical USD, interpreted using the actual values. A weaker network is not automatically a coding failure.

**If stuck:** For example, an MAE of 2.5 means about 2500 historical USD average absolute error, not 2.5%. This example is not an expected score.

**Then:** wait for the actual output and necessary interpretation. Introduce the next cell only after verification.

### [R10] A new input and the same scaler

**Explain before editing/running:** Use a raw test sample to illustrate the path of a new input. This is not an additional independent test. Preserve the sample-count dimension even for one row.

**Current action only:** Select the first raw R_X_test row as a two-dimensional slice named R_new. Transform it with the fitted R_scaler to create R_new_s, then predict with R_model. Print input and output shapes and the prediction.

**Required evidence:** Your code, both shapes and why transform is used instead of fit_transform.

**Acceptance criteria — do not recite as the answer before the student responds:** (1, 13) input and (1, 1) output, using the same fitted scaler and column order.

**If stuck:** Selecting index 0 and selecting slice 0:1 produce different shapes.

**Then:** wait for the actual output and necessary interpretation. Introduce the next cell only after verification.

### [M01] MNIST and a smaller training subset

**Explain before editing/running:** MNIST contains 28×28 images of handwritten digits. To keep the exercise manageable, choose a stratified subset of 12000 from the 60000 original training images: 10000 for training and 2000 for validation. Keep the original 10000 test images separate.

**Current action only:** Run the loader. Report the three image-array shapes and the range of integer labels.

**Required evidence:** Three shapes and the available labels.

**Acceptance criteria — do not recite as the answer before the student responds:** (10000, 28, 28), (2000, 28, 28), (10000, 28, 28); labels 0–9. The first dimension counts images.

**If stuck:** The 10000 test images are not drawn from the 12000-image training subset.

**Then:** wait for the actual output and necessary interpretation. Introduce the next cell only after verification.

### [M02] One image and its true label

**Explain before editing/running:** Index 3 selects the fourth image. M_y_test still stores integer labels. The label records which digit the dataset says the image represents.

**Current action only:** Run the cell. State the ordinal number of the image and its true label.

**Required evidence:** The image position and the integer label from your output.

**Acceptance criteria — do not recite as the answer before the student responds:** The fourth image and its actual displayed label. Do not ask the student to guess a future model output.

**If stuck:** Index 0 is the first item, so index 3 is the fourth.

**Then:** wait for the actual output and necessary interpretation. Introduce the next cell only after verification.

### [M03] Normalize and flatten

**Explain before editing/running:** Raw uint8 pixels range from 0 to 255. Converting to float32 and dividing by 255 gives values in 0–1. A 28×28 image retains all 784 values when reshaped into a vector.

**Current action only:** From the raw M_train_images, M_val_images and M_test_images, create float32 arrays M_X_train, M_X_val and M_X_test. Divide by 255 and reshape each image to 784 values. Print the three shapes and the training minimum and maximum.

**Required evidence:** Your code, the shapes, value range and an explanation of -1.

**Acceptance criteria — do not recite as the answer before the student responds:** (10000, 784), (2000, 784), (10000, 784), float32 values in 0–1. -1 asks NumPy to infer the sample count.

**If stuck:** Apply the 6×6 HTML example to this image size. Always use the raw image arrays so re-running does not divide already scaled data again.

**Then:** wait for the actual output and necessary interpretation. Introduce the next cell only after verification.

### [M04] One-hot target vectors

**Explain before editing/running:** A one-hot vector has one position per class. The correct class position contains 1 and other positions contain 0. Preserve the original integer label arrays.

**Current action only:** Use keras.utils.to_categorical to create M_y_train_oh, M_y_val_oh and M_y_test_oh with ten classes. Print the training target shape and the first integer label with its one-hot vector.

**Required evidence:** Your code, the (10000, 10) shape and one matching integer/vector pair.

**Acceptance criteria — do not recite as the answer before the student responds:** Correct ten-class one-hot labels with original integer labels preserved. The position of the 1 matches the label index.

**If stuck:** Do not encode an _oh array again. Always start with the original integer labels.

**Then:** wait for the actual output and necessary interpretation. Introduce the next cell only after verification.

### [M05] Build the digit classifier

**Explain before editing/running:** Two dense hidden layers process 784 pixels. Dropout randomly zeros some activations during training. Ten softmax outputs correspond to the ten digits.

**Current action only:** Create M_model with 784 inputs, 128 ReLU units, dropout 0.3, 64 ReLU units, another dropout 0.3, and ten softmax outputs. Display its summary.

**Required evidence:** Model code, the final shape and the reason for ten outputs.

**Acceptance criteria — do not recite as the answer before the student responds:** (None, 10), the specified Dense layers and both dropout layers. Outputs are not directly integer digits.

**If stuck:** Correct only the affected layer first. Dropout does not randomly remove activations during predict.

**Then:** wait for the actual output and necessary interpretation. Introduce the next cell only after verification.

### [M06] Choose a classification loss

**Explain before editing/running:** Our labels are one-hot vectors and the model uses softmax, so categorical_crossentropy is appropriate. Accuracy measures correct class decisions and is different from loss.

**Current action only:** Compile M_model with adam, a loss suitable for one-hot targets and accuracy. Create M_stop monitoring val_loss with patience=4 and restore_best_weights=True. Print the loss name.

**Required evidence:** Compile and callback code with a reason for the chosen loss.

**Acceptance criteria — do not recite as the answer before the student responds:** categorical_crossentropy with one-hot targets. A sparse variant is only valid if all later target handling is consistently changed to integer labels.

**If stuck:** Derive the choice from the actual target shape rather than asking the student to memorize the loss name.

**Then:** wait for the actual output and necessary interpretation. Introduce the next cell only after verification.

### [M07] Train the classifier

**Explain before editing/running:** Use at most 20 epochs and a batch size of 256. Validation images and targets are separate. verbose=1 shows progress; the final test is still unused.

**Current action only:** Run training and wait for it to finish. Send the epoch count and the highest validation accuracy.

**Required evidence:** The completed epoch count and validation accuracy from your run.

**Acceptance criteria — do not recite as the answer before the student responds:** 1–20 epochs and an accuracy in 0–1. No fixed minimum score is required.

**If stuck:** An accuracy of 0.94 means 94%, not 0.94%. Do not restart the cell while it is running.

**Then:** wait for the actual output and necessary interpretation. Introduce the next cell only after verification.

### [M08] Plot loss and accuracy separately

**Explain before editing/running:** The left plot shows cross-entropy and the right plot shows accuracy. Dropout is active during training and inactive during validation, so the relative positions alone do not prove an error.

**Current action only:** Run the plots. Make one specific training-versus-validation observation on either plot.

**Required evidence:** An image or a specific description based on your plots.

**Acceptance criteria — do not recite as the answer before the student responds:** The student identifies which metric is being discussed and does not treat accuracy and loss as the same quantity.

**If stuck:** Higher validation accuracy with dropout does not by itself prove data leakage.

**Then:** wait for the actual output and necessary interpretation. Introduce the next cell only after verification.

### [M09] Test performance and one digit prediction

**Explain before editing/running:** predict returns ten values for one image. The position of the largest value is the predicted digit. Read the true integer label from the preserved M_y_test array.

**Current action only:** Evaluate M_model on M_X_test and M_y_test_oh, storing M_loss and M_acc. Pass the image at M_index to predict using a two-dimensional slice, then use np.argmax to store M_predicted_digit. Print accuracy, the ten outputs, the predicted digit and its true label.

**Required evidence:** Your code, accuracy, output vector, predicted digit and true digit.

**Acceptance criteria — do not recite as the answer before the student responds:** Ten outputs for one image, an argmax in 0–9 and an integer true label. A wrong prediction does not automatically imply wrong code.

**If stuck:** A one-hot vector is not itself a digit. predict does not directly return the class index.

**Then:** wait for the actual output and necessary interpretation. Introduce the next cell only after verification.

### [M10] Inspect classification errors

**Explain before editing/running:** The complete test output is 10000×10. argmax(axis=1) chooses a class for each image. Confusion-matrix rows are true labels and columns are predictions. The code displays a wrong prediction if one exists.

**Current action only:** Run the cell. Interpret one matrix cell using its true label, predicted label and count.

**Required evidence:** One actual matrix cell or a misclassified image label pair, plus the full test error count.

**Acceptance criteria — do not recite as the answer before the student responds:** Correct row/column meaning and a concrete count. If no errors exist, a diagonal entry is sufficient; never demand a nonexistent error.

**If stuck:** A single prediction cannot replace full test evaluation. Do not use this test result to start a new model-selection search.

**Then:** wait for the actual output and necessary interpretation. Introduce the next cell only after verification.

### [A01] Synthetic transactions and labels

**Explain before editing/running:** As in the source notebook, generate 1000 normal and 50 shifted anomalous samples with five features. These are artificial numbers rather than real transaction fields. Label 0 means normal and 1 means anomalous; this simple dataset does not represent real bank fraud complexity.

**Current action only:** Run the cell. Report both class counts, the input shape and the anomaly label.

**Required evidence:** Class meanings, counts and input shape.

**Acceptance criteria — do not recite as the answer before the student responds:** 0: 1000 normal, 1: 50 anomalies; shape (1050, 5). The anomaly proportion is 50/1050, about 4.76% of all samples.

**If stuck:** Anomalies are 5% relative to the normal count, but about 4.76% relative to the full dataset.

**Then:** wait for the actual output and necessary interpretation. Introduce the next cell only after verification.

### [A02] Split before fitting a scaler

**Explain before editing/running:** Stratification preserves class proportions. These are still raw inputs: no scaler has been fitted to the full dataset. Select normal samples after splitting.

**Current action only:** Run the split. Send the three subset sizes and the class counts in the test set.

**Required evidence:** 630 / 210 / 210 and the test label counts.

**Acceptance criteria — do not recite as the answer before the student responds:** The test contains 200 normal samples and 10 anomalies. No data-derived preprocessing parameter has been fitted yet.

**If stuck:** With only ten test anomalies, changing a single detected anomaly changes recall by ten percentage points.

**Then:** wait for the actual output and necessary interpretation. Introduce the next cell only after verification.

### [A03] Normal training data and separate calibration

**Explain before editing/running:** Select normal rows using label 0. Split normal validation samples into one subset for early stopping and another for threshold calibration, so the threshold uses neither final test data nor the early-stopping subset.

**Current action only:** Create A_normal_train and A_normal_val from normal training and validation rows. Split A_normal_val equally into A_normal_stop and A_normal_cal using train_test_split with random_state=42. Print the three resulting shapes.

**Required evidence:** Your filtering code and the three shapes.

**Acceptance criteria — do not recite as the answer before the student responds:** (600, 5), (100, 5), (100, 5), using explicit label-0 selection. The mixed test set is unchanged.

**If stuck:** Casting labels directly to bool selects the 1s, which are anomalies here. Use an explicit comparison.

**Then:** wait for the actual output and necessary interpretation. Introduce the next cell only after verification.

### [A04] Learn the normal input scale

**Explain before editing/running:** Apply the same scaler to normal stopping, normal calibration and mixed test inputs. Scaled anomalies may exceed 1. Do not clip them: the deviation can carry information.

**Current action only:** Create A_scaler as a MinMaxScaler, then A_train_s, A_stop_s, A_cal_s and A_test_s. Fit only on A_normal_train. Print n_samples_seen_ and all four shapes.

**Required evidence:** Your code, the 600-sample fitting count and four shapes.

**Acceptance criteria — do not recite as the answer before the student responds:** Fit only on normal training data; shapes (600, 5), (100, 5), (100, 5), (210, 5). No new fitting on test data.

**If stuck:** The scaler must not learn from calibration or test data. New scaled values need not all stay inside 0–1.

**Then:** wait for the actual output and necessary interpretation. Introduce the next cell only after verification.

### [A05] Build an autoencoder with a bottleneck

**Explain before editing/running:** Reconstruct five features through a three-value middle layer. These artificial normal inputs are not intrinsically low-dimensional, so compression can also cause normal reconstruction error. Five sigmoid outputs match the normal training range 0–1 and cannot exactly reproduce inputs outside that range.

**Current action only:** Build A_model: 5 inputs → 16 ReLU → 3 linear → 16 ReLU → 5 sigmoid outputs. Compile with adam and mse, and show its summary.

**Required evidence:** Model code and the meaning of the five outputs and three-value middle layer.

**Acceptance criteria — do not recite as the answer before the student responds:** 5→16→3→16→5 with five sigmoid outputs, not one binary output. The model reconstructs inputs rather than learning class labels.

**If stuck:** The later error threshold creates the 0/1 decision. At this stage, the network outputs five numbers.

**Then:** wait for the actual output and necessary interpretation. Introduce the next cell only after verification.

### [A06] Train inputs to reconstruct themselves

**Explain before editing/running:** Normal training inputs also serve as targets. The stopping subset contains normal samples only. Calibration and test data are not passed to fit.

**Current action only:** Run training. Report the epoch count and explain why the first two fit arguments are the same array.

**Required evidence:** Completed epoch count and an explanation of input=target.

**Acceptance criteria — do not recite as the answer before the student responds:** The model learns normal reconstruction, not 0/1 targets.

**If stuck:** If class labels were used as targets, rebuild A05 and repeat A06. Do not continue with an incorrectly trained model.

**Then:** wait for the actual output and necessary interpretation. Introduce the next cell only after verification.

### [A07] One calibration error per sample

**Explain before editing/running:** Reconstruct the separate normal calibration samples. Average the five squared feature errors along each row to obtain one error per sample. A single whole-array average cannot support per-sample decisions.

**Current action only:** Use A_model.predict on A_cal_s to create A_cal_recon. Compute per-sample MSE as A_cal_errors with np.mean along the correct axis. Print both shapes and the first five errors.

**Required evidence:** Your code, reconstruction shape, error shape and axis explanation.

**Acceptance criteria — do not recite as the answer before the student responds:** (100, 5) reconstructions and (100,) finite, nonnegative errors. axis=1 averages the five features.

**If stuck:** Explain the axis using another small example with two samples and three features, then let the student correct their own line.

**Then:** wait for the actual output and necessary interpretation. Introduce the next cell only after verification.

### [A08] Fix the threshold before testing

**Explain before editing/running:** Choose the 97th percentile of normal calibration errors. This is a preselected teaching rule, not a guarantee of 3% false alarms on every future dataset. Mean plus two standard deviations is another possible heuristic, not a universal law.

**Current action only:** Create A_threshold using np.quantile at 0.97 on A_cal_errors. Print the threshold and calibration count. Explain why test errors are not used.

**Required evidence:** Your code, threshold, 100 calibration samples and the independence argument.

**Acceptance criteria — do not recite as the answer before the student responds:** np.quantile(A_cal_errors, 0.97), with a finite threshold fixed before test inspection.

**If stuck:** 97% is not an expected classification accuracy. Test data must not determine the threshold.

**Then:** wait for the actual output and necessary interpretation. Introduce the next cell only after verification.

### [A09] Mixed test decisions and metrics

**Explain before editing/running:** The 210 test samples contain both classes. An error larger than the fixed threshold produces decision 1. Use true labels only to evaluate the resulting decisions.

**Current action only:** Reconstruct A_test_s as A_test_recon, compute per-sample MSE as A_test_errors, and create integer 0/1 decisions A_pred using A_threshold. Print a classification_report with labels=[0, 1], target_names=["Normal", "Anomaly"] and zero_division=0.

**Required evidence:** Your code and the report, including precision and recall in the Anomaly row.

**Acceptance criteria — do not recite as the answer before the student responds:** 210 errors and decisions, correct > comparison and anomaly as positive class 1. Interpret the actual result even if no anomalies were detected.

**If stuck:** Precision concerns the reliability of alerts; recall concerns finding actual anomalies. Normal-class recall is not anomaly recall.

**Then:** wait for the actual output and necessary interpretation. Introduce the next cell only after verification.

### [A10] Error distributions and mistakes

**Explain before editing/running:** The confusion matrix summarizes correct and incorrect decisions. Histograms show reconstruction errors for the two true classes; the vertical line is the previously fixed threshold. Do not adjust it after inspecting the test.

**Current action only:** Run the cell. Send TN, FP, FN and TP, and interpret one false alarm or missed anomaly.

**Required evidence:** Four actual counts and their interpretation, with the threshold unchanged.

**Acceptance criteria — do not recite as the answer before the student responds:** Counts sum to 210; TN+FP=200 and FN+TP=10. If a particular error count is zero, interpreting that zero is acceptable.

**If stuck:** FP means an alert on a normal sample; FN means a real anomaly without an alert. Do not choose a new threshold from this test result.

**Then:** wait for the actual output and necessary interpretation. Introduce the next cell only after verification.

### [Z01] Save and conclude

**Explain before editing/running:** The three tasks use different targets and metrics. This summary collects results from your own runs. Save your completed notebook using Colab’s save or download options.

**Current action only:** Run the summary, send it to Inno, and save your completed notebook.

**Required evidence:** All three result groups and confirmation that the notebook was saved.

**Acceptance criteria — do not recite as the answer before the student responds:** Only genuinely completed runs may be recorded. Ask the three closing reflection questions one at a time afterwards.

**If stuck:** Identify omitted or blocked work explicitly. Do not claim full completion when a required part is missing.

**Then:** wait for the actual output and necessary interpretation. Introduce the next cell only after verification.
