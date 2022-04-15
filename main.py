from cmath import tan
import cvxpy as cp
import numpy as np
from matplotlib import pyplot as plt
import utils

# Prediction horizon
dt = 1
time = 1000
N = int(time/dt)

#Physics parameters
n = 0.00113
Ad, Bd = utils.getABd_zoh(n,dt)
[nx, nu] = Bd.shape

# Initial and terminal conditions
leading = 1
x0 = np.array([50.,leading * 100.,50.,0.,0.,0.])
xT = np.array([0.,0.,0.,0.,0.,0.])

# Define problem
u = cp.Variable((nu, N))
x = cp.Variable((nx, N+1))

th = np.deg2rad(45)     #Larger angle is less constraining
S = np.array([[1, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0]
            ])
c = np.array([0, -np.tan(th), 0, 0, 0, 0])

umax = 0.01
x_init = cp.Parameter(nx)
objective = 0
constraints = [x[:,0] == x0]
constraints += [x[:,N-1] == xT]

for k in range(N):
    #objective += cp.norm(u[:,k], 1)        #L1-norm penalty
    objective += cp.sum_squares(u[:,k])    #L2-norm penalty
    constraints += [x[:,k+1] == Ad@x[:,k] + Bd@u[:,k]]
    constraints += [cp.norm(u[:,k]) <= umax]
    constraints += [cp.norm(S @ x[:,k]) <= leading * np.tan(th)*x[1,k]]
    #constraints += [cp.norm(S @ x[:,k],2) + c @ x[:,k] <= 0]

prob = cp.Problem(cp.Minimize(objective), constraints)

prob.solve(verbose = False)

#Plotting
plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(x.value[0,:], x.value[1,:], x.value[2,:])
ax.set_xlim(-10, 100); ax.set_ylim(-10, 100); ax.set_zlim(-10, 100)


plt.figure()
plt.plot(x.value[1,:],x.value[0,:])
plt.axis('equal')

plt.figure()
plt.plot(np.transpose(u.value))

plt.show()
