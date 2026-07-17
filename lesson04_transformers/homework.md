# Lesson 4 - Transformers Homework (With Answers)

## 🎯 Goal

The goal of this homework is to verify understanding of:

- Why Transformers replaced RNNs
- Self-Attention
- Query, Key, Value (QKV)
- Attention Scores and Attention Weights
- Multi-Head Attention
- Transformer Blocks
- Residual Connections
- Layer Normalization
- Feed Forward Network
- Decoder-Only Transformers
- GPT Next Token Prediction
- Training vs Inference

---

# Part 1: Transformer Fundamentals

---

## Q1. Why did RNNs struggle with long sentences?

### Answer:

RNNs process text sequentially, one word at a time.

Example:

```
I → love → artificial → intelligence
```

The model must remember previous words through its hidden state.

Problems:

- Long sentences can cause information loss.
- Earlier words become difficult to remember.
- Training is slow because words cannot be processed in parallel.
- Long-distance relationships between words are difficult to capture.

Transformers solve this using **Self-Attention**, where every word can directly interact with every other word.

---

# Q2. What problem does Self-Attention solve?

### Answer:

Self-Attention helps the model understand relationships between words regardless of their position in a sentence.

Example:

```
The dog chased the ball because it was tired.
```

The model needs to understand:

```
it → dog
```

Self-Attention assigns higher importance to relevant words and creates context-aware representations.

---

# Part 2: Embeddings and QKV

---

# Q3. Why can't Transformers directly use Token IDs?

### Answer:

Token IDs are only integer identifiers created by the tokenizer.

Example:

```
cat → 523
dog → 892
```

The numbers themselves have no meaning.

The Transformer needs embeddings because embeddings convert token IDs into dense vectors that capture semantic relationships.

Example:

```
cat embedding ≈ dog embedding

because both are animals
```

---

# Q4. Explain the Self-Attention process from embeddings to output.

### Answer:

The process:

```
Embedding Vectors

↓

Create Query, Key, Value

↓

Calculate Attention Scores

Q × Kᵀ

↓

Apply Softmax

↓

Attention Weights

↓

Multiply with Value

Attention Weights × V

↓

Context-aware Embedding
```

Explanation:

1. Embeddings represent token meaning.
2. The model creates Query, Key, and Value vectors.
3. Query and Key calculate how much attention each word should receive.
4. Softmax converts scores into probabilities.
5. Attention weights determine how much information to take from each Value vector.

---

# Q5. Explain Query, Key, and Value.

### Answer:

## Query (Q)

Represents:

"What information am I looking for?"

---

## Key (K)

Represents:

"What information do I contain?"

---

## Value (V)

Represents:

"The actual information passed forward."

---

Example:

Sentence:

```
The cat drank milk
```

The word "drank" creates a Query asking:

"What words help me understand my action?"

The Keys of "cat" and "milk" are compared with that Query.

---

# Q6. What is the difference between Attention Score and Attention Weight?

### Answer:

## Attention Score

Formula:

```
Q × Kᵀ
```

It measures similarity between Query and Key.

Example:

```
cat → drank = high score
```

---

## Attention Weight

Formula:

```
Softmax(Attention Scores)
```

It converts scores into probabilities.

Example:

Before:

```
cat-drank = 5.5
cat-milk = 2.0
```

After Softmax:

```
cat-drank = 85%
cat-milk = 15%
```

---

# Part 3: Multi-Head Attention

---

# Q7. Why do Transformers use Multi-Head Attention?

### Answer:

One attention mechanism may not capture all relationships in language.

Multiple heads allow the model to learn different patterns.

Example:

Head 1:

```
subject relationship

cat → drank
```

Head 2:

```
object relationship

drank → milk
```

Head 3:

```
grammar relationship

The → cat
```

The outputs from all heads are combined to create a richer representation.

---

# Q8. Why does every attention head have separate Wq, Wk, and Wv matrices?

### Answer:

Each attention head learns a different way of understanding relationships.

Separate matrices allow each head to create different Query, Key, and Value representations.

This allows the model to capture:

- Grammar
- Meaning
- Long-distance relationships
- Context

---

# Part 4: Transformer Block

---

# Q9. Why are Residual Connections used?

### Answer:

Residual connections preserve original information while adding new information learned by the layer.

Formula:

```
Output = Input + New Information
```

Benefits:

