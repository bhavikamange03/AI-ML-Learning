# Lesson 5 — Part 1: Position Information in Transformers

## Learning Objectives

By the end of this lesson, you should understand:

- Why Transformers need position information.
- Why embeddings alone cannot represent word order.
- Why self-attention does not know the order of words.
- Why positional information is added **before** computing Q, K, and V.
- The difference between:
  - Word Embedding
  - Position Vector
  - Input Embedding

---

# The Problem

Consider these two sentences:

```
Dog bites man.
```

```
Man bites dog.
```

Both sentences contain exactly the same words.

Only the order changes.

However, their meanings are completely different.

A Transformer must understand this difference.

---

# What Does a Word Embedding Represent?

A word embedding represents the **meaning (semantic information)** of a word.

Example:

```
Dog   → [0.2, 0.8, ...]
Bites → [0.7, 0.1, ...]
Man   → [0.5, 0.6, ...]
```

A word embedding tells the model:

- What the word means.
- Which words have similar meanings.

A word embedding **does not** tell the model:

- Which word comes first.
- Which word comes last.
- The position of the word in the sentence.

---

# Why Doesn't Self-Attention Know the Order?

The self-attention formula is:

```
Attention(Q, K, V) = Softmax((Q × Kᵀ) / √dₖ) × V
```

Notice that the formula only uses:

- Query (Q)
- Key (K)
- Value (V)

There is **no position information** in this equation.

Therefore, self-attention alone cannot determine the order of words.

---

# The Solution

Before creating Q, K, and V, the Transformer adds positional information to every embedding.

The pipeline becomes:

```
Sentence
    │
    ▼
Tokenizer
    │
    ▼
Token IDs
    │
    ▼
Word Embedding
    │
    ▼
+ Position Vector
    │
    ▼
Input Embedding
    │
    ▼
Q, K, V
    │
    ▼
Self-Attention
```

This is the actual input pipeline used by Transformers.

---

# Input Embedding

The input embedding is calculated as:

```
Input Embedding = Word Embedding + Position Vector
```

Example:

Word embedding:

```
cat

[2, 5, 1]
```

Position vector (Position 2):

```
[10, 20, 30]
```

Input embedding:

```
[2,5,1]
+
[10,20,30]
=
[12,25,31]
```

This final vector is used to compute:

- Q
- K
- V

---

# Important Correction to Earlier Lessons

For simplicity, our previous lessons showed:

```
Embedding
    │
    ▼
Q
K
V
```

The complete Transformer pipeline is:

```
Embedding
      +
Position Vector
      │
      ▼
Input Embedding
      │
      ▼
Q
K
V
```

Whenever you see:

```
Q = Embedding × Wq
```

Mentally replace it with:

```
Q = (Embedding + Position Vector) × Wq
```

---

# Why Must Position Be Added Before Q, K, and V?

Suppose we add positional information **after** Q, K, and V are computed.

```
Embedding
    │
    ▼
Q, K, V
    │
    ▼
+ Position
```

This does **not** work because attention scores have already been calculated using Q and K.

If Q and K do not contain positional information, attention cannot learn the order of words.

Therefore, positional information must be added **before** creating Q, K, and V.

---

# Why Add Instead of Concatenate?

Suppose:

```
Embedding Size = 768
Position Size = 768
```

### If we concatenate

```
768 + 768 = 1536 dimensions
```

The model becomes much larger and slower.

### If we add

```
768 + 768
↓

768 dimensions
```

The embedding size remains unchanged.

This makes the Transformer much more efficient.

---

# Does the Transformer Separate Embedding and Position Again?

No.

After addition, the Transformer works with the combined vector.

Mathematically:

```
Q = (Embedding + Position) × Wq
```

Using the distributive property:

```
Q = Embedding × Wq + Position × Wq
```

This means:

- One part of Q comes from the word meaning.
- One part of Q comes from the positional information.

The model learns during training how to use both.

---

# Key Takeaways

- Word embeddings represent the meaning of words.
- Embeddings do **not** contain positional information.
- Self-attention does not know the order of words.
- Position information is added before creating Q, K, and V.
- The Transformer uses **Input Embeddings** (Word Embedding + Position Vector).
- Position vectors are added instead of concatenated to keep the embedding size unchanged.
- The model never separates the embedding and position again; it learns from the combined representation.

