# ❓ Questions & Doubts

- Why exactly is self-attention *quadratic* in sequence length? Need to see the actual math (Q, K, V matrices) — coming in the next lecture.
- Bahdanau attention (2014) vs. Transformer self-attention (2017) — how exactly do they differ mechanically? Both are called "attention" but the Transformer version seems more general.
- If transformers are so compute-heavy, what are the current approaches to make attention cheaper (e.g. sparse attention, linear attention)? Worth a future deep-dive.
- How does the same architecture (self-attention over tokens) get adapted for images in Vision Transformers — what counts as a "token" for an image?
