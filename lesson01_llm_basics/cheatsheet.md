# Lesson 1 - LLM Basics Cheatsheet

## What is an LLM?

LLM = Large Language Model

A deep learning model trained on massive text data that learns language patterns and predicts the next token.

---

# LLM Core Concept

Input:


The capital of France is


Model predicts:


Paris


LLM = Next Token Prediction

---

# AI Hierarchy


Artificial Intelligence

    ↓

Machine Learning

    ↓

Deep Learning

    ↓

Large Language Models


---

# Parameters

Parameters are learned numerical values inside the model.

They help the model learn:

- Language patterns
- Relationships
- Context

They are NOT:

- Stored sentences
- A database of facts

---

# Token

Token = Basic unit processed by an LLM.

Examples:


Hello

↓

Token


A word can be:

- One token
- Multiple tokens

Tokens are important because:

- API cost depends on tokens
- Context window is measured in tokens

---

# Context Window

Context window = Amount of information the model can consider at one time.

Includes:

- Current prompt
- Conversation history
- Documents

Measured in tokens.

---

# LLM Memory

## Short-Term Memory

Current conversation.

Provided through context window.

---

## Long-Term Memory

Implemented by applications.

Stored in:

- Databases
- Vector databases
- Memory systems

Examples:

- User preferences
- Goals
- Projects

---

# LLM Pipeline


Text

↓

Tokenizer

↓

Token IDs

↓

Embeddings

↓

Transformer

↓

Next Token Prediction

↓

Response


---

# Interview One-Liners

## What is an LLM?

A deep learning model trained on massive text data that predicts the next token based on learned patterns.

---

## What does an LLM predict?

The next token.

---

## Why is it called Large?

Because of:

1. Large training datasets
2. Large number of parameters

---

## Does an LLM remember users?

Not by itself.

Applications add memory using external storage and retrieved context.

---

# Remember ⭐

LLM does not understand text like humans.

It learns mathematical patterns between tokens and uses those patterns to generate responses.