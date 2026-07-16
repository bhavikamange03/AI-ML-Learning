# Lesson 1 - LLM Basics Homework

## 🎯 Goal

The goal of this homework is to verify understanding of:

- What an LLM is
- How LLMs generate responses
- Tokens and context windows
- LLM memory vs application memory
- AI application architecture

---

# Part 1: Concept Understanding

## Q1. Explain LLM in your own words.

### Answer

An LLM (Large Language Model) is a deep learning model based on neural networks that is trained on a massive amount of text data. During training, it learns statistical patterns and relationships in language. When given a prompt, it predicts the most likely next token based on those learned patterns to generate a response.

---

## Q2. LLM Prediction

Consider this input:

```
The sun rises in the
```

### Answer

The main task of the LLM is to **predict the next token**.

It does **not**:
- Search the internet for every question.
- Retrieve a stored sentence from a database.

Instead, it uses the patterns learned during training to calculate the probability of possible next tokens. For this example, it may predict:

```
east
```

because that token has the highest probability in this context.

---

## Q3. Parameters

### What are parameters in an LLM?

Parameters are the internal numerical values that the model learns during training.

### Why are they important?

Parameters store learned language patterns and relationships. During training, they are updated continuously so the model becomes better at predicting the next token.

Parameters do **not** store complete sentences or facts. Instead, they encode patterns learned from the training data.

---

## Q4. Why is it called a Large Language Model?

It is called **Large** for two reasons:

1. **Large Training Dataset**
   - The model is trained on massive amounts of text such as books, articles, websites, and code.

2. **Large Number of Parameters**
   - Modern LLMs contain millions or billions of parameters that allow them to learn complex language patterns.

---

# Part 2: Token Understanding

## Q5. Why don't LLMs directly process words?

Computers cannot understand raw text. Neural networks perform mathematical operations on numbers, not words.

Therefore, text must first be converted into tokens and then into token IDs before it can be processed by the model.

---

## Q6. Token Example

Input:

```
I love artificial intelligence
```

Token IDs:

```
[10, 25, 103, 500]
```

### Answer

These numbers are called **token IDs**.

Each token ID represents a token in the tokenizer's vocabulary.

The numbers themselves do **not** have any meaning. They are simply identifiers used to look up the corresponding embedding vector inside the model.

---

# Part 3: Context Window

## Q7. What is a Context Window?

A context window is the amount of information (measured in tokens) that an LLM can consider while generating a response.

It may include:

- Current prompt
- Previous conversation
- Uploaded documents
- Retrieved information from the application

It is important because the model can only use information that is inside the current context window.

If information falls outside the context window, the model can no longer use it when generating responses.

---

## Q8. Practical Example

Conversation:

```
User:
My favorite programming language is Python.

AI:
Great!

User:
What language do I like?
```

### Answer

The model can answer **Python** because that information is still present in the current context window.

---

# Part 4: LLM Memory

## Q9. Short-Term vs Long-Term Memory

### Short-Term Memory

Short-term memory is the current conversation available inside the context window.

Example:

```
User:
My favorite language is Python.
```

The model can answer questions about it during the same conversation.

---

### Long-Term Memory

Long-term memory is implemented by the application, not by the LLM itself.

Examples:

- User name
- Learning goals
- Preferences
- Completed lessons
- Project progress

The application retrieves this information from a database and includes it in the prompt before sending the request to the LLM.

---

## Q10. AI Application Design

### Information to Store Permanently

- User name
- Learning goals
- Preferred programming language
- Completed lessons
- Weak topics
- Project progress

### Information Not to Store

- Temporary emotions
- Today's mood
- What the user had for lunch
- Temporary conversations with no future value

Permanent information helps personalize future interactions, while temporary information usually provides little long-term benefit.

---

# Part 5: Think Like an AI Engineer

## Q11. Design Question

The user says:

```
My goal is to become an AI engineer.
```

One month later:

```
What should I learn next?
```

### Answer

The application should store the user's learning goal in a database.

Architecture:

```
User

↓

Application

↓

Database
(Store learning goal)

↓

LLM

↓

Response
```

When the user returns, the application retrieves the stored learning goal and includes it in the prompt sent to the LLM.

The LLM then generates a response using both the current question and the retrieved information.

---

# Reflection

## 1. What was the most interesting concept from this lesson?

Understanding that an LLM does not memorize answers or search the internet. Instead, it predicts the next token using patterns learned during training.

---

## 2. What concept is still unclear?

I would like to understand in more depth how the transformer learns language patterns from embeddings and how attention works internally.

---

## 3. Explain an LLM to a non-technical person.

Imagine someone who has read millions of books and articles. Instead of memorizing every sentence, they learn how language is typically used. When you ask a question, they predict what words are most likely to come next based on everything they have learned. An LLM works in a similar way—it predicts the next token to generate meaningful responses.