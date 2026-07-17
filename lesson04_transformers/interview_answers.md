# Lesson 4 - Transformers Interview Answers

## 🎯 Purpose

This document contains detailed answers to Transformer and GPT architecture interview questions.

Topics covered:

- RNN limitations
- Self-Attention
- Embeddings
- Query, Key, Value
- Attention Scores
- Attention Weights
- Multi-Head Attention
- Transformer Architecture
- GPT

---

# 🟢 Beginner Level Answers

---

# Q1. What problem did Transformers solve that RNNs struggled with?

## Answer:

RNNs process text sequentially, meaning they read one word at a time.

Example:


I → love → artificial → intelligence


Because information must travel through each step, RNNs struggle to remember relationships between words that are far apart.

Transformers solve this using **Self-Attention**, which allows every word to directly interact with every other word.

Example:


The dog chased the ball because it was tired.


Self-Attention helps understand:


it → dog


even though the words are separated.

Benefits of Transformers:

- Parallel processing
- Better long-range understanding
- Faster training
- Ability to scale to billions of parameters

---

# Q2. Why are RNNs slow compared to Transformers?

## Answer:

RNNs process tokens sequentially.

Example:


Word 1
↓
Word 2
↓
Word 3
↓
Word 4


The model cannot process Word 4 before finishing Word 1, 2, and 3.

Transformers process all tokens together:


Word 1 Word 2 Word 3 Word 4

   ↓

Self-Attention


This allows parallel computation using GPUs, making training much faster.

---

# Q3. What is Self-Attention?

## Answer:

Self-Attention is a mechanism that allows each word in a sentence to look at all other words and determine which ones are important for understanding its meaning.

Example:

Sentence:


The animal didn't cross the street because it was tired.


The model needs to understand:


it → animal


Self-Attention calculates relationships between words and creates a context-aware representation.

---

# Q4. Explain Self-Attention using a simple real-world example.

## Answer:

Imagine attending a conversation.

If someone says:

"She went to the bank."

The meaning of "bank" depends on other words:


bank + money → financial bank

bank + river → river bank


Your brain pays attention to related words to understand meaning.

Self-Attention works similarly by assigning importance to related words.

---

# Q5. Why can't a Transformer directly understand Token IDs?

## Answer:

Token IDs are only numerical labels created by the tokenizer.

Example:


cat → 523
dog → 892


The number 523 does not mean that cat is related to animals.

Token IDs only tell the model:

"Which token is this?"

They do not contain semantic information.

Embeddings are required because they convert tokens into meaningful vectors.

---

# Q6. What is the difference between Token IDs and Embeddings?

## Answer:

## Token ID

A unique integer assigned to a token.

Example:


cat → 523


Properties:

- Created by tokenizer
- Used for lookup
- No semantic meaning


## Embedding

A dense vector representing meaning.

Example:


cat →

[0.23, 0.87, -0.45, ...]


Properties:

- Learned during training
- Captures relationships
- Similar words have similar vectors

---

# Q7. Why do Transformers need embeddings?

## Answer:

Transformers perform mathematical operations.

They cannot understand raw text or token IDs.

Embeddings convert tokens into vectors that contain information about:

- Meaning
- Relationships
- Context

Example:


cat vector ≈ dog vector


because both are animals.

---

# Q8. What are Query, Key, and Value in Attention?

## Answer:

Query, Key, and Value are three different representations created from embeddings.

They help the model decide what information to focus on.

## Query (Q)

Represents:

"What information am I looking for?"

## Key (K)

Represents:

"What information do I contain?"

## Value (V)

Represents:

"What information should I pass forward?"

Together:


Query compares with Keys

↓

Find importance

↓

Collect information from Values


---

# Q9. How are Query, Key, and Value vectors created?

## Answer:

Starting with embedding vector:


X


The model applies learned weight matrices:


Q = X × Wq

K = X × Wk

V = X × Wv


Where:

- Wq creates Query representation
- Wk creates Key representation
- Wv creates Value representation

These weight matrices are learned during training.

---

# Q10. What are Wq, Wk, and Wv?

## Answer:

Wq, Wk, and Wv are trainable weight matrices.

They are randomly initialized before training.

During training:


Prediction

↓

