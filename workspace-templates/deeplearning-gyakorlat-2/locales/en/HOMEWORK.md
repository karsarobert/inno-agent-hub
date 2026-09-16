# Homework – explain the pipeline, then make one controlled change

Use `G02_03_fit_and_evaluate.py`.

## Part A – explain the program

In your own words, describe the role of each step:

1. CSV loading;
2. separating features and target;
3. training/validation/test split;
4. scaling;
5. network architecture;
6. `compile()`;
7. `fit()`;
8. `history` and the learning curve.

The goal is not to reproduce library documentation. Explain the **data flow**.

## Part B – one small experiment

Run the original program once. Then change:

```python
EPOCHS = 15
```

Run it again and compare the two learning curves.

Answer:

- Did the shorter run finish with a higher or lower validation MAE?
- What does changing the number of epochs change?
- What does it **not** change? For example, does it change the number of input
  features or the network architecture?

Do not add new layers, classification, dropout or batch normalization for this
homework.
