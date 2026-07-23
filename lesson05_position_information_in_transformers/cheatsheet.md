# Lesson 5 — Position Information in Transformers
# Cheat Sheet

---

# Why Do Transformers Need Position?

## Problem:

Self-attention sees all tokens together.

Example:

```
The cat drinks milk
```

and

```
Milk drinks cat The
```

have the same words but different meanings.

Attention understands:

✅ Word relationships

But does not understand:

❌ Word order

Solution:

```
Add Position Information
```

---

# Word Embedding vs Position Encoding

## Word Embedding

Answers:

```
What does this word mean?
```

Example:

```
cat

↓

[0.2,0.5,0.8]
```

Contains:

- Semantic meaning
- Word relationships

---

## Positional Encoding

Answers:

```
Where is this word?
```

Contains:

- Token position
- Order information

---

# Original Transformer Position Flow

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

---

# Sinusoidal Positional Encoding

Used in:

```
Original Transformer (2017)
```

Formula:

```
PE(pos,2i) = sin(pos / 10000^(2i/d))

PE(pos,2i+1) = cos(pos / 10000^(2i/d))
```

---

# Why Sine and Cosine?

They provide:

✅ Unique position patterns

✅ Smooth changes between positions

✅ Different frequencies

This helps the model understand:

- Short distance relationships
- Long distance relationships

---

# Sinusoidal Encoding Example

Sentence:

```
The cat drinks milk
```

Positions:

```
The     → 0

cat     → 1

drinks  → 2

milk    → 3
```

Each position gets a vector.

Example:

```
Position 0:

[0.0,1.0,0.0,1.0]


Position 1:

[0.84,0.54,...]
```

---

# Modern LLM Problem

Large models need:

- Longer context
- Better relative position understanding

Examples:

```
Token 10

and

Token 10000
```

The model needs to understand their relationship.

Solution:

```
RoPE
```

---

# RoPE

## Full Form:

```
Rotary Positional Embeddings
```

Used by:

- GPT-style models
- Llama
- Mistral
- Qwen

---

# Main Idea of RoPE

RoPE does NOT add position vectors.

Instead:

```
Rotate Query and Key vectors
based on token position
```

---

# RoPE Pipeline

```
Token IDs

↓

Token Embedding

↓

Create Q,K,V

↓

Apply RoPE(Q,K)

↓

Attention

↓

Transformer Block
```

---

# Sinusoidal vs RoPE

| | Sinusoidal | RoPE |
|-|-|-|
| Method | Add position vector | Rotate vectors |
| Applied to | Embeddings | Q and K |
| Location | Before attention | Inside attention |
| Used by | Original Transformer | Modern LLMs |

---

# Why Rotate Vectors?

A vector has:

```
Magnitude

+

Direction
```

Rotation changes:

```
Direction
```

but keeps:

```
Magnitude
```

So the model receives position information without destroying meaning.

---

# Rotation Formula

For vector:

```
[x,y]
```

Rotation:

```
x' = x cosθ - y sinθ


y' = x sinθ + y cosθ
```

where:

```
θ = position-dependent angle
```

---

# Why Apply RoPE Only to Q and K?

Attention:

```
Attention = Softmax(QKᵀ)V
```

Token relationship depends on:

```
Query

+

Key
```

Therefore:

RoPE:

```
Q ✅

K ✅

V ❌
```

---

# Relative Position Understanding

Attention compares:

```
Token i

with

Token j
```

RoPE helps model understand:

```
distance = i - j
```

Example:

```
cat -------- drinks
```

The model learns their relative distance.

---

# Complete Modern GPT Flow

```
Text

↓

Tokenizer

↓

Token IDs

↓

Embedding

↓

Q,K,V

↓

RoPE(Q,K)

↓

Multi-Head Attention

↓

Feed Forward Network

↓

Transformer Block

↓

Next Token Prediction
```

---

# Interview One-Liners

## Why do Transformers need positional encoding?

```
Self-attention does not know token order,
so positional encoding provides sequence information.
```

---

## Difference between embedding and positional encoding?

```
Embedding provides word meaning.
Position encoding provides word location.
```

---

## Difference between sinusoidal and RoPE?

```
Sinusoidal adds position vectors to embeddings.

RoPE rotates Q and K vectors based on position.
```

---

## Why does RoPE modify Q and K?

```
Because attention calculates relationships using Q and K.
```

---

## How does GPT know positions?

```
Modern GPT models use RoPE, which injects
position information by rotating query and key vectors.
```

---

# Remember This

```
Embedding = Meaning

Position Encoding = Order

Attention = Relationship

RoPE = Relative Position Awareness
```

---

# Lesson 5 Final Architecture

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

# Lesson 5 Completed ✅

Topics Covered:

✅ Why position matters

✅ Sinusoidal positional encoding

✅ Learned vs fixed positions

✅ RoPE intuition

✅ RoPE mathematics

✅ NumPy implementation

✅ Interview preparation

Next:

# Lesson 7 — Layer Normalization