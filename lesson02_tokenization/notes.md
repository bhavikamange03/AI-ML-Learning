# Lesson 2 - Tokenization

## 🎯 Learning Objectives

By the end of this lesson, we should understand:

- Why LLMs need tokenization
- How text becomes tokens
- What is a token ID
- Difference between character, word, and subword tokenization
- Why subword tokenization is commonly used
- What is a tokenizer vocabulary
- How tokenizer and LLM are connected
- Why we cannot freely swap tokenizers between models

---

# 1. Why Do LLMs Need Tokenization?

Humans understand text:


I love artificial intelligence


But computers work with numbers.

A neural network cannot directly process:


"I love AI"


It needs numerical input.

Therefore, before sending text to an LLM:


Text

↓

Tokenizer

↓

Numbers (Token IDs)

↓

LLM


The tokenizer acts as a bridge between human language and machine language.

---

# 2. What is Tokenization?

Tokenization is the process of breaking text into smaller units called tokens.

Example:

Input:


I love AI


Possible tokens:


[I] [love] [AI]


The tokenizer then assigns each token a number.

Example:


I → 5
love → 20
AI → 101


The model receives:


[5, 20, 101]


These numbers are called token IDs.

---

# 3. What is a Token?

A token is the basic unit of text processed by an LLM.

A token can be:

- A complete word
- Part of a word
- A character
- Punctuation

Examples:

## Example 1: Complete word


cat


may become:


[cat]


---

## Example 2: Long word


unbelievable


may become:


un
+
believ
+
able


---

## Example 3: Punctuation

Sentence:


Hello!


Possible tokens:


Hello
!


---

# 4. Types of Tokenization

There are three common approaches:

1. Character Tokenization
2. Word Tokenization
3. Subword Tokenization

---

# 5. Character Tokenization

Each character becomes a token.

Example:


hello


becomes:


h e l l o


## Advantages:

- Can handle any word
- No unknown words

## Problems:

- Creates too many tokens
- Loses word-level meaning
- Requires longer sequences

Example:


artificial intelligence


creates many tokens.

More tokens means:

- More computation
- Higher cost
- Larger context usage

---

# 6. Word Tokenization

Each word becomes a token.

Example:


I love AI


becomes:


I
love
AI


## Advantage:

- Simple
- Keeps word meaning

## Problems:

Vocabulary becomes huge.

Example:

Words:


play
played
playing
player
replay


The model needs separate tokens:


play
played
playing
player
replay


This creates:

- Large vocabulary
- Poor handling of new words

---

# 7. Subword Tokenization

Subword tokenization is the compromise between character and word tokenization.

Instead of storing every complete word:

It breaks words into reusable pieces.

Example:


playing


becomes:


play + ing

developer


becomes:


develop + er

development


becomes:


develop + ment


The model can reuse:


develop


in multiple words.

---

# 8. Why Subword Tokenization is Better

It provides:

## Reusability

Example:


develop


can appear in:


developer
developing
development
redevelop


---

## Smaller Vocabulary

The model does not need millions of complete words.

---

## Handles Unknown Words

Example:

New word:


ChatGPTish


The tokenizer can split:


ChatGPT + ish


instead of failing.

---

# 9. Token IDs

The tokenizer maintains a vocabulary.

Example:

| Token | ID |
|---|---|
| hello | 10 |
| love | 20 |
| AI | 101 |

Input:


I love AI


After tokenization:


[5,20,101]


Important:

Token IDs themselves have no meaning.

Example:


AI = 101


The number 101 does not mean intelligence.

It is only an index used to find the token.

---

# 10. Vocabulary

A tokenizer has a vocabulary containing:

- Tokens
- Their assigned IDs

Example:


Vocabulary size = 50,000 tokens


The tokenizer knows:


101 → AI


and:


AI → 101


---

# 11. Tokenizer and LLM Relationship

The tokenizer and LLM are trained together.

The LLM learns patterns using the token IDs created by that tokenizer.

Example:

Tokenizer A:


OpenAI

↓

[450]


Tokenizer B:


OpenAI

↓

[800,50]


The LLM trained with tokenizer A learned:


450 represents OpenAI


If we replace tokenizer:

The model receives IDs it was never trained on.

The learned patterns no longer match.

---

# 12. Complete Flow


User Text

"I love AI"

    |
    v

Tokenizer

    |
    v

Token IDs

[5,20,101]

    |
    v

Embedding Lookup

    |
    v

Vectors

    |
    v

Transformer

    |
    v

Next Token Prediction


---

# 13. Common Misconceptions

## ❌ Token means word

Not always.

A token can be:

- Word
- Part of word
- Character
- Symbol

---

## ❌ Token IDs contain meaning

No.

Token IDs are only identifiers.

Meaning comes from embeddings learned during training.

---

## ❌ Any tokenizer works with any LLM

No.

Tokenizer and LLM are a matched pair.

---

# 📝 Lesson 2 Key Takeaways

1. LLMs cannot process raw text.
2. Tokenization converts text into tokens.
3. Tokens are converted into token IDs.
4. Token IDs are only identifiers.
5. Subword tokenization balances vocabulary size and flexibility.
6. Embeddings give token IDs meaning.
7. Tokenizer and LLM must stay compatible.

---

# 🚀 Next Lesson

## Lesson 3: Embeddings

Topics:

- Why token IDs are not enough
- Embedding vectors
- Embedding matrix
- Embedding lookup
- How embeddings learn relationships
- Vector similarity