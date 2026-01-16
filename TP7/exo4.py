import numpy as np
import matplotlib.pyplot as plt

Omega = 4.0
Gamma = 0.5
Sigma = 0.1

X0 = np.array([1.0, 0.0])
V0 = np.array([1.0, 1.0])

dt = 1e-2
N = 2000

X = np.zeros((N + 1, 2))
V = np.zeros((N + 1, 2))

X[0] = X0
V[0] = V0

for n in range(N):
    dB = np.random.normal(0, 1) * np.sqrt(dt)
    V[n + 1] = V[n] + (-Omega ** 2 * X[n] - Gamma * V[n]) * dt + Sigma * dB
    X[n + 1] = X[n] + V[n] * dt

plt.figure(figsize=(5,5))
plt.plot(X[:, 0], X[:, 1])
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
