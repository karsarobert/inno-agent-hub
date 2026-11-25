# Deep Learning · Lab 11 — Tutor instructions

Internal tutor material. Present only the current step: purpose, full code, run in Colab, question, then wait. Keep the tutor check out of the initial prompt.

## W01 — Install Gensim

This cell asks pip to install Gensim. It may report that the requirement is already satisfied.

```python
pip install gensim
```

**Run the existing W01 cell. After it runs:** Does the cell install a library or train a model?

**Tutor check:** It installs a library. An already satisfied requirement is normal.

## W02 — Import the libraries

NumPy handles vector operations. The Gensim downloader will supply the pre-trained vectors. This cell can succeed without printing anything.

```python
import numpy as np
from gensim.models import KeyedVectors
import gensim.downloader as api
import gensim # generate similar rövidítése
# Gensim egy nyílt forráskódú Python-könyvtár témamodellezéshez, dokumentumfürtözéshez és más, nem felügyelt tanulási feladatokhoz
%matplotlib inline
```

**Run the existing W02 cell. After it runs:** Which library provides the downloader we import as api?

**Tutor check:** Gensim provides it through gensim.downloader.

## W03 — Load the GloVe embeddings

The Gensim downloader loads glove-wiki-gigaword-100 into word_vectors. The first download is about 128 MB; wait for it to finish.

```python
word_vectors = api.load("glove-wiki-gigaword-100")
```

**Run the existing W03 cell. After it runs:** Did your runtime train the vectors or load existing ones?

**Tutor check:** It loaded existing GloVe vectors. The notebook explores embeddings and does not train a Word2Vec model.

## W04 — List the available models

The call lists names from the downloader catalog. The vectors stored in word_vectors stay the same.

```python
print(list(gensim.downloader.info()['models'].keys()))
```

**Run the existing W04 cell. After it runs:** Does displaying the catalog download all the listed models?

**Tutor check:** No. It lists model names; we continue using the GloVe vectors already loaded.

## W05 — Look up word vectors

get_vector retrieves each named word's vector; len counts its components.

```python
apple = word_vectors.get_vector('apple')
pear  = word_vectors.get_vector('pear')
dog   = word_vectors.get_vector('dog')
hotel = word_vectors.get_vector('hotel')
motel = word_vectors.get_vector('motel')
bird = word_vectors.get_vector('bird')
len(apple), len(pear), len(dog)
```

**Run the existing W05 cell. After it runs:** What do the three lengths in your output have in common?

**Tutor check:** The vectors for apple, pear and dog each contain 100 components.

## W06 — Inspect a single vector

The last expression displays the numeric values looked up for apple.

```python
apple
```

**Run the existing W06 cell. After it runs:** Does one number represent another word or one component of the same word's vector?

**Tutor check:** It is one component of the vector for apple.

## W07 — Define cosine similarity

The function computes cosine similarity from a dot product and rounds to four decimal places. This cell defines the rule for later calls.

```python
def cosine_similarity(v1, v2):
    sim = np.dot(v1, v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))
    return np.round(sim, 4)
```

**Run the existing W07 cell. After it runs:** Which two quantities form the normalization term in the denominator?

**Tutor check:** The product of the two vector norms. This definition has no printed result.

## W08 — Compare two fruits and an animal

The same function is applied to three pairs. Colab displays the scores in the order of the calls.

```python
cosine_similarity(apple, pear), cosine_similarity(apple, dog), cosine_similarity(pear, dog),
```

**Run the existing W08 cell. After it runs:** Which pair is most similar in your output, and how can you tell?

**Tutor check:** In the reference run it was apple–pear. The largest score should justify the choice in the learner's output.

## W09 — Compare accommodation and other words

There are four calls, so match each returned score to its word pair by position.

```python
cosine_similarity(motel, hotel), cosine_similarity(motel, dog), cosine_similarity(hotel, dog), cosine_similarity(motel, apple)
```

**Run the existing W09 cell. After it runs:** Where is the motel–hotel score, and how does it compare with the others?

