# Lesson 5 — Interview Questions & Answers
# Position Information in Transformers

---

# Q1. Why do Transformers need positional information?

## Answer:

Transformers use self-attention, which processes all tokens in parallel.

Self-attention knows:

- Which words are related.
- How much attention one word should give to another word.

However, it does not know the order of words.

Example:

```
Dog bites man
```

and

```
Man bites dog
```

contain the same words, but the meaning is different.

Therefore, Transformers need positional information to understand token order.

---

# Q2. Why can't word embeddings alone represent position?

## Answer:

Word embeddings represent the meaning of words.

Example:

```
cat → [0.2,0.5,0.8]
dog → [0.3,0.6,0.7]
```

They tell the model:

- What a word means.
- Similarity between words.

They do not tell:

- Where the word appears.
- The order of words.

Therefore, positional information is added separately.

---

# Q3. Where is positional information added in a Transformer?

## Answer:

In the original Transformer:

```
Token Embedding

+

Positional Encoding

↓

Input Embedding

↓

Q,K,V

↓

Attention
```

Position information is added before calculating Query, Key, and Value.

---

# Q4. What happens if we do not add positional information?

## Answer:

The Transformer would treat the sentence as a collection of words without order.

Example:

```
I love AI
```

and

```
AI love I
```

would look very similar because attention only sees relationships between tokens.

The model would not understand sequence order.

---

# Q5. What is positional encoding?

## Answer:

Positional encoding is a method to give every token a unique representation of its position in a sequence.

It creates a position vector for each token and combines it with the word embedding.

Formula:

```
Input Embedding =
Word Embedding + Position Encoding
```

---

# Q6. What positional encoding method was used in the original Transformer?

## Answer:

The original Transformer used:

```
Sinusoidal Positional Encoding
```

It uses:

- Sine functions for even dimensions.
- Cosine functions for odd dimensions.

Formula:

```
PE(pos,2i)=sin(pos/10000^(2i/d))

PE(pos,2i+1)=cos(pos/10000^(2i/d))
```

---

# Q7. Why does the original Transformer use sine and cosine?

## Answer:

Sine and cosine functions provide:

1. Unique patterns for different positions.
2. Smooth changes between nearby positions.
3. Different frequencies across dimensions.

This allows the model to learn both:

- Short-distance relationships.
- Long-distance relationships.

---

# Q8. Is sinusoidal positional encoding learned during training?

## Answer:

No.

Sinusoidal positional encoding is fixed.

It is generated using a mathematical formula.

The model does not learn position vectors.

```
Position

↓

Mathematical Formula

↓

Position Vector
```

---

# Q9. What is the difference between learned positional embeddings and sinusoidal encoding?

## Answer:

### Sinusoidal Encoding

```
Position
   |
Formula
   |
Vector
```

- Fixed.
- No additional parameters.
- Used in original Transformer.


### Learned Position Embeddings

```
Position
   |
Neural Network
   |
Vector
```

- Learned during training.
- Adds parameters.
- Limited to trained sequence length.

---

# Q10. What is RoPE?

## Answer:

RoPE stands for:

```
Rotary Positional Embeddings
```

It is a modern positional encoding method used by many LLMs.

Examples:

- GPT-style models.
- Llama.
- Mistral.
- Qwen.

Instead of adding position vectors, RoPE rotates Query and Key vectors based on token position.

---

# Q11. What is the difference between sinusoidal encoding and RoPE?

## Answer:

| Sinusoidal | RoPE |
|-|-|
| Adds position vector | Rotates vectors |
| Applied before Q,K,V | Applied after Q,K,V |
| Modifies input embeddings | Modifies Q and K |
| Original Transformer | Modern LLMs |

---

# Q12. Why does RoPE rotate vectors?

## Answer:

A vector contains:

- Direction.
- Magnitude.

Rotation changes the direction but keeps the magnitude.

This allows position information to be added without changing the semantic strength of the vector.

---

# Q13. Why does RoPE apply only to Query and Key?

## Answer:

Attention calculation:

```
Attention = Softmax(QKᵀ)V
```

The relationship between tokens is calculated using:

```
Query + Key
```

Position affects how tokens compare with each other.

Therefore, RoPE is applied to:

```
Q
K
```

not usually:

```
V
```

---

# Q14. How does RoPE help with relative positions?

## Answer:

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

This helps the model understand:

- Nearby words.
- Long-distance relationships.

---

# Q15. Explain the modern GPT position pipeline.

## Answer:

Modern LLM pipeline:

```
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

# Q16. Does RoPE change the meaning of word embeddings?

## Answer:

No.

RoPE does not modify the original word embedding.

It modifies Query and Key representations used for attention.

The semantic information remains in the embedding.

---

# Q17. Why is relative position better than absolute position?

## Answer:

Absolute position tells:

```
This token is at position 100
```

Relative position tells:

```
This token is 5 positions away from another token
```

Language relationships often depend on distance.

Example:

```
The cat that was sitting outside drank milk
```

The relationship between:

```
cat → drank
```

depends on their distance.

---

# Q18. Which modern LLMs use RoPE?

## Answer:

Many modern LLMs use RoPE:

- Llama
- Mistral
- Qwen
- GPT-style models

---

# Q19. Where does RoPE appear inside a Transformer block?

## Answer:

RoPE appears inside the attention mechanism:

```
Input Embedding

↓

Q,K,V Projection

↓

RoPE(Q,K)

↓

Attention Calculation

↓

Attention Output
```

---

# Q20. Explain positional encoding in one interview answer.

## Answer:

Transformers use self-attention, which does not naturally understand token order. Positional encoding provides position information to tokens. The original Transformer used sinusoidal positional encoding by adding position vectors to embeddings. Modern LLMs use RoPE, which rotates query and key vectors based on token positions, allowing attention to understand relative positions between tokens.

---

# Coding Questions

---

# Q21. Implement sinusoidal positional encoding.

## Answer:

Steps:

1. Create position matrix.
2. Create dimension matrix.
3. Calculate angle rates.
4. Apply sine to even dimensions.
5. Apply cosine to odd dimensions.

---

# Q22. Implement simple RoPE rotation.

## Answer:

For a 2D vector:

```
x' = x cos(theta) - y sin(theta)

y' = x sin(theta) + y cos(theta)
```

The angle depends on token position.

---

# Key Interview Points To Remember

Remember these three lines:

```
Embeddings understand meaning.
```

```
Positional encoding provides order.
```

```
RoPE gives position information through Q,K rotation.
```

```
Original Transformer → Sinusoidal Encoding

Modern LLMs → RoPE
```