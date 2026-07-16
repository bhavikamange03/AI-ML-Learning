# Lesson 3 - Embeddings Interview Questions

## 🎯 Purpose

This document contains commonly asked interview questions about:

- Embeddings
- Token IDs
- Embedding Matrix
- Vector Similarity
- Semantic Search
- Vector Databases
- RAG Systems

Questions are organized from beginner to AI Engineer level.

---

# Beginner Level Questions

---

## Q1. What is an embedding?

### Answer:

An embedding is a numerical representation of text, words, or other data where the meaning and relationships are captured as a vector.

Instead of representing a word as a simple identifier:

```
cat → 15
```

an embedding represents it as:

```
cat →

[0.82, -0.15, 0.63, ...]
```

The vector contains learned semantic information.

Words with similar meanings have similar embeddings.

Example:

```
cat

dog
```

will have closer vectors because they appear in similar contexts.

---

# Q2. Why do we need embeddings?

### Answer:

LLMs cannot understand raw text or token IDs directly.

Token IDs are only identifiers.

Example:

```
cat → 15

dog → 42
```

The numbers 15 and 42 do not tell the model that cat and dog are both animals.

Embeddings convert these IDs into meaningful vectors that capture relationships between words.

---

# Q3. What is the difference between a Token ID and an Embedding Vector?

### Answer:

| Token ID | Embedding Vector |
|---|---|
| Created by tokenizer | Learned by model |
| Integer | List of numbers |
| Identifier | Semantic representation |
| No meaning | Contains learned meaning |

Example:

```
cat

↓

Token ID

15

↓

Embedding

[0.82,-0.15,0.63]
```

---

# Q4. Does a Token ID contain meaning?

### Answer:

No.

Token IDs are arbitrary numbers assigned by the tokenizer.

For example:

```
cat → 15
```

does not mean cat is represented by the number 15.

Another tokenizer could assign:

```
cat → 500
```

The meaning remains the same.

Meaning comes from the embedding vector.

---

# Q5. What is an embedding vector?

### Answer:

An embedding vector is a list of numbers representing the meaning of a token.

Example:

```
king:

[
0.21,
-0.45,
0.78,
...
]
```

Modern models use hundreds or thousands of dimensions.

---

# Intermediate Level Questions

---

# Q6. What is an Embedding Matrix?

### Answer:

An embedding matrix is a large table that stores embeddings for every token in the vocabulary.

Example:

```
Vocabulary:

50,000 tokens


Embedding size:

768 dimensions
```

Matrix size:

```
50,000 × 768
```

Each row represents one token's embedding vector.

---

# Q7. Explain Embedding Lookup.

### Answer:

Embedding lookup is the process of retrieving the embedding vector associated with a token ID.

Example:

Input:

```
Token ID = 15
```

The model performs:

```
Token ID

↓

Embedding Matrix

↓

[0.82,-0.15,0.63]
```

The transformer receives the vector, not the token ID.

---

# Q8. How are embeddings initialized?

### Answer:

Embeddings are initialized with random values before training.

At this stage:

```
cat

[0.12,-0.45,0.31]
```

has no meaning.

The model learns better embeddings during training through millions or billions of updates.

---

# Q9. How does the model learn embeddings?

### Answer:

The model learns embeddings through training.

Process:

```
Input Text

↓

Predict Next Token

↓

Compare Prediction With Actual Token

↓

Calculate Error

↓

Update Parameters

↓

Improve Embeddings
```

The model uses backpropagation and gradient descent to adjust the embedding values.

Over time, words appearing in similar contexts develop similar vectors.

---

# Q10. Why do similar words have similar embeddings?

### Answer:

Because embeddings are learned from context.

Example sentences:

```
The cat drinks milk.

The dog drinks milk.
```

The model observes that:

```
cat

dog
```

appear in similar situations.

Therefore their vectors become closer.

This follows the NLP idea:

> Words appearing in similar contexts have similar meanings.

---

# Q11. Why are embeddings called dense vectors?

### Answer:

Embeddings are called dense vectors because most dimensions contain meaningful values.

Example:

Sparse vector:

```
[0,0,0,1,0,0]
```

Dense vector:

```
[0.32,-0.51,0.76,0.18]
```

Modern AI models use dense representations because they can capture complex relationships.

---

# Similarity and Search Questions

---

# Q12. What is cosine similarity?

### Answer:

