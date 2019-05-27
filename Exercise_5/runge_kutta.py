import numpy as np
import matplotlib.pyplot as pl


def f(y):
    v = np.array([y[1], (-9.81/0.6) * np.sin(y[0])])
    return v


def rk():
    g = 9.81
    l = 0.6
    y = np.array([(3/4)*np.pi, 0])
    t = 0
    t_series = [t]
    y_series = [(3/4)*np.pi]
    while t <= 10:
        # compute theta'(t_(i+1))
        k_1 = y
        k_2 = y + 0.01*0.5*f(k_1)
        k_3 = y + 0.01*(-f(k_1)+2*f(k_2))

        y = y + 0.01 * (f(k_1)+4*f(k_2)+f(k_3))/6
        y_series.append(y[0])

        t += 0.01
        t_series.append(t)

    pl.plot(t_series, y_series)
    pl.show()
    print(y)

print(np.sin((3/4)*np.pi))
rk()