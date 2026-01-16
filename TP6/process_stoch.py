import numpy as np
import matplotlib.pyplot as plt
from time import time

def random_walk(size, p=0.5, batch=1):
    return np.cumsum(2 * np.random.binomial(1, p, (batch,size)) - 1, axis=-1)

traj = random_walk(1000)

# plt.plot(traj[0])
# plt.show()

trajs = random_walk(1000, batch=1000)

# plt.plot(trajs.T)
# plt.show()

# plt.hist(trajs[:, -1])
# plt.show()


def rand_time(stop, prob, k):
    jumps = np.random.binomial(1, prob, stop)
    steps = np.cumsum(2*jumps-1)
    return np.where(steps >= k)[0].min()

def ech_time(sample, k=10, stop=int(10e5), prob=0.5):
    return np.array([rand_time(stop, prob, k) for _ in range(sample)])

# start = time()
# times = ech_time(1000)
# print("Temps écoulé :", time() - start)

def proc_poisson(jumps, lamb=0.5, batch=1):
    intertimes = np.random.exponential(scale=1/lamb, size=(batch, jumps))
    return intertimes.cumsum(axis=-1)

# jumps = 20
# times = proc_poisson(jumps, lamb=10)
# plt.step(times[0], np.arange(jumps))
# plt.title("Poisson Process Steps")
# plt.xlabel("Time")
# plt.ylabel("Steps")
# plt.show()