Cosine similarity measures how similar two vectors are by comparing their direction.

Formula:

```
       A · B
--------------
     ||A|| ||B||
```

Range:

```
1   → Same direction

0   → Unrelated

-1  → Opposite direction
```

---

# Q13. Why use cosine similarity for embeddings?

### Answer:

Because semantic meaning is represented by the direction of vectors rather than their magnitude.

Cosine similarity ignores vector length and focuses on the relationship between vectors.

---

# Q14. How can embeddings find similar documents?

### Answer:

The system:

1. Converts documents into embeddings.
2. Converts user query into an embedding.
3. Calculates similarity between query and documents.
4. Returns documents with the highest similarity score.

Example:

Query:

```
How to repair my automobile?
```

Document:

```
How to fix your car.
```

The embeddings are similar even though words are different.

---

# RAG and Vector Database Questions

---

# Q15. What role do embeddings play in RAG?

### Answer:

Embeddings allow RAG systems to retrieve relevant information based on meaning.

RAG pipeline:

```
User Question

↓

Question Embedding

↓

Vector Database

↓

Similarity Search

↓

Relevant Documents

↓

LLM

↓

Answer
```

---

# Q16. Why not directly search text in RAG?

### Answer:

Keyword search only finds exact matches.

Example:

```
automobile
```

may not match:

```
car
```

Embeddings understand semantic similarity.

Therefore:

```
automobile ≈ car
```

---

# Q17. What is a Vector Database?

### Answer:

A vector database stores and searches embedding vectors efficiently.

Examples:

- Pinecone
- Weaviate
- Milvus
- Qdrant
- ChromaDB

It enables fast similarity search over millions of vectors.

---

# Q18. Traditional Database vs Vector Database?

### Answer:

| Traditional DB | Vector DB |
|-|-|
| Stores structured data | Stores vectors |
| SQL queries | Similarity search |
| Exact matching | Semantic matching |
| Rows and columns | High-dimensional vectors |

---

# Advanced AI Engineer Questions

---

# Q19. What is the difference between token embeddings and sentence embeddings?

### Answer:

## Token Embeddings

Represent individual tokens.

Used internally by LLMs.

Example:

```
"I love AI"

↓

I vector

love vector

AI vector
```

---

## Sentence Embeddings

Represent the meaning of the entire sentence.

Example:

```
"I love AI"

↓

Single vector
```

Used for:

- Semantic search
- RAG
- Document retrieval

---

# Q20. Are embeddings the same for every model?

### Answer:

No.

Embeddings depend on:

- Training data
- Model architecture
- Training objectives

The same word can have different embeddings in different models.

Example:

Apple:

Model A:

```
apple → fruit
```

Model B:

```
Apple → technology company
```

---

# Q21. Why can't we use embeddings from one model with another model?

### Answer:

Because each model learns its own vector space.

The meaning of dimensions and relationships between vectors are specific to that model.

Embeddings generated by different models are usually not directly compatible.

---

# Q22. Can embeddings understand synonyms?

### Answer:

Yes, because they learn relationships from context.

Example:

```
car

automobile
```

may have similar vectors because they appear in similar contexts.

---

# Common Interview Mistakes

---

## Mistake 1:

❌ "Token IDs contain meaning."

Correct:

✅ Token IDs are only identifiers.

---

## Mistake 2:

❌ "Each embedding dimension represents one specific feature."

Correct:

✅ Meaning is distributed across many dimensions.

---

## Mistake 3:

❌ "Embeddings are manually created."

Correct:

✅ Embeddings are learned during training.

---

## Mistake 4:

❌ "Similar words have identical vectors."

Correct:

✅ Similar words have nearby vectors.

---

# Quick Interview Revision

## One Sentence Answers

### What is an embedding?

A numerical representation that captures semantic meaning.

---

### Why do we need embeddings?

Because token IDs do not contain meaning.

---

### How are embeddings learned?

Through training using prediction error and parameter updates.

---

### Why use cosine similarity?

To compare semantic similarity between vectors.

---

### Why are embeddings important in RAG?

They allow retrieval based on meaning instead of keywords.

---

# Final Mental Model

Remember:

```
Tokenizer

↓

Token IDs

↓

Embedding Matrix

↓

Embedding Vectors

↓

Transformer

↓

Prediction
```


For AI applications:

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

LLM Response
```

Embeddings are the bridge between human language and machine understanding.