# 📝 Notes — Introduction to Transformers

- Transformer = deep learning architecture for sequence data, uses **self-attention** instead of recurrence.
- Introduced in **"Attention Is All You Need"** (Vaswani et al., 2017, Google).
- Before transformers: RNNs / LSTMs processed tokens sequentially → slow, hard to parallelize, struggled with long-range dependencies.
- Seq2Seq (encoder-decoder RNN) models compressed the whole input into **one fixed-length vector** → information bottleneck on long sentences.
- **Bahdanau et al. (2014)** — "Neural Machine Translation by Jointly Learning to Align and Translate" — introduced attention to let the decoder focus on relevant input words at each step. Direct ancestor of self-attention.
- Core claim of the 2017 paper: recurrence isn't necessary — attention alone is enough.
- **Advantages:** parallel training, better long-range dependencies, transfer learning, scalability.
- **Disadvantages:** quadratic compute cost in attention, needs lots of data/compute, less interpretable.
- **Applications:** translation, chatbots, summarization, code generation (Codex), protein folding (AlphaFold), image generation (DALL·E 2).
- Same architecture generalizes across modalities → basis for multimodal AI (text, image, audio).
- Considered a unifying architecture across deep learning domains (vs. CNNs for vision, RNNs for text historically).

## Quick Timeline
1. RNN/LSTM Seq2Seq (bottleneck: fixed-length context vector)
2. Bahdanau Attention (2014) — fixes bottleneck
3. "Attention Is All You Need" (2017) — removes recurrence entirely, introduces Transformer
4. BERT, GPT and later models scale up the Transformer architecture
