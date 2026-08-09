"""
Hands-on practice: One-Hot Encoding, Bag of Words, and TF-IDF
using scikit-learn on a tiny toy corpus.
"""

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

corpus = [
    "I ate an apple today",
    "Apple released a new iPhone",
    "I love eating a fresh apple",
]

print("Corpus:")
for doc in corpus:
    print(" -", doc)
print()

# --- 1. One-Hot Encoding (word-level, manual) ---
vocab = sorted(set(" ".join(corpus).lower().split()))
word_to_index = {w: i for i, w in enumerate(vocab)}

def one_hot(word):
    vec = np.zeros(len(vocab))
    vec[word_to_index[word.lower()]] = 1
    return vec

print("--- One-Hot Encoding ---")
print(f"Vocabulary size: {len(vocab)}")
print(f"One-hot vector for 'apple': {one_hot('apple')}")
print(f"One-hot vector for 'iphone': {one_hot('iphone')}")
print("Notice: these vectors share no information about similarity —")
print("they're just as different as any other unrelated pair of words.\n")

# --- 2. Bag of Words ---
count_vectorizer = CountVectorizer()
bow_matrix = count_vectorizer.fit_transform(corpus)

print("--- Bag of Words ---")
print("Feature names:", count_vectorizer.get_feature_names_out())
print("BoW matrix (rows = documents, cols = word counts):")
print(bow_matrix.toarray())
print()

# --- 3. TF-IDF ---
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)

print("--- TF-IDF ---")
print("Feature names:", tfidf_vectorizer.get_feature_names_out())
print("TF-IDF matrix (weighted scores, rounded to 2 decimals):")
print(np.round(tfidf_matrix.toarray(), 2))
print()
print("Notice how common words (e.g. 'a', 'an') get low weight while")
print("more distinctive words get higher weight — but there's still no")
print("sense of 'apple' meaning fruit vs. company in any of these three")
print("representations.")