Calculate Error

↓

Backpropagation

↓

Update Wq, Wk, Wv


Over millions of training steps, they learn useful representations.

---

# Q11. Explain the complete Self-Attention process step by step.

## Answer:

Step 1:

Input embeddings:


Word embeddings


Step 2:

Create Q, K, V:


Q = X × Wq

K = X × Wk

V = X × Wv


Step 3:

Calculate attention scores:


Q × Kᵀ


This measures similarity.

Step 4:

Apply Softmax:


Softmax(scores)


Creates attention weights.

Step 5:

Multiply weights with Values:


Attention Output = Attention Weights × V


The result is a context-aware representation.

---

# Q12. What is the formula for calculating Attention Scores?

## Answer:

The formula is:


Attention Score = Q × Kᵀ


It measures how much one token should attend to another token.

Example:


cat Query

compared with

dog Key


creates a similarity score.

---

# Q13. What is the difference between Attention Score and Attention Weight?

## Answer:

## Attention Score

Formula:


Q × Kᵀ


It is the raw similarity value.

Example:


cat → drank = 8.5
cat → milk = 3.2



## Attention Weight

Formula:


Softmax(Attention Score)


It converts scores into probabilities.

Example:


cat → drank = 85%

cat → milk = 15%


Weights are used to combine Value vectors.

---

# Q14. Why do we apply Softmax after calculating attention scores?

## Answer:

Softmax converts raw scores into normalized probabilities.

Before Softmax:


5.8
2.1
0.5


After Softmax:


85%
10%
5%


Benefits:

- Makes values easier to compare
- Ensures weights sum to 1
- Creates attention distribution

---

# Q15. What does an Attention Weight represent?

## Answer:

Attention weight represents the importance of another token when processing the current token.

Example:

Sentence:


The cat drank milk


When processing:


drank


The model may assign:


cat → 70%

milk → 25%

The → 5%


This tells the model which words provide useful context.


# 🟡 Intermediate Level Answers

---

# Q16. Why does every attention head have separate Wq, Wk, and Wv matrices?

## Answer:

Each attention head learns a different way of understanding relationships between words.

If all heads used the same Wq, Wk, and Wv matrices, every head would learn the same pattern and the model would lose the benefit of multiple perspectives.

Different attention heads can focus on different relationships.

Example:

Sentence:


The cat drank milk


One attention head may learn:


cat → subject relationship


Another head may learn:


drank → action relationship


Another head may learn:


milk → object relationship


Each head has its own:


Query:

Q = X × Wq

Key:

K = X × Wk

Value:

V = X × Wv


where Wq, Wk, and Wv are different for each head.

The final output combines information from all heads.

---

# Q17. What is Multi-Head Attention?

## Answer:

Multi-Head Attention is a mechanism where multiple self-attention operations run in parallel.

Instead of having one attention mechanism, the Transformer creates multiple attention heads.

Each head learns different relationships between tokens.

Example:

Input:


The dog chased the ball


Possible attention heads:


Head 1:

dog → chased

(action relationship)

Head 2:

chased → ball

(object relationship)

Head 3:

The → dog

(grammar relationship)


The outputs from all heads are combined:


Head 1 Output
+
Head 2 Output
+
Head 3 Output

      ↓

Concatenation

      ↓

Linear Projection

      ↓

Final Attention Output


This gives the Transformer a richer understanding of language.

---

# Q18. Why is Multi-Head Attention better than single-head attention?

## Answer:

A single attention head can only focus on one type of relationship at a time.

Language contains many types of relationships:

- Grammar relationships
- Semantic meaning
- Long-distance dependencies
- Subject-object relationships
- Pronoun references

Multiple heads allow the model to analyze different aspects of language simultaneously.

Example:

Sentence:


The animal didn't cross the road because it was tired.


Different heads may focus on:


Head 1:

it → animal

Head 2:

tired → reason

Head 3:

cross → road


Combining these perspectives creates a better representation.

---

# Q19. Give examples of different relationships different attention heads might learn.

## Answer:

Different attention heads can specialize in different patterns.

Example sentence:


The dog chased the ball because it was excited.


Possible attention patterns:

---

## Head 1: Subject Relationship

Focus:


dog → chased


