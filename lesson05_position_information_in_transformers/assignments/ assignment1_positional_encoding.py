# ==========================================================
# Assignment 1 — Sinusoidal Positional Encoding
# Lesson 5: Position Information in Transformers
#
# Objective:
# Implement the positional encoding used in the original
# Transformer paper using NumPy.
#
# Requirements:
# 1. Create positional encoding function
# 2. Generate position vectors
# 3. Create random word embeddings
# 4. Add positional encoding to embeddings
# 5. Observe final input embeddings
# ==========================================================


import numpy as np


# ----------------------------------------------------------
# Step 1: Create Sinusoidal Positional Encoding
# ----------------------------------------------------------

def positional_encoding(sequence_length, embedding_size):

    # Position of each token
    #
    # Example:
    #
    # [
    #  [0],
    #  [1],
    #  [2],
    #  [3]
    # ]
    position = np.arange(sequence_length)[:, np.newaxis]


    # Embedding dimensions
    #
    # Example:
    #
    # [
    #  [0,1,2,3,4,5,6,7]
    # ]
    dimension = np.arange(embedding_size)[np.newaxis, :]


    # Calculate angle rates
    angle_rates = 1 / np.power(
        10000,
        (2 * (dimension // 2)) / embedding_size
    )


    # Calculate angles for every position
    angle = position * angle_rates


    # Create empty positional encoding matrix

    positional_encoding = np.zeros(
        (sequence_length, embedding_size)
    )


    # Apply sine to even dimensions
    #
    # index: 0,2,4,6...

    positional_encoding[:, 0::2] = np.sin(
        angle[:, 0::2]
    )


    # Apply cosine to odd dimensions
    #
    # index: 1,3,5,7...

    positional_encoding[:, 1::2] = np.cos(
        angle[:, 1::2]
    )


    return positional_encoding



# ----------------------------------------------------------
# Step 2: Create Sentence
# ----------------------------------------------------------

sentence = [
    "The",
    "cat",
    "drinks",
    "milk"
]


sequence_length = len(sentence)


# Transformer embedding size
embedding_size = 8



# ----------------------------------------------------------
# Step 3: Create Word Embeddings
# ----------------------------------------------------------

# In a real Transformer:
#
# Token
#   |
# Embedding Layer
#
# Here we create random values
# only for learning.

np.random.seed(42)


word_embeddings = np.random.rand(
    sequence_length,
    embedding_size
)



print("Sentence:")
print(sentence)


print("\nWord Embeddings:")
print(word_embeddings)



# ----------------------------------------------------------
# Step 4: Generate Positional Encoding
# ----------------------------------------------------------

position_embeddings = positional_encoding(
    sequence_length,
    embedding_size
)


print("\nPositional Encoding:")
print(position_embeddings)



# ----------------------------------------------------------
# Step 5: Add Position Information
# ----------------------------------------------------------

# Transformer input:
#
# Input Embedding =
# Word Embedding + Position Encoding

input_embeddings = (
    word_embeddings 
    + position_embeddings
)



print("\nInput Embeddings:")
print(input_embeddings)



# ----------------------------------------------------------
# Step 6: Check Dimensions
# ----------------------------------------------------------

print("\nShapes:")

print(
    "Word Embedding:",
    word_embeddings.shape
)

print(
    "Position Encoding:",
    position_embeddings.shape
)

print(
    "Input Embedding:",
    input_embeddings.shape
)