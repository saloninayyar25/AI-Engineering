# 🚀 Day 1 — AI Engineering Learning Journey

Today's focus: understanding **why Transformers exist** and **how self-attention
solves a real limitation of earlier NLP representations**.

## 📂 Structure

```
day-01-ai-engineering/
├── 01-introduction-to-transformers/
│   ├── README.md        → Explanation in my own words
│   ├── Notes.md          → Quick revision bullets
│   ├── Code/              → Small illustrative code
│   ├── Images/            → Diagrams (to be added)
│   ├── Questions.md      → Open doubts
│   └── Progress.md       → Today's log
│
└── 02-nlp-word-embeddings-self-attention/
    ├── README.md
    ├── Notes.md
    ├── Code/
    │   ├── 01_ohe_bow_tfidf.py
    │   └── 02_toy_self_attention.py
    ├── Images/
    │   └── nlp_representation_evolution.svg
    ├── Questions.md
    └── Progress.md
```

## 📺 Videos Covered
1. [Introduction to Transformers | Transformers Part 1](.) — CampusX (1:00:05)
2. [What is Self Attention | Transformers Part 2](.) — CampusX (23:21)

## 🎯 Key Takeaway of the Day
Transformers exist because RNN/LSTM-based Seq2Seq models bottlenecked all
information into one fixed-length vector. Self-attention — the mechanism at
the heart of transformers — also solves a separate, later problem: static
word embeddings (Word2Vec/GloVe) give a word the *same* vector no matter the
context, which breaks down for polysemous words like "apple" (fruit vs.
company). Self-attention produces **contextual embeddings** instead, fixing
this.
