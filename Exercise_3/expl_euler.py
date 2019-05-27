import numpy as np
from matplotlib import pyplot


def ex_sol(t):
    return -np.log(np.exp(0.5) - t - 0.5*(t**2))


def euler(bound):
    error=[]
    for i in range (1,6):
        y = -1/2
        t = 0
        y_series = [y]
        t_series = [t]
        y_error = [ex_sol(t) - y]
        #y_error = [ex_sol(t)+ 10**-i * np.exp(y) * (1 + t) - ex_sol(t + 10**-i)]
        while t < bound:
            y += 10**-i * np.exp(y) * (1 + t)
            y_series.append(y)
            y_error.append(ex_sol(np.round(t+10**-i, 5))-y)
            #y_error.append(ex_sol(t)+ 10**-i * np.exp(y) * (1 + t) - ex_sol(t + 10**-i))
            t = np.round(t+10**-i, 5)
            t_series.append(t)
        error.append(ex_sol(t)-y)
        pyplot.plot(t_series, y_series)
        pyplot.plot(t_series, y_error)
    print(error)
    pyplot.show()
    return (np.log(error[3]/(error[4]))/(np.log(10**-4/10**-5)))


print(euler(1))
