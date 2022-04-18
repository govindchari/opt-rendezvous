import trajopt
import plotter
from matplotlib import pyplot as plt

n = 0.00113

X,U = trajopt.monte_carlo_l2(1000,1,n,10)
plotter.plot_monte_carlo(X)
plt.show()