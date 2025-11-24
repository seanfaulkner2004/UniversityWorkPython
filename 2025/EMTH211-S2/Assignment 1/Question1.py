import numpy as np
import matplotlib.pyplot as plt

def create_themepark_matrix(themepark_map, move_factor = 3):
    """"creates a model leslie matrix for the themepark"""
    n = len(themepark_map)
    P = np.zeros((n, n))
    for i in range(n):
        d = len(themepark_map[i])
        stay_prob = 1 / (1 + move_factor*d)
        move_prob = move_factor / (1 + move_factor*d)
        P[i, i] = stay_prob
        for j in themepark_map[i]:
            P[i, j] = move_prob
    return P

def create_no_repeat_matrix(adj):
    n = len(adj)
    P = np.zeros((n, n))
    for i in range(n):
        neighbors = adj[i]
        d = len(neighbors)
        for j in neighbors:
            P[i,j] = 1/d
    return P

def simulate_themepark(P, initial, steps):
    """"uses the iterative power methid to project after a num of iterations"""
    pops = [initial]
    state = initial
    for _ in range(steps):
        state = state @ P
        pops.append(state)
    return np.array(pops)

def compute_iterations(P, x0, tol=0.01, max_steps=1000):
    """The num of iterations required to get the relative error below 1%"""
    x = x0.copy()
    history = [x0.copy()]
    error_history = []
    eigvals, eigvecs = np.linalg.eig(P.T)
    index = np.argmin(np.abs(eigvals - 1))
    pi = np.real(eigvecs[:, index])
    pi = pi / pi.sum()
    step = 0
    while step < max_steps:
        x = x @ P
        history.append(x.copy())
        error = np.max(np.abs(x - pi))
        error_history.append(error)
        if error < tol:
            break
        step += 1
    return np.array(history), pi, step+1, error_history

def long_term_projection(L):
    """predictes long-term behaviour of matrix"""
    eigvals, eigvecs = np.linalg.eig(L)
    index = np.argmax(np.real(eigvals))
    long_term = eigvecs[:, index]
    long_term_normalized = long_term / long_term.sum()
    return long_term_normalized, np.real(eigvals[index])
    
def main():
    themepark_map = {
        0:[1,3,5],      # A connected to B,D,F
        1:[0,2,5],    # B connected to A,C,F
        2:[1,3,4],    # C connected to B,D,E
        3:[0,2,4,9],      # D connected to A,C,E,I
        4:[2,3,5],    # E connected to C,D,F
        5:[0,1,4,7],  # F connected to A,B,E,H
        6:[7,9],      # G connected to H,J
        7:[5,6,8,9],  # H connected to F,G,I,J
        8:[7,9],      # I connected to H,J
        9:[3,6,7,8],    # J connected to G,H,I
    }
    A = create_themepark_matrix(themepark_map)
    long_term, eigval = long_term_projection(A)
    rides = ["A","B","C","D","E","F","G","H","I","J"]
    print("Themepark Matrix:")
    table_str = "\n".join(["\t".join([f" {x:.2f}" for x in row]) for row in A])
    print(table_str)
    print("\nLong-term visitor distribution:")
    for ride, prob in zip(rides, long_term):
        print(f"Ride {ride}: {float(prob)*100:.2f}%")
    x0 = np.zeros(10)
    x0[0] = 1
    colors = plt.cm.tab10.colors
    history, pi, steps_needed, errors = compute_iterations(A, x0, tol=0.01)
    print(f"Number of steps to reach <1% error: {steps_needed}")
    plt.figure(figsize=(10,6))
    plt.stackplot(range(len(history)), history.T, labels=rides, colors=colors)
    plt.xlabel("Step")
    plt.ylabel("Probability distribution")
    plt.title("Theme Park Visitor Distribution Over Time")
    plt.legend(loc="upper right")
    plt.show()
    plt.figure(figsize=(8,4))
    plt.plot(range(1, len(errors)+1), errors, marker='o')
    plt.axhline(0.01, color='red', linestyle='--', label='1% tolerance')
    plt.xlabel("Step")
    plt.ylabel("Infinity-norm error vs long-term distribution")
    plt.title("Convergence to Stationary Distribution")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
