import include.trajopt as trajopt
from matplotlib import pyplot as plt
import numpy as np

n = 0.00113 #Mean motion
dt = 1      #Discretization granularity
T = 1000    #Time horizon

x0 = np.array([500.,1000.,0.,0.,0.,0.])      #Initial Condition
X,U,cost = trajopt.planner_l2(T, dt, n, x0)  #Compute Trajectory

#Plot in-plane trajectory
plt.figure()
plt.plot(X[1,:], X[0,:], label='Trajectory')

plt.xlim(0, 1000)
plt.ylim(-100,600)
plt.ylabel('Radial (m)')
plt.xlabel('Along Track (m)')
plt.legend()
plt.title('Rendezvous Trajectories')
plt.show()
