# Lesson 3 - Embeddings


# Part 1: Embedding Fundamentals

# 🎯 Learning Objectives

By the end of this lesson, you should be able to answer the following questions confidently:

- What is an embedding?
- Why are token IDs not enough for an LLM?
- What is the difference between a token ID and an embedding?
- Why do we need dense vectors?
- How do embeddings help a model understand relationships between words?
- Why are similar words represented by similar vectors?
- How do embeddings fit into the complete LLM pipeline?

---

# What is an Embedding?

An **embedding** is a numerical representation (vector) of a token that captures its **meaning** and **relationship** with other tokens.

Instead of representing a word as just a number, an embedding represents it as **hundreds or thousands of numbers** that encode semantic information.

For example:

```
cat
```

is **not** represented as:

```
17
```

Instead it might be represented as:

```
[0.21, -0.88, 1.42, 0.56, ..., 0.91]
```

This list of numbers is called an **embedding vector**.

Each number is called a **dimension** of the vector.

Modern embedding vectors often have:

- 384 dimensions
- 768 dimensions
- 1024 dimensions
- 1536 dimensions
- 3072 dimensions

depending on the model.

---

# Why Do We Need Embeddings?

Let's think like engineers.

Suppose our tokenizer produced:

```
I love AI

↓

[5, 20, 101]
```

The transformer receives:

```
5
20
101
```

Now imagine you are the transformer.

What can you understand from these numbers?

```
5
20
101
```

Nothing.

These are simply integers.

Does **101** mean AI?

No.

Does **20** mean love?

No.

The numbers themselves contain **no meaning**.

They are simply identifiers.

---

## Think About This

Suppose I tell you:

```
Person A
↓

Employee ID = 1057
```

Can you tell me:

- Their age?
- Their profession?
- Their personality?
- Their hobbies?

Of course not.

The employee ID is simply an identifier.

Token IDs work exactly the same way.

---

# Why Token IDs Are Not Enough

Let's consider three words.

```
cat

dog

pizza
```

Suppose the tokenizer assigns:

| Word | Token ID |
|------|---------:|
| cat | 15 |
| dog | 42 |
| pizza | 200 |

The transformer receives:

```
15

42

200
```

Can it tell that:

- cat and dog are animals?
- cat and dog are more similar than cat and pizza?

No.

Because:

```
15

42

200
```

are arbitrary numbers.

The tokenizer could just as easily assign:

| Word | Token ID |
|------|---------:|
| cat | 800 |
| dog | 3 |
| pizza | 91 |

Nothing changes.

The IDs are only labels.

The numerical values themselves do **not** carry semantic information.

---

# The Big Problem

If the transformer only receives:

```
[15, 42, 200]
```

it has no idea that:

```
cat

↓

animal
```

or

```
dog

↓

pet
```

or

```
pizza

↓

food
```

The transformer needs **meaning**, not identifiers.

This is exactly why embeddings exist.

---

# The Solution: Embeddings

Instead of giving the transformer:

```
15
```

we give it something like:

```
[0.82,
-0.15,
0.63,
...
]
```

Instead of:

```
42
```

we give:

```
[0.79,
-0.18,
0.59,
...
]
```

Notice something interesting.

The vectors for **cat** and **dog** look similar.

That is intentional.

During training, the model learns that:

```
cat

↓

animal

↓

pet
```

and

```
dog

↓

animal

↓

pet
```

appear in similar contexts.

Therefore their vectors become similar.

---

# Intuition: Why Similar Words Have Similar Vectors

Imagine organizing a library.

Books about cooking are placed together.

Books about mathematics are placed together.

Books about history are placed together.

You don't randomly place books.

You organize them based on similarity.

Embeddings work in a similar way.

Instead of organizing books,

they organize **words**.

Example:

```
          Animals

      cat

          dog

             lion



            Food

        pizza

          burger



          Vehicles

          car

        bicycle
```

Words with similar meanings are located close together in vector space.

---

# Dense Vectors

An embedding is called a **dense vector**.

But what does "dense" mean?

Let's compare two types of vectors.

---

## Sparse Vector

Imagine we have 10 dimensions.