**Tutor check:** It is first and was the largest in the reference run. Relate the position in the tuple to the call.

## W10 — Label the similarity scores

The print calls put the word pair beside each score from the fruit example.

```python
print('apple-pear:', cosine_similarity(apple, pear))
print('apple-dog:', cosine_similarity(apple, dog))
print('pear-dog:', cosine_similarity(pear, dog))
```

**Run the existing W10 cell. After it runs:** What makes this output easier to read than the earlier tuple?

**Tutor check:** Each value has the name of its pair next to it.

## W11 — Compare difference vectors

The function compares the directions of two vector differences: king−queen and man−woman.

```python
cosine_similarity(word_vectors.get_vector('king')-word_vectors.get_vector('queen'),
                  word_vectors.get_vector('man')-word_vectors.get_vector('woman'))
```

**Run the existing W11 cell. After it runs:** How does this differ from measuring the similarity between king and queen directly?

**Tutor check:** The inputs are two differences, each formed from a pair, rather than the two original word vectors.

## W12 — King − man + woman

most_similar combines positive and negative terms and returns five near matches with scores.

```python
word_vectors.most_similar(positive=['king', 'woman'], negative=['man'], topn=5)
```

**Run the existing W12 cell. After it runs:** What is the effect of negative=['man'] in this query?

**Tutor check:** That term contributes in the negative direction. The ranked results illustrate an analogy, not an exact equality.

## W13 — Transfer a singular-to-plural relation

The query adds the cats−cat direction to carrot, then retrieves five neighbors of the combined direction.

```python
word_vectors.most_similar(positive=['cats', 'carrot'], negative=['cat'], topn=5)
```

**Run the existing W13 cell. After it runs:** Which relationship is the query trying to transfer?

**Tutor check:** Singular to plural, from cat/cats to carrot.

## W14 — Find neighbors of Mozart

The query uses only the mozart vector. It looks for nearby vectors without an analogy equation.

```python
word_vectors.most_similar('mozart', topn=5)
```

**Run the existing W14 cell. After it runs:** Which returned word can you relate to Mozart, and why?

**Tutor check:** For example, Beethoven or Haydn is also a composer. Accept a plausible explanation based on the learner's actual output.

## W15 — The Messi–Mozart analogy

The query tries to transfer the occupation relationship from Messi to Mozart. Results reflect the model's vector space.

```python
word_vectors.most_similar(positive=['footballer', 'mozart'], negative=['messi'], topn=5)
```

**Run the existing W15 cell. After it runs:** Which visible result is closest to the occupation being looked for?

**Tutor check:** The reference result includes composer. Other actual returned results with a plausible interpretation can be accepted.

## W16 — Relate sushi to Italy

The query uses sushi and italy as positive terms and japan as a negative term. The scores reflect relations learned from the corpus.

```python
word_vectors.most_similar(positive=['sushi', 'italy'], negative=['japan'], topn=5)
```

**Run the existing W16 cell. After it runs:** Why is the first result insufficient to establish that a dish is Italian?

**Tutor check:** It reflects embedding similarity, not verified culinary or cultural facts.

## W17 — Relate sushi to Hungary

The new query replaces italy with hungary while leaving the other terms in place.

```python
word_vectors.most_similar(positive=['sushi', 'hungary'], negative=['japan'], topn=5)
```

**Run the existing W17 cell. After it runs:** What changed in your result list compared with the previous cell?

**Tutor check:** Any observable difference between the two outputs, such as a different top result.

## W18 — Find neighbors of goulash

This is a neighbor search from one word vector, with the function's default number of results.

```python
word_vectors.most_similar("goulash")
```

**Run the existing W18 cell. After it runs:** What makes this search different from the sushi and country example?

**Tutor check:** It uses one vector, goulash, with no vector analogy.

## W19 — Find the country that does not match

split breaks the string into words. doesnt_match looks for the word that fits the group least well in the embedding space.

```python
word_vectors.doesnt_match('germany hungary slovakia usa france italy'.split())
```

