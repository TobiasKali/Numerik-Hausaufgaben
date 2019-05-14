import numpy as np
from matplotlib import pyplot


def ex_sol(t):
    return -np.log(np.exp(0.5) - t - 0.5*(t**2))


def euler(delta_t, bound):
    y = -1/2
    t = 0

    y_series = [y]
    t_series = [t]

    #y_error = [ex_sol(t) - y]
    y_error = [ex_sol(t)+ delta_t * np.exp(y) * (1 + t) - ex_sol(t + delta_t)]
    while t < bound:
        y += delta_t * np.exp(y) * (1 + t)
        y_series.append(y)
        #y_error.append(ex_sol(t + delta_t)-y)
        y_error.append(ex_sol(t)+ delta_t * np.exp(y) * (1 + t) - ex_sol(t + delta_t))
        t += delta_t
        t_series.append(t)

    pyplot.plot(t_series, y_series)
    pyplot.plot(t_series, y_error)
    pyplot.show()


euler(10**-5, 1)