---

# Summary

```
Sentence
    │
    ▼
Tokenizer
    │
    ▼
Token IDs
    │
    ▼
Word Embedding
    │
    ▼
+ Position Vector
    │
    ▼
Input Embedding
    │
    ▼
Q = Input Embedding × Wq
K = Input Embedding × Wk
V = Input Embedding × Wv
    │
    ▼
Self-Attention
```

---

# Next Lesson

**Part 2 — Positional Encoding**

Topics:

- What is Positional Encoding?
- Sinusoidal Positional Encoding
- Why sine and cosine functions were used
- How every token receives a unique position vector

# Lesson 5 — Part 2: Positional Encoding (Sinusoidal)

## Learning Objectives

By the end of this lesson, you should understand:

- Why Transformers need positional encoding.
- How positional encoding gives position information to tokens.
- Why the original Transformer used sine and cosine functions.
- How sinusoidal positional encoding works.
- Difference between learned and fixed positional embeddings.
- Limitations of sinusoidal positional encoding.

---

# Recap: Why Do We Need Position Information?

Transformers use self-attention.

Self-attention can understand relationships between words:

```
The cat drinks milk
```

But attention does not know:

- Which word came first.
- Which word came after.
- The distance between words.

The attention formula:

```
Attention(Q,K,V)
=
Softmax((QKᵀ)/√dₖ)V
```

does not contain any position information.

Therefore, we need to provide position information separately.

---

# Complete Transformer Input Pipeline

The actual Transformer pipeline:

```
Token
  |
  ▼
Token ID
  |
  ▼
Word Embedding
  |
  +
Position Encoding
  |
  ▼
Input Embedding
  |
  ▼
Q, K, V
  |
  ▼
Self-Attention
```

The Transformer receives:

```
Input Embedding

=
Word Embedding + Position Encoding
```

---

# What Is Positional Encoding?

Positional encoding creates a unique vector for every token position.

Example:

Sentence:

```
The cat drinks milk
```

Positions:

```
The     → Position 0
cat     → Position 1
drinks  → Position 2
milk    → Position 3
```

Each position receives a vector:

```
Position 0:

[0.0, 1.0, 0.0, 1.0]


Position 1:

[0.84, 0.54, 0.01, 0.99]


Position 2:

[0.91,-0.41,0.02,0.98]
```

These vectors help the model identify token locations.

---

# Why Not Just Use Position Numbers?

A simple approach:

```
The     → 0
cat     → 1
drinks  → 2
milk    → 3
```

Problem:

A single number does not provide enough information.

The model needs to understand:

- Relative distance between tokens.
- Relationships between positions.
- Patterns across long sequences.

Example:

```
Position 5
```

does not tell the model:

- How far it is from position 1.
- Whether it is before or after another token.

---

# Sinusoidal Positional Encoding

The original Transformer paper introduced:

## Sinusoidal Positional Encoding

It uses:

- Sine functions
- Cosine functions

to generate position vectors.

Formula:

For even dimensions:

```
PE(pos,2i) = sin(pos / 10000^(2i/d))
```

For odd dimensions:

```
PE(pos,2i+1) = cos(pos / 10000^(2i/d))
```

Where:

```
pos = token position

i = embedding dimension index

d = embedding size
```

---

# Why Use Sine and Cosine?

Sine and cosine functions provide:

## 1. Smooth changes

Nearby positions have similar values.

Example:

```
Position 1
Position 2
Position 3
```

change gradually.

---

## 2. Different frequencies

Each dimension changes at a different speed.

Example:

Fast-changing dimensions:

```
0.1
0.8
0.2
0.9
```

Slow-changing dimensions:

```
0.01
0.02
0.03
0.04
```

Together they create a unique position pattern.

---

# Positional Encoding as a Fingerprint

Think of positional encoding like a barcode.

Each position has a unique pattern.

Example:

```
Position 0:

▮ ▯ ▮ ▯


Position 1:

▮ ▮ ▯ ▯


Position 2:

▯ ▮ ▮ ▯
```

The Transformer does not explicitly read:

```
This is position 2
```