**Run the existing W19 cell. After it runs:** Which word was picked, and how would you interpret the result?

**Tutor check:** The reference picked usa; the other countries in the list are European. Interpret the actual result.

## W20 — Find the name that does not match

This time the same method is applied to names. Associations learned from the corpus affect which name it selects.

```python
word_vectors.doesnt_match('einstein hawking darwin bohr curie tesla'.split())
```

**Run the existing W20 cell. After it runs:** What determines the person that the function picks?

**Tutor check:** The supplied group and the loaded embedding space. This is not an authoritative classification of scientists.

## W21 — Run the repeated cell

The same source appears twice in the notebook. Run this second cell too.

```python
word_vectors.doesnt_match('einstein hawking darwin bohr curie tesla'.split())
```

**Run the existing W21 cell. After it runs:** Why should it return the same name as the preceding cell?

**Tutor check:** It has the same inputs, vector space, and operation.

## W22 — Find the subject that does not match

The method now compares the named school subjects in the embedding space.

```python
word_vectors.doesnt_match('physics mathematics chemistry biology history'.split())
```

**Run the existing W22 cell. After it runs:** What does the returned subject tell you about the given group?

**Tutor check:** It fits the group least closely in the embedding space. In the reference it was history.

## W23 — Store the results

The query for the rupee–India–Japan analogy assigns its result to results.

```python
results = word_vectors.most_similar(positive=['rupee', 'japan'], negative=['india'])
```

**Run the existing W23 cell. After it runs:** Why can the cell succeed without displaying a list?

**Tutor check:** An assignment stores the list in results without displaying it.

## S01 — Switch to the text generation notebook

Open **PTE_DL11_text_generation_COLAB_EN.ipynb** in Google Colab. In **Runtime → Change runtime type**, select **GPU** and runtime version **2026.04**, then save. This notebook starts in a separate runtime. Ask the learner to confirm the setup. Wait for the reply before showing T00.

## T00 — Check TensorFlow, Keras and GPU

The original model needs the legacy Keras API. This setup cell selects it before the first TensorFlow import and reports the loaded environment.

```python
# T00 — Colab setup for the original legacy Keras model.
import os
import subprocess
import sys
from importlib.metadata import PackageNotFoundError, version

try:
    tf_version = version("tensorflow")
except PackageNotFoundError:
    tf_version = ""
if not tf_version.startswith("2.19."):
    raise RuntimeError("Colab: choose GPU and runtime version 2026.04 (TensorFlow 2.19), then rerun T00.")

try:
    legacy_version = version("tf-keras")
except PackageNotFoundError:
    legacy_version = None

if legacy_version != "2.19.0":
    subprocess.check_call([
        sys.executable, "-m", "pip", "install", "-q", "--no-deps", "tf-keras==2.19.0"
    ])

os.environ["TF_USE_LEGACY_KERAS"] = "1"
import tensorflow as tf

keras_backend = tf.keras.__name__
gpu_devices = tf.config.list_physical_devices("GPU")
print("TensorFlow:", tf.__version__)
print("Keras:", keras_backend)
print("GPU:", gpu_devices)
if not keras_backend.startswith("tf_keras"):
    raise RuntimeError("Legacy Keras was not loaded. Restart the Colab session and run T00 first.")
if not gpu_devices:
    raise RuntimeError("Colab: Runtime > Change runtime type > GPU > Save. Then rerun T00.")

```

**Run the existing T00 cell. After it runs:** What appeared on your TensorFlow:, Keras:, and GPU: lines?

**Tutor check:** TensorFlow 2.19.x, a module name starting with tf_keras, and a nonempty GPU list.

## T01 — Import TensorFlow and helper libraries

This cell imports TensorFlow and NumPy. The legacy Keras selection has already been made by the separate setup cell, before the first TensorFlow import.

```python
import tensorflow as tf

import numpy as np
import os
import time

import os
os.environ['TF_USE_LEGACY_KERAS']='1'
```

