# Lesson 3 - Embeddings Cheat Sheet

## 🎯 Quick Revision Guide

Embeddings are one of the most important concepts in modern AI systems.

They are the foundation of:

- LLMs
- Semantic Search
- RAG Systems
- Vector Databases
- Recommendation Systems

---

# 1. What is an Embedding?

## Simple Definition

An embedding is a numerical representation of text where meaning is captured as a vector.

Example:

```
cat

↓

[0.82, -0.15, 0.63, 0.21]
```

The vector itself does not have human-readable meaning.

The relationship between vectors represents meaning.

---

# 2. Why Do We Need Embeddings?

Computers cannot understand words directly.

Example:

```
cat

↓

Token ID

15
```

The number:

```
15
```

does not tell the model:

- cat is an animal
- cat is similar to dog
- cat drinks milk

Embeddings solve this problem.

---

# 3. Complete Flow

```
Text

↓

Tokenizer

↓

Token IDs

↓

Embedding Lookup

↓

Embedding Vectors

↓

Transformer

↓

Prediction
```

---

# 4. Token ID vs Embedding

| Token ID | Embedding |
|-|-|
| Created by tokenizer | Learned by model |
| Integer | Vector |
| Identifier | Meaning representation |
| No semantic information | Contains relationships |

Example:

```
cat

Token ID:

15


Embedding:

[0.82,-0.15,0.63]
```

---

# 5. Embedding Matrix

The embedding matrix stores vectors for all tokens.

Example:

Vocabulary:

```
50,000 tokens
```

Embedding size:

```
768 dimensions
```

Matrix:

```
50,000 × 768
```

Example:

```
             Vector Dimensions

cat     [0.2,0.5,-0.1,...]

dog     [0.3,0.4,-0.2,...]

car     [0.7,-0.8,0.1,...]
```

---

# 6. Embedding Lookup

Process:

```
Token ID

↓

Embedding Matrix

↓

Vector
```

Example:

Input:

```
Token ID = 15
```

Lookup:

```
15

↓

[0.82,-0.15,0.63]
```

---

# 7. How Embeddings Start

Before training:

```
cat:

[0.12,-0.44,0.31]
```

Random values.

No meaning.

---

# 8. How Embeddings Learn

Training process:

```
Input Text

↓

Predict Next Token

↓

Compare With Actual Answer

↓

Calculate Error

↓

Update Parameters

↓

Improve Embeddings
```

This repeats millions/billions of times.

---

# 9. Why Similar Words Have Similar Embeddings?

Because they appear in similar contexts.

Example:

```
The cat drinks milk.

The dog drinks milk.
```

The model learns:

```
cat ≈ dog
```

because they are used similarly.

---

# 10. Dense Vector

An embedding is called a dense vector.

Example:

Dense:

```
[0.23,-0.51,0.76,0.12]
```

Sparse:

```
[0,0,0,1,0,0]
```

Dense vectors store information across many dimensions.

---

# 11. Cosine Similarity

Purpose:

Measure similarity between vectors.

Formula:

```
        A · B
----------------
     ||A|| ||B||
```

Meaning:

```
1

↓

Very similar


0

↓

Unrelated


-1

↓

Opposite
```

---

# 12. Similarity Example

Words:

```
king
queen
apple
car
```

Similarity:

```
king

↓

queen

(high)


king

↓

apple

(low)
```

---

# 13. Semantic Search

Traditional Search:

```
Keyword matching
```

Example:

Search:

```
automobile repair
```

May not find:

```
car fixing guide
```

---

Semantic Search:

```
Convert text into embeddings

↓

Compare meaning
```

Understands:

```
automobile ≈ car
```

---

# 14. Sentence Embedding vs Token Embedding

## Token Embedding

Represents each token.

Used inside LLMs.

Example:

```
I love AI

↓

I vector

love vector

AI vector
```

---

## Sentence Embedding

Represents the whole sentence.

Example:

```
I love AI

↓

Single vector
```

Used for:

- Search
- RAG
- Recommendations

---

# 15. Embeddings in RAG

RAG:

Retrieval-Augmented Generation

Pipeline:

```
User Question

↓

Create Question Embedding

↓

Vector Database

↓

Similarity Search

↓

Retrieve Documents

↓

LLM

↓

Answer
```

---

# 16. Vector Database

A database designed to store and search embeddings.

Examples:

- Pinecone
- Weaviate
- Milvus
- Qdrant
- ChromaDB

Stores:

```
Document

+

Embedding Vector
```

---

# 17. Traditional DB vs Vector DB

| Traditional DB | Vector DB |
|-|-|
| SQL Query | Similarity Search |
| Exact Match | Meaning Match |
| Rows | Vectors |
| Structured Data | Embeddings |

---

# 18. Interview One-Liners

## What is an embedding?

A numerical representation that captures semantic meaning of data.

---

## Why can't LLM use token IDs directly?

Because token IDs are only identifiers and contain no semantic information.

---

## How are embeddings learned?

They are initialized randomly and updated during training using prediction error and backpropagation.

---

## Why cosine similarity?

Because it compares vector direction, which represents semantic similarity.

---

## Why embeddings in RAG?

They allow retrieving relevant information based on meaning rather than exact keywords.

---

# 19. Common Mistakes

❌ Token IDs have meaning

✅ Token IDs are just identifiers


---

❌ One dimension represents one concept

Example:

```
Dimension 20 = intelligence
```

✅ Meaning is distributed across many dimensions.


---

❌ Embeddings are manually created

✅ Embeddings are learned during training.


---

❌ Similar words have identical vectors

✅ Similar words have nearby vectors.

---

# Final Mental Model

Remember this:

```
Tokenizer

↓

Token IDs

↓

Embedding Matrix

↓

Meaningful Vectors

↓

Transformer

↓

Prediction
```

For AI Applications:

```
Text

↓

Embedding Model

↓

Vector Database

↓

Similarity Search

↓

Relevant Context

↓

LLM Answer
```

---

# ⭐ Key Takeaways

1. Token IDs identify tokens.
2. Embeddings add meaning.
3. Embeddings are learned during training.
4. Similar concepts have similar vectors.
5. Cosine similarity compares embeddings.
6. RAG uses embeddings for retrieval.
7. Vector databases store and search embeddings.

---
