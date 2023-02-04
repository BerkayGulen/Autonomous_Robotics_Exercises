import numpy as np
import matplotlib.pyplot as plt
from sheet3_2_a import diffdrive

plt.gca().set_aspect('equal')

l = 0.5
x, y, theta = 1.5, 2.0, (np.pi)/2.0

plt.quiver(x, y, np.cos(theta), np.sin(theta))
print (f"starting pose: x: {x}, y: {y}, theta:{theta}" )

# first motion
v_l = 0.3
v_r = 0.3
t = 3
x, y, theta = diffdrive(x, y, theta, v_l, v_r, t, l)
plt.quiver(x, y, np.cos(theta), np.sin(theta))
print (f"after motion 1: x: {x}, y: {y}, theta:{theta}")

# second motion
v_l = 0.1
v_r = -0.1
t = 1
x, y, theta = diffdrive(x, y, theta, v_l, v_r, t, l)
plt.quiver(x, y, np.cos(theta), np.sin(theta))
print (f"after motion 2: x: {x}, y: {y}, theta:{theta}")

# third motion
v_l = 0.2
v_r = 0.0
t = 2
x, y, theta = diffdrive(x, y, theta, v_l, v_r, t, l)
plt.quiver(x, y, np.cos(theta), np.sin(theta))
print (f"after motion 3: x: {x}, y: {y}, theta:{theta}")

plt.xlim([0.5, 3.5])
plt.ylim([0.5, 3.5])
plt.savefig("pose.png")
plt.show()