**Run the existing T01 cell. After it runs:** Is a model already being built in this cell?

**Tutor check:** No; it imports the libraries for the rest of the notebook.

## T02 — Download the corpus

The cell downloads the English Shakespeare corpus from the TensorFlow tutorial and saves the local file path in `path_to_file`.

```python
path_to_file = tf.keras.utils.get_file('shakespeare.txt', 'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
```

**Run the existing T02 cell. After it runs:** Which corpus does this notebook actually load?

**Tutor check:** It loads the English Shakespeare corpus, `shakespeare.txt`.

## T03 — Decode the text as UTF-8

The file is first read as bytes and then decoded to a Python string.

```python
# Read, then decode for py2 compat.
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
# length of text is the number of characters in it
print(f'Length of text: {len(text)} characters')
```

**Run the existing T03 cell. After it runs:** Does the printed length count bytes or characters?

**Tutor check:** It counts characters in the decoded string. A UTF-8 character can take more than one byte.

## T04 — Display the first 250 characters

The slice gives a small view of the corpus, including spaces, line breaks and punctuation.

```python
# Take a look at the first 250 characters in text
print(text[:250])
```

**Run the existing T04 cell. After it runs:** Will the model learn with words or individual characters as its basic units?

**Tutor check:** Individual characters, including spaces and punctuation.

## T05 — List the distinct characters

set removes repetitions and sorted puts the distinct characters into order.

```python
# The unique characters in the file
vocab = sorted(set(text))
print(f'{len(vocab)} unique characters')
```

**Run the existing T05 cell. After it runs:** Does the count describe the length of the entire book or the number of distinct characters?

**Tutor check:** It counts distinct characters; the Shakespeare corpus has 65.

## T06 — Map between characters and indices

char2idx maps a character to an integer; idx2char works in the other direction. The corpus becomes a sequence of integers in the original order.

```python
char2idx = {u:i for i, u in enumerate(vocab)}
idx2char = np.array(vocab)

text_as_int = np.array([char2idx[c] for c in text]) #szöveget pontosabban a karaktereket számokká konvertáljuk
```

**Run the existing T06 cell. After it runs:** Which variable helps turn a chosen index back into a character?

**Tutor check:** idx2char: the index is the position in that array.

## T07 — Inspect the index mapping

The loop prints the first 20 entries. repr gives a visible representation of characters such as a line break.

```python
print('{')
for char,_ in zip(char2idx, range(20)):
    print('  {:4s}: {:3d},'.format(repr(char), char2idx[char]))
print('  ...\n}')
```

**Run the existing T07 cell. After it runs:** What does repr help you see in this output?

**Tutor check:** It shows otherwise invisible characters through representations such as \n.

## T08 — Encode the first 13 characters

The output displays the beginning of the source text and its integer encoding side by side.

```python
print ('{} ---- characters mapped to int ---- > {}'.format(repr(text[:13]), text_as_int[:13]))
```

**Run the existing T08 cell. After it runs:** Why might an index appear more than once here?

**Tutor check:** The same character occurs at more than one position.

## T09 — Build a stream of single characters

from_tensor_slices makes a stream over the one-dimensional array. take(10) displays just ten items.

```python
seq_length = 100
examples_per_epoch = len(text)//(seq_length+1)


char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)

for i in char_dataset.take(10):
  print(idx2char[i.numpy()])
```

**Run the existing T09 cell. After it runs:** What does one dataset element contain at this stage?

**Tutor check:** One integer index representing a single character.

## T10 — Build chunks of 101 characters

batch groups 101 consecutive indices; drop_remainder drops a short final chunk.

```python
sequences = char_dataset.batch(seq_length+1, drop_remainder=True)

for item in sequences.take(5):
  print(repr(''.join(idx2char[item.numpy()])))
```

**Run the existing T10 cell. After it runs:** Why use 101 characters to make a training pair of length 100?

**Tutor check:** The shifted target needs one extra character for its last element.

## T11 — Split the input and target

