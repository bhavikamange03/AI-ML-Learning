# Lesson 3: Embeddings in Large Language Models (LLMs)

## 🎯 Overview

Embeddings are one of the most important concepts in modern Artificial Intelligence.

They are the bridge between:

```
Human Language

        ↓

Machine Understandable Numbers
```

LLMs do not understand words directly.

They convert text into numerical representations called **embeddings**, which allow models to understand relationships, similarity, and meaning.

In this lesson, we learn:

- What embeddings are
- Why token IDs are not enough
- How embedding matrices work
- How embeddings are learned
- How similarity search works
- How embeddings power RAG systems
- How vector databases store embeddings

---

# 📚 Learning Objectives

By the end of this lesson, you should understand:

✅ What an embedding vector represents

✅ Difference between token IDs and embeddings

✅ What an embedding matrix is

✅ How embedding lookup works

✅ How embeddings are trained

✅ How cosine similarity compares vectors

✅ How semantic search works

✅ How embeddings are used in RAG

✅ How vector databases work

---

# 🧠 Core Concepts Covered

---

# 1. Token IDs Are Not Enough

A tokenizer converts text into token IDs.

Example:

```
"cat"

↓

Token ID

15
```

However:

```
15
```

has no meaning.

The model does not know:

```
cat = animal
cat ≈ dog
```

The embedding layer solves this problem.

---

# 2. Embeddings

An embedding is a numerical representation of meaning.

Example:

```
cat

↓

[
0.82,
-0.15,
0.63,
...
]
```

Similar concepts have similar vectors.

Example:

```
cat

↓

dog

(close vectors)
```

---

# 3. Embedding Matrix

The embedding matrix stores vectors for every token.

Example:

```
Vocabulary Size:

50,000 tokens


Embedding Dimension:

768
```

Matrix:

```
50,000 × 768
```

Each row represents one token embedding.

---

# 4. Embedding Lookup

The process:

```
Token ID

↓

Embedding Matrix

↓

Embedding Vector
```

Example:

```
Token ID:

15


↓

Embedding:

[0.82,-0.15,0.63]
```

---

# 5. Learning Embeddings

Initially:

```
Random Values
```

Example:

```
cat:

[0.12,-0.44,0.31]
```

During training:

```
Predict

↓

Compare

↓

Calculate Error

↓

Update Parameters
```

After billions of updates:

```
cat

and

dog
```

become closer because they appear in similar contexts.

---

# 6. Cosine Similarity

Cosine similarity measures how close two vectors are.

Range:

```
1

↓

Same meaning


0

↓

Unrelated


-1

↓

Opposite
```

Example:

```
king

≈

queen
```

has high similarity.

---

# 7. Semantic Search

Traditional search:

```
Exact keyword matching
```

Example:

```
car repair
```

may not match:

```
automobile fixing
```

Semantic search:

```
Convert text into embeddings

↓

Compare meaning
```

It understands:

```
car ≈ automobile
```

---

# 8. Embeddings in RAG

RAG:

**Retrieval-Augmented Generation**

It allows LLMs to answer questions using external knowledge.

Pipeline:

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

# 9. Vector Databases

Vector databases store embeddings and perform similarity searches.

Examples:

- Pinecone
- Weaviate
- Milvus
- Qdrant
- ChromaDB

They allow searching based on meaning instead of keywords.

---

# 📂 Folder Structure

```
lesson03_embeddings/

│
├── README.md
│
├── notes.md
│
├── homework.md
│
├── interview_questions.md
│
├── cheatsheet.md
│
└── embedding_practice.py
```

---

# 📝 Files Explanation

## notes.md

Detailed lesson notes covering:

- Embedding fundamentals
- Embedding matrix
- Training process
- Similarity search
- RAG architecture
- Interview concepts

---

## homework.md

Practice exercises:

- Concept questions
- Reflection questions
- Thought exercises
- Coding assignment

---

## interview_questions.md

Interview preparation:

- Beginner questions
- Intermediate questions
- AI Engineer questions
- RAG questions

---

## cheatsheet.md

Quick revision before interviews.

Contains:

- Important definitions
- Diagrams
- One-line answers

---

## embedding_practice.py

Hands-on coding practice:

Topics:

- Generate embeddings
- Calculate cosine similarity
- Compare words
- Perform similarity search

---

# 💻 Running the Coding Assignment

## Step 1: Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Mac/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

---

## Step 2: Install Dependencies

```bash
pip install sentence-transformers numpy
```

---

## Step 3: Run Program

```bash
python embedding_practice.py
```

---

# Expected Output Example

```
king vs queen:

0.78


king vs apple:

0.20


Closest word to king:

queen
```

---

# 🔗 Connection With Previous Lessons

## Lesson 1: LLM Basics

Learned:

```
LLM predicts next token
```

↓

## Lesson 2: Tokenization

Learned:

```
Text

↓

Token IDs
```

↓

## Lesson 3: Embeddings

Learned:

```
Token IDs

↓

Meaningful Vectors
```

↓

## Next Lesson

```
Transformers and Attention
```

---

# 🚀 What's Next?

## Lesson 4: Transformers & Attention

Topics:

- Why transformers changed NLP
- Encoder vs Decoder
- Self-attention
- Query, Key, Value (QKV)
- Multi-head attention
- Transformer architecture
- How ChatGPT generates responses

---

# ⭐ Final Mental Model

Remember this complete flow:

```
Human Text

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

Next Token Prediction

↓

Generated Response
```

For AI applications:

```
User Query

↓

Embedding

↓

Vector Database

↓

Relevant Context

↓

LLM

↓

Answer
```

---

# Lesson 3 Completed ✅

You now understand the foundation behind:

- Semantic Search
- RAG Systems
- Vector Databases
- Modern AI Applications