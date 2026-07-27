# 📝 Notes — NLP Representations & Self-Attention

## One-Hot Encoding (OHE)
- One `1`, rest `0`s. Vector size = vocab size.
- ❌ High-dimensional, sparse, no similarity between words, no context.

## Bag of Words (BoW)
- Vector of word counts per document.
- ✅ Simple, captures frequency.
- ❌ No semantics, no word order, common words dominate.

## TF-IDF
- Weighs words by importance (frequency in doc, rarity across corpus).
- ✅ Downweights common words like "the", "is".
- ❌ Still no semantics, still sparse, still no word order.

## Word Embeddings (Word2Vec / GloVe)
- Dense, low-dimensional vectors learned from context.
- ✅ Captures semantic similarity (`king - man + woman ≈ queen`).
- ❌ **Static vectors** — one fixed vector per word regardless of context.
  → **Polysemy problem**: "apple" (fruit) and "apple" (company) get the
  *same* vector. Informally, the vector behaves like an "average" of all
  the contexts the word appeared in during training.
  Problem of word embedding - "Average meaning Problem" means same word will be given same vector even though means differnt things
  like bank (river bank) and bank(financal bank) both will have same vector here 
## Self-Attention
- Produces a **contextual embedding**: each word's final vector depends
  on the other words in the same sentence.
- Fixes the static-vector / polysemy problem — "apple" gets different
  vectors in "I ate an apple" vs. "Apple released a new iPhone."
- This is the core mechanism inside the Transformer architecture.

## One-Line Comparison
OHE/BoW/TF-IDF → sparse, no meaning.
Word Embeddings → dense, meaning, but static.
Self-Attention → dense, meaning, **and** context-aware.
