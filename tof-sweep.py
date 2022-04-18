import include.trajopt as trajopt
import numpy as np
from matplotlib import pyplot as plt

n = 0.00113
N = 100
x0 = np.array([500.,1000.,500.,0.,0.,0.])
val_list = np.zeros(N)
tof_list = np.linspace(700,1500,N)


for i in range(N):
    x,u,val = trajopt.planner_l2(tof_list[i], 1, n, x0)
    val_list[i] = val
    print(i)

print(val_list)
plt.plot(tof_list,val_list)
plt.ylabel('Cost')
plt.xlabel('Rendezvous Time (s)')
plt.title('Cost vs Rendezvous Time')
plt.show()

