from matplotlib import pyplot as plt
import numpy as np

def plot_trajectory(X):
    N, Cols = X.shape
    # Trajectory plot
    plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot3D(X[0,:], X[1,:], X[2,:], color='black', label='Trajectory')
    ax.set_xlabel('Radial (m)')
    ax.set_ylabel('Along Track (m)')
    ax.set_zlabel('Out of Plane (m)')
    ax.set_title('Rendezvous Trajectory')
    ax.legend()
    plt.show()

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

    # Trajectory plot
    plt.figure()
    for i in range(int(N/6)):
        plt.plot(X[i * 6 + 1,:], X[i * 6,:])
    ac = np.linspace(0,1000,100)
    plt.plot(ac,ac,label = 'Approach Cone',color="black")
    plt.plot(ac,-ac,color="black")
    plt.xlim(0, 1000)
    plt.ylim(-500,500)
    plt.ylabel('Radial (m)')
    plt.xlabel('Along Track (m)')
    plt.title('Rendezvous Trajectories')
    plt.legend()


    # Trajectory plot
    plt.figure()
    for i in range(int(N/6)):
        plt.plot(X[i * 6 + 1,:], X[i * 6 + 2,:])
    
    plt.xlim(0, 1000)
    plt.ylim(-500,500)
    plt.ylabel('Out of Plane (m)')
    plt.xlabel('Along Track (m)')
    plt.title('Rendezvous Trajectories')
    plt.legend()

def plot_control(U):
    plt.figure()
    plt.plot(np.transpose(U), label=['$f_x$','$f_y$','$f_z$'])
    plt.xlabel('Timestep')
    plt.ylabel('Specific Force ($m/s^2$)')
    plt.title('Control History')
    plt.autoscale()
    plt.legend()
    plt.show()