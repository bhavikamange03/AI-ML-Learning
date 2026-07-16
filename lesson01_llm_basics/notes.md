# Lesson 1 - Large Language Model (LLM) Basics

## 🎯 Learning Objectives

By the end of this lesson, we should understand:

- What is Artificial Intelligence (AI)?
- What is Machine Learning (ML)?
- What is Deep Learning?
- What is a Large Language Model (LLM)?
- How does an LLM generate responses?
- What are parameters in an LLM?
- What is a context window?
- How does LLM memory work?
- Common misconceptions about LLMs

---

# 1. What is Artificial Intelligence (AI)?

Artificial Intelligence is the field of computer science that focuses on building systems that can perform tasks that normally require human intelligence.

Examples:

- Understanding language
- Recognizing images
- Making decisions
- Playing games
- Generating text

Examples of AI applications:

- Chatbots
- Recommendation systems
- Voice assistants
- Self-driving cars
- Image recognition

---

# 2. What is Machine Learning (ML)?

Machine Learning is a subset of AI where computers learn patterns from data instead of being explicitly programmed with every rule.

Traditional Programming:


Rules + Data
|
v
Output


Example:

A programmer writes rules:


If email contains "win money"
and many capital letters
then mark as spam


---

Machine Learning:


Data + Expected Results
|
v
Machine Learning Model
|
v
Learned Patterns


The model learns the rules automatically.

Example:

Provide thousands of:


Spam emails
Non-spam emails


The model learns patterns that identify spam.

---

# 3. What is Deep Learning?

Deep Learning is a subset of Machine Learning that uses neural networks with multiple layers.

Relationship:


Artificial Intelligence

    |
    v

Machine Learning

    |
    v

Deep Learning

    |
    v

Large Language Models


Deep learning models are good at handling:

- Text
- Images
- Audio
- Video

---

# 4. What is a Neural Network?

A neural network is a mathematical model inspired by how the human brain processes information.

It contains:

- Input layer
- Hidden layers
- Output layer

Example:


Input
|
v
Hidden Layer
|
v
Hidden Layer
|
v
Output


The model learns by adjusting internal values called parameters.

---

# 5. What is an LLM?

LLM stands for:

**Large Language Model**

An LLM is a deep learning model trained on a massive amount of text data to learn patterns in language.

Examples:

- ChatGPT
- Claude
- Gemini
- Llama

An LLM can perform tasks like:

- Answering questions
- Writing code
- Summarizing documents
- Translating languages
- Generating content

---

# 6. Why is it called "Large"?

The word "Large" refers to:

## 1. Large Training Dataset

LLMs are trained on huge amounts of text.

Examples:

- Books
- Websites
- Research papers
- Code repositories
- Articles

---

## 2. Large Number of Parameters

Parameters are internal values that the model learns during training.

Example:

A model may have:


Billions of parameters


These parameters store learned patterns.

Important:

Parameters are NOT stored sentences.

The model does not store:


"Paris is the capital of France"


Instead, it learns patterns that help it generate the correct response.

---

# 7. How Does an LLM Learn?

Training process:

Example:

Input:

The capital of France is _____

Expected answer: Paris

The model makes a prediction.

Initially:

Prediction:
London

Wrong.

The model calculates the error and adjusts its parameters.

After seeing billions of examples:

The model becomes better at predicting patterns.

---

# 8. What Does an LLM Actually Do?

The most important concept:

## An LLM predicts the next token.

Example:

Input:


The capital of France is


The model calculates probabilities:


Paris 95%
London 2%
Berlin 1%
Tokyo 1%


It selects a likely next token:


Paris


Then continues predicting:


The capital of France is Paris and it is...


---

Important:

An LLM does NOT:

❌ Search Google for every answer

❌ Think like a human

❌ Store every sentence from training data

It:

✅ Learns patterns from training data

✅ Uses those patterns to generate new text

---

# 9. What is a Token? (Introduction)

A token is the basic unit an LLM processes.

Models do not directly read words.

Text is converted into tokens.

Example:


I love AI


might become:


[I] [love] [AI]


or internally:


[5, 20, 101]


These numbers are called token IDs.

(Tokenization will be covered in Lesson 2.)

---

# 10. What is a Context Window?

A context window is the amount of information an LLM can consider at one time.

It is measured in tokens.

The context window includes:

- Current prompt
- Previous conversation
- Uploaded documents
- Additional information provided to the model

Example:

Conversation:


User:
My name is Bhavika.

AI:
Nice to meet you.

User:
What is my name?


If the previous message is inside the context window:

The model can answer:


Bhavika


If the information is outside the context window:

The model cannot access it.

---

# 11. LLM Memory vs Application Memory

## Short-Term Memory

The current conversation.

Example:


User:
My favorite language is Python.

Later:
What language do I like?


The model can answer because the information exists in the current context.

---

## Long-Term Memory

The application stores information separately.

Examples:


User name
Learning goals
Preferences
Completed lessons
Projects
Skills


Before sending a request to the LLM:

The application retrieves stored information and adds it to the prompt.

---

Architecture:


User

|
v

Application

|
+----------------+
| |
v v

Memory DB LLM

|
v

Response


---

# 12. Common Misconceptions

## Misconception 1:

"LLMs know everything."

Reality:

LLMs learn patterns from training data. They can make mistakes.

---

## Misconception 2:

"LLMs search the internet automatically."

Reality:

An LLM only uses information provided during training or additional tools connected by the application.

---

## Misconception 3:

"LLMs memorize all training data."

Reality:

LLMs learn statistical patterns and relationships between tokens.

---

## Misconception 4:

"More parameters always means better."

Reality:

Performance depends on:

- Training data quality
- Architecture
- Training methods
- Fine-tuning
- Evaluation

---

# 13. Complete LLM High-Level Flow


User Text

|
v

Tokenizer

|
v

Token IDs

|
v

Embedding Layer

|
v

Transformer Model

|
v

Predict Next Token

|
v

Generate Response


---

# 📝 Lesson 1 Key Takeaways

Remember these interview points:

1. An LLM is a deep learning model trained on massive text data.

2. An LLM learns patterns, not exact sentences.

3. The main task of an LLM is next-token prediction.

4. Parameters are learned values that store language patterns.

5. Text is converted into tokens before the model processes it.

6. Context window defines how much information the model can consider at once.

7. LLM memory and application memory are different concepts.

8. Tokenization, embeddings, and transformers are important components of the LLM pipeline.

---

# 🚀 Next Lesson

## Lesson 2: Tokenization

Topics:

- Why do LLMs use tokens?
- Character vs Word vs Subword tokenization
- Token IDs
- Vocabulary
- Byte Pair Encoding (BPE)
- Why tokenizer and LLM are tightly connected