The function omits the last character for the input and the first for the target. Each position pairs the current character with the next one.

```python
def split_input_target(chunk):
    input_text = chunk[:-1]
    target_text = chunk[1:]
    return input_text, target_text


```

**Run the existing T11 cell. After it runs:** For the chunk abc, what are the input and target?

**Tutor check:** The input is ab and the target is bc.

## T12 — Try the one-character shift

The cell applies the function to a character list for Tensorflow.

```python
split_input_target(list("Tensorflow"))
```

**Run the existing T12 cell. After it runs:** What target character is paired with the initial T?

**Tutor check:** e, which immediately follows T.

## T13 — Build training pairs for the whole dataset

map applies the splitting function to every chunk. The cell sets up the transformation without printing an example.

```python
dataset = sequences.map(split_input_target)
```

**Run the existing T13 cell. After it runs:** What is in each dataset element after this step?

**Tutor check:** One input sequence and one equally long target sequence shifted by one character.

## T14 — Inspect one input–target pair

The cell decodes the two index sequences to display the pair as readable text.

```python
for input_example, target_example in  dataset.take(1):
  print ('Input data: ', repr(''.join(idx2char[input_example.numpy()])))
  print ('Target data:', repr(''.join(idx2char[target_example.numpy()])))
```

**Run the existing T14 cell. After it runs:** What shift can you see between the two lines?

**Tutor check:** The target starts one character later in the original text.

## T15 — Match the first five time steps

zip pairs input and target indices at matching positions. The output shows both the numbers and the corresponding characters.

```python
for i, (input_idx, target_idx) in enumerate(zip(input_example[:5], target_example[:5])):
    print("Step {:4d}".format(i))
    print("  input: {} ({:s})".format(input_idx, repr(idx2char[input_idx])))
    print("  expected output: {} ({:s})".format(target_idx, repr(idx2char[target_idx])))
```

**Run the existing T15 cell. After it runs:** What do the first few input–expected output pairs confirm?

**Tutor check:** The target at each position is the next character in the source text.

## T16 — Shuffle and group 64 training pairs

shuffle operates on whole pairs; batch groups 64 pairs together. The character order within a pair stays intact.

```python
BATCH_SIZE = 64
BUFFER_SIZE = 10000
dataset = dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE, drop_remainder=True)

dataset
```

**Run the existing T16 cell. After it runs:** What does a training input of shape (64, 100) represent?

**Tutor check:** 64 sequences in each batch, with 100 character indices per sequence.

## T17 — Set three model dimensions

vocab_size describes the character vocabulary. embedding_dim is the size of one character vector, and rnn_units is the GRU state size.

```python
# Length of the vocabulary in StringLookup Layer
vocab_size = len(vocab)

# The embedding dimension
embedding_dim = 256

# Number of RNN units
rnn_units = 1024
```

**Run the existing T17 cell. After it runs:** Does 256 describe the vocabulary size or the embedding dimension?

**Tutor check:** The embedding dimension; len(vocab) supplies the vocabulary size.

## T18 — Define the Embedding, GRU and Dense model

Embedding retrieves a vector, GRU processes the sequence, and Dense returns raw scores (logits) for the character classes. This cell defines the function.

```python
def build_model(vocab_size, embedding_dim, rnn_units, batch_size):

    model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim,batch_input_shape=[batch_size, None]),
    tf.keras.layers.GRU(rnn_units,return_sequences=True,stateful=True,recurrent_initializer='glorot_uniform'),
    tf.keras.layers.Dense(vocab_size)
  ])
    return model

#Ez a kaggleről van
```

**Run the existing T18 cell. After it runs:** Which option makes the GRU return an output at every time step?

**Tutor check:** return_sequences=True.

## T19 — Build the training model

Calling build_model builds the model for batches of 64. The stateful GRU keeps state by batch position.

```python
model = build_model(vocab_size=vocab_size,
    embedding_dim=embedding_dim,
    rnn_units=rnn_units, batch_size=BATCH_SIZE)
```

