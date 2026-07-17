# Lesson 4 - Transformers Cheat Sheet

## 🎯 Goal

This cheat sheet is a quick revision guide for the key concepts of Transformers and GPT.

---

# 1. Why Transformers?

## Problems with RNNs

- Process words one at a time (sequential)
- Slow to train
- Hard to parallelize
- Struggle with long-range dependencies
- Suffer from vanishing gradients

## Transformer Advantages

- Processes all tokens in parallel
- Captures long-distance relationships
- Faster training
- Better scalability
- Foundation of modern LLMs (GPT, Llama, Gemini, Claude)

---

# 2. Transformer Pipeline

```
Input Text
      │
      ▼
Tokenizer
      │
      ▼
Token IDs
      │
      ▼
Embedding Lookup
      │
      ▼
Embedding Vectors
      │
      ▼
Transformer Blocks
      │
      ▼
Linear Layer
      │
      ▼
Vocabulary Logits
      │
      ▼
Softmax
      │
      ▼
Next Token
```

---

# 3. Self-Attention

Self-Attention allows each token to understand its relationship with every other token in the sentence.

Example:

```
The dog chased the ball because it was tired.
```

Attention helps determine:

```
it → dog
```

---

# 4. Query, Key, and Value (QKV)

Each embedding vector is projected into three new vectors:

```
Embedding
      │
      ├── Wq ─► Query (Q)
      ├── Wk ─► Key (K)
      └── Wv ─► Value (V)
```

### Query (Q)

"What information am I looking for?"

### Key (K)

"What information do I contain?"

### Value (V)

"The information passed to the next layer."

---

# 5. Attention Calculation

### Step 1

Calculate Attention Scores

```
Q × Kᵀ
```

---

### Step 2

Apply Softmax

```
Scores

↓

Softmax

↓

Attention Weights
```

Softmax converts raw scores into probabilities.

---

### Step 3

Generate Attention Output

```
Attention Weights × Value
```

Result:

Context-aware token representations.

---

# 6. Attention Score vs Attention Weight

| Attention Score | Attention Weight |
|-----------------|------------------|
| Raw similarity value | Normalized probability |
| Calculated using Q × Kᵀ | Produced by Softmax |
| Can be any real number | Values between 0 and 1 |
| Intermediate step | Used to weight Value vectors |

---

# 7. Multi-Head Attention

Instead of one attention mechanism, Transformers use multiple attention heads.

```
Input Embeddings
        │
        ├── Head 1
        ├── Head 2
        ├── Head 3
        └── Head 4
              │
              ▼
        Concatenate
              │
              ▼
      Linear Projection
```

Each head learns different relationships.

---

# 8. Transformer Block

```
Input
  │
  ▼
Multi-Head Attention
  │
  ▼
Residual Connection
  │
  ▼
Layer Normalization
  │
  ▼
Feed Forward Network
  │
  ▼
Residual Connection
  │
  ▼
Layer Normalization
  │
  ▼
Output
```

---

# 9. Residual Connection

Formula:

```
Output = Input + New Information
```

Purpose:

- Preserve information
- Improve gradient flow
- Enable deep Transformers

---

# 10. Layer Normalization

Purpose:

- Stabilize values
- Faster convergence
- Prevent exploding or shrinking activations
- Improve training stability

---

# 11. Feed Forward Network (FFN)

Processes each token independently after attention.

```
Linear
   │
Activation (GELU/ReLU)
   │
Linear
```

Purpose:

- Learn richer features
- Transform contextual representations

---

# 12. Decoder-Only Transformer

Original Transformer:

```
Encoder

+

Decoder
```

GPT:

```
Decoder Only
```

GPT generates text by predicting the next token.

---

# 13. Causal (Masked) Self-Attention

GPT cannot attend to future tokens.

```
          The  cat drank milk

The        ✓    ✗    ✗    ✗

cat        ✓    ✓    ✗    ✗

drank      ✓    ✓    ✓    ✗

milk       ✓    ✓    ✓    ✓
```

This ensures left-to-right text generation.

---

# 14. Training vs Inference

| Training | Inference |
|----------|-----------|
| Correct next token known | Correct next token unknown |
| Uses Teacher Forcing | Uses own predictions |
| Updates weights | Weights fixed |
| Uses backpropagation | No backpropagation |
| Goal: Learn | Goal: Generate |

---

# 15. Teacher Forcing

During training, the model always receives the correct previous token, even if it predicted incorrectly.

Benefits:

- Faster learning
- Stable training
- Better convergence

---

# 16. GPT Prediction Pipeline

```
User Prompt
      │
      ▼
Tokenizer
      │
      ▼
Token IDs
      │
      ▼
Embedding Lookup
      │
      ▼
Transformer Blocks
      │
      ▼
Vocabulary Logits
      │
      ▼
Softmax
      │
      ▼
Next Token
      │
      ▼
Repeat
```

---

# 17. Token Selection

## Greedy Decoding

Choose the highest-probability token.

Advantages:

- Fast
- Deterministic

Disadvantages:

- Less diverse output

---

## Sampling

Randomly sample according to token probabilities.

Advantages:

- More creative
- More varied responses

Disadvantages:

- Less predictable

---

# 18. Temperature

Controls randomness during generation.

### Low Temperature (e.g., 0.2)

- Predictable
- Focused
- Less creative

### High Temperature (e.g., 1.5)

- More diverse
- More creative
- Higher chance of unusual outputs

---

# 19. Key Formulas

## Query

```
Q = X × Wq
```

## Key

```
K = X × Wk
```

## Value

```
V = X × Wv
```

## Attention Scores

```
Q × Kᵀ
```

## Attention Weights

```
Softmax(Q × Kᵀ)
```

## Attention Output

```
Attention Weights × V
```

## Residual Connection

```
Output = Input + Layer Output
```

---

# ⭐ Interview Tips

Remember these points:

- GPT predicts **one token at a time**, not complete sentences.
- Token IDs are just integer identifiers; embeddings carry semantic meaning.
- Q, K, and V are created by multiplying embeddings with learned weight matrices.
- Attention Scores become Attention Weights after applying Softmax.
- Multi-Head Attention allows the model to learn multiple relationships in parallel.
- Residual Connections preserve information and improve gradient flow.
- Layer Normalization stabilizes training.
- The Feed Forward Network transforms each token independently after attention.
- GPT is a **Decoder-Only Transformer** that uses **Causal (Masked) Self-Attention**.
- During training, GPT uses **Teacher Forcing**; during inference, it relies on its own predictions.
- The response is generated by repeating **next-token prediction** until completion.