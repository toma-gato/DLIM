import numpy as np
import matplotlib.pyplot as plt

def random_stochastic_matrix(n, seed=None):
    rng = np.random.default_rng(seed)
    P = rng.random((n, n))
    P /= P.sum(axis=1, keepdims=True)
    return P

# matrice de transition 100x100
P = random_stochastic_matrix(100, seed=42)

def traj_markov(P, times):
    traj = np.zeros(times, dtype=int)
    n_states = P.shape[0]
    for t in range(1, times):
        traj[t] = np.random.choice(n_states, p=P[traj[t-1]])
    return traj

def plot_traj_markov(traj):
    import matplotlib.pyplot as plt
    plt.step(range(len(traj)), traj, where='post')
    plt.ylim(-0.5, np.max(traj)+0.5)
    plt.xlabel("Time")
    plt.ylabel("State")
    plt.title("Markov Chain Trajectory")
    plt.show()

traj = traj_markov(P, 1000)
plot_traj_markov(traj)