**Run the existing T19 cell. After it runs:** Why must the model's batch size match the data pipeline?

**Tutor check:** The state has a fixed position for each item in the batch, so the shapes must match.

## T20 — Read the model summary

summary reports the layers, shapes and parameter counts.

```python
model.summary()
```

**Run the existing T20 cell. After it runs:** Which three layer types appear in the output?

**Tutor check:** Embedding, GRU and Dense.

## T21 — Try a forward pass on one batch

One batch passes through the model. The three output axes are batch, time and character class.

```python
for input_example_batch, target_example_batch in dataset.take(1):
  example_batch_predictions = model(input_example_batch)
  print(example_batch_predictions.shape, "# (batch_size, sequence_length, vocab_size)")
```

**Run the existing T21 cell. After it runs:** What does the last output dimension count?

**Tutor check:** The character classes scored at each time step: 65 for the Shakespeare corpus.

## T22 — Read the model summary again

This is the original second summary call, placed after the trial forward pass.

```python
model.summary()
```

**Run the existing T22 cell. After it runs:** Does calling summary again update the weights?

**Tutor check:** No. It displays the architecture and shapes.

## T23 — Sample from the trial output

The first sequence's logits are sampled once per time step. squeeze removes the extra axis of length one.

```python
sampled_indices = tf.random.categorical(example_batch_predictions[0], num_samples=1)
sampled_indices = tf.squeeze(sampled_indices,axis=-1).numpy()
```

**Run the existing T23 cell. After it runs:** Why can we call tf.random.categorical without applying softmax ourselves?

**Tutor check:** The sampling function accepts logits directly.

## T24 — Inspect the sampled indices

The cell displays the index array from the previous step.

```python
sampled_indices
```

**Run the existing T24 cell. After it runs:** What does one entry in the array represent?

**Tutor check:** The vocabulary index of one sampled next character at that time step.

## T25 — Decode the untrained model's sample

idx2char converts the indices to visible characters. The steps in this example still use the known input sequence.

```python
print("Input: \n", repr("".join(idx2char[input_example_batch[0]])))
print()
print("Next Char Predictions: \n", repr("".join(idx2char[sampled_indices ])))
```

**Run the existing T25 cell. After it runs:** Why should we not expect a meaningful sentence from this output yet?

**Tutor check:** The model weights have not been trained. This is a check that the shapes and decoding work.

## T26 — Set up the loss function

SparseCategoricalCrossentropy takes integer target indices. Inspect the argument passed to it.

```python
loss = tf.losses.SparseCategoricalCrossentropy(from_logits=True)
```

**Run the existing T26 cell. After it runs:** Which setting tells the loss to interpret the model output as raw scores?

**Tutor check:** from_logits=True.

## T27 — Inspect the initial mean loss

The loss compares the true character indices with the batch's predicted logits and prints a single mean value.

```python
example_batch_mean_loss = loss(target_example_batch, example_batch_predictions)
print("Prediction shape: ", example_batch_predictions.shape, " # (batch_size, sequence_length, vocab_size)")
print("Mean loss:        ", example_batch_mean_loss)
```

**Run the existing T27 cell. After it runs:** Does this value describe the model before or after training?

**Tutor check:** Before training. fit has not run yet.

## T28 — Exponentiate the mean loss

For an approximately uniform prediction, cross-entropy is near the natural log of the number of classes.

```python
tf.exp(example_batch_mean_loss).numpy()
```

**Run the existing T28 cell. After it runs:** What value is the exponentiated loss expected to be near at initialization?

**Tutor check:** The vocabulary size. This is an initial sanity check, not test accuracy.

## T29 — Compile the training model

compile sets the Adam optimizer and the loss function.

```python
model.compile(optimizer='adam', loss=loss)
```

**Run the existing T29 cell. After it runs:** Which later call starts the weight updates?

**Tutor check:** model.fit. Compile configures training without running it.

## T30 — Configure weight checkpoints

ModelCheckpoint is set to save weights locally after each epoch. Saving weights does not create a standalone model with its architecture.