Understanding who performed the action.

---

## Head 2: Object Relationship

Focus:


chased → ball


Understanding what received the action.

---

## Head 3: Pronoun Resolution

Focus:


it → dog


Understanding what a pronoun refers to.

---

## Head 4: Grammar Relationship

Focus:


The → dog


Understanding article-noun relationships.

---

## Head 5: Semantic Relationship

Focus:


excited → dog


Understanding meaning and context.

---

This specialization is learned automatically during training.

The model is not manually programmed to create these heads.

---

# Q20. What happens after multiple attention heads produce outputs?

## Answer:

After each attention head produces an output, the Transformer combines them.

The process:


Input Embeddings

    ↓

Multi-Head Attention

    ↓

Head 1 Output
Head 2 Output
Head 3 Output
...
Head N Output

    ↓

Concatenate Outputs

    ↓

Linear Projection

    ↓

Final Attention Output


---

## Step 1: Concatenation

All head outputs are joined together.

Example:


Head 1:

[0.2, 0.5]

Head 2:

[0.8, 0.1]

Combined:

[0.2,0.5,0.8,0.1]


---

## Step 2: Linear Projection

A learned weight matrix transforms the combined vector back into the required dimension.

Example:


Concatenated Vector

    ×

Output Weight Matrix

    ↓

Attention Output


---

## Why is this needed?

Each attention head provides different information.

The final projection combines all these different perspectives into one useful representation that can be passed to the next layer.

---

# Key Interview Point ⭐

Remember:


Single Attention Head:

One perspective

Multi-Head Attention:

Multiple perspectives

↓

Combined understanding


A good interview answer:

> Multi-Head Attention allows the Transformer to learn different types of relationships between 

---

# 🟡 Transformer Block Answers

---

# Q21. What are the main components of a Transformer Block?

## Answer:

A Transformer Block contains four major components:

Multi-Head Self-Attention
Residual Connection
Layer Normalization
Feed Forward Network

A simplified Transformer Block:


Input Embeddings

    ↓

Multi-Head Attention

    ↓

Residual Connection

    ↓

Layer Normalization

    ↓

Feed Forward Network

    ↓

Residual Connection

    ↓

Layer Normalization

    ↓

Output


Each block improves the representation of the tokens.

Modern LLMs like GPT stack many Transformer Blocks together.

Example:


Input

↓

Transformer Block 1

↓

Transformer Block 2

↓

Transformer Block 3

↓

...

↓

Final Representation


---

# Q22. Explain the complete Transformer Block architecture.

## Answer:

A Transformer Block processes information in two main stages:

1. Understanding relationships between tokens
2. Transforming the learned information

---

## Step 1: Multi-Head Self-Attention

The model determines relationships between tokens.

Example:


The dog chased the ball because it was tired.


Attention helps understand:


it → dog


The output becomes a context-aware representation.

---

## Step 2: Residual Connection

The original input is added back:

Formula:


Output = Input + Attention Output


Purpose:

- Preserve original information
- Prevent information loss
- Improve gradient flow

---

## Step 3: Layer Normalization

The values are normalized to keep training stable.

Purpose:

- Prevent unstable activations
- Improve convergence
- Make deep networks easier to train

---

## Step 4: Feed Forward Network

The FFN processes each token individually.

Example:


Attention output

↓

Linear Layer

↓

Activation Function (GELU)

↓

Linear Layer

↓

Better Representation


---

## Step 5: Another Residual Connection + Normalization

The FFN output is added back to the previous representation.

Final output:


Context-aware + transformed representation


---

# Q23. Why do Transformers use Residual Connections?

## Answer:

Residual connections allow information to flow directly through the network.

Without residual connections, each layer would need to completely transform the input, which can cause information loss.

Formula:


Output = Input + New Information


Example:

Before:


Original word meaning:

cat = animal


After attention:


cat + sentence context


Residual connection keeps:


Original meaning

New contextual information


Benefits:

1. Preserves important information
2. Helps gradients flow backward
3. Allows very deep Transformer models

---

# Q24. What problem do Residual Connections solve?

## Answer:

Residual connections solve the problem of training very deep neural networks.

When networks become very deep:

- Gradients can become very small
- Earlier layers may stop learning effectively
- Information can disappear

