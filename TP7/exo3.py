import numpy as np
import matplotlib.pyplot as plt

alpha = 2
beta = 0.005
gamma = 1
delta = 0.002
X0 = 1000
Y0 = 100

dt = 1e-3
sigma = (0.3, 0.3)
N = 10000


X = np.zeros(N + 1)
Y = np.zeros(N + 1)

X[0] = X0
Y[0] = Y0

for n in range(N):
    dBX = np.random.normal(0, 1) * np.sqrt(dt)
    dBY = np.random.normal(0, 1) * np.sqrt(dt)

    X[n + 1] = X[n] + (alpha * X[n] - beta * X[n] * Y[n]) * dt + sigma[0] * X[n] * dBX
    Y[n + 1] = Y[n] + (-gamma * Y[n] + delta * X[n] * Y[n]) * dt + sigma[1] * Y[n] * dBY


plt.plot(X, label = 'Proies')
plt.plot(Y, label = 'Prédateurs')
plt.legend()
plt.title('Modèle Lotka-Volterra bruité')
plt.show()

