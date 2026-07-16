# Lesson 2 - Tokenization Interview Questions

## Beginner

### Q1. What is tokenization?

**Answer:**

Tokenization is the process of converting text into smaller units called tokens that can be processed by an LLM.

---

### Q2. Why can't LLMs process raw text?

**Answer:**

Neural networks perform mathematical operations on numbers, not text.

Therefore, text must first be converted into token IDs.

---

### Q3. What is a token?

**Answer:**

A token is the smallest unit processed by an LLM.

A token may be:

- A word
- Part of a word
- A punctuation mark
- A symbol

---

### Q4. What is a Token ID?

**Answer:**

A Token ID is the numerical identifier assigned to a token in the tokenizer's vocabulary.

---

## Intermediate

### Q5. What are the three types of tokenization?

**Answer**

1. Character Tokenization
2. Word Tokenization
3. Subword Tokenization

Modern LLMs typically use **Subword Tokenization**.

---

### Q6. Why is Character Tokenization inefficient?

**Answer**

It creates too many tokens, increasing computation and making it harder for the model to learn meaningful patterns.

---

### Q7. Why is Word Tokenization not ideal?

**Answer**

It requires an extremely large vocabulary and struggles with unknown or newly created words.

---

### Q8. Why is Subword Tokenization preferred?

**Answer**

It balances vocabulary size and flexibility by reusing common word pieces.

Advantages:

- Smaller vocabulary
- Handles unknown words
- Better generalization
- Efficient computation

---

## Advanced

### Q9. Explain the complete pipeline before the Transformer.

**Answer**

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

---

### Q10. Can two LLMs use different tokenizers?

**Answer**

Yes.

Different LLMs often use different tokenizers and vocabularies.

However, each model must use the tokenizer it was trained with.

---

### Q11. Why can't we replace the tokenizer after training?

**Answer**

Because the model learned relationships based on specific token IDs.

Changing the tokenizer changes those IDs, so the learned patterns no longer apply.

---

### Q12. Do Token IDs contain semantic meaning?

**Answer**

No.

Token IDs are only identifiers.

Semantic meaning comes from the learned embedding vectors.

---

# Common Interview Mistakes

❌ Token = Word

✅ A token can be a word, part of a word, punctuation, or symbol.

---

❌ Token IDs contain meaning.

✅ Token IDs are only identifiers.

---

❌ Word tokenization is always better.

✅ Modern LLMs use subword tokenization because it balances efficiency and flexibility.