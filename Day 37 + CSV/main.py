"""
Day 37 Activity: Dot Product

Tasks:

1) Compute dot product of two vectors

2) Compute cosine similarity

3) Interpret results

"""
import numpy as np

# Provided vectors (edit if you want different values)

a = np.array([1.0, 2.0, 3.0])

b = np.array([0.5, 1.0, 1.5])

# TODO: Compute dot and cosine similarity

dot_product = np.dot(a, b)
norm_a = np.linalg.norm(a)
norm_b = np.linalg.norm(b)
cosine_similarity = dot_product / (norm_a * norm_b) if norm_a > 0 and norm_b > 0 else 0

print("Dot product:", dot_product)
print("Cosine similarity:", cosine_similarity)