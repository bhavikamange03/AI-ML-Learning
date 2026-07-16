# Lesson 1 - LLM Basics Interview Questions

---

# Beginner Level

## Q1. What is an LLM?

### Answer:

LLM stands for Large Language Model.

An LLM is a deep learning model trained on a massive amount of text data to learn patterns in language. It generates responses by predicting the most likely next token based on patterns learned during training.

---

## Q2. Why is it called a Large Language Model?

### Answer:

It is called "Large" because:

1. It is trained on a very large amount of data.
2. It contains a large number of parameters that help it learn complex language patterns.

---

## Q3. What does an LLM actually predict?

### Answer:

An LLM predicts the next token.

It does not directly predict:

- Complete answers
- Sentences
- Facts

It generates text by repeatedly predicting the next token.

---

## Q4. What is a token?

### Answer:

A token is the basic unit of text processed by an LLM.

A token can be:

- A complete word
- Part of a word
- Punctuation

LLMs process tokens instead of raw text.

---

# Intermediate Level

## Q5. How does an LLM learn?

### Answer:

During training:

1. The model receives text examples.
2. It predicts the next token.
3. The prediction is compared with the actual token.
4. The error is calculated.
5. Parameters are updated using optimization techniques.

This process repeats billions of times.

---

## Q6. What are parameters in an LLM?

### Answer:

Parameters are internal numerical values learned during training.

They store patterns and relationships learned from data.

They are not stored sentences or facts.

---

## Q7. Does an LLM memorize all training data?

### Answer:

No.

An LLM mainly learns statistical patterns and relationships between tokens.

It does not store a database of every sentence it has seen.

---

## Q8. What is a context window?

### Answer:

A context window is the maximum amount of information, measured in tokens, that an LLM can consider while generating a response.

It includes:

- Current prompt
- Previous conversation
- Provided documents

---

# Advanced Level

## Q9. What is the difference between LLM memory and application memory?

### Answer:

An LLM itself does not permanently remember users.

Short-term memory comes from the current context window.

Long-term memory is implemented by the application using external storage such as databases.

The application retrieves relevant information and includes it in the prompt.

---

## Q10. How would you design memory for an AI assistant?

### Answer:

I would separate memory into:

### Short-term memory:
Current conversation stored in the context window.

### Long-term memory:
Important user information stored in a database.

Examples:

- User preferences
- Learning goals
- Previous projects

Temporary information would not be stored.

---

## Q11. Does increasing parameters always improve an LLM?

### Answer:

No.

Performance depends on multiple factors:

- Data quality
- Architecture
- Training process
- Fine-tuning
- Evaluation methods

More parameters alone do not guarantee better results.

---

## Q12. Explain LLM flow at a high level.

### Answer:

The flow is:


Text Input

↓

Tokenizer

↓

Token IDs

↓

Embedding Layer

↓

Transformer

↓

Next Token Prediction

↓

Generated Response


---

# Common Interview Mistakes

❌ "LLM searches the internet for answers."

Correct:

LLMs generate responses based on learned patterns unless connected to external tools.

---

❌ "Parameters store all sentences."

Correct:

Parameters store learned patterns.

---

❌ "LLM predicts the answer."

Correct:

LLM predicts the next token.