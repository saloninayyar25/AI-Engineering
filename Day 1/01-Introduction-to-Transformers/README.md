# 🧠 Introduction to Transformers

> Part of my **AI Engineering Learning Journey** — Day 1
> Source: CampusX — *Transformers Part 1: Introduction*

## What I Learned

Transformers are the neural network architecture behind almost every modern
large language model (GPT, BERT, LLaMA, etc.). This lecture was a
high-level map of *why* they exist and *why* they matter, before going into
any math.

### 1. What is a Transformer?
A deep learning architecture introduced to process sequential data (like text)
without relying on recurrence (RNNs/LSTMs). It processes an entire sequence
in parallel using a mechanism called **self-attention**, which lets every
word "look at" every other word in the sequence to build its representation.

### 2. History / Research Paper
Transformers were introduced in the 2017 paper **"Attention Is All You Need"**
by Vaswani et al. (Google). Before this, sequence modeling in NLP relied on
RNNs and LSTMs, which process tokens one at a time — this made training slow
and made it hard to capture long-range dependencies in a sentence.

### 3. Impact on NLP
Transformers removed the sequential bottleneck of RNNs/LSTMs:
- Enabled full parallelization during training → much faster training on GPUs/TPUs.
- Captured long-range dependencies better than RNNs/LSTMs.
- Became the foundation of essentially all modern NLP systems.

### 4. Democratizing AI
Because transformers are so effective and reusable (pre-train once,
fine-tune for many tasks), they lowered the barrier for building powerful
NLP applications — enabling smaller teams and individuals to build on top
of huge pre-trained models instead of training from scratch.

### 5. Multimodal Capability
The same core architecture (attention over a sequence of tokens) generalizes
beyond text: images (Vision Transformers), audio, and combinations of
modalities (text+image, e.g. CLIP, DALL·E). This is why transformers became
the backbone of multimodal AI, not just language models.

### 6. Acceleration of Generative AI
Transformers are the core architecture behind generative models like GPT.
Their ability to scale well with more data and compute directly fueled the
current generative AI boom.

### 7. Unification of Deep Learning
Before transformers, different domains (vision, text, speech) largely used
different specialized architectures (CNNs for images, RNNs for text). The
transformer became a common architecture across domains — a step toward a
more unified approach to deep learning.

### 8. Why Were Transformers Created? — Seq-to-Seq Learning
Earlier sequence-to-sequence (Seq2Seq) models used an encoder-decoder RNN
setup for tasks like translation. Their key limitation: the encoder had to
compress an entire input sentence into a **single fixed-length context
vector**, which lost information — especially on long sentences.

### 9. Neural Machine Translation by Jointly Learning to Align and Translate
This 2014 paper (Bahdanau et al.) introduced the **attention mechanism** as
a fix for the fixed-length context vector problem — letting the decoder
"attend" to different parts of the input sentence at each decoding step,
instead of relying on one compressed vector. This idea is the direct
ancestor of the self-attention used inside transformers.

### 10. "Attention Is All You Need"
This paper's key claim: you don't need recurrence (RNN/LSTM) at all —
attention alone is sufficient to build a state-of-the-art sequence model.
This is where the Transformer architecture was formally introduced.

### 11. Timeline, Advantages, and Real-World Applications
- **Advantages:** parallelization, better long-range dependency handling,
  transfer learning via pre-training, scalability with data/compute.
- **Real-world applications:** machine translation, chatbots, search,
  summarization, code generation, protein structure prediction, image
  generation, and more.
- **Notable transformer-based systems mentioned:** DALL·E 2, AlphaFold
  (Google DeepMind), OpenAI Codex.

### 12. Disadvantages of Transformers
- Computationally expensive (quadratic cost in self-attention with respect
  to sequence length).
- Require large amounts of data and compute to train from scratch.
- Less interpretable ("black box").

### 13. The Future of Transformers
Continued scaling, efficiency improvements (e.g. sparse/linear attention
variants), and expansion into more modalities and agentic use cases.

## Why This Matters for AI Engineering
This lecture is the "why" before the "how." Before diving into the math of
self-attention (Day 1, Video 2), it's important to understand the historical
gap transformers filled (RNN bottlenecks) and why the field converged on
this architecture.

---
📌 See `Notes.md` for quick revision bullets, `Questions.md` for open
questions, and `Progress.md` for today's log.
