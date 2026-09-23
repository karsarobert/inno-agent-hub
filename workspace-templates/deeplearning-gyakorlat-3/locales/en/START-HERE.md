# Getting started in Inno Agent

1. Open the unzipped folder as a separate workspace.
2. Start a new conversation: **Let's start the 3rd Deep Learning lab!**
3. Following Inno's guidance, open the `environment_check.py` file,
   and start it with the **Run** button.
4. If the check succeeds, continue the first task with the tutor.

You edit and save the file yourself, then start it with Run. There is no Colab,
notebook cell or mandatory terminal directory change. Run handles the path.
A new run starts from a new Python process and a new model, it does not continue the old one.

**If a Python package is missing, ask the instructor for help!** Show them the
last lines of the error and the interpreter path printed in the environment check.
Do not start installing packages yourself. For any other error, paste into Inno the last
lines of the error and the code part concerned.

While training, wait for the run summary; a silent run is not an error in itself.
Do not start parallel trainings. If the process stopped with an error,
do not treat the possibly created partial output as a finished result.

**After every new run, refresh the View folder / file list!** Then, in the
folder under `results` that was just printed, open the images. For example the
new `loss.png` appears after the refresh. Do not mix an image from an earlier run with the new one.
The final test does not create a loss curve; there we look at the decision figure and the matrix.

At the end of the lab Inno asks ten questions one by one, scores them,
then clearly signals the completion. You do not need to restore the code.


## Using the 1.2 edition

Unzip the corrected package into a new working folder, and start a new tutor conversation.
Keep your earlier work and results separately. The tutoring instruction belonging to the new
folder should be active; downloading the ZIP alone does not update the old preset.
In the new procedure the rate change 0.01 -> 0.001 is compulsory, and you write the reason
for the model choice in your own words. The tutor helps, but does not decide in advance instead of you.
The run folders get a short label (R1_baseline_lr0.01, R2_16n_lr0.01,
R3_50x2_lr0.01, R4_50x2_lr0.001); you enter this label into L03_04_final_evaluation.py, and you do not
need to copy a long folder name. Before the test the program prints whether the chosen
run has the lowest validation loss.
