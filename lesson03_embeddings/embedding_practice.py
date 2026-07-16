"""
Lesson 3 - Embedding Practice

Goal:
1. Understand cosine similarity.
2. Compare fake embeddings.
3. Use a pre-trained Sentence Transformer model.
4. Find the closest word to "king".
"""

import numpy as np
from sentence_transformers import SentenceTransformer


def cosine_similarity(vec1, vec2):
    """
    Calculate cosine similarity between two vectors.

    Cosine Similarity = (A · B) / (||A|| * ||B||)

    Returns a value between:
    1   -> Exactly similar
    0   -> Unrelated
    -1  -> Opposite direction
    """
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))


# ============================================================
# Part 1: Practice with Fake Embeddings
# ============================================================

print("=" * 60)
print("PART 1: Fake Embeddings")
print("=" * 60)

words = {
    "cat": np.array([0.8, 0.2, -0.5]),
    "dog": np.array([0.7, 0.3, -0.4]),
    "pizza": np.array([-1.8, 2.5, 0.9]),
}

print("\nEmbedding Vectors:")
for word, vector in words.items():
    print(f"{word:6} -> {vector}")

print("\nCosine Similarities:")

pairs = [
    ("cat", "dog"),
    ("cat", "pizza"),
    ("dog", "pizza"),
]

for word1, word2 in pairs:
    similarity = cosine_similarity(words[word1], words[word2])

    print(f"{word1:6} <-> {word2:6}: {similarity:.4f}")


# ============================================================
# Part 2: Real Embeddings using Sentence Transformers
# ============================================================

print("\n")
print("=" * 60)
print("PART 2: Real Embeddings")
print("=" * 60)

model = SentenceTransformer("all-MiniLM-L6-v2")

word_list = [
    "king",
    "queen",
    "man",
    "woman",
    "apple",
    "car",
]

print("\nGenerating embeddings...")

# Generate each embedding only once
embeddings = {}

for word in word_list:
    embeddings[word] = model.encode(word)

print("Done!\n")


king_embedding = embeddings["king"]

best_word = None
best_similarity = -1

print("Similarity with 'king':\n")

for word in word_list:

    if word == "king":
        continue

    similarity = cosine_similarity(
        king_embedding,
        embeddings[word]
    )

    print(f"king -> {word:6}: {similarity:.4f}")

    if similarity > best_similarity:
        best_similarity = similarity
        best_word = word

print("\n" + "=" * 60)
print(f"Closest word to 'king' is: {best_word}")
print(f"Cosine Similarity: {best_similarity:.4f}")
print("=" * 60)


# ============================================================
# Part 3: Rank all words by similarity
# ============================================================

print("\nRanking words by similarity to 'king':\n")

scores = []

for word in word_list:

    if word == "king":
        continue

    similarity = cosine_similarity(
        king_embedding,
        embeddings[word]
    )

    scores.append((word, similarity))

scores.sort(key=lambda x: x[1], reverse=True)

for rank, (word, score) in enumerate(scores, start=1):
    print(f"{rank}. {word:6} -> {score:.4f}")