This is called:


Vanishing Gradient Problem


Residual connections create a shortcut:


Input
|
|----------------
|
↓
Layer
|
↓
Output

Input + Output


This allows information and gradients to move more easily.

---

# Q25. Explain:


Output = Input + New Information


## Answer:

This formula describes a residual connection.

Instead of replacing the original representation:


Output = New Information


the Transformer keeps the original information and adds improvements:


Output:

Original Information

Information learned by attention/FFN


Example:

Input:


bank


Original meaning:


financial place OR river side


After attention:


bank + surrounding words


Sentence:


I deposited money in the bank.


The representation becomes:


bank = financial institution


The residual connection preserves the original token information while adding context.

---

# Q26. Why is Layer Normalization needed in Transformers?

## Answer:

Layer Normalization keeps the values inside the network stable.

During training, activations can become:

Too large:


[5000, 8000, 12000]


or too small:


[0.0001, 0.0003]


This makes learning difficult.

Layer Normalization:

- Stabilizes activations
- Makes training faster
- Improves convergence
- Allows deeper networks

Example:

Before:


[5000, -3000, 9000]


After normalization:


[0.8, -1.1, 0.3]


---

# Q27. What happens if we remove Layer Normalization?

## Answer:

Without Layer Normalization:

1. Training becomes unstable.
2. Gradients may become too large or too small.
3. The model may take longer to converge.
4. Very deep Transformers become harder to train.

Large language models have billions of parameters, so normalization is essential for stable training.

---

# Q28. What is the purpose of the Feed Forward Network (FFN)?

## Answer:

The Feed Forward Network processes and transforms each token representation after attention.

Self-Attention answers:

> "Which other words are important?"

FFN answers:

> "How should this information be transformed?"

The FFN usually contains:


Linear Layer

↓

Activation Function (GELU)

↓

Linear Layer


Purpose:

- Learn complex patterns
- Increase model capacity
- Transform token representations

---

Example:

After attention:


The word "bank" is related to money.


FFN helps refine this representation:


bank → financial institution


---

# Q29. How is Feed Forward Network different from Attention?

## Answer:

The main difference:

| Self-Attention | Feed Forward Network |
|---|---|
| Looks at relationships between tokens | Processes each token individually |
| Combines information from other words | Transforms the token representation |
| Uses Q, K, V | Uses linear layers |
| Learns context | Learns complex features |

Example:

Sentence:


The dog drank water.


---

Attention:


dog ↔ drank ↔ water


Finds relationships.

---

FFN:


dog representation

↓

Transforms and enriches meaning


---

Together:


Attention:

"What information should I use?"

FFN:

"How should I process this information?"


---

# ⭐ Interview Summary

A strong interview answer:

> A Transformer Block consists of Multi-Head Self-Attention, Residual Connections, Layer Normali

---

# 🔴 Advanced Level Answers

# GPT Architecture

---

# Q30. Why is GPT called a Decoder-Only Transformer?

## Answer:

GPT is called a **Decoder-Only Transformer** because it uses only the decoder part of the original Transformer architecture.

The original Transformer architecture contains:


Encoder

Decoder


The Encoder is used to understand an input sequence.

The Decoder is used to generate an output sequence.

Example:

Machine Translation:


English Sentence

    ↓

Encoder

    ↓

Decoder

    ↓

French Sentence


GPT's task is different.

GPT only needs to generate text by predicting the next token.

Example:


Input:

The cat drank

↓

Prediction:

milk


Therefore, GPT does not need an encoder.

Architecture:


Input Tokens

  ↓

Decoder Blocks

  ↓

Next Token Prediction


---

# Q31. What is the difference between Encoder and Decoder?

## Answer:

The Encoder and Decoder have different purposes.

---

## Encoder

Purpose:

> Understand the input.

It creates a representation of the input sequence.

Example:

Input:


The dog is running


Encoder understands:

- dog = animal
- running = action
- relationship between words

Used in:

- BERT
- Classification models
- Text understanding tasks

---

## Decoder

Purpose:

> Generate output.

It predicts the next token based on previous tokens.

Example:

Input:


The dog is


Prediction:


running


Used in:

- GPT
- Text generation models