```
[0,0,0,1,0,0,0,0,0,0]
```

Most values are zero.

This is called a **sparse vector**.

---

## Dense Vector

Now consider:

```
[0.42,
-0.81,
0.19,
0.55,
-0.12,
0.63,
0.04,
-0.37,
0.91,
0.28]
```

Almost every value contains useful information.

This is called a **dense vector**.

Modern embeddings are dense vectors because information is distributed across many dimensions.

---

# Why Dense Vectors Are Powerful

Suppose we want to describe a person.

Instead of one number,

we describe many characteristics:

```
Height

Weight

Age

Strength

Speed

Confidence

Creativity
```

Each characteristic adds more information.

Similarly,

an embedding vector uses hundreds of dimensions to describe different aspects of a word's meaning.

The model learns these dimensions automatically during training.

Humans cannot usually assign a specific meaning to each dimension.

Instead, the **combination of all dimensions** captures semantic information.

---

# Token ID vs Embedding

This is one of the most common interview questions.

| Token ID | Embedding |
|----------|-----------|
| Created by the tokenizer | Learned during training |
| Integer | Dense vector |
| Identifier | Semantic representation |
| No meaning | Contains learned meaning |
| Used for lookup | Used by the transformer |

Example:

```
Word

↓

cat

↓

Tokenizer

↓

Token ID = 15

↓

Embedding Lookup

↓

[0.82, -0.15, 0.63, ...]
```

Notice the two separate steps.

The tokenizer only assigns the ID.

The embedding layer converts that ID into a meaningful vector.

---

# Real-Life Analogy

Imagine a school.

Every student has:

```
Student ID
```

Example:

```
Alice

↓

Student ID = 105
```

The ID only identifies Alice.

It tells you nothing about her.

Now imagine a detailed student profile.

```
Academic Performance

Sports Skills

Creativity

Leadership

Communication

Mathematics

Programming
```

This profile contains meaningful information.

Similarly:

```
Token ID

↓

Identifier
```

```
Embedding

↓

Meaningful profile
```

The transformer needs the **profile**, not just the ID.

---

# Visual Summary

```
Human Text

↓

Tokenizer

↓

Token IDs

↓

Embedding Lookup

↓

Dense Vectors

↓

Transformer

↓

Next Token Prediction
```

Everything after the tokenizer works with vectors—not raw text and not token IDs alone.

---

# ⭐ Interview Tip

If an interviewer asks:

> **Why can't an LLM directly use token IDs?**

A strong answer is:

> Token IDs are arbitrary identifiers created by the tokenizer. They contain no semantic information about the words they represent. The embedding layer converts each token ID into a dense vector that captures semantic relationships learned during training. These vectors allow the transformer to understand similarities and patterns between words.

---

# 📝 Key Takeaways

- A token ID is only an identifier.
- Token IDs do not contain meaning.
- Embeddings are dense vectors that represent semantic meaning.
- Similar words have similar embedding vectors.
- The transformer operates on embeddings, not raw token IDs.
- Embeddings are learned during training and improve as the model learns language patterns.

---

# 🚀 Coming Up Next

In the next section, we'll answer some of the most common questions beginners have:

- What is an Embedding Matrix?
- How does Embedding Lookup work?
- Why are embeddings initialized randomly?
- How does the model learn better embeddings during training?
- Why do similar words move closer together over time?

...


# Part 2: Embedding Matrix and Training

---

# Embedding Matrix

Now that we know **what an embedding is**, the next question is:

> **Where do these embedding vectors come from?**

The answer is:

**The Embedding Matrix.**

An **Embedding Matrix** is a large table where **each row corresponds to one token in the tokenizer's vocabulary**, and **each row stores that token's embedding vector**.

Think of it as a giant lookup table.

For example, suppose our tokenizer vocabulary contains only five words.

| Token ID | Token | Embedding Vector |
|---------:|-------|------------------|
| 0 | cat | [0.82, -0.15, 0.63, 0.21] |
| 1 | dog | [0.79, -0.18, 0.59, 0.30] |
| 2 | pizza | [-0.42, 1.11, -0.83, 0.77] |
| 3 | king | [0.91, -0.42, 0.66, -0.18] |
| 4 | queen | [0.88, -0.40, 0.69, -0.15] |

