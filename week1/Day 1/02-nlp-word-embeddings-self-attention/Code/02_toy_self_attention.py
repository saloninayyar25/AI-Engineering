"""
Toy self-attention implementation (pure NumPy) to demonstrate the core
idea: the SAME word ("apple") gets a DIFFERENT output vector depending
on the sentence it's in — unlike static word embeddings, which would
give it the exact same vector every time.

This is a simplified, from-scratch version of scaled dot-product
attention: Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V
"""

import numpy as np

np.random.seed(0)

d_model = 4  # embedding dimension (kept small for readability)

# Static "word embedding" table (like Word2Vec/GloVe would give) —
# ONE fixed vector per word, regardless of context.
vocab = ["i", "ate", "an", "apple", "released", "a", "new", "iphone"]
static_embeddings = {w: np.random.randn(d_model) for w in vocab}


def embed_sentence(words):
    """Look up static embeddings for each word in the sentence."""
    return np.stack([static_embeddings[w] for w in words])


def self_attention(X, seed=1):
    """
    Very small self-attention block.
    X: (seq_len, d_model) matrix of static input embeddings.
    Returns: (seq_len, d_model) matrix of CONTEXTUAL output embeddings.
    """
    rng = np.random.RandomState(seed)
    d_k = X.shape[1]

    # Learned projection matrices (random here, just to illustrate mechanics)
    W_q = rng.randn(d_model, d_k)
    W_k = rng.randn(d_model, d_k)
    W_v = rng.randn(d_model, d_k)

    Q = X @ W_q
    K = X @ W_k
    V = X @ W_v

    scores = Q @ K.T / np.sqrt(d_k)          # raw attention scores
    weights = np.exp(scores) / np.exp(scores).sum(axis=1, keepdims=True)  # softmax
    output = weights @ V                      # weighted sum of values
    return output, weights


sentence_1 = "i ate an apple".split()
sentence_2 = "apple released a new iphone".split()

X1 = embed_sentence(sentence_1)
X2 = embed_sentence(sentence_2)

out1, weights1 = self_attention(X1, seed=42)
out2, weights2 = self_attention(X2, seed=42)

apple_idx_1 = sentence_1.index("apple")
apple_idx_2 = sentence_2.index("apple")

print("Sentence 1:", " ".join(sentence_1))
print("Sentence 2:", " ".join(sentence_2))
print()

print("Static embedding for 'apple' (identical in both sentences):")
print(static_embeddings["apple"].round(3))
print()

print("Contextual (self-attention output) vector for 'apple' in sentence 1:")
print(out1[apple_idx_1].round(3))
print()

print("Contextual (self-attention output) vector for 'apple' in sentence 2:")
print(out2[apple_idx_2].round(3))
print()

cos_sim = np.dot(out1[apple_idx_1], out2[apple_idx_2]) / (
    np.linalg.norm(out1[apple_idx_1]) * np.linalg.norm(out2[apple_idx_2])
)
print(f"Cosine similarity between the two contextual 'apple' vectors: {cos_sim:.3f}")
print("-> Even though the static embedding was identical in both cases,")
print("   self-attention produces DIFFERENT output vectors depending on")
print("   the surrounding words — this is exactly the fix for the static")
print("   / polysemy problem discussed in the notes.")
