# Local setup – before class

The exercise is designed for **64-bit Linux x86-64, Python 3.12, CPU**. It does
not require Jupyter, Colab or a GPU.

## 1. Open the workspace

This material is already prepared as a workspace — there is nothing to extract.
Open it in Inno Agent (or in your file manager) and open a terminal **in the
workspace folder itself**; the lesson files sit directly in that folder.

```bash
pwd
ls
python3.12 --version
```

You should see these three lesson programs:

```text
G02_01_data_preparation.py
G02_02_model_and_compile.py
G02_03_fit_and_evaluate.py
```

## 2. Create and activate a virtual environment

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Do not use `sudo pip`. The `.venv` folder keeps the exercise packages separate
from the system Python installation.

## 3. Check the installation

```bash
python environment_check.py
```

A successful check ends with:

```text
Environment check successful. The exercise runs on CPU.
```

## 4. Run the lesson programs in order

```bash
python G02_01_data_preparation.py
python G02_02_model_and_compile.py
python G02_03_fit_and_evaluate.py
```

The third program trains a small network and creates a new `results/...` folder.
It saves a PNG learning curve there.

## 5. Open the visualizer

Open `visualizer.html` in a browser. No web server or internet connection is
required.

## Important classroom rule

Some code is present only to support the demonstration. In particular, students
do **not** need to understand every line of the plotting code. The lesson focuses
on the neural-network pipeline:

**data → preprocessing → network → compile → fit → validation**.