This table is called the **Embedding Matrix**.

Notice something important:

The tokenizer **does not create these vectors**.

It only creates the **Token IDs**.

The embedding matrix belongs to the **LLM**, not the tokenizer.

---

# What Does an Embedding Matrix Look Like?

Imagine our vocabulary contains **50,000 tokens**.

Suppose each embedding has **768 dimensions**.

Then the embedding matrix has:

```
50,000 rows

×

768 columns
```

Visually:

```
                Dimension

        1      2      3      4   ...   768

cat    0.82  -0.15   0.63   0.21 ...

dog    0.79  -0.18   0.59   0.30 ...

pizza -0.42   1.11  -0.83   0.77 ...

king   0.91  -0.42   0.66  -0.18 ...

queen  0.88  -0.40   0.69  -0.15 ...
```

Every row represents **one token**.

Every column represents **one learned feature**.

We usually **cannot interpret a single dimension**.

Instead, the **entire vector together** represents the word's meaning.

---

# Vocabulary Size vs Embedding Dimension

These two concepts are often confused.

## Vocabulary Size

The number of tokens known by the tokenizer.

Example:

```
Vocabulary Size

↓

50,000 tokens
```

---

## Embedding Dimension

The length of each embedding vector.

Example:

```
Embedding Dimension

↓

768 numbers
```

Example matrix:

```
50,000 × 768
```

Meaning:

- 50,000 rows
- 768 columns

---

# Embedding Lookup

Now imagine the tokenizer processes this sentence:

```
I love AI
```

It converts it into:

```
[5, 20, 101]
```

The transformer still cannot understand these IDs.

So what happens next?

The model performs an **Embedding Lookup**.

It uses each token ID to retrieve the corresponding vector from the embedding matrix.

```
Token IDs

↓

5

↓

Embedding Matrix

↓

[0.18, -0.22, 0.91, ...]



20

↓

Embedding Matrix

↓

[-0.64, 0.44, -0.18, ...]



101

↓

Embedding Matrix

↓

[0.81, 0.29, -0.55, ...]
```

The transformer now receives:

```
[
 [0.18, -0.22, 0.91, ...],
 [-0.64, 0.44, -0.18, ...],
 [0.81, 0.29, -0.55, ...]
]
```

Instead of integers, it now works with meaningful vectors.

---

# Complete Pipeline So Far

```
User Text

↓

Tokenizer

↓

Tokens

↓

Token IDs

↓

Embedding Lookup

↓

Embedding Vectors

↓

Transformer
```

Notice:

The tokenizer's job is finished after producing token IDs.

Everything after that is handled by the LLM.

---

# Where Do These Vectors Come From?

This is one of the biggest questions beginners ask.

When the model is first created...

Does it already know what "cat" means?

**No.**

Does it know "king" is related to "queen"?

**No.**

Does it know "car" is similar to "automobile"?

**No.**

Initially, the model knows **nothing**.

---

# How Are Embeddings Initialized?

At the beginning of training, every token receives a **random vector**.

Example:

```
cat

↓

[0.12,
-0.44,
0.37,
0.91]
```

```
dog

↓

[-0.73,
0.16,
-0.29,
0.51]
```

```
pizza

↓

[0.81,
-0.62,
0.10,
-0.14]
```

These numbers are **random**.

They contain **no meaning**.

---

# Why Random Numbers?

A common question is:

> Why not initialize them with meaningful values?

Because the model hasn't learned anything yet.

Imagine the first day of school.

A student has never studied mathematics.

Would you expect them to already know calculus?

Of course not.

Similarly, on the first day of training:

- the model doesn't know language,
- doesn't know grammar,
- doesn't know semantics,
- doesn't know relationships between words.

Random initialization gives every token a starting point.

Training gradually improves these vectors.

---

# How Embeddings Are Learned During Training

This is where the magic happens.

Suppose the training sentence is:

```
The cat drinks milk.
```

The model predicts the next token.

Maybe it predicts:

```
water
```

But the correct answer is:

```
milk
```

The prediction is wrong.