---

Comparison:

| Encoder | Decoder |
|---|---|
| Understands input | Generates output |
| Can see all input tokens | Uses previous tokens only |
| Used for understanding | Used for generation |
| Example: BERT | Example: GPT |

---

# Q32. Why does GPT not need an Encoder?

## Answer:

GPT is designed for autoregressive text generation.

Its goal is:

> Predict the next token based on previous tokens.

Example:

Input:


The weather today is


GPT predicts:


sunny


It does not need to encode a separate input sequence.

The decoder already contains:

- Self-attention
- Feed Forward Networks
- Context processing ability

Therefore, GPT can generate text using only decoder blocks.

---

# Q33. What does GPT actually predict?

## Answer:

GPT predicts the probability of the next token.

It does not directly predict:

❌ A complete sentence

❌ A paragraph

❌ The final answer

It predicts one token at a time.

Example:

Input:


The sky is


GPT calculates probabilities:


blue 70%

clear 15%

dark 5%

green 1%


The model selects:


blue


Now:


The sky is blue


Then it predicts the next token again.

This process repeats until completion.

---

# Q34. Does GPT generate a complete sentence at once?

## Answer:

No.

GPT generates text one token at a time.

Example:

User:


The cat


Step 1:

Prediction:


drank


Result:


The cat drank


---

Step 2:

Prediction:


milk


Result:


The cat drank milk


---

Step 3:

Prediction:


today


Result:


The cat drank milk today


The complete response is created through repeated next-token predictions.

---

# Q35. Explain Autoregressive Generation.

## Answer:

Autoregressive generation means that each new token depends on previously generated tokens.

The model uses its own output as the input for the next prediction.

Example:

Initial input:


I love


Prediction:


AI


New input:


I love AI


Prediction:


because


New input:


I love AI because


Prediction:


it


The process continues.

Formula:


Next Token = Function(previous tokens)


---

# Q36. Why does GPT generate one token at a time?

## Answer:

GPT generates one token at a time because it is trained as a next-token prediction model.

During training, the model learns:


Given previous tokens,
predict the next token.


Example:

Training data:


The cat drank milk


Training examples:


Input:

The

Target:

cat

Input:

The cat

Target:

drank

Input:

The cat drank

Target:

milk


Because the model learns this task, generation also happens the same way.

---

# Q37. What is Causal Masking?

## Answer:

Causal masking prevents GPT from looking at future tokens during generation.

GPT must predict tokens using only previous information.

Example:

Sentence:


The cat drank milk


When predicting:


drank


The model can see:


The cat


but cannot see:


milk


because milk would reveal the answer.

Attention mask:

      The   cat   drank   milk

The ✓ ✗ ✗ ✗

cat ✓ ✓ ✗ ✗

drank ✓ ✓ ✓ ✗

milk ✓ ✓ ✓ ✓


This ensures left-to-right generation.

---

# Q38. Why can't GPT see future tokens during generation?

## Answer:

If GPT could see future tokens, it would make the prediction task meaningless.

Example:

Question:


The cat drank ___


Future word:


milk


If GPT could see "milk", it would simply copy the answer.

Instead, GPT must learn:


The cat drank

↓

What is the most likely next token?


Causal masking ensures the model learns real language patterns.

Benefits:

- Prevents cheating during training
- Matches real-world generation
- Enables autoregressive text generation

---

# ⭐ Interview Summary

A strong interview answer:

> GPT is a decoder-only Transformer designed for autoregressive text generation. Unlike the original Transformer that contains both encoder and decoder, GPT only uses decoder blocks because its task is predicting the next token. During generation, GPT uses causal self-attention so each token can only attend to previous tokens. The model generates responses one token at a time, where each predicted token becomes part of the next input.

# 🔴 Training and Inference Answers

---

# Q39. Explain the difference between Training and Inference.

## Answer:

Training and inference are two different phases of an LLM.

---

## Training

Training is the learning phase.

During training:

1. The model receives text data.
2. It predicts the next token.
3. The prediction is compared with the actual token.
4. The error is calculated.
5. Model weights are updated using backpropagation.

Example:

Training data:


The cat drank milk


Input:


The cat


Model prediction:


jumped ❌


Correct answer:


