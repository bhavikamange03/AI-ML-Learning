# Lesson 5 — Position Information in Transformers

## Overview

Transformers use self-attention to understand relationships between words.

However, self-attention does not naturally understand the order of words.

Example:

```
The cat drinks milk
```

and

```
Milk drinks cat The
```

contain the same words, but the meaning is different.

Therefore, Transformers need **position information**.

In this lesson, we learn how Transformers understand word order using:

1. Sinusoidal Positional Encoding
2. Rotary Positional Embeddings (RoPE)

---

# Learning Objectives

By the end of this lesson, you will understand:

- Why Transformers need positional information.
- Difference between word embeddings and position encoding.
- How the original Transformer added position information.
- How sinusoidal positional encoding works.
- Why modern LLMs use RoPE.
- How RoPE rotates Query and Key vectors.
- Why RoPE helps understand relative positions.
- Implement positional encoding using NumPy.
- Implement simplified RoPE using NumPy.

---

# Transformer Position Evolution

## Original Transformer (2017)

The original Transformer uses:

```
Token IDs

↓

Embedding

+

Positional Encoding

↓

Input Embedding

↓

Q,K,V

↓

Attention
```

Position information is added before attention.

---

## Modern LLMs

Models like:

- GPT-style models
- Llama
- Mistral
- Qwen

use:

```
RoPE
```

Pipeline:

```
Token IDs

↓

Embedding

↓

Q,K,V

↓

RoPE(Q,K)

↓

Attention
```

---

# Lesson Structure

## Part 1 — Why Position Information Is Needed

Topics:

- Self-attention limitation.
- Why Transformers do not know word order.
- Importance of sequence position.

Example:

```
Dog bites man

vs

Man bites dog
```

Same words.

Different meaning.

---

# Part 2 — Sinusoidal Positional Encoding

Topics:

- Original Transformer positional encoding.
- Sine and cosine functions.
- Position vectors.
- Adding position to embeddings.

Formula:

```
Input Embedding

=

Word Embedding

+

Position Encoding
```

Implementation:

```
assignment1_positional_encoding.py
```

---

# Part 3 — Rotary Positional Embeddings (RoPE)

Topics:

- Why modern LLMs use RoPE.
- Difference between adding and rotating.
- Applying rotation to Q and K.
- Relative position understanding.

Key idea:

```
RoPE does not add position vectors.

It rotates Query and Key vectors
based on token position.
```

---

# Part 4 — Coding Implementation

## Assignment 1

### Sinusoidal Positional Encoding

File:

```
assignment1_positional_encoding.py
```

### What it does:

- Creates random word embeddings.
- Generates positional encoding.
- Adds position information.
- Prints final Transformer input embeddings.

Flow:

```
Word Embedding

+

Position Encoding

↓

Input Embedding

↓

Q,K,V
```

---

## Assignment 2

### Simple RoPE Implementation

File:

```
assignment2_rope.py
```

### What it does:

- Creates a query vector.
- Applies rotation at different positions.
- Shows how vectors change.

Example:

Before:

```
Q = [1,2]
```

After RoPE:

```
Position 0 → [1,2]

Position 5 → rotated vector

Position 10 → rotated vector
```

The direction changes but magnitude stays the same.

---

# How to Run

## Requirements

Python 3.x

Install NumPy:

```bash
pip install numpy
```

---

# Run Assignment 1

Navigate to lesson folder:

```bash
cd lesson-06-position-information
```

Run:

```bash
python assignment1_positional_encoding.py
```

Expected output:

```
Word Embedding Shape:
(4,8)

Position Encoding Shape:
(4,8)

Input Embedding Shape:
(4,8)
```

---

# Run Assignment 2

Run:

```bash
python assignment2_rope.py
```

Expected output:

```
Original Query Vector:

[1 2]


Rotated Query Vectors:

Position 0
Position 1
Position 5
Position 10
```

---

# Important Concepts

## Embedding

Answers:

```
What is this word?
```

Example:

```
cat → animal related meaning
```

---

## Position Encoding

Answers:

```
Where is this word?
```

Example:

```
cat appears after "The"
```

---

## Attention

Answers:

```
Which words should this token focus on?
```

---

## RoPE

Answers:

```
How far are these tokens from each other?
```

---

# Interview Preparation

Important questions covered:

### Why do Transformers need positional encoding?

Because self-attention does not know token order.

---

### Difference between embeddings and positional encoding?

Embedding provides meaning.

Position encoding provides location.

---

### Why does RoPE modify Q and K?

Because attention calculates relationships using:

```
QKᵀ
```

---

### Difference between sinusoidal encoding and RoPE?

Sinusoidal:

```
Adds position vector to embeddings
```

RoPE:

```
Rotates Q and K vectors
```

---

# Files in This Lesson

```
lesson-06-position-information/

│
├── README.md
│
├── notes.md
├── notes_part2.md
├── notes_part3.md
│
├── homework.md
├── interview_questions_answers.md
├── cheatsheet.md
│
├── assignment1_positional_encoding.py
└── assignment2_rope.py
```

---

# Lesson Completion Checklist

✅ Understand why Transformers need position information

✅ Understand sinusoidal positional encoding

✅ Understand RoPE intuition

✅ Understand why RoPE applies to Q and K

✅ Implement positional encoding using NumPy

✅ Implement simple RoPE rotation

✅ Explain position handling in GPT interviews

---

# Next Lesson

# Lesson 6 — Layer Normalization

Topics:

- Why normalization is needed.
- Mean and variance.
- LayerNorm formula.
- Gamma and Beta parameters.
- Pre-LN vs Post-LN Transformer.
- NumPy implementation.