The model calculates the error.

```
Prediction

↓

Wrong

↓

Calculate Error

↓

Update Parameters
```

One of the parameters that gets updated is the **Embedding Matrix**.

The vector for **cat** changes slightly.

The vector for **milk** changes slightly.

Many other model parameters also change.

---

# Tiny Improvements

Training does **not** completely replace vectors.

Instead, it makes **very small adjustments**.

Imagine the embedding for "cat" starts as:

```
[0.12,
-0.44,
0.37]
```

After one update:

```
[0.13,
-0.43,
0.36]
```

After another update:

```
[0.15,
-0.41,
0.38]
```

Each change is tiny.

But training may repeat this process **billions of times**.

Eventually, the vectors begin to capture semantic meaning.

---

# Why Do Similar Words Become Similar?

Suppose the model repeatedly sees sentences like:

```
The cat drank milk.

The dog drank milk.

The cat chased the mouse.

The dog chased the ball.
```

Notice that **cat** and **dog** appear in similar contexts.

Because of this, their embedding vectors gradually become closer together.

On the other hand:

```
pizza
```

appears in very different contexts.

So its vector remains farther away.

This is why:

```
cat

↓

dog

(close)

```

but

```
cat

↓

pizza

(far apart)
```

---

# Learning Through Context

The key idea is:

**Words that appear in similar contexts learn similar embeddings.**

This is one of the fundamental ideas in Natural Language Processing (NLP).

Examples:

```
king

queen

prince

princess
```

appear in similar contexts.

Therefore, they end up with similar vectors.

Likewise:

```
car

truck

bus

vehicle
```

also become close together.

---

# Real-Life Analogy

Imagine moving into a new neighborhood.

On Day 1, you know no one.

Everyone is a stranger.

As months pass:

- You meet your neighbors.
- You discover shared interests.
- You become closer to some people than others.

Eventually, you naturally group people based on similarity.

Embeddings learn in the same way.

Initially, every word is "a stranger."

Over millions of training examples, the model gradually learns which words belong together.

---

# Visual Example

**Before Training**

```
cat        *

dog                     *

pizza   *

king                         *

queen       *
```

Everything is randomly placed.

---

**After Training**

```
Animals

cat *

dog *

lion *

-------------------------

Royal Family

king *

queen *

prince *

-------------------------

Food

pizza *

burger *

pasta *
```

Now similar words are grouped together because the model learned from context.

---

# ⭐ Interview Tip

If an interviewer asks:

> **How are embeddings learned?**

A strong answer is:

> Embeddings are initialized with random values. During training, the model predicts the next token, compares its prediction with the correct token, calculates the error, and updates the embedding vectors along with other model parameters using backpropagation and gradient descent. After millions or billions of updates, similar words develop similar embeddings because they frequently appear in similar contexts.

---

# 📝 Key Takeaways

- The **Embedding Matrix** stores an embedding vector for every token.
- The tokenizer creates **Token IDs**, not embeddings.
- **Embedding Lookup** retrieves the correct vector for each token ID.
- Embeddings start as **random vectors**.
- During training, they are updated little by little.
- Similar words become close together because they appear in similar contexts.
- The transformer always processes **embedding vectors**, not token IDs.

---

# 🚀 Coming Up Next

In the next section, we'll explore:

- Cosine Similarity
- Measuring semantic similarity between vectors
- Why "king" is closer to "queen" than to "pizza"
- Sentence embeddings vs token embeddings
- Real-world applications in RAG and Vector Databases
```


# Part 3: Similarity Search and RAG

---

# Cosine Similarity

Now that we have embedding vectors, the next question is:

> **How do we compare two embeddings?**

Suppose we have the embeddings for:

```
king
queen
apple
car
```

How can the computer determine that:

- king is closer to queen
- king is farther from apple

The answer is **Cosine Similarity**.

---

# What is Cosine Similarity?

Cosine Similarity is a mathematical measure that tells us **how similar two vectors are by comparing the angle between them**, not their lengths.

It answers the question:

> **Are these two vectors pointing in the same direction?**

If two vectors point in almost the same direction, they represent similar meanings.

---

# Why Not Use Normal Distance?

Imagine two vectors:

```
A = [1, 1]

