# Lesson 4 - Transformers Interview Questions

## 🎯 Goal

This document contains interview questions covering:

- Transformer architecture
- Self-Attention
- Query, Key, Value (QKV)
- Attention Scores and Attention Weights
- Multi-Head Attention
- Transformer Blocks
- GPT Architecture
- Training vs Inference

Practice answering these questions without looking at notes.

---

# 🟢 Beginner Level

---

## Q1. What problem did Transformers solve that RNNs struggled with?

---

## Q2. Why are RNNs slow compared to Transformers?

---

## Q3. What is Self-Attention?

---

## Q4. Explain Self-Attention using a simple real-world example.

---

## Q5. Why can't a Transformer directly understand Token IDs?

---

## Q6. What is the difference between Token IDs and Embeddings?

---

## Q7. Why do Transformers need embeddings?

---

## Q8. What are Query, Key, and Value in Attention?

---

## Q9. How are Query, Key, and Value vectors created?

---

## Q10. What are Wq, Wk, and Wv?

---

# 🟡 Intermediate Level

---

## Q11. Explain the complete Self-Attention process step by step.

Include:

- Embeddings
- Query
- Key
- Value
- Attention Score
- Softmax
- Attention Weight
- Output

---

## Q12. What is the formula for calculating Attention Scores?

---

## Q13. What is the difference between Attention Score and Attention Weight?

---

## Q14. Why do we apply Softmax after calculating attention scores?

---

## Q15. What does an Attention Weight represent?

---

## Q16. Why does every attention head have separate Wq, Wk, and Wv matrices?

---

## Q17. What is Multi-Head Attention?

---

## Q18. Why is Multi-Head Attention better than single-head attention?

---

## Q19. Give examples of different relationships different attention heads might learn.

---

## Q20. What happens after multiple attention heads produce outputs?

---

# 🟡 Transformer Block Questions

---

## Q21. What are the main components of a Transformer Block?

---

## Q22. Explain the complete Transformer Block architecture.

---

## Q23. Why do Transformers use Residual Connections?

---

## Q24. What problem do Residual Connections solve?

---

## Q25. Explain:

```
Output = Input + New Information
```

---

## Q26. Why is Layer Normalization needed in Transformers?

---

## Q27. What happens if we remove Layer Normalization?

---

## Q28. What is the purpose of the Feed Forward Network (FFN)?

---

## Q29. How is Feed Forward Network different from Attention?

---

# 🔴 Advanced Level

---

# GPT Architecture

---

## Q30. Why is GPT called a Decoder-Only Transformer?

---

## Q31. What is the difference between Encoder and Decoder?

---

## Q32. Why does GPT not need an Encoder?

---

## Q33. What does GPT actually predict?

---

## Q34. Does GPT generate a complete sentence at once?

Explain.

---

## Q35. Explain Autoregressive Generation.

---

## Q36. Why does GPT generate one token at a time?

---

## Q37. What is Causal Masking?

---

## Q38. Why can't GPT see future tokens during generation?

---

# Training and Inference

---

## Q39. Explain the difference between Training and Inference.

---

## Q40. What happens when GPT predicts the wrong token during training?

---

## Q41. What happens when GPT predicts the wrong token during inference?

---

## Q42. Why can the model correct mistakes during training but not during inference?

---

## Q43. What is Teacher Forcing?

---

## Q44. Why does Teacher Forcing make training easier?

---

## Q45. What is Backpropagation in LLM training?

---

## Q46. When are model weights updated?

---

# Complete Pipeline Questions

---

## Q47. Explain the complete GPT pipeline from input text to generated response.

Include:

- Tokenization
- Token IDs
- Embeddings
- Transformer Blocks
- Attention
- Linear Layer
- Softmax
- Next Token Prediction

---

## Q48. Explain what happens when a user enters:

```
The cat
```

and GPT generates:

```
The cat drank milk
```

---

## Q49. What happens internally after GPT predicts one token?

---

## Q50. Explain GPT architecture to a non-technical person.

---

# ⭐ Scenario-Based Interview Questions

---

## Q51.

Sentence:

```
The dog chased the ball because it was tired.
```

How does Self-Attention help understand what "it" refers to?

---

## Q52.

Why can Transformers understand relationships between words far apart in a sentence?

---

## Q53.

Why are embeddings not enough by themselves to understand a complete sentence?

---

## Q54.

Why does each Transformer layer create new Query, Key, and Value vectors instead of reusing previous ones?

---

## Q55.

If GPT predicts:

```
The cat jumped
```

instead of:

```
The cat drank
```

Explain what happens during:

1. Training
2. Inference

---

# ⭐ Challenge Questions

---

## Q56.

Explain Self-Attention mathematically from embeddings to final output.

---

## Q57.

Why does increasing Transformer depth usually improve model capability?

---

## Q58.

What are logits?

---

## Q59.

How does Softmax convert logits into probabilities?

---

## Q60.

Explain the complete architecture of GPT as if you are answering in a machine learning interview.

---

# Interview Preparation Checklist

Before moving to the next lesson, make sure you can explain:

✅ Why RNNs struggled  
✅ Why Transformers use Attention  
✅ Token IDs vs Embeddings  
✅ QKV mechanism  
✅ Attention Score vs Attention Weight  
✅ Multi-Head Attention  
✅ Transformer Block  
✅ Residual Connections  
✅ Layer Normalization  
✅ Feed Forward Network  
✅ Decoder-Only Architecture  
✅ Causal Masking  
✅ Training vs Inference  
✅ Teacher Forcing  
✅ Complete GPT pipeline  

