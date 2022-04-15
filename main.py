import cvxpy as cp
import numpy as np
from scipy import sparse
from matplotlib import pyplot as plt
import utils

n = 0.00113
dt = 1
Ad, Bd = utils.getABd_zoh(n,dt)
[nx, nu] = Bd.shape

# Objective function
R = sparse.eye(3)

# Initial and reference states
x0 = np.array([0.,100.,0.,0.,0.,0.])
xT = np.array([0.,0.,0.,0.,0.,0.])

# Prediction horizon
N = 3000

# Define problem
u = cp.Variable((nu, N))
x = cp.Variable((nx, N+1))
x_init = cp.Parameter(nx)
objective = 0
constraints = [x[:,0] == x0]
constraints += [x[:,N-1] == xT]

for k in range(N):
    #objective += cp.norm(u[:,k], 1)
    objective += cp.sum_squares(u[:,k])
    constraints += [x[:,k+1] == Ad@x[:,k] + Bd@u[:,k]]

prob = cp.Problem(cp.Minimize(objective), constraints)

prob.solve()

plt.figure()
plt.plot(x.value[1,:],x.value[0,:])

plt.figure()
plt.plot(np.transpose(u.value))

plt.show()
