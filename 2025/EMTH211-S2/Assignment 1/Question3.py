import numpy as np
import matplotlib.pyplot as plt

# --- Define complex matrix A ---
A = np.array([
    [-2+0.5j, 0.1-0.5j, -0.1j, 0.1, 0],
    [0.2, 3, 0, 0.1+0.1j, 0.2j],
    [0.1j-0.1, 3, 2, 0.1-0.1j, 0],
    [1+0.2j, 1j, 0.3-4j, 1+1j, 0],
    [0.1, 0.2, 1, 0.1+0.1j, 3+0.1j]
], dtype=complex)
n = A.shape[0]

def shifted_inverse_power(A, q, tol=1e-8, max_iter=1000):
    """Compute eigenvalue of A closest to shift q."""
    B = A - q*np.eye(n)
    x = np.random.rand(n) + 1j*np.random.rand(n)
    x = x / np.linalg.norm(x)
    for _ in range(max_iter):
        y = np.linalg.solve(B, x)
        x_new = y / np.linalg.norm(y)
        if np.linalg.norm(x_new - x) < tol:
            break
        x = x_new
    lambda_ = np.vdot(x, A @ x) / np.vdot(x, x)
    return lambda_

# --- Gershgorin discs ---
centres = np.diag(A)
row_radii = np.array([np.sum(np.abs(A[i,:])) - np.abs(A[i,i]) for i in range(n)])

fig, ax = plt.subplots()
ax.grid(True)

for i in range(n):
    ax.add_patch(plt.Circle((centres[i].real, centres[i].imag),
                            row_radii[i], color='blue', alpha=0.2))

# --- Compute eigenvalues using shifted inverse power ---
# Use Gershgorin disc centers as shifts
shifts = centres
eig_shifted = [shifted_inverse_power(A, q) for q in shifts]
eig_shifted = np.array(eig_shifted)

ax.plot(eig_shifted.real, eig_shifted.imag, 'ro', label='Shifted Inverse Power')

# --- Eigenvalues using NumPy for comparison ---
eig_numpy = np.linalg.eigvals(A)
ax.plot(eig_numpy.real, eig_numpy.imag, 'kx', label='NumPy')

ax.set_xlabel('Real')
ax.set_ylabel('Imag')
ax.set_title('Gershgorin Discs and Eigenvalues of A')
ax.axis('equal')
ax.legend()
plt.show()

print("Eigenvalues from shifted inverse power method:")
print(eig_shifted)
print("Eigenvalues from NumPy:")
print(eig_numpy)
