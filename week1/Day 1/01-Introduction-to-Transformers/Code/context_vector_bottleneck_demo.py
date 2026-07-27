"""
Toy demo: the "fixed-length context vector" bottleneck in old Seq2Seq
models, and how keeping ALL hidden states (the idea behind attention)
avoids losing information.

This is NOT a real RNN — it's a simplified illustration using random
vectors to represent "hidden states" per word, just to show the concept.
"""

import numpy as np

np.random.seed(42)

sentence = "the quick brown fox jumps over the lazy dog".split()
hidden_dim = 8

# Pretend each word produces a hidden state vector (as an RNN encoder would)
hidden_states = np.random.randn(len(sentence), hidden_dim)

print(f"Sentence: {' '.join(sentence)}")
print(f"Number of words: {len(sentence)}")
print(f"Each word's hidden state has dimension: {hidden_dim}\n")

# --- OLD APPROACH: compress everything into ONE fixed-length vector ---
# (e.g. taking the final hidden state, or averaging all of them)
fixed_context_vector = hidden_states.mean(axis=0)
print("Old Seq2Seq approach — single fixed-length context vector:")
print(fixed_context_vector.round(2))
print(f"-> Shape: {fixed_context_vector.shape} (same size no matter how long the sentence is)\n")

# Problem: information from individual words is now blended together.
# A 5-word sentence and a 50-word sentence both get squeezed into the
# SAME size vector -> long sentences lose more detail.

# --- ATTENTION-STYLE APPROACH: keep every hidden state available ---
print("Attention-style approach — keep ALL per-word hidden states:")
print(f"-> Shape: {hidden_states.shape} (grows with sentence length)")
print("Now the decoder can 'attend' to specific words instead of relying")
print("on one compressed summary — this is the core idea that motivated")
print("attention, and eventually the full Transformer architecture.")