```python
# Directory where the checkpoints will be saved
checkpoint_dir = './training_checkpoints'
# Name of the checkpoint files
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt_{epoch}")

checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_prefix,
    save_weights_only=True)
```

**Run the existing T30 cell. After it runs:** Has any checkpoint been created just by running this cell?

**Tutor check:** No. fit calls the callback while training.

## T31 — Set the epoch count

The executable cell sets EPOCHS to 30 and is the source for how long training runs.

```python
EPOCHS = 30
```

**Run the existing T31 cell. After it runs:** How many passes over the prepared training dataset does the original code request?

**Tutor check:** 30 epochs.

## T32 — Train the character model

One fit call runs all 30 epochs. Keep this runtime connected and wait for the final epoch.

```python
history = model.fit(dataset, epochs=EPOCHS, callbacks=[checkpoint_callback])
```

**Run the existing T32 cell. After it runs:** How did the training loss in your run change from the first epoch to the last?

**Tutor check:** Accept the comparison from their run. A training loss decrease alone does not establish generalization.

## T33 — Find the latest checkpoint

latest_checkpoint checks the local checkpoint directory in this runtime.

```python
tf.train.latest_checkpoint(checkpoint_dir)
```

**Run the existing T33 cell. After it runs:** What path did the cell return, and what does it point to?

**Tutor check:** The path is the prefix of the latest local checkpoint, for example the epoch 30 checkpoint. None blocks the next step.

## T34 — Rebuild with batch size one and restore the weights

The notebook builds a new model instance for generation and loads the weights. model now refers to this new instance.

```python
model = build_model(vocab_size, embedding_dim, rnn_units, batch_size=1)

model.load_weights(tf.train.latest_checkpoint(checkpoint_dir))

model.build(tf.TensorShape([1, None]))
```

**Run the existing T34 cell. After it runs:** Why create the model with batch_size=1 before restoring the weights?

**Tutor check:** Generation follows one sequence, and the stateful GRU requires a fixed batch size.

## T35 — Define the generator

It converts the starting text to indices, resets the model state and samples from the last time step. The sampled index becomes the next input. The temperature is 1.0.

```python
def generate_text(model, start_string):

    num_generate = 1000
    input_eval = [char2idx[s] for s in start_string]
    input_eval = tf.expand_dims(input_eval, 0)


    text_generated = []

    temperature = 1.0

    model.reset_states()
    for i in range(num_generate):
        predictions = model(input_eval)
        predictions = tf.squeeze(predictions, 0) #1-es dimenziókat eltávolítja
        predictions = predictions / temperature
        predicted_id = tf.random.categorical(predictions, num_samples=1)[-1,0].numpy()

        input_eval = tf.expand_dims([predicted_id], 0)

        text_generated.append(idx2char[predicted_id])

    return (start_string + ''.join(text_generated))
```

**Run the existing T35 cell. After it runs:** What will the next iteration feed directly into the model?

**Tutor check:** The index of the character sampled in the previous iteration. State can change; weights are not updated.

## T36 — Generate text from the ROMEO: prefix

The call prints the prefix and 1,000 generated characters. Sampling means that runs can produce different text. The model generates text from the English Shakespeare corpus.

```python
print(generate_text(model, start_string=u"ROMEO:"))
```

**Run the existing T36 cell. After it runs:** Which recognizable pattern or visible flaw do you notice in your generated text?

**Tutor check:** A short example of punctuation, spacing, dialogue patterns, English-looking fragments or nonsense words is enough.

## T37 — Inspect one generation step

The cell encodes A as an input of shape (1, 1) and makes a prediction. text becomes a list for collecting characters. This cell does not reset the earlier GRU state.

```python
text =[]
input_eval = [char2idx[s] for s in 'A']
input_eval = tf.expand_dims(input_eval, 0)
predictions = model(input_eval)
```

**Run the existing T37 cell. After it runs:** Does this forward pass change the model's weights?

