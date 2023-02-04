import numpy as np 

def diffdrive(x, y, theta, v_l, v_r, t, l):

    if (v_l == v_r):
        thetaa = theta
        x_n = x + v_l * t * np.cos(theta)
        y_n = y + v_l * t * np.sin(theta)
    else:
        R = l/2.0 * ((v_l + v_r) / (v_r - v_l))


        ICC_x = x - R * np.sin(theta)
        ICC_y = y + R * np.cos(theta)

        omega = (v_r - v_l) / l

        chtheta = omega * t

        x_n = np.cos(chtheta)*(x-ICC_x) - np.sin(chtheta)*(y-ICC_y) + ICC_x
        y_n = np.sin(chtheta)*(x-ICC_x) + np.cos(chtheta)*(y-ICC_y) + ICC_y
        thetaa = theta + chtheta
    return x_n, y_n, thetaa

