# Lesson 4: Transformers and Attention

# Part 1: Introduction to Transformers

---

# 🎯 Learning Objectives

By the end of this section, you will understand:

- Why transformers were introduced
- Problems with previous NLP models
- How RNNs process text
- Limitations of RNNs and LSTMs
- The main idea behind transformers
- What attention means intuitively
- How transformers understand relationships between words

---

# 1. What is a Transformer?

A Transformer is a deep learning architecture designed to understand and generate human language.

It was introduced in the 2017 research paper:

> "Attention Is All You Need"

Transformers became the foundation of modern AI models:

- GPT
- ChatGPT
- Claude
- Gemini
- Llama

---

# 2. Where Does Transformer Fit in the LLM Pipeline?

Let's connect previous lessons.

## Step 1: Text Input

Example:

```
The cat drinks milk.
```

↓

## Step 2: Tokenization

Text becomes tokens:

```
[
"The",
"cat",
"drinks",
"milk"
]
```

↓

## Step 3: Token IDs

Tokens become numbers:

```
[
52,
101,
450,
230
]
```

↓

## Step 4: Embeddings

Token IDs become vectors:

```
[
[0.21,0.45,...],
[0.12,0.67,...],
[0.91,0.22,...]
]
```

↓

## Step 5: Transformer

The transformer understands:

- Relationships between words
- Context
- Importance of each word

↓

## Step 6:

Predicts next token.

---

# 3. Before Transformers: RNNs

Before transformers, many NLP systems used:

- RNN (Recurrent Neural Network)
- LSTM
- GRU

These models processed text sequentially.

Example:

Sentence:

```
I love artificial intelligence
```

RNN processes:

```
I

↓

love

↓

artificial

↓

intelligence
```

Each word depends on the previous word.

---

# 4. How RNN Works

RNN maintains a hidden state.

Think of hidden state as:

> Memory of what the model has seen so far.

Example:

Input:

```
I
```

Hidden state:

```
Remember: user said "I"
```

Next:

```
love
```

Hidden state updates:

```
Remember:
"I love"
```

Next:

```
AI
```

Hidden state:

```
Remember:
"I love AI"
```

---

# 5. Problem with RNN: Long-Term Memory

RNNs struggle when important information appears far away.

Example:

```
The book that I bought yesterday from the store was expensive.
```

The important relationship:

```
book

↓

was expensive
```

The model needs to remember:

```
book
```

after many words.

But older information can become weaker.

This is called:

## Long-Term Dependency Problem

---

# 6. Problem with RNN: Sequential Processing

RNN processes one token at a time.

Example:

```
Token 1

↓

Token 2

↓

Token 3

↓

Token 4
```

The next token cannot start until the previous token finishes.

This makes training slower.

---

# 7. Problem with RNN: Limited Context Understanding

Consider:

```
The animal didn't cross the road because it was tired.
```

Question:

What does "it" refer to?

Possible answers:

```
animal

or

road
```

The model needs to understand relationships between words.

RNNs struggle because they rely heavily on previous hidden states.

---

# 8. Transformer Solution

Transformers introduced a new idea:

# Attention

Instead of reading words one by one:

```
The → cat → drinks → milk
```

Transformers look at relationships between all words.

Example:

```
The
 |
cat
 |
drinks
 |
milk
```

The model asks:

> Which words are important for understanding this word?

---

# 9. What is Attention?

Attention is a mechanism that allows the model to assign different importance scores to different words.

Example:

Sentence:

```
The cat drank milk.
```

When understanding:

```
drank
```

The model focuses more on:

```
cat

milk
```

and less on:

```
The
```

---

# 10. Human Example of Attention

Sentence:

```
I deposited money in the bank.
```

The word:

```
bank
```

has multiple meanings:

Meaning 1:

```
Financial institution
```

Meaning 2:

```
River side
```

A human uses surrounding words:

```
deposited

money
```

to understand:

```
bank = financial institution
```

Transformers use attention in a similar way.

---

# 11. Attention Creates Relationships

Without attention:

```
cat

dog
```

are only separate tokens.

With attention:

The model learns:

```
cat

↔

animal

↔

dog
```

because they appear in similar contexts.

---

# 12. Transformer vs RNN

| RNN | Transformer |
|---|---|
| Processes sequentially | Processes tokens together |
| Limited long-term memory | Handles long-range relationships |
| Slower training | Parallel processing |
| Uses hidden state | Uses attention |
| Struggles with long context | Better context understanding |

---

# 13. Complete Transformer Intuition

