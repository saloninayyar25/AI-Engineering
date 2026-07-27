# 📅 Progress Log

**Date:** Day 1 of AI Engineering Learning Journey

## What I Learned Today
- Watched *What is Self Attention | Transformers Part 2* (CampusX).
- Covered the evolution of text representation techniques in NLP:
  One-Hot Encoding → Bag of Words → TF-IDF → Word Embeddings → Self-Attention.
- Understood the core limitation of word embeddings (static, context-independent
  vectors causing the polysemy problem — e.g. "apple" fruit vs. company) and how
  self-attention solves it by producing contextual embeddings.
- Implemented OHE, BoW, and TF-IDF from scratch/with scikit-learn.
- Built a toy self-attention mechanism in NumPy to concretely verify that
  the same word gets different output vectors in different sentences.

## Time Spent
- ~23 minutes video (23:21) + hands-on coding practice

## What's Next
- Learn the full self-attention math in detail (Q, K, V projections,
  scaled dot-product, softmax) beyond this toy version.
- Explore multi-head attention and how it's used inside the full
  Transformer encoder/decoder blocks.
- Revisit open questions once Query/Key/Value math is covered properly.