drank ✅


The model calculates the difference:


Prediction ≠ Actual Answer

↓

Calculate Error

↓

Update Weights


---

## Inference

Inference is the usage phase.

The model is already trained.

During inference:

- No learning happens.
- No weights are updated.
- No error is calculated.

Example:

User:


The cat


Model predicts:


drank


Then:


The cat drank


The model continues generating.

---

## Simple Difference:

| Training | Inference |
|---|---|
| Model learns | Model generates |
| Uses training data | Uses user input |
| Calculates error | No error calculation |
| Updates weights | Weights stay fixed |
| Learning phase | Production phase |

---

# Q40. What happens when GPT predicts the wrong token during training?

## Answer:

During training, the model learns from its mistakes.

Example:

Actual sentence:


The cat drank milk


Input:


The cat


Prediction:


jumped ❌


Correct token:


drank ✅


The model calculates loss:


Wrong prediction

↓

Loss calculation

↓

Backpropagation

↓

Update parameters


The parameters that are updated include:

- Embedding weights
- Attention weights
- Feed Forward Network weights
- Output layer weights

After many training examples, the model becomes better at predicting the correct token.

---

# Q41. What happens when GPT predicts the wrong token during inference?

## Answer:

During inference, the model does not learn from mistakes.

The model is already trained.

If it predicts:


The cat jumped


instead of:


The cat drank


nothing is updated.

The model continues from its own prediction.

Example:

Prediction:


The cat jumped


Next prediction uses:


The cat jumped


not:


The cat drank


because the model does not know the correct answer.

---

# Q42. Why can the model correct mistakes during training but not during inference?

## Answer:

The difference is the availability of the correct answer.

---

During training:

The model knows:


Prediction:

jumped

Correct:

drank


It can calculate the error.

---

During inference:

The model only sees:


User prompt


It does not know the expected answer.

Therefore:


No correct answer

↓

No loss calculation

↓

No weight update


---

Simple explanation:

Training is like practicing with an answer key.

Inference is like taking the exam without seeing the answers.

---

# Q43. What is Teacher Forcing?

## Answer:

Teacher forcing is a training technique where the model receives the correct previous token instead of its own prediction.

Example:

Training sentence:


The cat drank milk


Step 1:

Input:


The cat


Prediction:


jumped ❌


Correct:


drank ✅


Instead of continuing with:


The cat jumped


the model is given:


The cat drank


and learns the next prediction.

---

# Q44. Why does Teacher Forcing make training easier?

## Answer:

Without teacher forcing, errors can accumulate.

Example without teacher forcing:


The cat

↓

wrong prediction:

jumped

↓

next prediction uses wrong context

↓

more errors


This creates a chain of mistakes.

With teacher forcing:


The cat

↓

Correct token:

drank

↓

Learn next token:

milk


Benefits:

- Faster learning
- More stable training
- Prevents error accumulation

---

# Q45. What is Backpropagation in LLM training?

## Answer:

Backpropagation is the process of updating model parameters based on prediction errors.

The process:


Input Text

↓

Model Prediction

↓

Compare with Correct Token

↓

Calculate Loss

↓

Backpropagation

↓

Update Weights


The model adjusts millions or billions of parameters slightly.

Example:

Before training:


cat and dog relationship:

weak


After many updates:


cat and dog relationship:

strong


---

# Q46. When are model weights updated?

## Answer:

Model weights are updated only during training.

During training:


Prediction

↓

Loss

↓

Backpropagation

↓

Weight Update


During inference:


Prediction

↓

Response


No weight changes happen.

---

# 🟣 Complete GPT Pipeline Answers

---

# Q47. Explain the complete GPT pipeline from input text to generated response.

## Answer:

The complete pipeline:


User Text

↓

Tokenizer

↓

Token IDs

↓

Embedding Layer

↓

Transformer Blocks

↓

Linear Layer

↓

Softmax

↓

Next Token

↓

Repeat


---

## Step 1: Tokenization

Text is converted into tokens.

Example:


I love AI


becomes:


[45, 678, 912]


---

## Step 2: Embedding Lookup

Token IDs are converted into vectors.

Example:


Token ID

↓

Embedding Vector


---

## Step 3: Transformer Blocks

