import numpy as np
import matplotlib.pyplot as plt
# =====================================================
# Assignment 1 - Build Self-Attention using NumPy
#
# Sentence:
# The cat drinks milk.
#
# Pipeline:
#
# Text
#   ↓
# Embeddings
#   ↓
# Q, K, V
#   ↓
# Attention Scores
#   ↓
# Scale by √dk
#   ↓
# Softmax
#   ↓
# Attention Weights
#   ↓
# Attention Output
# =====================================================

# Make results reproducible
np.random.seed(42)

# -----------------------------------------------------
# Step 1: Create Embedding Vectors
# -----------------------------------------------------

the = np.array([0.5, -0.2, 0.1])
cat = np.array([0.8, 0.2, -0.5])
drinks = np.array([-0.1, 0.9, 0.3])
milk = np.array([-0.3, 0.4, 0.7])

words = ["The", "Cat", "Drinks", "Milk"]

# Create the embedding matrix
embeddings = np.array([
    the,
    cat,
    drinks,
    milk
])

print("=" * 60)
print("Embedding Matrix")
print("=" * 60)
print(embeddings)
print("\nShape:", embeddings.shape)

# -----------------------------------------------------
# Step 2: Create Random Weight Matrices
# -----------------------------------------------------

embedding_dim = embeddings.shape[1]

Wq = np.random.rand(embedding_dim, embedding_dim)
Wk = np.random.rand(embedding_dim, embedding_dim)
Wv = np.random.rand(embedding_dim, embedding_dim)

print("\n" + "=" * 60)
print("Weight Matrices")
print("=" * 60)

print("\nWq:\n", Wq)
print("\nWk:\n", Wk)
print("\nWv:\n", Wv)

# -----------------------------------------------------
# Step 3: Generate Query, Key and Value
# -----------------------------------------------------

Q = embeddings @ Wq
K = embeddings @ Wk
V = embeddings @ Wv

print("\n" + "=" * 60)
print("Query Matrix (Q)")
print("=" * 60)
print(Q)

print("\n" + "=" * 60)
print("Key Matrix (K)")
print("=" * 60)
print(K)

print("\n" + "=" * 60)
print("Value Matrix (V)")
print("=" * 60)
print(V)

# -----------------------------------------------------
# Step 4: Compute Attention Scores
# -----------------------------------------------------

d_k = K.shape[1]

attention_scores = (Q @ K.T) / np.sqrt(d_k)

print("\n" + "=" * 60)
print("Attention Scores")
print("=" * 60)
print(attention_scores)

# -----------------------------------------------------
# Step 5: Apply Softmax
# -----------------------------------------------------

def softmax(x):
    exp_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)

attention_weights = softmax(attention_scores)

print("\n" + "=" * 60)
print("Attention Weights")
print("=" * 60)
print(attention_weights)

# -----------------------------------------------------
# Step 6: Generate Attention Output
# -----------------------------------------------------

attention_output = attention_weights @ V

print("\n" + "=" * 60)
print("Attention Output")
print("=" * 60)
print(attention_output)

# -----------------------------------------------------
# Step 7: Interpret the Attention Matrix
# -----------------------------------------------------

print("\n" + "=" * 60)
print("Attention Interpretation")
print("=" * 60)

for i, word in enumerate(words):

    print(f"\n'{word}' attends to:")

    for j, other_word in enumerate(words):

        print(f"  {other_word:<8}: {attention_weights[i][j]:.3f}")

# -----------------------------------------------------
# Step 8: Display Tensor Shapes
# -----------------------------------------------------

print("\n" + "=" * 60)
print("Tensor Shapes")
print("=" * 60)

print("Embeddings        :", embeddings.shape)
print("Query Matrix (Q)  :", Q.shape)
print("Key Matrix (K)    :", K.shape)
print("Value Matrix (V)  :", V.shape)
print("Attention Scores  :", attention_scores.shape)
print("Attention Weights :", attention_weights.shape)
print("Attention Output  :", attention_output.shape)

# -----------------------------------------------------
# Step 9: Visualize Attention Weights
# -----------------------------------------------------

plt.figure(figsize=(6, 5))

plt.imshow(attention_weights, cmap="Blues")

plt.title("Self-Attention Weights")

plt.xticks(range(len(words)), words)
plt.yticks(range(len(words)), words)

plt.xlabel("Attending To")
plt.ylabel("Current Word")

plt.colorbar(label="Attention Weight")

plt.show()