B = [100, 100]
```

If we calculate the Euclidean distance, the vectors appear far apart because B is much longer.

However, both vectors point in exactly the same direction.

```
          B
         ↗
        /
       /
      /
     /
    /
   ↗ A
```

Although their magnitudes are different, they represent the same direction.

Cosine Similarity focuses on **direction**, which is more useful for comparing meanings.

---

# Cosine Similarity Formula

The mathematical formula is:

```
            A · B
--------------------------------
||A|| × ||B||
```

Where:

- **A · B** = Dot Product
- **||A||** = Magnitude (Length) of A
- **||B||** = Magnitude (Length) of B

You don't need to memorize the formula for interviews.

Instead, understand what it means.

---

# Understanding the Formula

The numerator:

```
A · B
```

Measures how much two vectors point in the same direction.

The denominator:

```
||A|| × ||B||
```

Normalizes the result so that vector length does not affect similarity.

This ensures we compare **meaning**, not size.

---

# Cosine Similarity Range

The result always lies between:

| Value | Meaning |
|------:|---------|
| 1 | Exactly the same direction |
| 0 | No relationship |
| -1 | Opposite directions |

Example:

```
king ↔ queen

≈ 0.82
```

Very similar.

```
king ↔ man

≈ 0.65
```

Somewhat similar.

```
king ↔ apple

≈ 0.18
```

Not very similar.

---

# Visualizing Cosine Similarity

### Similar Vectors

```
A ↗
B ↗
```

Small angle.

High similarity.

---

### Unrelated Vectors

```
A →

B ↑
```

90° angle.

Similarity ≈ 0.

---

### Opposite Vectors

```
A →

← B
```

180° angle.

Similarity = -1.

---

# Python Example

```python
import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )
```

This is exactly what we used in our coding assignment.

---

# Similarity Search

Now suppose we have embeddings for many words.

```
king
queen
man
woman
apple
car
computer
```

A user asks:

> Find the word most similar to "king".

The steps are:

```
Generate embedding for "king"

↓

Compare with every other embedding

↓

Calculate cosine similarity

↓

Sort by highest score

↓

Return the closest words
```

Example:

| Word | Similarity |
|------|-----------:|
| queen | 0.82 |
| man | 0.66 |
| woman | 0.61 |
| apple | 0.19 |
| car | 0.12 |

The model correctly returns:

```
queen
```

---

# Why Similarity Search Matters

Traditional search engines rely on exact keywords.

Example:

```
Document:

How to repair your car.
```

User searches:

```
How do I fix my automobile?
```

Keyword search struggles because:

```
car ≠ automobile
repair ≠ fix
```

Even though both sentences mean the same thing.

---

# Semantic Search

Embeddings solve this problem.

Instead of comparing words directly, we compare their embeddings.

```
repair

↓

Embedding

≈

fix
```

```
car

↓

Embedding

≈

automobile
```

Now the search engine understands the meaning instead of exact words.

This is called **Semantic Search**.

---

# Real-World Example

Suppose a customer asks:

```
My laptop battery drains quickly.
```

The knowledge base contains:

```
How to improve notebook battery life.
```

Even though:

```
laptop ≠ notebook
```

the embeddings are similar.

Therefore the correct article is retrieved.

---

# Where Is Semantic Search Used?

Semantic search is used in:

- Google Search
- ChatGPT
- GitHub Copilot
- Amazon Product Search
- Netflix Recommendations
- Spotify Music Search
- Customer Support Systems

Any application that searches by meaning instead of exact words uses embeddings.

---

# Embeddings in RAG

One of the biggest applications of embeddings is **Retrieval-Augmented Generation (RAG).**

Suppose we have thousands of documents.

```
Document 1

Document 2

Document 3

...

Document 10,000
```

The LLM cannot read every document for every question.

Instead, we first find only the most relevant documents.

How?

Using embeddings.

---

# RAG Pipeline

```
User Question

↓

Generate Question Embedding

↓

Vector Database

↓

Similarity Search

↓

Retrieve Top Documents

↓

Send Documents to LLM

