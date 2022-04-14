import numpy as np
import cvxpy as cp
import utils

# Problem data
Ac, Bc = (utils.getABc(1))
Ad, Bd = (utils.getABd(1,1))