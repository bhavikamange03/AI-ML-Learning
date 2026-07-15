import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

words = {
    "cat": [0.8, 0.2, -0.5],
    "dog": [0.7, 0.3, -0.4],
    "pizza": [-1.8, 2.5, 0.9]
}

cat = np.array(words["cat"])
dog = np.array(words["dog"])
pizza = np.array(words["pizza"])

print("cat:", cat)
print("dog:", dog)
print("pizza:", pizza)

print(cat @ dog)  # This is equivalent to np.dot(cat, dog)
print(cat @ pizza)  # This is equivalent to np.dot(cat, pizza)
print(dog @ pizza) # This is equivalent to np.dot(dog, pizza)


print("Cosine Similarity measures between cat and dog:", np.dot(cat, dog) / (np.linalg.norm(cat) * np.linalg.norm(dog)))
print("Cosine Similarity measures between cat and pizza:", np.dot(cat, pizza) / (np.linalg.norm(cat) * np.linalg.norm(pizza)))
print("Cosine Similarity measures between dog and pizza:", np.dot(dog, pizza) / (np.linalg.norm(dog) * np.linalg.norm(pizza)))

embedding = model.encode("king")
print("Embedding for 'king':", embedding)


print("cosine similarity between 'king' and 'queen':", np.dot(embedding, model.encode("queen")) / (np.linalg.norm(embedding) * np.linalg.norm(model.encode("queen"))))
print("Cosine similarity between 'king' and 'man':", np.dot(embedding, model.encode("man")) / (np.linalg.norm(embedding) * np.linalg.norm(model.encode("man"))))
print("Cosine similarity between 'king' and 'woman':", np.dot(embedding, model.encode("woman")) / (np.linalg.norm(embedding) * np.linalg.norm(model.encode("woman"))))
print("Cosine similarity between 'king' and 'apple':", np.dot(embedding, model.encode("apple")) / (np.linalg.norm(embedding) * np.linalg.norm(model.encode("apple"))))
print("Cosine similarity between 'king' and 'car':", np.dot(embedding, model.encode("car")) / (np.linalg.norm(embedding) * np.linalg.norm(model.encode("car"))))