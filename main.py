import trajopt
import plotter
from matplotlib import pyplot as plt

n = 0.00113

X,U = trajopt.monte_carlo(1000,1,n,100)
plotter.plot_monte_carlo(X)
plt.show()