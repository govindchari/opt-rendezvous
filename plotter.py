from matplotlib import pyplot as plt
import numpy as np

def plot_trajectory(X):
    N, Cols = X.shape
    # Trajectory plot
    plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot3D(X[0,:], X[1,:], X[2,:], color='black', label='Trajectory')
    plt.plot(X[0,N-1], X[1,N-1], X[2,N-1], marker="*", markersize=5, color="red", label='End')
    ax.set_xlim(-10, 100); ax.set_ylim(-10, 100); ax.set_zlim(-10, 100)
    ax.set_xlabel('Radial (m)')
    ax.set_ylabel('Along Track (m)')
    ax.set_zlabel('Out of Plane (m)')
    ax.set_title('Rendezvous Trajectory')
    ax.legend()

def plot_monte_carlo(X):
    N, Cols = X.shape
    # Trajectory plot
    plt.figure()
    ax = plt.axes(projection='3d')
    for i in range(int(N/6)):
        ax.plot3D(X[i * 6,:], X[i * 6 + 1,:], X[i * 6 + 2,:])
    ax.set_xlim(-500, 500); ax.set_ylim(-20, 1000); ax.set_zlim(-500, 500)
    ax.set_xlabel('Radial (m)')
    ax.set_ylabel('Along Track (m)')
    ax.set_zlabel('Out of Plane (m)')
    ax.set_title('Rendezvous Trajectories')

def aut():
    theta = np.linspace(0,2*np.pi,90)
    r = np.linspace(0,100,50)
    T, R = np.meshgrid(theta, r)
    X = R * np.cos(T)
    Z = R * np.sin(T)
    Y = leading * np.sqrt(X**2 + Z**2)/np.tan(th)
    Y[Y < 0] = np.nan
    ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10, label='Approach Cone')
    ax.set_xlim(-100, 100); ax.set_ylim(-10, 100); ax.set_zlim(-100, 100)



def plot_control(U):
    plt.figure()
    plt.plot(np.transpose(U), label=['$f_x$','$f_y$','$f_z$'])
    plt.xlabel('Timestep')
    plt.ylabel('Specific Force ($m/s^2$)')
    plt.title('Control History')
    plt.autoscale()
    plt.legend()
    plt.show()