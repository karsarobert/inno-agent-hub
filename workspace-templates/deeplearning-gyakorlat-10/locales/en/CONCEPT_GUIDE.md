# Concept guide

## Classification

conv5_block3_out:(batch, 7, 7, 2048); predictions kernel:(2048, 1000). One class’s weight column weights the activation channels. Bias is a separate constant rather than a spatial map. For direct GAP→Dense, mean(raw CAM)+bias equals the logit. Softmax uses all logits and is a different quantity.

Classic CAM is architecture-dependent weighted summation. Grad-CAM obtains channel weights from gradients; that is not computed here. A contribution map is neither a pixel mask nor causal proof. A common color scale supports numerical comparisons; independent normalization may emphasize a tiny score’s relative maximum.

Occlusion is fixed in advance:[64: 176, 64: 176], gray 127.5. Keep the original top 1 target rather than switching to a more favorable class afterward.

## Regression

The ResNet backbone is frozen and called with training=False. GAP produces 2048 values; the linear head trains 2048 weights+1 bias. Zero kernels and the training-median bias start at the baseline. No softmax or automatic uncertainty interval. MAE averages abs(prediction−label), in years. Negative signed error underestimates the label; positive error overestimates.

Age-label groups 0–19, 20–39, 40–59, 60+are fixed before evaluation. Read n together with errors; small groups are not population-level evidence. No automated purchase-eligibility decision follows.

X01 applies the learned regression weights to spatial features. Map mean+bias reconstructs prediction while retaining signs. This connects the same linear computation to another output rather than showing real ages of facial regions.

## Syntax support

- iter creates an iterator; next retrieves its next element, here a whole batch pair.
- argsort returns sort indices; [::-1]reverses; [: 5]takes five.
- get_layer selects by name; get_weights returns arrays, usually kernel and bias.
- tensordot(..., axes=([-1],[0]))pairs and sums the last activation and first weight axis.
- map applies the same transformation to Dataset items; batch groups them.
- GAP averages spatial axes and retains channels.
- preprocess_input is model-specific:raw RGB 255→BGR−ImageNet means here, not simple /255.
- shuffle changes head-training order; extraction and test order stay aligned.

## Interpretation rules

Actual output takes priority; no class, score decrease or target MAE is mandatory. Elephant/sunflower filenames are not verified ImageNet labels. The agent cannot automatically see images/results. Accept textual observations instead of inventing visual explanations. Every code cell is complete. Technical helpers are supplied infrastructure, not student implementation tasks. RECOVERY.md is technical support, not a new exam. No submission.
