import numpy as np
import matplotlib.pyplot as plt

sigma = 1
brownian_1D = sigma * np.random.normal(0, 1, 1000).cumsum()
#plt.plot(brownian_1D)
#plt.title('Brownian Motion 1D with variance = 1')
#plt.show()

sigma = 5
brownian_1D = sigma * np.random.normal(0, 1, 1000).cumsum()
#plt.plot(brownian_1D)
#plt.title('Brownian Motion 1D with variance = 5')
#plt.show()

brownian_2D = (np.random.normal(0, 1, 1000).cumsum(), np.random.normal(0, 1, 1000).cumsum())
#plt.plot(brownian_2D[0], brownian_2D[1])
#plt.title('Brownian Motion 2D with variance = 1')
#plt.show()

cor = 0.9
cov = np.array([[1, cor], [cor, 1]])
sigma = 1

brownian_dep = sigma * np.random.multivariate_normal(np.zeros(2), cov, (1000,)).cumsum(axis=0)
plt.plot(brownian_dep[:, 0], brownian_dep[:, 1])
plt.title('Brownian Motion with dependent dimensions')
plt.show()

