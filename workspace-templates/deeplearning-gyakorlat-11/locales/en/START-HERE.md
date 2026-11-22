# Get started: Google Colab and InnoAgent

1. Extract the lab bundle. In Colab, use **File → Upload notebook** to open [PTE_DL11_W2V_COLAB_EN.ipynb](PTE_DL11_W2V_COLAB_EN.ipynb) from the `innoagent` folder.
2. **Before running any code:** choose **Runtime → Change runtime type → Hardware accelerator: GPU (for example T4) → Save**. Tell InnoAgent when you have done so. E01 then shows whether Colab can see a GPU.
3. InnoAgent gives you one cell's purpose and full code, followed by a short question for after the run. Find the matching label in Colab and run the existing cell. A short explanation or the requested output is enough. You do not need to paste the code or a full log into chat.
4. After the word-vector section, InnoAgent will switch to [PTE_DL11_text_generation_COLAB_EN.ipynb](PTE_DL11_text_generation_COLAB_EN.ipynb). Select GPU and runtime version **2026.04** in this notebook too. **Run T00 before all other cells.** The corpus is in Hungarian and the model trains for 30 epochs.
5. If a cell fails, tell InnoAgent the step ID and the last relevant error lines. Take the final quiz in InnoAgent. There is no notebook submission.
