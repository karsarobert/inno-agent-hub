# Concept guide — tutor

| Concept | Where it appears in the notebooks |
| --- | --- |
| Pre-trained word vector | W03 loads 100-dimensional GloVe vectors. W05 looks up the vector saved for a word. The notebook is named Word2Vec and does not train new word vectors. |
| Cosine similarity | Divide the dot product by the product of the vector norms. Two nonzero vectors pointing in the same direction have similarity 1 even if their lengths differ. In W08, identify the largest score. |
| Analogy and odd one out | Positive and negative word vectors form a search direction. `doesnt_match` identifies the word that fits the group least well in the loaded embedding space. These learned associations do not verify cultural or biographical claims. |
| Character vocabulary | `char2idx` maps from character to integer index, and `idx2char` reverses the mapping. Spaces, line breaks, and punctuation are vocabulary entries too. The two notebooks use separate embeddings. |
| Next character | The chunk `abcd` yields input `abc` and target `bcd`. This is why 101 consecutive characters produce two sequences of length 100. Shuffling changes the order of pairs. |
| Batch, time step, and character class | In T21, the input shape `(64, 100)` becomes `(64, 100, vocab_size)`. The GRU returns an output at every time step and the Dense layer scores each character class. |
| Logits and loss | A logit is a raw score. Sparse categorical cross-entropy compares integer target indices with raw scores when `from_logits=True`. Training loss alone does not measure generalization. |
| Stateful GRU | The GRU carries state across calls by batch position. Because the data is shuffled, this does not trace the book in order between training batches. The training model has batch size 64; the generation model has batch size 1. |
| Checkpoint | The callback saves weights each epoch. T33 looks for the most recent checkpoint; `None` means no checkpoint was found. T34 restores the learned weights into the new batch-size-one model. |
| Autoregressive sampling | The generator resets state at the start. The index sampled from the final time step becomes the next input. Generation can change recurrent state while leaving the weights fixed. |
