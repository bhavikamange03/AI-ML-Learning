# Lesson 4 — Transformers & GPT Architecture 🤖

## Overview

In this lesson, I learned how modern Large Language Models (LLMs) like GPT work internally.

The main focus was understanding the **Transformer architecture**, especially how **self-attention** helps models understand relationships between words and generate meaningful responses.

This lesson connects the theory of LLMs with hands-on implementation.

---

# Learning Objectives 🎯

By completing this lesson, I learned:

- Why RNNs struggled with long sequences
- How Attention solved sequence understanding problems
- How Self-Attention works internally
- How Query, Key, and Value vectors are created
- How Transformer blocks are built
- How GPT predicts the next token
- Difference between Training and Inference
- How to use pretrained Transformer models using Hugging Face

---

# Topics Covered 📚

## 1. From RNNs to Transformers

Learned:

- Limitations of RNN architecture
- Sequential processing problem
- Long-term dependency problem
- Why attention is needed
- Why Transformers became the foundation of modern LLMs


---

## 2. Self-Attention Mechanism

Learned how a Transformer understands relationships between words.

Concepts:

- Token embeddings
- Query (Q)
- Key (K)
- Value (V)
- Attention scores
- Attention weights
- Softmax
- Contextual embeddings


Self-attention formula:

```
Attention(Q,K,V)
=
Softmax(QKᵀ / √dk)V
```


Flow:

```
Input Embeddings

        |
        ↓

Create Q, K, V

        |
        ↓

Calculate Attention Scores

        |
        ↓

Apply Softmax

        |
        ↓

Attention Weights

        |
        ↓

Weighted Sum of Values

        |
        ↓

Attention Output
```

---

## 3. Transformer Block

Learned the components inside a Transformer layer.


Architecture:

```
Input

  |
  ↓

Self Attention

  |
  ↓

Residual Connection

  |
  ↓

Layer Normalization

  |
  ↓

Feed Forward Network

  |
  ↓

Output
```


Concepts:

- Multi-head attention
- Residual connections
- Layer normalization
- Feed Forward Network
- Why these components improve training stability

---

## 4. GPT Architecture

Learned how GPT generates text.

GPT uses a:

```
Decoder-Only Transformer
```


Text generation flow:

```
User Prompt

      |
      ↓

Tokenizer

      |
      ↓

Token IDs

      |
      ↓

Embeddings

      |
      ↓

Transformer Blocks

      |
      ↓

Probability Distribution

      |
      ↓

Next Token Prediction

      |
      ↓

Generated Text
```


Topics:

- Causal attention
- Next-token prediction
- Training vs inference
- Teacher forcing
- Temperature
- Text generation

---

# Hands-on Implementation 💻

## Assignment 1 — Build Self-Attention Using NumPy ⭐⭐⭐⭐⭐

### Goal

Implement simplified self-attention from scratch using NumPy.

Implemented:

✅ Created word embeddings  
✅ Created random Wq, Wk, Wv matrices  
✅ Generated Query, Key, Value vectors  
✅ Calculated attention scores  
✅ Applied scaled dot-product attention  
✅ Applied Softmax  
✅ Generated attention output  
✅ Visualized attention weights using heatmap  


File:

```
assignments/self_attention.py
```

---

## Assignment 2 — GPT-2 Text Generation ⭐⭐⭐

### Goal

Use a pretrained Transformer model from Hugging Face.

Implemented:

✅ Loaded GPT-2 model  
✅ Generated text from prompts  
✅ Experimented with temperature values  
✅ Observed predictable vs creative outputs  


Example prompt:

```
Artificial Intelligence is
```


File:

```
assignments/gpt2_text_generation.py
```

---

# How to Run 🚀

## Prerequisites

Python:

```
Python 3.10+
```

---

# Assignment 1 — Self Attention

## Install Dependencies

```bash
pip3 install numpy matplotlib
```

For macOS:

```bash
python3 -m pip3 install numpy matplotlib
```


## Run Program

Navigate to assignments folder:

```bash
cd assignments
```

Run:

```bash
python3 self_attention.py
```


Expected output:

```
Embedding Matrix

Query Matrix (Q)

Key Matrix (K)

Value Matrix (V)

Attention Scores

Attention Weights

Attention Output
```


The program also displays an attention heatmap showing how words attend to each other.


Example sentence:

```
The cat drinks milk
```

---

# Assignment 2 — GPT-2 Text Generation


## Install Dependencies

```bash
pip3 install transformers torch
```

For macOS:

```bash
python3 -m pip3 install transformers torch
```


## Run Program

```bash
python gpt2_text_generation.py
```


The first run downloads the GPT-2 model from Hugging Face.

---

## Experiment with Temperature


Change:

```python
temperature=0.2
```

```python
temperature=0.7
```

```python
temperature=1.2
```


Observe:


| Temperature | Output Behavior |
|---|---|
| 0.2 | More predictable |
| 0.7 | Balanced |
| 1.2 | More creative/random |


---

# Repository Structure 📂

```
lesson04_transformers_gpt/

├── README.md
├── notes.md
├── homework.md
├── interview_questions.md
├── interview_answers.md
├── cheatsheet.md

└── assignments/

    ├── assignment1_self_attention_numpy.py

    └── assignment2_gpt2_text_generation.py
```

---

# Key Takeaways ⭐

After completing this lesson, I can explain:

✅ Why Transformers replaced RNNs  
✅ How attention works  
✅ How Q, K, and V vectors are created  
✅ Difference between attention score and attention weight  
✅ How Transformer blocks work  
✅ Why GPT is decoder-only architecture  
✅ How GPT predicts the next token  
✅ Difference between training and inference  
✅ How to use pretrained Transformer models  


---

# Progress Tracker 📊


| Topic | Status |
|---|---|
| RNN limitations | ✅ Completed |
| Attention mechanism | ✅ Completed |
| Self-attention mathematics | ✅ Completed |
| Query, Key, Value | ✅ Completed |
| Attention scores and weights | ✅ Completed |
| Transformer block | ✅ Completed |
| GPT architecture | ✅ Completed |
| NumPy self-attention implementation | ✅ Completed |
| GPT-2 text generation | ✅ Completed |


---

# Lesson Reflection 📝

## Most Interesting Concept

Self-attention was the most interesting concept because it explains how Transformers understand relationships between words instead of processing them only sequentially.

---

## Most Challenging Concept

Understanding how Query, Key, and Value vectors are created and how attention scores are calculated mathematically.

---

## Important Interview Explanation

A simple explanation:

> GPT is a decoder-only Transformer model that uses self-attention to understand relationships between tokens and predicts the next most likely token based on patterns learned during training.

---

# What's Next 🚀

## Lesson 5 — Building LLM Applications

Topics:

- LLM APIs
- Prompt Engineering
- System prompts
- User prompts
- Chat history management
- Temperature and generation parameters
- Building a simple AI application


After this:

## Lesson 6 — Retrieval Augmented Generation (RAG)

Production AI architecture:

```
Documents

    ↓

Embeddings

    ↓

Vector Database

    ↓

Retriever

    ↓

LLM

    ↓

Answer
```