The embeddings pass through many Transformer layers.

Each layer contains:

- Self-Attention
- Feed Forward Network
- Residual Connections
- Layer Normalization

The model builds contextual understanding.

---

## Step 4: Linear Layer

The final representation is converted into vocabulary scores.

Example:


Vector

↓

Vocabulary logits

↓

Probability for every token


---

## Step 5: Softmax

Converts logits into probabilities.

Example:


milk 80%

water 10%

juice 5%


---

## Step 6: Select Next Token

The model selects a token.

Then the process repeats.

---

# Q48. Explain what happens when a user enters:


The cat


and GPT generates:


The cat drank milk


## Answer:

Step 1:

Tokenizer converts:


"The cat"


into token IDs.

---

Step 2:

Token IDs become embeddings.

---

Step 3:

Transformer processes embeddings using attention.

It understands:


cat = animal

possible actions = drank, ran, slept


---

Step 4:

Output layer predicts probabilities:

Example:


drank 60%

ran 20%

slept 10%


Select:


drank


---

Step 5:

New input:


The cat drank


The model predicts:


milk


The process repeats until completion.

---

# Q49. What happens internally after GPT predicts one token?

## Answer:

After predicting one token:

Example:

Input:


The cat


Prediction:


drank


The generated token is added to the sequence:


The cat drank


Then the entire sequence is processed again to predict the next token.

The loop continues:


Generate token

↓

Add token to context

↓

Predict next token

↓

Repeat


---

# Q50. Explain GPT architecture to a non-technical person.

## Answer:

GPT is like a very advanced autocomplete system.

Imagine reading a sentence:


The weather today is


Your brain guesses:


sunny


GPT does something similar, but it learned patterns from a huge amount of text.

It uses:

- Embeddings to understand words
- Attention to understand relationships
- Transformer layers to process information
- Probability prediction to choose the next word

It does not search for an answer.

It generates text by predicting one token after another.

---

# ⭐ Final Interview Summary

A strong answer:

> GPT is a decoder-only Transformer model that generates text using autoregressive next-token prediction. Text is converted into tokens and embeddings, processed through multiple Transformer blocks containing self-attention and feed-forward networks, and finally converted into token probabilities. During training, the model learns by comparing predictions with actual tokens and updating weights through backpropagation. During inference, the trained model generates tokens without updating its parameters.

---

---

# ⭐ Scenario-Based Interview Answers

---

# Q51. Sentence:


The dog chased the ball because it was tired.


How does Self-Attention help understand what "it" refers to?

## Answer:

Self-Attention allows each word to look at all other words and determine which words are important for understanding meaning.

The word:


it


creates a Query asking:

> "Which previous words help me understand my meaning?"

The model compares this Query with the Keys of other words:


The
dog
chased
the
ball
because


The attention scores may look like:


it → dog high attention
it → ball low attention
it → chased medium attention


Because "tired" is more commonly associated with the subject performing an action, the model learns:


it → dog


The attention mechanism does not use a fixed rule. It learns these relationships from training data.

---

# Q52. Why can Transformers understand relationships between words far apart in a sentence?

## Answer:

RNNs process words sequentially, so information must travel through many steps.

Example:


The dog that was sitting near the tree chased the ball because it was tired.


The relationship:


it → dog


is far apart.

RNN:


dog → many steps → it


Information can be lost.

Transformer:


dog
|
|
Attention
|
|
it


Every token can directly attend to every other token.

This allows Transformers to capture long-range dependencies.

---

# Q53. Why are embeddings not enough by themselves to understand a complete sentence?

## Answer:

Embeddings represent the meaning of individual tokens.

Example:


bank embedding


can represent:

- financial bank
- river bank

The embedding alone does not know the sentence context.

Example:

Sentence 1:


I deposited money in the bank.


Sentence 2:


I sat near the river bank.


The same word has different meanings.

Self-Attention modifies embeddings into contextual embeddings.

Before attention:


bank = general meaning


After attention:


bank = financial institution


or


bank = river side


depending on context.

---

# Q54. Why does each Transformer layer create new Query, Key, and Value vectors instead of reusing previous ones?

## Answer:

Each Transformer layer learns a deeper understanding of language.

Early layers may learn:


