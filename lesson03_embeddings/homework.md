# Lesson 3 - Embeddings Homework

## 🎯 Goal

The goal of this homework is to verify your understanding of:

- What embeddings are
- Why token IDs are not enough
- Embedding matrix
- Embedding lookup
- How embeddings are learned
- Cosine similarity
- Semantic search
- RAG architecture
- Vector databases

---

# Part 1: Concept Understanding

---

## Q1. Why can't an LLM directly use token IDs?

Example:

```
[5, 20, 101]
```

Explain why the model needs embeddings.

### Answer:

Token IDs are only numerical identifiers created by the tokenizer.

They do not contain semantic information.

For example:

```
cat → 15

dog → 42
```

The numbers 15 and 42 do not tell the model that cat and dog are both animals.

The embedding layer converts these token IDs into dense vectors that contain learned semantic information.

Example:

```
Token ID

15

↓

Embedding Vector

[0.82, -0.15, 0.63...]
```

The transformer uses these vectors to understand relationships between words.

---

# Q2. Explain the difference between Token ID and Embedding Vector.

## Token ID

Answer:

A Token ID is an integer assigned by the tokenizer.

Example:

```
"cat"

↓

Token ID = 15
```

Properties:

- Created by tokenizer
- Used as an identifier
- Has no meaning by itself


## Embedding Vector

Answer:

An embedding vector is a dense numerical representation learned by the model.

Example:

```
cat

↓

[0.82, -0.15, 0.63, ...]
```

Properties:

- Learned during training
- Contains semantic information
- Similar words have similar vectors

---

# Q3. Why does "cat" need an embedding?

Explain why the model cannot directly understand:

```
cat
```

### Answer:

The model does not understand English words directly.

It processes numbers.

The token:

```
cat
```

is converted into:

```
Token ID
```

Then the embedding layer converts it into:

```
Vector representation
```

During training, the model learns that words appearing in similar contexts should have similar vectors.

For example:

```
cat

dog
```

appear in similar contexts:

```
The ___ drinks milk.
The ___ plays outside.
```

Therefore their embeddings become closer.

---

# Part 2: Embedding Matrix

---

## Q4. What is an Embedding Matrix?

### Answer:

An embedding matrix is a table that stores the embedding vector for every token in the vocabulary.

Example:

| Token ID | Token | Vector |
|-|-|-|
| 15 | cat | [0.8,0.2...] |
| 42 | dog | [0.7,0.3...] |

When the model receives a token ID, it looks up the corresponding vector.

---

# Q5. Explain Embedding Lookup.

### Answer:

Embedding lookup is the process of retrieving the vector associated with a token ID.

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

The transformer receives the vector, not the ID.

---

# Part 3: Learning Embeddings

---

## Q6. Why are embeddings initialized with random numbers?

### Answer:

At the beginning of training, the model has no knowledge about language.

Therefore, embeddings start with random values.

Example:

Before training:

```
cat

[0.12,-0.44,0.51]
```

These values have no meaning.

Training gradually adjusts them.

---

# Q7. How does the model learn embeddings?

### Answer:

The training process:

```
Text

↓

Tokenization

↓

Prediction

↓

Compare prediction with correct answer

↓

Calculate error

↓

Update parameters

↓

Improve embeddings
```

The model repeats this process billions of times.

Over time:

```
cat

and

dog
```

move closer because they appear in similar contexts.

---

# Part 4: Similarity

---

## Q8. Why are embeddings useful for finding similar words?

Example:

```
car

automobile
```

Explain.

### Answer:

Although the words are different, they have similar meanings.

During training, they appear in similar contexts.

Therefore their embeddings become close.

The model can compare vectors using cosine similarity.

---

# Q9. What is cosine similarity?

### Answer:

Cosine similarity measures how similar two vectors are by comparing their direction.

Range:

```
1   → Very similar

0   → Unrelated

-1  → Opposite
```

---

# Part 5: RAG and Vector Database

---

## Q10. Why are embeddings important for RAG?

### Answer:

RAG systems use embeddings to find relevant information from documents.

Flow:

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

LLM Answer
```

Embeddings allow retrieval based on meaning instead of exact keywords.

---

# Q11. Traditional Search vs Semantic Search

Explain the difference.

### Answer:

Traditional search:

```
Search keywords

↓

Exact match
```

Example:

Searching:

```
automobile repair
```

may not find:

```
car fixing guide
```


Semantic search:

```
Convert text to embeddings

↓

Compare meaning
```

It understands:

```
automobile ≈ car
```

---

# Part 6: Thought Exercises

---

# Q12.

Two models:

## Model A

Trained on cooking:

```
apple pie
apple juice
apple cake
```

## Model B

Trained on technology:

```
Apple released iPhone
Apple announced MacBook
```

Would the embedding of "apple" be the same?

Explain.

---

## Answer:

No.

The embeddings would be different.

Model A learns:

```
apple

↓

fruit
food
recipe
```

Model B learns:

```
Apple

↓

company
technology
products
```

Embeddings depend on training data and context.

---

# Q13. Explain embeddings to a non-technical person.

### Example Answer:

Embeddings are like organizing things on a map.

Things that are similar are placed close together.

For example:

```
Dog

Cat

Lion
```

would be close because they are animals.

But:

```
Dog

Car
```

would be far apart because they are unrelated.

AI uses numbers instead of physical locations, but the idea is similar.

---

# 💻 Coding Assignment

## Goal

Practice:

- Creating embeddings
- Vector similarity
- Cosine similarity


Create:

```
embedding_practice.py
```


Tasks:

1. Load a pre-trained embedding model.

Example:

```python
SentenceTransformer(
"all-MiniLM-L6-v2"
)
```


2. Generate embeddings for:

```
king
queen
man
woman
apple
car
```


3. Calculate cosine similarity.


4. Find:

```
Closest word to king
```


Expected:

```
king → queen
```

---

# Reflection Questions

Answer in your own words:

1. Why are token IDs not enough?

2. What information does an embedding contain?

3. Why do similar words have similar vectors?

4. How does RAG use embeddings?

5. What was the most interesting concept from this lesson?

6. What concept is still unclear?