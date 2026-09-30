"""Optional: jointly normalized probabilities from three scores."""
from helpers import np, plt, new_run_folder, save_data, save_figure, finished

logits = np.array([2.0, 1.0, 0.0])
common_shift = 0.0

# Subtracting the maximum does not change the softmax probabilities.
shifted_logits = logits + common_shift
exponentials = np.exp(shifted_logits - np.max(shifted_logits))
probabilities = exponentials / np.sum(exponentials)
print("Logits:", shifted_logits)
print("Probabilities:", np.round(probabilities, 6))
print("Sum:", np.sum(probabilities))
folder = new_run_folder(__file__)
save_data(folder, {"logits": logits.tolist(), "common_shift": common_shift},
               ["logit", "probability"], zip(shifted_logits, probabilities))
figure, t = plt.subplots()
t.bar([1, 2, 3], probabilities, color="#075ac8")
t.set(xlabel="Class number", ylabel="Estimated probability", ylim=(0, 1), xticks=[1, 2, 3])
save_figure(figure, folder, "softmax.png")
finished(folder)
