from polynumbers import *

from IPython.display import display

count = 5
print('count:', count)

NAME = 'polynumbers'
NAME += input(f'\nsession folder: {NAME}')

results = []
polys = []

limx, limy = (-0.1, 1.1), (-0.1, 1.1)

for n in range(1, count + 1):
    p = Spread(n)
    p = p.as_poly()

    if hasattr(p, 'expr'):
        polys.append(p)
        #  display(p.expr)
    if hasattr(p, 'coeffs'):
        cfs = p.all_coeffs()
        cfs.reverse()
        #  print(cfs)
        results.append(cfs)
    #  print('-----------------------')

xs = np.arange(limx[0], limx[1], .001)


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
    f = sp.lambdify(x, expr, 'numpy')
    ys = f(xs)
    #  print('ys:')
    #  print(ys)

    ax.plot(xs, ys)
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
    snapshot(f'{NAME}', f'{i:0>3}.png')
#  plots.save('spread_polynomials.png')

goldens = analyze_golden_pts(pts)
print('GOLDENS:', len(goldens))
for g in goldens:
    print(g)

plot_points(ax, pts)
snapshot(f'{NAME}', f'summary.png')
plt.show()
