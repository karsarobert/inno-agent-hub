# Getting started · Practice 10

**Before running any code cell, configure the Colab GPU:** Runtime → Change runtime type → Hardware accelerator: GPU (for example T4) → Save. Changing runtime can discard uploaded files and variables, so do this first. Tell your tutor separately if you use local Jupyter. Then run the E01 check.

1. Extract the ZIP and open `PTE_DL10_EXPLAINABILITY_EN.ipynb` through Colab’s open/upload notebook option or in local Jupyter. Run code there and discuss it with Innoagent.
2. In Colab choose Runtime → Change runtime type → GPU → Save. E01 checks the actual device and stops if the GPU list is empty. Local CPU can work, but full image feature extraction is much slower.
3. Start the instructor’s English tutor:“I opened the practice 10 notebook; let’s start E01.” If already run, send environment/TF/GPU lines.
4. One current cell at a time. All code is complete and unchanged supplied code need not be returned. Send requested short output and interpretation. K01, C08, Z01 are discussions.
5. After extracting the course ZIP, keep innoagent/DL10_assets.zip on your computer. C01 uses this bundle without external sample-image downloads. When C01 opens the Colab upload button, select this one file; in local Jupyter place it in the notebook working directory. The assets files are then created automatically. This is not a submission. A01 separately downloads the source CSV and 239 MB dataset archive.

assets, dl10_data and dl10_results live in the notebook’s current working directory. F02 caches in dl10_results/feature_cache and explicitly distinguishes extraction from cache hits. Colab runtime changes can remove files and variables.

For download/quota problems, the instructor can pre-place the exact labels.csv and final_files.zip from the source notebook in dl10_data. This is startup preparation, not a final submission. A01 checks local hashes too. Do not treat another archive as the same data version.

For restarts use RECOVERY.md. Personal saving is optional; no submission, sharing link or proof of saving is requested.

For local setup the instructor may use requirements.txt; students are not asked to use terminals. Check the live Innoagent and Colab GPUinterfaces before class. The package does not create a remote tutor.
