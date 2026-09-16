"""Exercise 2 / Part 1: follow the data before it reaches the neural network.

Learning goal:
- understand what one row means,
- separate input features (X) from the target (y),
- split the data into training, validation and test sets,
- scale the inputs without leaking information from validation/test data.

This program DOES NOT build or train a neural network yet.
"""

from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

print("PART 1 – DATA PREPARATION")
print("Goal: follow one dataset from the CSV file to model-ready input arrays.\n")

RANDOM_SEED = 42
DATA_FILE = Path(__file__).resolve().parent / "data" / "red-wine.csv"

# -----------------------------------------------------------------------------
# 1. LOAD THE TABLE
# -----------------------------------------------------------------------------
# pd.read_csv reads the CSV file into a pandas DataFrame.
# A DataFrame is a table with rows and named columns.
raw_data = pd.read_csv(DATA_FILE)

print("1) RAW TABLE")
print("Rows and columns:", raw_data.shape)
print("Column names:")
print(list(raw_data.columns))
print()

# In this teaching example, exact duplicate rows are kept only once.
data = raw_data.drop_duplicates().reset_index(drop=True)

print("One example row:")
print(data.head(1).to_string(index=False))
print()
print("Meaning: one row = one wine sample.")
print("The measured properties are the inputs; 'quality' is the value we want to predict.\n")

# -----------------------------------------------------------------------------
# 2. SEPARATE INPUTS (X) AND TARGET (y)
# -----------------------------------------------------------------------------
# X contains the information the model is allowed to use.
# y contains the correct answer that the model should learn to predict.
features = data.drop(columns=["quality"])
target = data["quality"]

print("2) INPUTS AND TARGET")
print("X / features shape:", features.shape)
print("y / target shape:", target.shape)
print("Number of input features per wine:", features.shape[1])
print("Target column: quality")
print()

# -----------------------------------------------------------------------------
# 3. SPLIT THE DATA
# -----------------------------------------------------------------------------
# First we reserve 20% for the final test set.
# Then we split the remaining 80% into training and validation parts.
# Final proportions are approximately 60% training, 20% validation, 20% test.
train_pool, test_features, train_pool_target, test_target = train_test_split(
    features,
    target,
    test_size=0.20,
    random_state=RANDOM_SEED,
)

train_features, validation_features, train_target, validation_target = train_test_split(
    train_pool,
    train_pool_target,
    test_size=0.25,  # 25% of the remaining 80% = 20% of the full dataset
    random_state=RANDOM_SEED,
)

print("3) TRAINING / VALIDATION / TEST SPLIT")
print("Training samples:  ", len(train_features))
print("Validation samples:", len(validation_features))
print("Test samples:      ", len(test_features))
print()
print("Training data: used to update the network weights.")
print("Validation data: used to check learning during development.")
print("Test data: kept untouched for the final evaluation.")
print()

# -----------------------------------------------------------------------------
# 4. SCALE THE INPUT FEATURES
# -----------------------------------------------------------------------------
# Different columns have different numerical ranges.
# MinMaxScaler learns the minimum and maximum of every input column.
# IMPORTANT: it learns these values from the TRAINING DATA ONLY.
scaler = MinMaxScaler()

train_scaled = pd.DataFrame(
    scaler.fit_transform(train_features),
    columns=train_features.columns,
    index=train_features.index,
)
validation_scaled = pd.DataFrame(
    scaler.transform(validation_features),
    columns=validation_features.columns,
    index=validation_features.index,
)
test_scaled = pd.DataFrame(
    scaler.transform(test_features),
    columns=test_features.columns,
    index=test_features.index,
)

print("4) SCALING")
example_index = train_features.index[0]
columns_to_show = ["fixed acidity", "density", "alcohol"]
comparison = pd.DataFrame({
    "before scaling": train_features.loc[example_index, columns_to_show],
    "after scaling": train_scaled.loc[example_index, columns_to_show],
})
print("The same training sample before and after scaling:")
print(comparison.round(4).to_string())
print()
print("The scaler was FIT on training data only.")
print("The same learned transformation was then APPLIED to validation and test data.")
print()

# -----------------------------------------------------------------------------
# 5. FINAL SHAPES – THESE ARE THE OBJECTS THAT WILL REACH THE NETWORK
# -----------------------------------------------------------------------------
print("5) MODEL-READY DATA")
print("train_scaled shape:     ", train_scaled.shape)
print("train_target shape:     ", train_target.shape)
print("validation_scaled shape:", validation_scaled.shape)
print("validation_target shape:", validation_target.shape)
print("test_scaled shape:      ", test_scaled.shape)
print("test_target shape:      ", test_target.shape)
print()
print("DATA FLOW:")
print("CSV -> DataFrame -> X and y -> train/validation/test -> scaling -> neural network")
print("No neural network has been created or trained in this file.")