Think of reading a sentence.

RNN:

```
Read word 1

↓

Remember

↓

Read word 2

↓

Remember

↓

Read word 3
```

The memory can become weaker.

---

Transformer:

```
Read all words together

↓

Look at relationships

↓

Decide which words matter

↓

Understand context
```

---

# 14. Important Interview Concepts

## Question:

Why were transformers created?

Answer:

> Transformers were created to overcome limitations of sequential models like RNNs. They use self-attention to capture relationships between all tokens in a sequence and allow parallel processing, making training faster and improving long-range dependency understanding.

---

## Question:

What is the main innovation of transformers?

Answer:

> The main innovation is the attention mechanism, which allows the model to dynamically determine which words are important when processing each token.

---

# 15. Mental Model

Remember:

```
RNN:

One word at a time

↓

Memory


Transformer:

All words together

↓

Attention

↓

Relationships
```

---

# End of Part 1

Next:

# Part 2: Self-Attention and QKV

We will learn:

```
Embedding Vectors

↓

Query

Key

Value

↓

Attention Scores

↓

Softmax

↓

Weighted Representation
```

This is the core mechanism that makes ChatGPT possible.


# Part 2: Self-Attention and Query-Key-Value (QKV)

---

# 🎯 Learning Objectives

By the end of this section, we will understand:

- Why Transformers need attention
- What self-attention means
- Why embeddings alone are not enough
- What Query, Key, and Value represent
- How Q, K, V vectors are created
- How attention scores are calculated
- Difference between attention scores and attention weights
- How attention matrices work
- How self-attention creates context-aware representations

---

# 1. Why Do We Need Attention?

Before Transformers, many NLP models used RNNs.

RNNs process text sequentially:
The → dog → chased → the → ball


They maintain a hidden state to remember previous information.

However, RNNs struggle with long-distance relationships.

Example:


The dog chased the ball because it was tired.


Question:

What does "it" refer to?

Possible options:


dog

or

ball


A human understands:


dog was tired


because dog is an animal.

The model needs a mechanism to understand relationships between words.

This mechanism is:

# Self-Attention

---

# 2. What is Self-Attention?

Definition:

> Self-attention is a mechanism where each token looks at all other tokens in the sentence and decides which tokens are important for understanding its meaning.

Example:


The cat drank milk.


Focus on:


drank


The model asks:


Which words help me understand "drank"?


It looks at:


The
cat
milk


It learns:


cat → important

milk → important

The → less important


The word "drank" gets a new representation containing information from:


drank + cat + milk


---

# 3. Embedding vs Attention

## Embedding

From Lesson 3:

Embedding gives general meaning.

Example:


cat

↓

[0.2, 0.8, 0.5]


The vector represents:


General meaning of cat


However, embedding alone does not know the current sentence.

---

Example:

Sentence 1:


The cat drank milk.


Sentence 2:


The cat chased mouse.


The meaning of "cat" changes slightly based on context.

Attention creates:


Context-aware representation


---

# 4. Query, Key, Value (QKV)

Self-attention uses three vectors:


Query (Q)

Key (K)

Value (V)


A simple analogy:

## Search Engine Example

Imagine searching Google.

---

## Query

Your question:


Find machine learning courses


Query means:


What information am I looking for?


---

## Key

Information describing available documents:


Machine Learning Course

Cooking Course

History Course


Key means:


What information do I contain?


---

## Value

The actual information:


Course videos

Examples

Details


Value means:


What information should I provide?


---

# 5. QKV in Transformers

Every token embedding creates three different vectors:

          Embedding

              |
    -------------------
    |        |        |
    ↓        ↓        ↓

    Q        K        V

Meaning:


Query:

What am I looking for?

Key:

What do I represent?

Value:

What information should I pass?


---

# 6. How Are Query, Key, Value Created?

Important:

Q, K, and V are not manually created.

The model learns three weight matrices:


Wq

Wk

Wv


during training.

---

Mathematical representation:

Input embedding:


X


Query:


Q = X × Wq


Key:


K = X × Wk


Value:


V = X × Wv


---

Example:

Embedding:


cat

[0.5, 0.2, 0.8]


After applying weight matrices:


Query:

[0.4, 0.7]

Key:

[0.8, 0.1]

Value:

[0.6, 0.9]


---

# 7. How Are These Weights Learned?

Initially:


Embedding Matrix

Wq

Wk

Wv


are initialized with random numbers.

The model does not know language initially.

---

Training process:


Input text

↓

Transformer

↓

