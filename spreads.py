from polynumbers import *
from IPython.display import display

PLOT = True
ZOOM = False

plt.rcParams['axes.prop_cycle'] = mp.cycler(color=['#F906', '#90F6', '#0F96'])

count = 2**4
# division across the unit
divisions = 2**12
span = sp.Rational(9, 8)
k = sp.Rational(1, divisions)

steps = span / k

print('count:', count)
print('division:', divisions)
print('k:', k)
print('span:', span)
print('steps:', steps)

NAME = 'polynumbers/spread/point'
NAME += input(f'\nsession folder: {NAME}')

results = []
polys = []

def meets(p1, p2):
    meet_pts = []
    p_sub = p1 - p2
    f = sp.lambdify(x, p1.expr)
    print('        sub: ', p_sub)
    for root in p_sub.all_roots():
        root_x = root.simplify()
        if root_x.is_algebraic:
            root_y = sp.simplify(f(root_x))
            print(f'        x: {root_x}')
            print(f'        y: {root_y}')
            print()
            pt = point(root_x, root_y)
            #  print(pt)
            pt = add_point(pt)
            meet_pts.append(pt)
        else:
            print(f'        x: {root_x}')
            print(f'        NOT ALGEBRAIC')
            print(f'        x: {float(root_x)}')
            print(f'        y: {f(float(root_x))}')
            print()
    return meet_pts


print('Generate:')
for n in range(1, count + 1):
    #  p = sp.chebyshevt_poly(n, x).as_poly()
    p = Spread(n)
    expr = p.expr
    print('---')
    print(n)
    print(expr)
    polys.append(p)

    if hasattr(p, 'coeffs'):
        cfs = p.all_coeffs()
        cfs.reverse()
        results.append(cfs)

    # find meets with previous curves
    for p_prev in polys[:-1]:
        print('    test: ', p_prev)
        meets(p, p_prev)

#  goldens = analyze_golden_pts(pts)
#  print('GOLDENS:', len(goldens))
#  for g in goldens:
    #  print(g)

if PLOT:
    #  xs = np.arange(limx[0], limx[1], .001)
    xs = []
    # starting point in the range
    xs.append(sp.Rational(-1, 16))

    # construct list of x rational values for plotting
    for _ in range(steps):
        xs.append(xs[-1] + k)

    xsf = [float(x_val) for x_val in xs]

    #plot config
    limx, limy = (-1/2**6, 1+1/2**6), (-1/2**6, 1+1/2**6)

    fig, (ax, ax_btm) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [10, 1]})
    ax.axis('off')
    ax_btm.axis('off')
    bounds = set_bounds(limx, limy)

    plt.tight_layout()
    ax_prep(ax, ax_btm, bounds, "spread polynomials")

    #  exprs = [p.expr for p in polys]
    for i, poly in enumerate(polys):
        
        ys = [poly.eval(x_val) for x_val in xs]
        ysf = [float(y_val) for y_val in ys]

        ax.plot(xsf, ysf)

        snapshot(f'{NAME}', f'{i:0>5}.png')


    if ZOOM:
        # zoom to origin
        #  left_zoom = np.arange(1, 1/256, -1/1024)
        num_steps = 2 ** 8
        steps = np.arange(num_steps)
        steps = np.sqrt(steps)
        steps = steps / steps.sum()
        steps = steps.cumsum()
        steps = reversed(steps)

        for i, xmax in enumerate(steps):
            ax.set_xlim(0, xmax)
            snapshot(f'{NAME}/left_zoom', f'{i:0>5}.png')

    ax.set_xlim(limx[0], limx[1])
    plot_points(ax, pts)
    snapshot(f'{NAME}', f'summary.png')
    plt.show()
