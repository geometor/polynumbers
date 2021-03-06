import matplotlib as mpl
import matplotlib.pyplot as plt
import sympy as sp
from geometor.render import *

def get_xs_values(limx, divisor):
    span = limx[1] - limx[0]
    h = sp.Rational(1, divisor)
    steps = int(span / h)
    
    xs = []
    # starting point in the range
    #  xs.append(sp.Rational(-1, 16))
    xs.append(limx[0])

    # construct list of x rational values for plotting
    for _ in range(steps):
        xs.append(xs[-1] + h)

    xsf = [float(x_val) for x_val in xs]

    return xs, xsf

def ax_left_zoom(folder, ax, num_steps = 2**8):

    num_steps = 2 ** 8
    steps = np.arange(num_steps)
    steps = np.sqrt(steps)
    steps = steps / steps.sum()
    steps = steps.cumsum()
    steps = reversed(steps)

    for i, xmax in enumerate(steps):
        ax.set_xlim(0, xmax)
        snapshot(f'{folder}/left_zoom', f'{i:0>5}.png')

    ax.set_xlim(limx[0], limx[1])

def plot_polys(folder, ax, polys, limx, limy, divisor, colors=''):
    if colors:
        plt.rcParams['axes.prop_cycle'] = mp.cycler(color=colors)

    xs, xsf = get_xs_values(limx, divisor)

    for i, poly in enumerate(polys):
        ys = [poly.eval(x_val) for x_val in xs]
        ysf = [float(y_val) for y_val in ys]

        ax.plot(xsf, ysf)

        snapshot(f'{folder}', f'{i:0>5}.png')