↓

Generate Answer
```

Notice:

The LLM only reads the retrieved documents.

This makes RAG:

- Faster
- Cheaper
- More accurate
- Able to answer questions about private data

---

# Example

Question:

```
How can I reset my password?
```

Every document has already been converted into embeddings.

The question is also converted into an embedding.

The system compares:

```
Question Embedding

↓

Document Embeddings

↓

Cosine Similarity
```

The documents with the highest similarity scores are retrieved.

Those documents are then sent to the LLM as additional context.

---

# Embeddings in Vector Databases

Imagine storing one million document embeddings.

```
[0.18, -0.22, ...]

[0.63, 0.51, ...]

[-0.44, 0.29, ...]

...
```

Searching through all of them one by one would be too slow.

A **Vector Database** is designed to store and search embeddings efficiently.

Examples include:

- Pinecone
- Weaviate
- Milvus
- Qdrant
- ChromaDB
- FAISS (library)

Instead of searching text, these systems search vectors.

---

# Traditional Database vs Vector Database

| Traditional Database | Vector Database |
|----------------------|-----------------|
| Stores rows and columns | Stores embedding vectors |
| SQL queries | Similarity search |
| Exact matching | Semantic matching |
| Text search | Vector search |

---

# Sentence Embeddings vs Token Embeddings

This is a common interview topic.

## Token Embeddings

Each token gets its own embedding.

Example:

```
I love AI
```

Tokenizer:

```
I

love

AI
```

Each token has its own vector.

The transformer processes all token embeddings.

---

## Sentence Embeddings

Sometimes we need one vector for an entire sentence.

Example:

```
I love learning AI.
```

↓

One embedding vector.

This vector represents the meaning of the complete sentence.

Sentence embeddings are commonly generated using models like:

- Sentence-BERT (SBERT)
- all-MiniLM-L6-v2
- OpenAI embedding models

---

# When Do We Use Each?

| Task | Token Embeddings | Sentence Embeddings |
|------|------------------|---------------------|
| Next-token prediction | ✅ | ❌ |
| LLM training | ✅ | ❌ |
| Semantic search | ❌ | ✅ |
| RAG | ❌ | ✅ |
| Document retrieval | ❌ | ✅ |
| Similarity search | ❌ | ✅ |

---

# Putting Everything Together

Suppose a user asks:

```
How do I repair my automobile?
```

The pipeline is:

```
Question

↓

Sentence Embedding

↓

Vector Database

↓

Similarity Search

↓

Relevant Documents

↓

LLM

↓

Final Answer
```

Without embeddings, the system would rely only on exact keyword matches and often miss relevant information.

---

# ⭐ Interview Tip

If an interviewer asks:

> **Why do we use cosine similarity instead of Euclidean distance?**

A strong answer is:

> Cosine similarity compares the direction of two embedding vectors rather than their magnitude. In NLP, the direction captures semantic meaning, while the magnitude is often less important. Therefore, cosine similarity is a better measure of semantic similarity between embeddings.

---

# 📝 Key Takeaways

- Cosine similarity measures semantic similarity between vectors.
- Similar words have higher cosine similarity scores.
- Semantic search compares embeddings, not keywords.
- RAG retrieves relevant documents using embedding similarity.
- Vector databases are optimized for storing and searching embeddings.
- Token embeddings represent individual tokens.
- Sentence embeddings represent an entire sentence or document.

---

# 🚀 Coming Up Next

In the final section, we'll connect everything we've learned into one complete LLM pipeline, clear up common misconceptions, cover interview questions, and summarize the most important concepts from Lesson 3.

...
# Part 4: Complete LLM Pipeline

---

# Complete LLM Pipeline

Now let's connect everything we have learned so far.

An LLM does not directly understand human text.

There are multiple stages between:

```
Human Language

↓

Model Understanding

↓

Generated Response
```

Let's walk through the complete pipeline.

---

# Step 1: User Provides Text

Example:

```
User:

What is the capital of France?
```

At this point, we have normal human language.

The model cannot directly process this text.

---

# Step 2: Tokenization

The tokenizer converts text into smaller pieces called tokens.

Example:

```
"What is the capital of France?"