Prediction

↓

Compare with correct answer

↓

Calculate error

↓

Update weights


The model updates:


Embedding Matrix

Wq

Wk

Wv

Other Transformer parameters


This happens millions/billions of times.

---

# 8. Important: Parameters vs Calculations

## Learned Parameters

These are stored and updated during training:


Embedding Matrix

Wq

Wk

Wv


---

## Temporary Calculations

These are created for every input:


Query

Key

Value

Attention Score

Attention Weight


They are not stored.

---

# 9. Attention Score

Now the model needs to decide:


How related are two words?


It calculates:


Attention Score = Query × Keyᵀ


---

Example:

Sentence:


The cat drank milk.


Focus:


drank


The Query of "drank" compares with all Keys:


Query(drank) × Key(The)

Query(drank) × Key(cat)

Query(drank) × Key(milk)


Example scores:


The 0.2

cat 0.8

milk 0.9


Meaning:


cat and milk are more related to drank.


---

# 10. Attention Score vs Attention Weight

These two are different.

---

## Attention Score

Raw similarity value.

Example:


cat 8

milk 10

The 2


It answers:


How related are these words?


---

## Attention Weight

After applying Softmax.

Example:


cat 30%

milk 65%

The 5%


It answers:


How much importance should I give?


---

Relationship:


Attention Score

    ↓

 Softmax

    ↓

Attention Weight


---

# 11. Softmax

Why do we need Softmax?

Raw scores:


8

10

2


are difficult to use.

Softmax converts them into probabilities:


cat 30%

milk 65%

The 5%


Total:


100%


---

# 12. Using Values

Attention weights decide how much information to take from each Value.

Formula:


Output =

(weight × Value)

(weight × Value)

(weight × Value)


Example:


cat information × 30%

milk information × 65%

The information × 5%


The result:


Context-aware representation


---

# 13. Attention Matrix

So far we looked at one word.

Example:


drank → cat
drank → milk


But Transformers calculate attention for all words.

Sentence:


The cat drank milk


Every word creates:


Query

Key

Value


Every Query compares with every Key.

---

Example Attention Score Matrix:

          The   cat   drank  milk

The 0.8 0.2 0.1 0.1

cat 0.3 0.9 0.6 0.2

drank 0.1 0.8 0.7 0.9

milk 0.2 0.3 0.8 0.9


Rows represent:


Which word is asking?


Columns represent:


Which word is being attended to?


---

Example:

Row:


drank


means:


While understanding "drank":

The → low importance

cat → high importance

milk → high importance


---

# 14. Attention Weight Matrix

After Softmax:

          The    cat   drank  milk

The 80% 10% 5% 5%

cat 20% 50% 20% 10%

drank 5% 30% 20% 45%

milk 10% 15% 35% 40%


This represents:


How much attention each word gives to other words.


---

# 15. Complete Self-Attention Pipeline


Tokens

↓

Token Embeddings

↓

Create Q K V

↓

Q × Kᵀ

↓

Attention Score Matrix

↓

Softmax

↓

Attention Weight Matrix

↓

Multiply with Values

↓

Context-aware Representation


---

# 16. Why is it called Self-Attention?

Because a sentence attends to itself.

Example:


The cat drank milk


The word:


drank


looks at:


The

cat

milk


inside the same sentence.

Therefore:


Self + Attention


---

# ⭐ Part 2 Key Takeaways

Remember:

## 1. Embedding vs Attention

Embedding:


What is this word generally?


Attention:


What does this word mean in this sentence?


---

## 2. QKV

Query:


What information do I need?


Key:


What information do I contain?


Value:


What information should I pass?


---

## 3. Attention Score


Query × Key


Measures relationship.

---

## 4. Attention Weight


Softmax(Attention Score)


Determines importance.

---

## 5. Final Output

Weighted values create:


Context-aware token representation


---

# Interview One-Line Answer

> Self-attention allows each token to look at every other token and determine their importance. 

# Part 3: Multi-Head Attention & Transformer Block

---

# 🎯 Learning Objectives

By the end of this section, you will understand:

- Why one attention mechanism is not enough
- What Multi-Head Attention is
- How multiple attention heads work together
- Residual Connections (Skip Connections)
- Layer Normalization
- Feed Forward Network (FFN)
- Complete Transformer Block
- How GPT is built by stacking Transformer blocks

---

# 1. Why Isn't One Attention Head Enough?

In Part 2, we learned that self-attention helps each word understand its relationship with every other word.

Example:

```
The dog chased the ball because it was tired.
```

