import numpy as np


def softmax(x):
    exp_x = np.exp(
        x - np.max(x, axis=-1, keepdims=True)
    )
    return exp_x / np.sum(
        exp_x,
        axis=-1,
        keepdims=True
    )


# Sentence embeddings
embeddings = np.array([
    [0.2,0.5,0.1,0.7,0.3,0.8,0.4,0.6],
    [0.9,0.1,0.4,0.2,0.8,0.5,0.7,0.3],
    [0.6,0.3,0.9,0.1,0.5,0.2,0.8,0.4],
    [0.1,0.7,0.5,0.8,0.2,0.6,0.3,0.9]
])


embedding_size = 8
num_heads = 2
head_dim = embedding_size // num_heads


Wq = np.random.rand(8,8)
Wk = np.random.rand(8,8)
Wv = np.random.rand(8,8)
Wo = np.random.rand(8,8)


Q = embeddings @ Wq
K = embeddings @ Wk
V = embeddings @ Wv


Q = Q.reshape(4,num_heads,head_dim)
K = K.reshape(4,num_heads,head_dim)
V = V.reshape(4,num_heads,head_dim)

# We want: Head dimension first
# Change:
# Before: (words, heads, dimensions) : (4,2,4)
# After: (heads, words, dimensions): (2,4,4)

Q = Q.transpose(1,0,2)
K = K.transpose(1,0,2)
V = V.transpose(1,0,2)


scores = Q @ K.transpose(0,2,1)

scores = scores / np.sqrt(head_dim)


weights = softmax(scores)


head_output = weights @ V


head_output = head_output.transpose(1,0,2)


concat = head_output.reshape(4,8)


final_output = concat @ Wo


print(final_output)