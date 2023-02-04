import numpy as np
import matplotlib.pyplot as plt


def diffdrive(x, y, theta, v_l, v_r, t, l):
    # straight line when left wheel speed = right wheel speed
    if (v_l == v_r):
        final_theta = theta
        final_x = x + v_l * t * np.cos(theta)
        final_y = y + v_l * t * np.sin(theta)

    # circular motion left wheel speed != right wheel speed
    else:
        # Calculate the radius
        R = l / 2.0 * ((v_l + v_r) / (v_r - v_l))

        # center of curvatures
        ICC_x = x - R * np.sin(theta)
        ICC_y = y + R * np.cos(theta)

        # computing theta prime
        theta_prime = ((v_r - v_l) * t) / l

        # forward kinematics for differential drive
        final_x = np.cos(theta_prime) * (x - ICC_x) - np.sin(theta_prime) * (y - ICC_y) + ICC_x
        final_y = np.sin(theta_prime) * (x - ICC_x) + np.cos(theta_prime) * (y - ICC_y) + ICC_y
        final_theta = theta + theta_prime

    return final_x, final_y, final_theta


plt.gca().set_aspect("equal")

# distance between the wheels and the initial robot position
x = 1.5
y = 2.0
l = 0.5
theta = (np.pi) / 2.0

# starting position
plt.quiver(x, y, np.cos(theta), np.sin(theta))
print(f"starting pose: x: {x}, y: {y}, theta:{theta}")

# first motion
v_l = 0.3
v_r = 0.3
t = 3
x, y, theta = diffdrive(x, y, theta, v_l, v_r, t, l)
plt.quiver(x, y, np.cos(theta), np.sin(theta))
print(f"after motion 1: x: {x}, y: {y}, theta:{theta}")

# second motion
v_l = 0.1
v_r = -0.1
t = 1
x, y, theta = diffdrive(x, y, theta, v_l, v_r, t, l)
plt.quiver(x, y, np.cos(theta), np.sin(theta))
print(f"after motion 2: x: {x}, y: {y}, theta:{theta}")

# third motion
v_l = 0.2
v_r = 0.0
t = 2
x, y, theta = diffdrive(x, y, theta, v_l, v_r, t, l)
plt.quiver(x, y, np.cos(theta), np.sin(theta))
print(f"after motion 3: x: {x}, y: {y}, theta:{theta}")

# plot the poses
plt.xlim([0.5, 3.5])
plt.ylim([0.5, 3.5])
plt.savefig("poses.png")
plt.show()
