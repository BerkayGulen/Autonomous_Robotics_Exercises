import numpy as np
import math
import matplotlib.pyplot as plt
import sheet5_ex1 as sample_normal_distribution

# Berkay Gülen -- 20170613017

def sample_normal(mu, sigma):
    return sample_normal_distribution.sample_normal_twelve(mu,sigma)

def sample_odometry_motion_model(x, u, a):
    # x => pose of the robot before moving [x, y, theta]
    # u => odometry reading obtained from the robot [rot1, rot2, trans]
    # a => noise parameters of the motion model [a1, a2, a3, a4]

    delta_hat_r1 = u[0] + sample_normal(0, a[0]*abs(u[0]) + a[1]*u[2])
    delta_hat_t = u[2] + sample_normal(0, a[2]*u[2] + a[3]*(abs(u[0])+abs(u[1])))
    delta_hat_r2 = u[1] + sample_normal(0, a[0]*abs(u[1]) + a[1]*u[2])
    x_prime = x[0] + delta_hat_t * math.cos(x[2] + delta_hat_r1)
    y_prime = x[1] + delta_hat_t * math.sin(x[2] + delta_hat_r1)
    theta_prime = x[2] + delta_hat_r1 + delta_hat_r2
    return np.array([x_prime, y_prime, theta_prime])


def main():
    x = [2, 4, 0]
    u = [np.pi/2, 0, 1]
    a = [0.1, 0.1, 0.01, 0.01]

    num_samples = 5000
    x_prime = np.zeros([num_samples, 3])

    for i in range(0, num_samples):
        x_prime[i,:] = sample_odometry_motion_model(x,u,a)

    plt.plot(x[0], x[1], "bo")
    plt.plot(x_prime[:,0], x_prime[:,1], "r,")
    plt.xlim([1, 3])
    plt.xlabel("x position")
    plt.ylabel("y position ")
    plt.savefig("odometry_samples.png")
    plt.show()


if __name__ == "__main__":
    main()