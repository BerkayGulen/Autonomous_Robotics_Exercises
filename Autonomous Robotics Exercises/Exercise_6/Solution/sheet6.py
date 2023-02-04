import math
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
from matplotlib import cm


def likelihood(m):
    x0 = np.array([12, 4])  # tower 0
    x1 = np.array([5, 7])  # tower 1
    d0 = 3.9  # distance 0
    d1 = 4.5  # distance 1
    var0 = 1  # variance 0
    var1 = 1.5  # variance 1

    # expected distance measurements
    d0_Hat = math.sqrt(np.sum(np.square(m - x0)))
    d1_Hat = math.sqrt(np.sum(np.square(m - x1)))

    p0 = scipy.stats.norm.pdf(d0, d0_Hat, math.sqrt(var0))
    p1 = scipy.stats.norm.pdf(d1, d1_Hat, math.sqrt(var1))
    return p0 * p1


# locations
m0 = np.array([10, 8])  # university
m1 = np.array([6, 3])  # home
x0 = np.array([12, 4])  # tower 0
x1 = np.array([5, 7])  # tower 1

# mesh grid for plotting
x = np.arange(3.0, 15.0, 0.5)
y = np.arange(-5.0, 15.0, 0.5)
X, Y = np.meshgrid(x, y)

# likelihood for each position
z = np.array([likelihood(np.array([x, y])) for x, y in zip(X.flatten(), Y.flatten())])
Z = z.reshape(X.shape)

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, alpha=0.5)
ax.scatter(m0[0], m0[1], likelihood(m0), c='g', marker='o', s=100)
ax.scatter(m1[0], m1[1], likelihood(m1), c='r', marker='o', s=100)
ax.scatter(x0[0], x0[1], likelihood(x0), c='g', marker='^', s=100)
ax.scatter(x1[0], x1[1], likelihood(x1), c='r', marker='^', s=100)

ax.set_xlabel('mx')
ax.set_ylabel('my')
ax.set_zlabel('likelihood')
plt.show()
plt.savefig('likelihood.jpg')

# The plotted likelihood is not a probability density function, because we are plotting p(z | m)
# over map locations m, not measurements z. To get the probability
# distribution p(m | z) over map locations m, we need to know p(m) and p(z) to
# normalize the distribution
