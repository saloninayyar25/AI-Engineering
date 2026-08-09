# 🧠 NLP Text Representations & Self-Attention

> Part of my **AI Engineering Learning Journey** — Day 1
> Source: CampusX — *What is Self Attention | Transformers Part 2*

## What I Learned

This lecture builds up, step by step, the different ways text has been
converted into numbers for machine learning — and why each method was
eventually replaced by a better one, ending with why self-attention was
needed.

### 1. Why NLP Needs Numerical Representations
Machine learning models only understand numbers, not raw text. So the
first job in any NLP pipeline is to convert words into some numerical
form. The techniques below are different attempts at doing this, each
solving a problem with the previous one — and introducing a new one.

### 2. One-Hot Encoding (OHE)
Represents each word as a vector of all zeros except a single `1` at the
index assigned to that word.
- **Advantage:** simple, easy to implement.
- **Problems:**
  - Vector size = vocabulary size → very high-dimensional and sparse for
    large vocabularies.
  - No notion of similarity between words — "apple" and "orange" are just
    as "different" as "apple" and "car" (all vectors are orthogonal).
  - No word order/context captured at all.

### 3. Bag of Words (BoW)
Represents a *document* as a vector of word counts (or presence/absence),
ignoring grammar and word order entirely.
- **Advantage:** captures word frequency in a document, easy to use for
  tasks like basic text classification.
- **Problems:**
  - Still no semantic meaning — frequency alone doesn't capture what a
    word *means*.
  - Loses word order (e.g. "not good" and "good not" look the same).
  - Common but unimportant words (like "the", "is") can dominate counts.

### 4. TF-IDF (Term Frequency – Inverse Document Frequency)
An improvement over plain BoW: instead of raw counts, it weighs each word
by how important it is to a document *relative to the whole corpus* —
words that appear in almost every document (like "the") get a lower
weight, rare-but-relevant words get a higher weight.
- **Advantage:** down-weights common uninformative words, so more
  discriminative words stand out.
- **Problems:**
  - Still doesn't capture semantic meaning between words.
  - Still a sparse, high-dimensional representation.
  - Still ignores word order/context.

### 5. Word Embeddings
Instead of sparse, hand-crafted vectors, word embeddings (e.g. Word2Vec,
GloVe) learn a **dense, low-dimensional vector** for each word from large
amounts of text, such that words used in similar contexts end up with
similar vectors.
- **Advantage:** captures semantic meaning — e.g. `king − man + woman ≈
  queen`, and similar words (like "happy" and "joyful") end up close
  together in the vector space.
- **The problem faced by word embeddings — static vectors:**
  Each word gets exactly **one fixed vector**, learned once from the
  training corpus and then reused everywhere. This causes a real problem
  with **polysemy** (words with multiple meanings): the word "apple" gets
  a single vector whether it's used to mean the *fruit* or the *tech
  company* — the model has no way to tell these apart at inference time,
  because the same static vector is looked up regardless of context.
  > This is often informally described as the vector ending up as a kind
  > of "average" of all the contexts the word appeared in during
  > training — which is a reasonable intuition, though the standard name
  > for this limitation is the **static / context-independent embedding
  > problem** (or polysemy problem).

### 6. Self-Attention — Solving the Static Embedding Problem
Self-attention (the core mechanism inside transformers) generates a
**contextual embedding** for each word: the final vector for a word is
computed by looking at (attending to) the *other words in the same
sentence*, so the same word can get **different vectors in different
contexts**.
- "Apple" in *"I ate an apple"* gets a vector pulled toward fruit-related
  words like "ate."
- "Apple" in *"Apple released a new iPhone"* gets a vector pulled toward
  tech-related words like "iPhone" and "released."
- This directly fixes the static-vector limitation of Word2Vec/GloVe —
  the same word can now carry different meanings depending on its
  sentence, because the representation is computed dynamically rather
  than looked up from a fixed table.

## Summary Table

| Method | Captures Semantics? | Context-Aware? | Dense? |
|---|---|---|---|
| One-Hot Encoding | ❌ | ❌ | ❌ (sparse) |
| Bag of Words | ❌ | ❌ | ❌ (sparse) |
| TF-IDF | ❌ (weighting only) | ❌ | ❌ (sparse) |
| Word Embeddings (Word2Vec/GloVe) | ✅ | ❌ (static) | ✅ |
| Self-Attention (Transformer embeddings) | ✅ | ✅ | ✅ |

---
📌 See `Notes.md` for quick revision bullets, `Code/` for hands-on
implementations of each method, `Questions.md` for open questions, and
`Progress.md` for today's log.
