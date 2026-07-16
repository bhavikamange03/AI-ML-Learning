# Lesson 2 - Tokenization Cheatsheet

## What is Tokenization?

Converts human-readable text into machine-readable tokens.

```
Text

↓

Tokens

↓

Token IDs
```

---

## Why Tokenization?

Computers understand numbers, not words.

The tokenizer converts text into numbers.

---

## Token

A token may be:

- Word
- Subword
- Character
- Punctuation

---

## Types of Tokenization

### Character

```
hello

↓

h e l l o
```

✅ Any word

❌ Too many tokens

---

### Word

```
I love AI

↓

I
love
AI
```

✅ Simple

❌ Huge vocabulary

---

### Subword

```
developer

↓

develop + er
```

```
development

↓

develop + ment
```

```
developing

↓

develop + ing
```

✅ Reusable

✅ Small vocabulary

✅ Handles unknown words

---

## Token ID

```
AI

↓

101
```

A Token ID is simply an identifier.

It has **no meaning by itself**.

---

## Vocabulary

Maps:

```
Token

↔

Token ID
```

---

## Complete Flow

```
User Text

↓

Tokenizer

↓

Token IDs

↓

Embedding Lookup

↓

Vectors

↓

Transformer
```

---

## Tokenizer + LLM

Always stay together.

Why?

Because the LLM learned patterns using that tokenizer's token IDs.

Changing the tokenizer changes the IDs and breaks those learned patterns.

---

# Interview One-Liners

✔ Tokenization converts text into tokens.

✔ Token IDs are identifiers.

✔ Meaning comes from embeddings.

✔ Character → Too many tokens.

✔ Word → Huge vocabulary.

✔ Subword → Best balance.

✔ Modern LLMs use subword tokenization.

---

# Remember ⭐

> **Tokenization converts language into numbers. Embeddings convert those numbers into meaning.**