word relationships


Middle layers may learn:


grammar and syntax


Later layers may learn:


complex meaning and reasoning patterns


Each layer has different learned matrices:


Layer 1:

Q1 = X × Wq1

Layer 2:

Q2 = X × Wq2

Layer 3:

Q3 = X × Wq3


Each layer extracts different information.

Reusing the same QKV would limit the model's ability to learn deeper representations.

---

# Q55. GPT predicts:


The cat jumped


instead of:


The cat drank


Explain training vs inference.

## Answer:

## During Training:

The correct answer is available.

Input:


The cat


Prediction:


jumped ❌


Correct:


drank ✅


The model calculates loss:


Wrong prediction

↓

Backpropagation

↓

Update weights


The model learns to increase the probability of:


drank


---

## During Inference:

The model is already trained.

If it generates:


The cat jumped


there is no correction.

No:

- loss calculation
- backpropagation
- weight update

The model continues from:


The cat jumped


---

# Q56. Explain Self-Attention mathematically from embeddings to final output.

## Answer:

Starting with embeddings:


X


Create Query, Key, Value:


Q = XWq

K = XWk

V = XWv


Calculate attention scores:


Scores = QKᵀ


Scale values:


Scores / √dk


Apply Softmax:


Weights = Softmax(QKᵀ / √dk)


Multiply weights with values:


Attention Output = Weights × V


The output contains contextual information.

Complete formula:


Attention(Q,K,V)

=

Softmax(QKᵀ / √dk)V


---

# Q57. Why does increasing Transformer depth usually improve model capability?

## Answer:

More Transformer layers allow the model to learn increasingly complex patterns.

Example:

Lower layers:


Word meaning


Middle layers:


Grammar relationships


Higher layers:


Complex concepts and reasoning


More layers provide more transformation steps.

However, increasing depth also requires:

- More data
- More computation
- Better training techniques

---

# Q58. What are logits?

## Answer:

Logits are raw scores produced by the final layer before applying Softmax.

Example:

Vocabulary:


["cat", "dog", "milk"]


Model output:


cat 2.1
dog 5.7
milk 1.3


These values are logits.

They are not probabilities yet.

Softmax converts them:


cat 10%
dog 80%
milk 10%


---

# Q59. How does Softmax convert logits into probabilities?

## Answer:

Softmax converts raw scores into normalized probabilities.

Formula:


Softmax(xi) =
e^xi / Σe^x


Example:

Logits:


cat = 2
dog = 5
milk = 1


After Softmax:


cat = 12%
dog = 84%
milk = 4%


The probabilities:

- Are between 0 and 1
- Add up to 100%

The highest probability token is usually selected as the next token.

---

# Q60. Explain the complete architecture of GPT as if you are answering in a machine learning interview.

## Answer:

GPT is a decoder-only Transformer model designed for autoregressive text generation.

The pipeline:


Input Text

↓

Tokenizer

↓

Token IDs

↓

Embedding Layer

↓

Transformer Decoder Blocks

↓

Self-Attention

+

Feed Forward Network

+

Residual Connections

+

Layer Normalization

↓

Linear Layer

↓

Logits

↓

Softmax

↓

Next Token Prediction


During training:

- GPT predicts the next token.
- The prediction is compared with the actual token.
- Loss is calculated.
- Backpropagation updates model weights.

During inference:

- The trained model receives a prompt.
- It predicts one token at a time.
- Each generated token becomes part of the next input.

A concise interview answer:

> GPT is a decoder-only Transformer architecture that uses self-attention to understand relationships between tokens and predicts the next token using learned patterns. It converts text into embeddings, processes them through multiple Transformer blocks, generates logits, applies Softmax, and selects the next token. During training it learns by updating weights, while during inference it generates text without changing parameters.

---

# 🎉 Lesson 4 Interview Answers Completed

Covered:

✅ Transformer Architecture  
✅ Self-Attention  
✅ QKV  
✅ Attention Scores  
✅ Attention Weights  
✅ Multi-Head Attention  
✅ Transformer Blocks  
✅ GPT Architecture  
✅ Training vs Inference  
✅ Teacher Forcing  
✅ Logits  
✅ Softmax  
✅ Complete GPT Pipeline  