↓

[
"What",
"is",
"the",
"capital",
"of",
"France",
"?"
]
```

Then tokens are converted into token IDs.

Example:

```
[
523,
45,
18,
900,
76,
2341,
12
]
```

Important:

These numbers are only identifiers.

They do not contain meaning.

---

# Step 3: Embedding Lookup

The token IDs are passed to the embedding layer.

Example:

```
Token ID:

2341

↓

Embedding Matrix

↓

[0.21, -0.45, 0.73, 0.18, ...]
```

Each token ID is converted into an embedding vector.

Now the model has numerical representations that contain learned semantic information.

---

# Step 4: Positional Information

A transformer also needs to understand word order.

Consider:

```
Dog bites man
```

and

```
Man bites dog
```

The same words are used, but the meaning changes.

Therefore, the model receives information about position.

Example:

```
Token Embedding

+

Position Information

↓

Transformer Input
```

---

# Step 5: Transformer Processing

Now the transformer processes these vectors.

The transformer uses:

- Attention mechanism
- Multiple layers
- Neural network operations

to understand relationships between tokens.

Example:

Sentence:

```
The animal didn't cross the road because it was tired.
```

The model needs to understand:

```
it

↓

animal
```

or

```
it

↓

road
```

Attention helps the model determine relationships between words.

---

# Step 6: Predict Next Token

The main job of an LLM is:

> Predict the next most likely token.

Example:

Input:

```
The capital of France is
```

The model calculates probabilities:

```
Paris     95%

London     2%

Berlin     1%

Tokyo      0.5%
```

The model selects:

```
Paris
```

as the next token.

---

# Step 7: Convert Token ID Back to Text

The model outputs a token ID.

Example:

```
Token ID:

5678
```

The tokenizer performs reverse lookup:

```
5678

↓

Paris
```

Finally:

```
Paris
```

is displayed to the user.

---

# Complete LLM Flow Diagram

```
                 User Text

                    |
                    v

              Tokenizer

                    |
                    v

              Token IDs

                    |
                    v

          Embedding Lookup

                    |
                    v

          Embedding Vectors

                    |
                    v

          Positional Encoding

                    |
                    v

             Transformer

                    |
                    v

          Next Token Prediction

                    |
                    v

              Token ID

                    |
                    v

              Tokenizer

                    |
                    v

             Generated Text
```

---

# Complete Architecture View

```
                INPUT

                  |
                  v

          Text: "Hello AI"


                  |
                  v

            Tokenizer


                  |
                  v

        Token IDs: [101,52]


                  |
                  v

        Embedding Layer


                  |
                  v

        Vector Representations


                  |
                  v

          Transformer Layers

       +--------------------+
       |                    |
       | Attention          |
       | Feed Forward NN    |
       | Normalization      |
       |                    |
       +--------------------+


                  |
                  v

        Probability Distribution


                  |
                  v

        Next Token Selection


                  |
                  v

             Output Text
```

---

# Common Misconceptions

Understanding what an LLM does NOT do is equally important.

---

## Misconception 1: "LLM Searches Google"

❌ Incorrect:

> ChatGPT searches the internet for every answer.

✅ Correct:

During normal operation, an LLM generates responses using patterns learned during training.

It does not automatically search the internet.

---

## Misconception 2: "LLM Stores Every Sentence"

❌ Incorrect:

> The model memorizes all training data like a database.

✅ Correct:

The model learns statistical patterns by adjusting billions of parameters.

It learns relationships, not a simple collection of documents.

---

## Misconception 3: "Token IDs Have Meaning"

❌ Incorrect:

```
Token ID 101 must mean an important word.
```

✅ Correct:

Token IDs are arbitrary identifiers.

Meaning comes from embeddings.

---

## Misconception 4: "Embedding Dimension Represents Specific Meaning"

Example:

```
Dimension 20 = intelligence

Dimension 50 = emotion
```

❌ Usually incorrect.

The meaning is distributed across many dimensions.

The combination of dimensions represents meaning.

---

## Misconception 5: "Similar Words Have Identical Embeddings"

Example:

```
cat

