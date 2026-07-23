import numpy as np# ==========================================================
# Assignment 2 — Simple RoPE (Rotary Positional Embeddings)
# Lesson 5: Position Information in Transformers
#
# Objective:
# Understand how RoPE adds position information by rotating
# Query and Key vectors based on token position.
#
# Requirements:
# 1. Create a rotation function
# 2. Rotate the same vector at different positions
# 3. Observe how the vector changes
# ==========================================================


import numpy as np


# ----------------------------------------------------------
# Step 1: Create Rotation Function
# ----------------------------------------------------------

def rotate_vector(vector, theta):

    """
    Apply 2D rotation.

    Formula:

    x' = x*cos(theta) - y*sin(theta)

    y' = x*sin(theta) + y*cos(theta)

    """

    x = vector[0]
    y = vector[1]


    rotated_vector = np.array([
        x * np.cos(theta) - y * np.sin(theta),
        x * np.sin(theta) + y * np.cos(theta)
    ])


    return rotated_vector



# ----------------------------------------------------------
# Step 2: Create Query Vector
# ----------------------------------------------------------

# Imagine this is a Query vector
# created from a token embedding.

q = np.array([1, 2])


print("Original Query Vector:")
print(q)



# ----------------------------------------------------------
# Step 3: Apply RoPE at Different Positions
# ----------------------------------------------------------

positions = [0, 1, 5, 10]


print("\nRotated Query Vectors:")


for position in positions:

    # In real RoPE:
    #
    # theta depends on:
    # - token position
    # - embedding dimension
    #
    # Here we use position directly
    # for learning.

    theta = position


    rotated_q = rotate_vector(
        q,
        theta
    )


    print(
        f"Position {position}:",
        rotated_q
    )



# ----------------------------------------------------------
# Step 4: Compare Vector Length
# ----------------------------------------------------------

print("\nVector Length Comparison:")


original_length = np.linalg.norm(q)


print(
    "Original length:",
    original_length
)


for position in positions:

    rotated_q = rotate_vector(
        q,
        position
    )


    print(
        f"Position {position} length:",
        np.linalg.norm(rotated_q)
    )