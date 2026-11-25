# Recover from an error or interruption

| Situation | What to do next |
| --- | --- |
| T00: `GPU: []` | In Colab, choose **Runtime → Change runtime type → GPU → Save**. Reconnect and rerun the active setup cell. If a GPU cannot be assigned, ask the instructor. This step remains blocked. |
| T00: wrong runtime or Keras version | Before running code in the second notebook, choose **2026.04** and GPU. If that runtime is unavailable, ask the instructor about a TensorFlow 2.19.x runtime. If TensorFlow or a different Keras backend was already used, warn about state loss, start a fresh session, and run T00 first. The Keras name should start with `tf_keras`. |
| W01–W02: package or import error | Ask for the active ID and the last one to three relevant error lines. If the installation requires a restart after replacing a package, reconnect and try the import again. Escalate repeated failures to the instructor. |
| W03–W04, T00 or T02: download error | Wait while the download is making progress. Retry once after an actual error. For repeated failures, ask the instructor to check the original source. Keep the specified package version, model, corpus, and URL. |
| T19, T30, or T36: Keras error | Ask for the exact cell and error. Verify the T00 output, especially the `tf_keras` module name. After recovering, rerun only the dependencies needed by the active step. Keep the original model code. |
| T32 is still running | Wait until epoch 30 has finished. Do not start a second training run or the following cell. After the run, ask the learner to compare the first and last loss. |
| T33: `None` | Confirm that T32 finished in the same runtime and that files exist in `training_checkpoints`. Continue to T34 only with an available checkpoint path. |
| T34 completes but warns about unmatched optimizer values | If there was no exception, the loaded model weights can be used for generation. This process does not restore the training run. For an exception or mismatched model weights, stay at T34. |
| Runtime state is lost | In the text generation notebook, rerun T00 first. Rerun the prerequisites for the current cell in order; keep understanding already checked. Each notebook uses a separate runtime. |
| Runtime state is lost but the completed run's checkpoint is still present | After T00, rebuild the required variables with T01–T06, T17–T18, T30, and T33. If T33 reports the correct checkpoint, continue at T34. This restores weights for generation. |
| Training was interrupted or a checkpoint is missing | A partial checkpoint does not complete T32. To train again, rerun the required data cells and build a new batch-size-64 model at T19 before the remaining training steps. A new runtime may not contain the old files. If there is no time to retrain, tell the instructor. |
