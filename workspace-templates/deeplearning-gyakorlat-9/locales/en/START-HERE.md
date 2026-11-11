# Getting started · Practice 9

1. Extract the ZIP. Open `PTE_DL9_CNN_LAB_EN.ipynb` through Google Colab’s open/upload notebook option or in local Jupyter. Run code there and use Innoagent to discuss explanations and results.
2. In Colab choose Runtime → Change runtime type → GPU → Save. E01 checks the actual device and stops on GPU: []. Menu wording may vary. A local Jupyter CPU is also supported, with slower training.
3. Start the instructor-configured Innoagent for practice 9. Say: “I have opened the practice 9 notebook; let’s start E01.” If already run, send its environment/TF/GPU lines.
4. Run only the current cell. The tutor explains and asks about the code or actual output. All code is complete. Do not send unchanged supplied code back; send the requested short output and interpretation. For errors, send relevant code and final error lines.
5. Open `sources/deep_learning_masterclass_en.html` in a browser. For B01, select **1 Batch Normalization** and inspect section **1.1**. For R00, select **2 Skip Connections (ResNet)** and inspect section **2.2**. The English CONCEPT_GUIDE.md includes navigation and self-contained alternatives if the HTML or its external styling resources cannot load. Do not paste HTML into a Python cell. Z01 is a discussion.

Internet is needed for CIFAR-10: the archive is about 170 MB and its extracted cache needs more space. Keras caches data locally; run artifacts go in `dl9_results`. Colab restarts can remove local files; personal saving is optional. There is no notebook submission. The two CNNs each run 6 epochs; wait for active training to finish.

For local installation the instructor/technical environment may use requirements.txt; students are not asked to use a terminal. Reference environment: Python 3.12,TensorFlow 2.21.0 CPU. Other devices/versions may produce different numbers. A separate pre-class check on the live Innoagent platform and Colab GPU is recommended.
