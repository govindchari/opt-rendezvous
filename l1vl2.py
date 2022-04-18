import include.trajopt as trajopt
import numpy as np
from matplotlib import pyplot as plt

n = 0.00113
x0 = np.array([500.,1000.,500.,0.,0.,0.])


x2,u2,val = trajopt.planner_l2(1000, 1, n, x0)
x1,u1,val = trajopt.planner_l1(1000, 1, n, x0)

#Plotting
plt.figure()
plt.plot(np.transpose(u1))
plt.plot(np.transpose(u2))
plt.xlabel('Timestep')
plt.ylabel('Specific Force ($m/s^2$)')
plt.title('Control History')

plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(x1[0,:], x1[1,:], x1[2,:], label='L1 Norm')
ax.plot3D(x2[0,:], x2[1,:], x2[2,:], label='L2 Norm')
ax.set_xlim(-10, 600); ax.set_ylim(-10, 1000); ax.set_zlim(-10, 600)
ax.set_xlabel('Radial (m)')
ax.set_ylabel('Along Track (m)')
ax.set_zlabel('Out of Plane (m)')
ax.set_title('Rendezvous Trajectory')
ax.legend()

plt.show()
