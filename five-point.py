from polynumbers import *
from IPython.display import display

PLOT = True
POINTS = True
ZOOM = False

#  plt.rcParams['axes.prop_cycle'] = mp.cycler(color=['#F906', '#90F6', '#0F96'])
plt.rcParams['axes.prop_cycle'] = mp.cycler(color=['#F906', '#90F6'])

count = 2**3
# division across the unit
divisions = 2**12

NAME = 'polynumbers/spread/point'
NAME += input(f'\nsession folder: {NAME}')

results = []
polys = []


print('Generate:')
for n in range(1, count + 1):
    #  p = sp.hermite_poly(n, x).as_poly()
    #  p = sp.jacobi_poly(n, x).as_poly()
    #  p = sp.chebyshevt_poly(n, x).as_poly()
    p = Spread(n)
    expr = p.expr
    print('------------------------------')
    print(n)
    print(expr)
    polys.append(p)

    if hasattr(p, 'coeffs'):
        cfs = p.all_coeffs()
        cfs.reverse()
        results.append(cfs)

    print('    roots: ')
    root_points(p)

    print('    vertices: ')
    vertex_points(p)

    # find meets with previous curves
    for p_prev in polys[:-1]:
        print('    meet: ', p_prev)
        meet_points(p, p_prev)

#  goldens = analyze_golden_pts(pts)
#  print('GOLDENS:', len(goldens))
#  for g in goldens:
    #  print(g)

if PLOT:
    print('PLOT')
    #  span = sp.Rational(9, 8)
    #plot config
    #  limx, limy = (-1/2**6, 1+1/2**6), (-1/2**6, 1+1/2**6)
    limx, limy = get_limits_from_points(pts, margin=.0625)

    span = limx[1] - limx[0]
    k = sp.Rational(1, divisions)
    steps = int(span / k)
    
    xs = []
    # starting point in the range
    #  xs.append(sp.Rational(-1, 16))
    xs.append(limx[0])

    # construct list of x rational values for plotting
    for _ in range(steps):
        xs.append(xs[-1] + k)

    xsf = [float(x_val) for x_val in xs]


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


    five = []
    five.append(pts[0])
    five.append(pts[9])
    five.append(pts[3])
    five.append(pts[8])
    five.append(point(0, 1))
    
    conic = find_conic_from_pts(five)
    print('conic: ', conic)


    print('count:', count)
    print('division:', divisions)
    print('k:', k)
    print('span:', span)
    print('steps:', steps)

    print('points: ', len(pts))

    plt.show()
