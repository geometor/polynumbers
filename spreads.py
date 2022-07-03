from polynumbers import *

from IPython.display import display
#  plt.rcParams['image.cmap'] = 'copper'
#  plt.set_cmap('copper')
#  from cycler import cycler

plt.rcParams['axes.prop_cycle'] = mp.cycler(color=['#F906', '#90F6', '#0F96'])

count = 2**7
# division across the unit
divisions = 2**16
span = sp.Rational(9, 8)
k = sp.Rational(1, divisions)

steps = span / k

print('count:', count)
print('division:', divisions)
print('k:', k)
print('span:', span)
print('steps:', steps)

NAME = 'polynumbers/spread'
NAME += input(f'\nsession folder: {NAME}')

results = []
polys = []


for n in range(1, count + 1):
    p = Spread(n)
    
    #  p = sp.chebyshevt_poly(n, x).as_poly()

    if hasattr(p, 'expr'):
        polys.append(p)
        #  display(p.expr)
    if hasattr(p, 'coeffs'):
        cfs = p.all_coeffs()
        cfs.reverse()
        #  print(cfs)
        results.append(cfs)
    #  print('-----------------------')



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

exprs = [p.expr for p in polys]
for i, poly in enumerate(polys):
    expr = poly.expr
    print('---')
    print(i)
    print(expr)
    
    #  f = sp.lambdify(x, expr)
    #  ys = [f(x_val) for x_val in xs]
    ys = [poly.eval(x_val) for x_val in xs]
    ysf = [float(y_val) for y_val in ys]

    ax.plot(xsf, ysf)

    if i > 0 and i < 5:
        sub = expr - exprs[0]
        print(f'    sub: {sub}')

        #  roots = sp.solve(sub, x)
        roots = sp.roots(sub)
        f = sp.lambdify(x, expr)
        for root in roots:
            root = root.simplify()
            print(f'        {root}')
            #  print(f'        {sp.simplify(root)}')
            print(f'        {f(root)}')
            print()
            pt = point(root, f(root))
            print(pt)
            add_point(pt)
    snapshot(f'{NAME}', f'{i:0>5}.png')
#  plots.save('spread_polynomials.png')

# zoom to origin
#  left_zoom = np.arange(1, 1/256, -1/1024)
num_steps = 2 ** 10
steps = np.arange(num_steps)
steps = np.sqrt(steps)
steps = steps / steps.sum()
steps = steps.cumsum()
steps = reversed(steps)

print(steps)

for i, xmax in enumerate(steps):

    ax.set_xlim(0, xmax)
    snapshot(f'{NAME}/left_zoom', f'{i:0>5}.png')

for i, xmax in enumerate(steps):
    xmax = xmax / 2
    
    ax.set_xlim(xmax, .5 + xmax)
    snapshot(f'{NAME}/center', f'{i:0>5}.png')


goldens = analyze_golden_pts(pts)
print('GOLDENS:', len(goldens))
for g in goldens:
    print(g)

plot_points(ax, pts)
snapshot(f'{NAME}', f'summary.png')
plt.show()
