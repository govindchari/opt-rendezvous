import numpy as np
import trajopt
import plotter
from matplotlib import pyplot as plt

n = 0.00113

X,U = trajopt.monte_carlo(1000,1,n,10)
plotter.plot_monte_carlo(X)

#plotter.plot_control(U)
plt.show()