Attention helps determine:

```
it → dog
```

But language contains many different types of relationships.

For example:

- Grammar
- Semantic meaning
- Subject–Verb relationships
- Object relationships
- Position in the sentence
- Long-distance dependencies

Trying to learn all of these using one attention mechanism is difficult.

Instead, Transformers use **Multiple Attention Heads**.

---

# 2. What is Multi-Head Attention?

Instead of running one self-attention mechanism, the Transformer runs several attention mechanisms **in parallel**.

```
                 Input Embeddings
                        │
        ┌───────────────┼───────────────┐
        │               │               │
        ▼               ▼               ▼
      Head 1         Head 2         Head 3
        │               │               │
        ▼               ▼               ▼
    Self-Attention  Self-Attention  Self-Attention
        │               │               │
        └───────────────┼───────────────┘
                        ▼
                 Concatenate Outputs
                        ▼
                  Linear Projection
                        ▼
            Multi-Head Attention Output
```

Each attention head learns a different way of understanding the sentence.

---

# 3. What Does Each Head Learn?

The Transformer is **not programmed** to assign a specific job to each head.

Instead, during training, each head naturally specializes.

Example:

Sentence:

```
The cat drank milk.
```

Possible behaviors:

### Head 1

Focuses on:

```
cat → drank
```

Learns:

```
Who performed the action?
```

---

### Head 2

Focuses on:

```
drank → milk
```

Learns:

```
What was consumed?
```

---

### Head 3

Focuses on nearby words.

Example:

```
The ↔ cat
```

Useful for grammar.

---

### Head 4

Focuses on long-distance relationships.

Example:

```
The dog chased the ball because it was tired.
```

Learns:

```
it → dog
```

---

# Important

The model never receives instructions like:

```
Head 1 = Grammar

Head 2 = Meaning

Head 3 = Position
```

Instead, these behaviors **emerge automatically** during training.

---

# 4. How Multi-Head Attention Works

From Part 2:

Each token embedding creates:

```
Query

Key

Value
```

using learned matrices.

For Multi-Head Attention, **each head has its own matrices**.

## Head 1

```
Q₁ = X × Wq₁

K₁ = X × Wk₁

V₁ = X × Wv₁
```

---

## Head 2

```
Q₂ = X × Wq₂

K₂ = X × Wk₂

V₂ = X × Wv₂
```

---

## Head 3

```
Q₃ = X × Wq₃

K₃ = X × Wk₃

V₃ = X × Wv₃
```

Every head learns different projections of the same embeddings.

---

# 5. Why Is Multi-Head Attention Better?

Imagine four detectives investigating the same case.

Detective 1:

Looks for fingerprints.

Detective 2:

Looks for DNA.

Detective 3:

Interviews witnesses.

Detective 4:

Checks CCTV footage.

Each detective finds different evidence.

Combining all evidence gives a better understanding.

Multi-Head Attention works the same way.

Each head contributes a different perspective.

---

# 6. Combining the Heads

Each attention head produces an output.

```
Head 1 Output

Head 2 Output

Head 3 Output

Head 4 Output
```

These outputs are:

1. Concatenated
2. Passed through another linear layer

Result:

```
Final Multi-Head Attention Output
```

Diagram:

```
Head 1 Output ─┐
               │
Head 2 Output ─┼──► Concatenate ─► Linear Layer ─► Final Output
               │
Head 3 Output ─┤
               │
Head 4 Output ─┘
```

---

# 7. Residual Connections (Skip Connections)

## Why do we need Residual Connections?

As Transformers become deeper (dozens or even hundreds of layers), useful information can gradually disappear.

Instead of replacing the original representation, Transformers keep it.

Without Residual Connection:

```
Input

↓

Attention

↓

Output
```

The original representation is lost.

---

With Residual Connection:

```
               Input
                 │
                 │───────────────┐
                 ▼               │
        Multi-Head Attention      │
                 │               │
                 ▼               │
        Attention Output          │
                 │               │
                 └───────► Add ◄─┘
                          │
                          ▼
                       Output
```

Formula:

```
Output = Input + Attention Output
```

The model keeps:

- Original information
- Newly learned contextual information

---

# Example

Suppose:

Input vector:

```
[1.2, 0.5, 0.8]
```

Attention output:

```
[0.3, -0.1, 0.4]
```

Residual output:

```
[1.2,0.5,0.8]

+

[0.3,-0.1,0.4]

=

[1.5,0.4,1.2]
```

The original information is preserved while adding new context.

---