- Prevent information loss
- Improve gradient flow
- Help train deeper networks

---

# Q10. Why is Layer Normalization needed?

### Answer:

Layer Normalization keeps activations stable during training.

Without normalization:

```
Large values
Small values
```

can make training unstable.

Benefits:

- Faster training
- More stable learning
- Better convergence

---

# Q11. What is the purpose of Feed Forward Network (FFN)?

### Answer:

The Feed Forward Network transforms each token representation after attention.

Attention answers:

```
Which words are important?
```

FFN answers:

```
How should this information be processed?
```

It helps the model learn more complex patterns.

---

# Part 5: GPT Architecture

---

# Q12. Why is GPT called a Decoder-Only Transformer?

### Answer:

The original Transformer contains:

```
Encoder + Decoder
```

GPT uses only the decoder because its goal is text generation.

GPT predicts the next token using previous tokens.

Architecture:

```
Input

↓

Decoder Blocks

↓

Next Token
```

---

# Q13. What does GPT actually predict?

### Answer:

GPT predicts the next token.

It does not directly predict:

- Sentences
- Paragraphs
- Answers

Example:

Input:

```
The sky is
```

Prediction:

```
blue
```

Then:

```
The sky is blue
```

The process repeats.

---

# Q14. Explain Autoregressive Generation.

### Answer:

Autoregressive generation means each new token depends on previously generated tokens.

Example:

```
I love

↓

I love AI

↓

I love AI because

↓

I love AI because it
```

Each generated token becomes part of the next input.

---

# Q15. Why does GPT use Causal Masking?

### Answer:

Causal masking prevents GPT from seeing future tokens.

Example:

When predicting:

```
drank
```

GPT should not see:

```
milk
```

because that would be cheating.

It ensures generation happens from left to right.

---

# Part 6: Training vs Inference

---

# Q16. Explain Training vs Inference.

### Answer:

## Training

During training:

- Correct answer is known.
- Model prediction is compared with the actual token.
- Error is calculated.
- Weights are updated using backpropagation.

Example:

```
Input:

The cat

Prediction:

jumped ❌

Correct:

drank ✅
```

The model learns from the mistake.

---

## Inference

During inference:

- Model is already trained.
- No weight updates happen.
- Model generates text using previous predictions.

Example:

```
The cat

↓

jumped

↓

The cat jumped
```

If the prediction is wrong, it still continues.

---

# Q17. What is Teacher Forcing?

### Answer:

Teacher forcing is a training technique where the model receives the correct previous tokens instead of its own predictions.

Example:

Correct:

```
The cat drank milk
```

Prediction:

```
The cat jumped
```

During training, the model still receives:

```
The cat drank
```

This makes learning faster and more stable.

---

# Part 7: Complete GPT Pipeline

---

# Q18. Explain the complete GPT pipeline.

### Answer:

```
User Input

↓

Tokenizer

↓

Token IDs

↓

Embedding Lookup

↓

Embedding Vectors

↓

Transformer Blocks

↓

Linear Layer

↓

Vocabulary Logits

↓

Softmax

↓

Token Probability

↓

Next Token

↓

Repeat
```

Explanation:

1. Text is converted into tokens.
2. Tokens become embeddings.
3. Transformer blocks create contextual understanding.
4. Final layer predicts probabilities for every vocabulary token.
5. The highest probability token is selected.
6. Process repeats.

---

# Part 8: Reflection

---

## Q19. Explain GPT to a non-technical person.

### Answer:

GPT is like a very advanced autocomplete system.

It reads the words before a missing word and predicts what word is most likely to come next.

It learned language patterns by reading a huge amount of text.

---

## Q20. What was the biggest learning from this lesson?

### Answer:

The biggest learning is understanding that GPT is not searching for answers. It creates responses by repeatedly predicting the next token using:

- Embeddings
- Self-Attention
- Transformer Blocks
- Learned patterns from training

---

# ⭐ Lesson 4 Completed

Topics mastered:

✅ Transformer Architecture  
✅ Self-Attention  
✅ QKV  
✅ Attention Scores  
✅ Attention Weights  
✅ Multi-Head Attention  
✅ Residual Connections  
✅ Layer Normalization  
✅ Feed Forward Network  
✅ Decoder-Only Transformer  
✅ GPT Prediction Pipeline  
✅ Training vs Inference  
✅ Teacher Forcing  
