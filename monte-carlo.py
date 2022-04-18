import include.trajopt as trajopt
import include.plotter as plotter
from matplotlib import pyplot as plt

n = 0.00113

X,U = trajopt.monte_carlo_l2(1000,1,n,100)
plotter.plot_monte_carlo(X)
plt.show()