**Tutor check:** No. The recurrent state may change. There is no weight update.

## T38 — Remove the one-item batch axis

tf.squeeze(predictions, 0) removes the first axis of size one and keeps the time and character axes.

```python
predictions = tf.squeeze(predictions, 0)
```

**Run the existing T38 cell. After it runs:** Which axis disappears?

**Tutor check:** Axis 0, the batch axis.

## T39 — Inspect a single character score

predictions[0,1] looks up a score for one character class at the first time step.

```python
predictions[0,1]
```

**Run the existing T39 cell. After it runs:** Is this value necessarily a probability between zero and one?

**Tutor check:** No. It is a raw logit and may be outside that interval.

## T40 — Sample one character index

After sampling, [-1,0] selects the first sample from the final time step.

```python
predicted_id = tf.random.categorical(predictions, num_samples=1)[-1,0].numpy()
```

**Run the existing T40 cell. After it runs:** What does predicted_id store?

**Tutor check:** The integer vocabulary index of the sampled next character.

## T41 — Build the next input and collect the character

The index is wrapped as a (1, 1) input. idx2char recovers the character and append stores it in a list. Nothing is printed.

```python
input_eval = tf.expand_dims([predicted_id], 0)
text.append(idx2char[predicted_id])
```

**Run the existing T41 cell. After it runs:** Where is the sampled character stored if the cell displays nothing?

**Tutor check:** In the text list. input_eval holds the index formatted for a later model call.

## Z01 — Final quiz

What does api.load("glove-wiki-gigaword-100") do in this lab?

- **A.** Trains new vectors from the source corpus.
- **B.** Loads a pre-trained GloVe embedding space.
- **C.** Turns word vectors into character IDs.
- **D.** Lists every available model's name.

## Z02 — Final quiz

What does cosine similarity compare?

- **A.** The number of characters in the words.
- **B.** The difference between the vector lengths.
- **C.** The words' corpus frequencies.
- **D.** The directions of the two vectors.

## Z03 — Final quiz

What question does king − man + woman ask in the notebook?

- **A.** Which vocabulary vectors are closest to the analogy's combined direction?
- **B.** Which vector has the same length in components as king?
- **C.** Which word has a meaning exactly equal to queen mathematically?
- **D.** Which word occurs most often in the training corpus?

## Z04 — Final quiz

What does doesnt_match return?

- **A.** The grammatically incorrect word.
- **B.** The longest word.
- **C.** The word least aligned with the given group in the embedding space.
- **D.** The rarest word in the entire vocabulary.

## Z05 — Final quiz

What input–target pair does split_input_target make from abcd?

- **A.** Input abc, target bcd.
- **B.** Input abc, target abc.
- **C.** Input bcd, target abc.
- **D.** Input abcd, target d.

## Z06 — Final quiz

What does 65 represent in an output shape of (64, 100, 65)?

- **A.** Training batch size.
- **B.** The number of training epochs.
- **C.** The number of time steps per example.
- **D.** The number of character classes scored per time step.

## Z07 — Final quiz

Why is from_logits=True set?

- **A.** Targets are not represented by integer indices.
- **B.** The Dense layer produces raw scores.
- **C.** The model handles only one character class.
- **D.** The outputs are already normalized probabilities.

## Z08 — Final quiz

What does tf.train.latest_checkpoint return if it finds no checkpoint?

- **A.** The latest epoch number.
- **B.** The loss from the final epoch.
- **C.** None.
- **D.** The corpus filename.

## Z09 — Final quiz

Why rebuild the model with batch_size=1 for generation?

- **A.** The vocabulary contains just one character.
- **B.** The saved weights have to be trained again.
- **C.** We generate one sequence, and the stateful GRU has a fixed batch size.
- **D.** The GRU must be removed for generation.

## Z10 — Final quiz

What becomes the direct input to the next model call in the generation loop?

- **A.** The index of the character just sampled.
- **B.** The full training corpus.
- **C.** A fresh batch of 64 sequences.
- **D.** The previous epoch's loss.