Instead, it learns:

```
This vector pattern represents this location.
```

---

# Why Multiple Dimensions?

Suppose embedding size:

```
4 dimensions
```

A position vector contains:

```
[
dimension 1,
dimension 2,
dimension 3,
dimension 4
]
```

Each dimension uses a different sine/cosine frequency.

This allows the model to represent:

- Short distances.
- Long distances.
- Relative positions.

---

# Example

Sentence:

```
I love AI
```

Word embeddings:

```
I      → E1

love   → E2

AI     → E3
```

Position encodings:

```
I      → P0

love   → P1

AI     → P2
```

Input embeddings:

```
I:

E1 + P0


love:

E2 + P1


AI:

E3 + P2
```

Then:

```
Input Embedding

        ↓

Q, K, V

        ↓

Attention
```

Now attention understands:

```
love is between I and AI
```

---

# Is Sinusoidal Encoding Learned?

No.

Original Transformer uses a fixed mathematical formula.

The model does not learn:

```
Position 0 vector
Position 1 vector
Position 2 vector
```

Instead:

```
Position
   |
Mathematical Formula
   |
Position Vector
```

The same formula generates position vectors.

---

# Learned vs Fixed Position Embeddings

## Fixed Positional Encoding

Used in original Transformer:

```
Position
    |
Formula
    |
Vector
```

Advantages:

- No additional parameters.
- Can generalize to unseen positions.

---

## Learned Positional Embeddings

Some models use:

```
Position
    |
Neural Network learns
    |
Vector
```

Advantages:

- Can learn better patterns.

Disadvantages:

- Adds parameters.
- Limited to trained sequence length.

---

# Limitations of Sinusoidal Encoding

Sinusoidal encoding works well, but modern LLMs found some limitations:

- Very long context lengths are challenging.
- Position is added directly to embeddings.
- Less flexible for extremely large models.

Because of this, modern LLMs use:

```
RoPE
(Rotary Positional Embeddings)
```

Examples:

- GPT-style models
- Llama
- Mistral
- Qwen

---

# Key Takeaways

- Self-attention does not know token order.
- Positional encoding provides location information.
- Original Transformer uses sinusoidal encoding.
- Sinusoidal encoding uses sine and cosine functions.
- Each position gets a unique vector pattern.
- Positional encoding is added before Q, K, and V computation.
- Original sinusoidal encoding is fixed, not learned.
- Modern LLMs usually use RoPE instead.

---

# Complete Flow

```
Text

↓

Tokenizer

↓

Token IDs

↓

Word Embedding

↓

+

Positional Encoding

↓

Input Embedding

↓

Q = Input Embedding × Wq

K = Input Embedding × Wk

V = Input Embedding × Wv

↓

Self-Attention
```

---

# Next Part

##  Part 3: RoPE (Rotary Positional Embeddings)

Topics:

- Why modern LLMs moved beyond sinusoidal encoding.
- What rotation means in embeddings.
- How RoPE applies position information to Q and K.
- Why GPT/Llama models use RoPE.

# Part 3: RoPE (Rotary Positional Embeddings)

## Learning Objectives

By the end of this lesson, you should understand:

- Why modern LLMs moved beyond sinusoidal positional encoding.
- What RoPE (Rotary Positional Embeddings) is.
- The difference between adding position and rotating vectors.
- Why RoPE is applied to Query and Key vectors.
- How RoPE helps attention understand relative positions.
- Why GPT-style models use RoPE.

---

# Recap: Sinusoidal Positional Encoding

Original Transformer architecture:

```
Token

↓

Word Embedding

+

Position Encoding

↓

Input Embedding

↓

Q, K, V

↓

Attention
```

The position vector was added directly to the word embedding.

Example:

```
Word Embedding:

[0.2, 0.5, 0.8, 0.1]


Position Vector:

[0.3, 0.4, 0.1, 0.7]


Input:

[0.5, 0.9, 0.9, 0.8]
```

The Transformer receives this combined vector.

---

# Why Do We Need RoPE?

Sinusoidal encoding works well, but modern LLMs need:

- Very long context windows.
- Better understanding of token relationships.
- Better relative position understanding.

Examples:

```
Token 10

and

Token 10000
```

