# Lesson 5 — Homework
# Position Information in Transformers

## Objective

The goal of this homework is to understand:

- Why Transformers need positional information.
- How sinusoidal positional encoding works.
- How RoPE adds position information differently.
- How position information affects attention.

---

# Part 1 — Concept Questions

## Q1. Why does self-attention not understand word order?

### Answer:

Self-attention processes all tokens at the same time.

It can understand relationships between words but does not know:

- Which word came first.
- Which word came later.
- The distance between words.

Therefore, additional positional information is required.

---

# Q2. Explain the difference between word embedding and positional encoding.

### Answer:

Word embedding represents the meaning of a word.

Example:

```
cat → [0.2,0.5,0.8]
```

It tells the model:

"cat is an animal-related word."

Positional encoding represents the location of the word.

Example:

```
Position 1 → [0.4,0.7,0.1]
```

It tells the model:

"cat appears at this position."

Together:

```
Input Embedding

=

Word Meaning

+

Position Information
```

---

# Q3. Explain the original Transformer position pipeline.

### Answer:

The original Transformer uses:

```
Token IDs

↓

Word Embedding

+

Sinusoidal Positional Encoding

↓

Input Embedding

↓

Q,K,V

↓

Attention
```

---

# Q4. Why can't we simply give position numbers?

Example:

```
The = 0

cat = 1

drinks = 2

milk = 3
```

### Answer:

A single number does not provide enough information.

The model needs to understand:

- Relative distance.
- Position relationships.
- Long-range dependencies.

A position vector provides richer information.

---

# Q5. Why does sinusoidal encoding use sine and cosine?

### Answer:

Sine and cosine provide:

- Different patterns for different positions.
- Smooth changes between nearby positions.
- Different frequencies across dimensions.

This helps the model learn both short and long relationships.

---

# Part 2 — RoPE Questions

---

# Q6. What is the main idea behind RoPE?

### Answer:

RoPE (Rotary Positional Embeddings) does not add position vectors.

Instead:

It rotates Query and Key vectors based on token position.

```
Embedding

↓

Q,K,V

↓

Rotate Q,K using RoPE

↓

Attention
```

---

# Q7. Why does RoPE modify Query and Key but not Value?

### Answer:

Attention calculation:

```
Attention = Softmax(QKᵀ)V
```

The similarity between tokens is calculated using:

```
Q and K
```

Position affects token relationships, therefore RoPE is applied to Q and K.

---

# Q8. What information does RoPE add?

### Answer:

RoPE adds:

- Token position.
- Relative distance between tokens.
- Direction information through rotation.

---

# Q9. Compare Sinusoidal Encoding and RoPE.

### Answer:

| Sinusoidal | RoPE |
|---|---|
| Adds position vector | Rotates vectors |
| Applied before Q,K,V | Applied after Q,K,V |
| Changes input embedding | Changes Q,K |
| Original Transformer | Modern LLMs |

---

# Part 3 — Coding Homework

---

# Assignment 1 — Implement Sinusoidal Positional Encoding

File:

```
assignment1_positional_encoding.py
```

Requirements:

Create:

```python
positional_encoding()
```

The program should:

- Create sequence:

```
The cat drinks milk
```

- Create random embeddings.
- Generate positional encoding.
- Add:

```
Embedding + Position Encoding
```

- Print:

```
Word Embeddings

Position Encoding

Final Input Embeddings
```

Expected shape:

```
(4,8)
```

---

# Assignment 2 — Implement Simple RoPE

File:

```
assignment2_rope.py
```

Requirements:

Create:

```python
rotate_vector()
```

Input:

```
Vector = [1,2]
```

Apply rotation for:

```
Position 0

Position 1

Position 5

Position 10
```

Observe:

- Vector direction changes.
- Vector length remains the same.

---

# Part 4 — Thinking Exercise

## Q10. Why does GPT need RoPE if embeddings already contain meaning?

### Answer:

Embeddings contain semantic information.

Example:

```
cat embedding
```

tells the model:

"cat is an animal."

But it does not tell:

"cat appeared after The."

RoPE provides position information during attention.

---

# Q11. Where does RoPE happen in GPT?

### Answer:

Inside the attention layer.

Flow:

```
Embedding

↓

Q,K,V

↓

RoPE(Q,K)

↓

Attention

↓

Transformer Block
```

---

# Q12. Explain this sentence:

"Embeddings understand meaning, RoPE understands position."

### Answer:

Embedding answers:

```
What is this word?
```

RoPE helps answer:

```
Where is this word?
How far is it from another word?
```

Both are required for language understanding.

---

# Revision Checklist

Before moving to Lesson 7, make sure you can explain:

✅ Why Transformers need position information.

✅ Difference between embedding and positional encoding.

✅ Original Transformer positional encoding.

✅ Sinusoidal encoding formula idea.

✅ Why modern LLMs use RoPE.

✅ Difference between adding position and rotating vectors.

✅ Why RoPE applies to Q and K.

✅ Complete GPT input flow.

---

# Lesson 6 Completion

Completed:

✅ Position Information

✅ Sinusoidal Positional Encoding

✅ RoPE Understanding

✅ NumPy Implementation

Next Lesson:

# Lesson 7 — Layer Normalization

Topics:

- Why normalization is needed.
- Mean and variance.
- LayerNorm formula.
- Gamma and Beta parameters.
- Pre-LN vs Post-LN Transformer.
- NumPy implementation.