dog
```

They are not identical.

They are simply closer in vector space.

Example:

```
cat:

[0.21,0.54,-0.12]


dog:

[0.25,0.51,-0.10]
```

Similar, but different.

---

## Misconception 6: "Bigger Models Always Understand Better"

More parameters can help models learn complex patterns.

However performance also depends on:

- Training data quality
- Architecture
- Training methods
- Fine-tuning
- Alignment

---

# Interview Tips

## Question 1:

### Why can't an LLM directly use token IDs?

Strong Answer:

> Token IDs are only numerical identifiers created by the tokenizer. They do not contain semantic information. The embedding layer converts token IDs into dense vectors that capture relationships between words. The transformer uses these vectors to understand language patterns.

---

## Question 2:

### What is an embedding?

Strong Answer:

> An embedding is a dense numerical representation of text where similar concepts have similar vector representations. Embeddings allow machine learning models to understand relationships and semantic meaning.

---

## Question 3:

### How are embeddings learned?

Strong Answer:

> Embeddings start with random values. During training, the model predicts the next token, calculates the error between prediction and actual output, and updates model parameters using backpropagation. After many iterations, embeddings capture semantic relationships.

---

## Question 4:

### Why are embeddings useful in RAG?

Strong Answer:

> Embeddings allow documents and queries to be compared based on meaning rather than exact keywords. In RAG systems, embeddings help retrieve relevant documents from vector databases before sending context to the LLM.

---

## Question 5:

### Difference between token embeddings and sentence embeddings?

Strong Answer:

> Token embeddings represent individual tokens and are used internally by LLMs. Sentence embeddings represent the meaning of an entire sentence or document and are commonly used for semantic search and retrieval.

---

# Lesson 3 Summary

Let's summarize everything.

---

## Tokenization

Converts:

```
Text

↓

Token IDs
```

Example:

```
"Hello"

↓

[15496]
```

---

## Embeddings

Converts:

```
Token ID

↓

Vector Representation
```

Example:

```
15496

↓

[0.21, -0.43, 0.88...]
```

---

## Embedding Matrix

Stores:

```
Every Token

↓

Its Learned Vector
```

---

## Embedding Lookup

Retrieves the correct vector using the token ID.

---

## Training

Initially:

```
Random vectors
```

After training:

```
Meaningful vectors
```

---

## Similarity

Uses:

```
Cosine Similarity
```

to compare vector relationships.

---

## Semantic Search

Searches by:

```
Meaning

not

Exact words
```

---

## RAG

Uses:

```
Question Embedding

↓

Vector Database

↓

Relevant Documents

↓

LLM Answer
```

---

# Key Takeaways ⭐

Remember these five statements:

## 1.

> Token IDs identify tokens, but they do not contain meaning.

---

## 2.

> Embeddings convert tokens into meaningful numerical representations.

---

## 3.

> Similar concepts have similar embeddings because they appear in similar contexts.

---

## 4.

> Cosine similarity measures how close embeddings are.

---

## 5.

> Embeddings are the foundation of modern AI applications like semantic search, RAG, and recommendation systems.

---

# What's Next?

Now that we understand embeddings, the next important concepts are:

## Lesson 4: Transformers and Attention

We will learn:

- Why transformers replaced older NLP models
- What attention means
- Query, Key, Value (QKV)
- Self-attention mechanism
- How transformers understand relationships between words
- Multi-head attention
- Transformer architecture

---

## Future AI Engineering Roadmap

After transformers:

```
Lesson 1
LLM Basics

↓

Lesson 2
Tokenization

↓

Lesson 3
Embeddings

↓

Lesson 4
Transformers & Attention

↓

Lesson 5
Vector Databases

↓

Lesson 6
RAG Systems

↓

Lesson 7
Prompt Engineering

↓

Lesson 8
Fine-tuning

↓

Lesson 9
AI Application Architecture
```

---

# Final Thought

A powerful mental model:

```
Tokenizer

=
Converts language into IDs


Embedding

=
Adds meaning to IDs


Transformer

=
Learns relationships and predicts next tokens


RAG

=
Provides external knowledge
```

Understanding this pipeline is the foundation for becoming an AI Engineer.

...