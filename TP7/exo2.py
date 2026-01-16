import numpy as np
import matplotlib.pyplot as plt

h = 1e-7
m = 2e-14
gamma = 1e-8
kB = 1.380649e-23
T = 300
N = 300

X = np.zeros(N + 1)
V = np.zeros(N + 1)

sigma = np.sqrt(2 * gamma * kB * T)

for n in range(N):
    dB = np.random.normal(0, 1) * np.sqrt(h)
    V[n + 1] = V[n] + (-gamma / m * V[n]) * h + (sigma / m) * dB
    X[n + 1] = X[n] + V[n] * h

plt.plot(X)
plt.title('Position')
plt.show()

plt.plot(V)
plt.title('Vitesse')
plt.show()
