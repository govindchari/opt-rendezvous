from turtle import color
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

# Trajectory plot
plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(x.value[0,:], x.value[1,:], x.value[2,:], color='black', label='Trajectory')
plt.plot(x.value[0,0], x.value[1,0], x.value[2,0], marker="*", markersize=5, color="green", label='Start')
plt.plot(x.value[0,N-1], x.value[1,N-1], x.value[2,N-1], marker="*", markersize=5, color="red", label='End')
ax.set_xlim(-10, 100); ax.set_ylim(-10, 100); ax.set_zlim(-10, 100)

theta = np.linspace(0,2*np.pi,90)
r = np.linspace(0,100,50)
T, R = np.meshgrid(theta, r)
X = R * np.cos(T)
Z = R * np.sin(T)
Y = leading * np.sqrt(X**2 + Z**2)/np.tan(th)
Y[Y < 0] = np.nan
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10, label='Approach Cone')
ax.set_xlim(-100, 100); ax.set_ylim(-10, 100); ax.set_zlim(-100, 100)
ax.set_xlabel('Radial (m)')
ax.set_ylabel('Along Track (m)')
ax.set_zlabel('Out of Plane (m)')
ax.set_title('Rendezvous Trajectory')
ax.legend()


# Thrust Plot
plt.figure()
plt.plot(np.transpose(u.value))

plt.show()