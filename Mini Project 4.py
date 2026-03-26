import numpy as np

# =========================
# 1) Generate Synthetic Data
# =========================
np.random.seed(42)

n = 200  # samples per class
mean1 = [0, 0]
mean2 = [3, 3]
mean3 = [0, 4]

cov = [[1, 0.5], [0.5, 1]]

X1 = np.random.multivariate_normal(mean1, cov, n)
X2 = np.random.multivariate_normal(mean2, cov, n)
X3 = np.random.multivariate_normal(mean3, cov, n)

X = np.vstack((X1, X2, X3))
y = np.array([0]*n + [1]*n + [2]*n)

# =========================
# 2) One-Hot Encoding
# =========================
num_classes = 3
y_onehot = np.zeros((len(y), num_classes))
y_onehot[np.arange(len(y)), y] = 1

# =========================
# 3) Initialize Parameters
# =========================
d = X.shape[1]
W = np.random.randn(d, num_classes) * 0.01
b = np.zeros((1, num_classes))

# =========================
# 4) Softmax Function
# =========================
def softmax(z):
    exp_z = np.exp(z - np.max(z, axis=1, keepdims=True))
    return exp_z / np.sum(exp_z, axis=1, keepdims=True)

# =========================
# 5) Training Loop
# =========================
lr = 0.1
epochs = 1000

for epoch in range(epochs):

    # Forward
    scores = X.dot(W) + b
    probs = softmax(scores)

    # Cross-Entropy Loss
    loss = -np.mean(np.sum(y_onehot * np.log(probs + 1e-9), axis=1))

    # Backward (Gradients)
    grad_scores = probs - y_onehot
    dW = X.T.dot(grad_scores) / len(X)
    db = np.sum(grad_scores, axis=0, keepdims=True) / len(X)

    # Update
    W -= lr * dW
    b -= lr * db

    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss: {loss:.4f}")

# =========================
# 6) Accuracy
# =========================
scores = X.dot(W) + b
probs = softmax(scores)
predictions = np.argmax(probs, axis=1)

accuracy = np.mean(predictions == y)
print("Final Accuracy:", accuracy)