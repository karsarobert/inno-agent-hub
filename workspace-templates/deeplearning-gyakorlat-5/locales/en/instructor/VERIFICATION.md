# Verification — English version 1.1 — 2026-10-04

Environment: Linux x86-64, Python 3.12.14, NumPy 2.3.5, Matplotlib 3.10.8,
TensorFlow CPU 2.20.0, Keras 3.15.1. TensorFlow's visible GPU list is empty.

All 13 runs passed: environment check; G01 indices 0/3; G02 10/30 epochs and
optional bottleneck 16; G03 indices 0/3; G04 thresholds 0.04/0.025/0.06 and
edge cases 0/1. They were launched from a separate working directory. Each
created figures and a JSON summary, printed an English View-refresh reminder,
and produced no stderr warnings. Sequential test runs preserved the 10 → 30 order.

The 10- and 30-epoch models had identical initial weights. The 30-epoch outputs
were identical to the supplied reference in this environment. Every numeric
array and source-row identifier was unchanged from the Hungarian package after
renaming the archive keys. All 896 selected source rows were disjoint.
Reference threshold counts and undefined precision with no alerts were verified.
Invalid indices were rejected with understandable English messages.

Short folder numbering and preservation of previous contents were checked.
The own-run comparison selected the matching 10-epoch predecessor and did not
compare bottleneck 16 against bottleneck 8. English sample figures were regenerated
from the English programs; axis=1, precision/recall and comparison figures were
also visually inspected. No test-run view folders are included in the ZIP.

The two baseline training runs took approximately 7.2–9.2 seconds each,
including imports, evaluation and figure saving. Other machines may differ.
Detailed machine-readable results: verified_runs.json.

The ZIP was checked for corruption, correct root layout and default settings.
The extracted G03 also ran without TensorFlow; the environment check correctly
reported a partial environment in that case. Internal file references, English
text and the ten quiz questions were checked before packaging.

Live Innoagent conversations have not been tested in the application.
AGENT_TEST_CHECKLIST.md gives targeted pre-class checks. Python verification and
prompt review alone do not establish correct application message handling.
