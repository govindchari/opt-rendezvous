import cvxpy as cp
import numpy as np
import utils

def planner(time, dt, n, x0):
    # Prediction horizon
    N = int(time/dt)

    #Physics parameters
    Ad, Bd = utils.getABd_zoh(n,dt)
    [nx, nu] = Bd.shape

    # Initial and terminal conditions
    if x0[1]>0:
        leading = 1
    else:
        leading = -1
    xT = np.array([0.,0.,0.,0.,0.,0.])

    # Define problem
    u = cp.Variable((nu, N))
    x = cp.Variable((nx, N+1))
    x_init = cp.Parameter(nx)

    th = np.deg2rad(45)     #Larger angle is less constraining
    S = np.array([[1, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0]
                ])
    c = np.array([0, -np.tan(th), 0, 0, 0, 0])

    umax = 0.01
    objective = 0
    constraints = [x[:,0] == x_init]
    constraints += [x[:,N-1] == xT]

    for k in range(N):
        #objective += cp.norm(u[:,k], 1)        #L1-norm penalty
        objective += cp.sum_squares(u[:,k])    #L2-norm penalty
        constraints += [x[:,k+1] == Ad @ x[:,k] + Bd @ u[:,k]]
        constraints += [cp.norm(u[:,k]) <= umax]
        constraints += [cp.norm(S @ x[:,k]) <= leading * np.tan(th) * x[1,k]]

    x_init.value = x0
    prob = cp.Problem(cp.Minimize(objective), constraints)

    prob.solve(verbose = False)
    return (x.value, u.value)

def monte_carlo(time, dt, n, no_trials):
    # Prediction horizon
    N = int(time/dt)

    #Physics parameters
    Ad, Bd = utils.getABd_zoh(n,dt)
    [nx, nu] = Bd.shape

    # Initial and terminal conditions
    xT = np.array([0.,0.,0.,0.,0.,0.])

    # Define problem
    u = cp.Variable((nu, N))
    x = cp.Variable((nx, N+1))
    x_init = cp.Parameter(nx)

    th = np.deg2rad(45)     #Larger angle is less constraining
    S = np.array([[1, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0]
                ])
    c = np.array([0, -np.tan(th), 0, 0, 0, 0])

    umax = 0.01
    objective = 0
    constraints = [x[:,0] == x_init]
    constraints += [x[:,N-1] == xT]

    for k in range(N):
        #objective += cp.norm(u[:,k], 1)        #L1-norm penalty
        objective += cp.sum_squares(u[:,k])    #L2-norm penalty
        constraints += [x[:,k+1] == Ad @ x[:,k] + Bd @ u[:,k]]
        constraints += [cp.norm(u[:,k]) <= umax]
        constraints += [cp.norm(S @ x[:,k]) <= np.tan(th) * x[1,k]]

    x0 = [np.random.uniform(-500,500), 1000, np.random.uniform(-500,500), 0., 0., 0.]
    x_init.value = x0
    prob = cp.Problem(cp.Minimize(objective), constraints)
    prob.solve(verbose = False)
    X = x.value
    U = u.value

    for i in range(no_trials):
        x0 = [np.random.uniform(-500,500), 1000, np.random.uniform(-500,500), 0., 0., 0.]
        x_init.value = x0
        prob.solve(verbose = False)
        X = np.append(X,x.value,axis=0)
        U = np.append(U,u.value,axis=0)
        if (((i / no_trials)*100)%10 == 0):
            print("%d percent complete" % int(((i / no_trials)*100)))
    return (X, U)