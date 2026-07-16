# Lesson 2 - Tokenization Homework

## 🎯 Goal

The goal of this homework is to verify your understanding of:

- Why LLMs need tokenization
- Types of tokenization
- Token IDs
- Vocabulary
- Why subword tokenization is preferred
- Why tokenizers and LLMs cannot be swapped

---

# Part 1: Understanding Tokenization

## Q1. What is tokenization?

### Answer

Tokenization is the process of breaking text into smaller units called **tokens** so that an LLM can process them.

Humans understand text, but computers understand numbers. Therefore, text is first converted into tokens and then into token IDs.

---

## Q2. Why do LLMs need tokenization?

### Answer

LLMs cannot process raw text directly because neural networks perform mathematical operations on numbers.

The tokenizer converts text into token IDs, which the model can process.

---

## Q3. Explain the complete flow from text to token IDs.

### Answer

```
User Text

↓

Tokenizer

↓

Tokens

↓

Token IDs

↓

LLM
```

The tokenizer acts as the bridge between human language and machine-readable numbers.

---

# Part 2: Types of Tokenization

## Q4. Explain Character Tokenization.

### Answer

Character tokenization treats every character as a separate token.

Example:

```
hello

↓

h e l l o
```

### Advantages

- Handles every possible word.
- No unknown words.

### Disadvantages

- Produces many tokens.
- Increases computation.
- Loses word-level meaning.

---

## Q5. Explain Word Tokenization.

### Answer

Word tokenization treats each word as a token.

Example:

```
I love AI

↓

I
love
AI
```

### Advantages

- Easy to understand.
- Preserves complete words.

### Disadvantages

- Very large vocabulary.
- Cannot easily handle new or rare words.

---

## Q6. Explain Subword Tokenization.

### Answer

Subword tokenization splits words into meaningful reusable pieces.

Example:

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

This allows the tokenizer to reuse common parts across many words.

---

## Q7. Why is Subword Tokenization preferred?

### Answer

Subword tokenization provides a balance between character-level and word-level tokenization.

Benefits:

- Smaller vocabulary
- Better reuse of common word parts
- Handles unknown words
- Lower computational cost

---

# Part 3: Token IDs

## Q8. What is a Token ID?

### Answer

A token ID is a numerical identifier assigned to each token in the tokenizer's vocabulary.

Example:

| Token | Token ID |
|-------|---------:|
| AI | 101 |
| love | 20 |
| Python | 350 |

These IDs are used by the model during processing.

---

## Q9. Do Token IDs have meaning?

### Answer

No.

Token IDs are simply identifiers.

Meaning is learned later through embeddings.

Example:

```
AI → 101
```

The number **101** itself has no meaning.

---

# Part 4: Vocabulary

## Q10. What is a tokenizer vocabulary?

### Answer

A tokenizer vocabulary is a collection of all tokens known by the tokenizer along with their corresponding token IDs.

Example:

```
Token

↓

Token ID
```

The tokenizer uses this vocabulary to convert text into numbers and vice versa.

---

# Part 5: Think Like an AI Engineer

## Q11. Why can't we swap tokenizers between different LLMs?

### Answer

Every LLM is trained using a specific tokenizer.

During training, the model learns patterns based on that tokenizer's token IDs.

If we replace the tokenizer, the same text may produce different token IDs.

Since the model never learned those new IDs in that context, its predictions become inaccurate.

---

## Q12. Design Question

Suppose you are designing a tokenizer for these words:

```
Developer
Developing
Development
Redevelop
FastAPI
OpenAI
Tokenization
```

How would you split them?

### Example Answer

```
Developer      → develop + er
Developing     → develop + ing
Development    → develop + ment
Redevelop      → re + develop
FastAPI        → Fast + API
OpenAI         → Open + AI
Tokenization   → token + ization
```

Reason:

The tokenizer can reuse common subwords, reducing vocabulary size and improving efficiency.

---

# Reflection

1. Why is subword tokenization the best compromise?

2. Which concept is still confusing?

3. Explain tokenization to a non-technical person.