The model needs to understand their relationship.

Modern LLMs use:

```
RoPE

(Rotary Positional Embeddings)
```

---

# Main Idea of RoPE

RoPE does not add a position vector.

Instead:

> RoPE rotates Query and Key vectors based on their position.

The pipeline changes.

---

# Old Transformer

```
Embedding

+

Position Encoding

↓

Input Embedding

↓

Q,K,V

↓

Attention
```

---

# Modern LLM Pipeline

```
Token IDs

↓

Token Embedding

↓

Q,K,V Projection

↓

Apply RoPE to Q and K

↓

Attention
```

---

# What Does Rotation Mean?

A vector has:

- Length
- Direction


Example:

Before rotation:

```
[1,0]
```

After 90 degree rotation:

```
[0,1]
```

The direction changes, but the information is preserved.

---

# How RoPE Uses Rotation

The same word at different positions gets different rotations.

Example:

Word:

```
cat
```

Query vector:

```
Q = [1,2]
```

Position 0:

```
No rotation

Q0 = [1,2]
```

Position 5:

```
Rotate by position angle

Q5 = rotated vector
```

The word is the same, but the position changes the vector.

---

# Why Apply RoPE Only to Q and K?

Attention calculation:

```
Attention = Softmax(QKᵀ) × V
```

The relationship between tokens is calculated using:

```
Query

+

Key
```

Attention asks:

> How similar is this token to another token?

Position information is important during this comparison.

Therefore RoPE is applied to:

```
Q
K
```

Not usually:

```
V
```

---

# Rotation Formula

A 2D rotation:

```
x' = x cos(θ) - y sin(θ)

y' = x sin(θ) + y cos(θ)
```

Where:

```
θ = position-dependent rotation angle
```

Different positions create different rotations.

---

# Why Is Relative Position Important?

Attention compares:

```
Query at position i

with

Key at position j
```

RoPE makes the relationship depend on:

```
i - j
```

which represents the distance between tokens.

Example:

Sentence:

```
The cat drinks milk
```

Relationship:

```
cat → milk
```

The model learns:

```
Distance = 2 positions
```

This helps understand:

- Nearby words.
- Long-range relationships.
- Word dependencies.

---

# Sinusoidal vs RoPE

| Feature | Sinusoidal Encoding | RoPE |
|---|---|---|
| Used in | Original Transformer | Modern LLMs |
| Adds position vector | Yes | No |
| Applied to | Input embeddings | Q and K |
| Changes embeddings | Yes | No |
| Relative position understanding | Good | Better |
| Used by GPT/Llama | No | Yes |

---

# Complete Modern GPT Architecture Flow

```
Text

↓

Tokenizer

↓

Token IDs

↓

Token Embedding

↓

Create Q,K,V

↓

Apply RoPE(Q,K)

↓

Multi-Head Attention

↓

Feed Forward Network

↓

Transformer Block
```

---

# Why RoPE Is Important for AI Engineers

You usually will not implement RoPE when building:

- RAG applications.
- AI agents.
- LLM applications.

However, interviews often ask:

## Question:

How does GPT know token positions?

## Answer:

Modern GPT-style models use Rotary Positional Embeddings (RoPE). Instead of adding positional vectors to embeddings, RoPE rotates query and key vectors based on token positions. This allows attention to understand relative distances between tokens.

---

# Key Takeaways

- RoPE = Rotary Positional Embeddings.
- RoPE is used by modern LLMs.
- RoPE does not add position vectors.
- RoPE rotates Query and Key vectors.
- Rotation depends on token position.
- RoPE helps attention understand relative positions.
- RoPE keeps word embeddings cleaner.
- GPT, Llama, Mistral, and Qwen use RoPE.

---

# Comparison Summary

Original Transformer:

```
Embedding

+

Position Encoding

↓

Q,K,V

↓

Attention
```


Modern LLM:

```
Embedding

↓

Q,K,V

↓

RoPE(Q,K)

↓

Attention
```

---

# Next Part

## Part 4: Coding Implementation

Topics:

- Implement sinusoidal positional encoding using NumPy.
- Understand rotation mathematically.
- Implement simple RoPE intuition.
- Visualize position changes.