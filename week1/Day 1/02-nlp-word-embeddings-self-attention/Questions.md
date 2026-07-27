# ❓ Questions & Doubts

- In the toy self-attention code, the projection matrices (W_q, W_k, W_v) are random — in a real trained transformer, how do these get learned to actually separate meanings like "fruit apple" vs "company apple"?
- TF-IDF still doesn't capture semantics — is it ever used *alongside* embeddings in modern pipelines, or has it been fully replaced?
- How many self-attention "heads" (multi-head attention) does a real model like BERT use, and why is one head not enough in practice?
- The static embedding "average meaning" idea — is this mathematically accurate (i.e. is the Word2Vec vector literally an average of context vectors), or just a helpful intuition? Worth digging into Word2Vec's training objective (skip-gram / CBOW) to check precisely.