# Why Residual Connections Matter

Residual connections:

- Preserve useful information
- Improve gradient flow
- Make very deep Transformers easier to train
- Reduce information loss

Without them, modern GPT models would be much harder to train.

---

# 8. Layer Normalization

After adding vectors, values can become very large or very small.

Example:

Before normalization:

```
[3500, -700, 1800]
```

or

```
[0.00002, -0.00001, 0.00004]
```

These unstable values make training difficult.

---

Layer Normalization rescales the values.

Example:

Before:

```
[3500, -700, 1800]
```

After:

```
[0.81, -1.12, 0.31]
```

The relationships remain similar, but the scale becomes stable.

---

# Why Layer Normalization?

Benefits:

- Stable training
- Faster convergence
- Prevents exploding or shrinking values
- Improves learning in deep networks

---

# 9. Feed Forward Network (FFN)

Many beginners think attention does everything.

It doesn't.

Attention answers:

> Which tokens are important?

The Feed Forward Network answers:

> How should I process this information?

---

A Feed Forward Network is a small neural network applied **independently to each token**.

```
Input

↓

Linear Layer

↓

Activation Function (GELU/ReLU)

↓

Linear Layer

↓

Output
```

---

Example

Suppose attention produces:

```
cat

↓

[0.5, 0.8, 0.2]
```

The FFN transforms it into:

```
[0.9, 0.3, 0.7]
```

The token representation becomes richer and more expressive.

---

# Attention vs Feed Forward Network

Attention:

```
Find relationships between different tokens.
```

Feed Forward Network:

```
Transform each token independently.
```

Analogy:

Attention:

```
Collect ingredients.
```

Feed Forward Network:

```
Cook the meal.
```

Both are necessary.

---

# 10. Complete Transformer Block

One Transformer block consists of:

```
                    Input
                      │
                      ▼
          Multi-Head Attention
                      │
                      ▼
              Add (Residual)
                      │
                      ▼
            Layer Normalization
                      │
                      ▼
          Feed Forward Network
                      │
                      ▼
              Add (Residual)
                      │
                      ▼
            Layer Normalization
                      │
                      ▼
                    Output
```

This output becomes the input to the next Transformer block.

---

# 11. Stacking Transformer Blocks

GPT is **not a single Transformer block**.

It stacks many identical Transformer blocks.

```
Input Text

↓

Tokenizer

↓

Token IDs

↓

Embeddings

↓

Transformer Block 1

↓

Transformer Block 2

↓

Transformer Block 3

↓

...

↓

Transformer Block N

↓

Prediction Layer

↓

Next Token
```

Each block produces a richer understanding of the input.

---

# 12. Why Are Multiple Transformer Blocks Needed?

Each block learns increasingly abstract information.

Example:

### Block 1

Learns:

```
Nearby relationships
```

---

### Block 2

Learns:

```
Grammar
```

---

### Block 3

Learns:

```
Meaning
```

---

### Higher Blocks

Learn:

- Long-range dependencies
- Reasoning
- Context
- Complex language patterns

The deeper the model, the more sophisticated the learned representations become.

---

# ⭐ Key Takeaways

✅ One attention head cannot capture every type of relationship.

✅ Multi-Head Attention allows multiple perspectives.

✅ Each head has its own learned Q, K, and V matrices.

✅ Residual Connections preserve information and improve training.

✅ Layer Normalization stabilizes the values after each major operation.

✅ Feed Forward Networks transform each token independently after attention.

✅ A Transformer block consists of:

- Multi-Head Attention
- Residual Connection
- Layer Normalization
- Feed Forward Network
- Residual Connection
- Layer Normalization

✅ GPT is built by stacking many Transformer blocks together.

---

# 📌 Interview Summary

### Q1. Why does a Transformer use multiple attention heads?

**Answer:**

Multiple attention heads allow the model to learn different types of relationships between tokens simultaneously, such as semantic meaning, grammar, and long-distance dependencies.

---

### Q2. What is the purpose of a Residual Connection?

**Answer:**

Residual connections add the original input back to the output of a layer. This preserves useful information, improves gradient flow during backpropagation, and makes deep Transformer models easier to train.

---

### Q3. Why is Layer Normalization used?

**Answer:**

Layer normalization stabilizes the values inside the network, leading to faster and more stable training while preventing extremely large or small activations.

---

### Q4. What is the role of the Feed Forward Network?

**Answer:**

The Feed Forward Network processes each token independently after attention, transforming its representation into richer features before passing it to the next Transformer layer.