from polynumbers import *

from IPython.display import display

NAME = 'polynumbers'
NAME += input(f'\nsession folder: {NAME}')

def Chebyshev(n):
    n = sp.Integer(n)

    p = sp.Poly((-((-1)**n+1)/2)**((n+4)/2))
    for i in range(1, n+1):
        i = sp.Integer(i)
        p += sp.Poly(n*(((-1)**(n+i)+1)/2 * (-1)**((n-i)/2)) * 2**(i-1) * \
                sp.factorial((n-2+i)//2)/(sp.factorial((n-i)//2) * sp.factorial(i)) * x**i)
    return p

results = []
polys = []

count = 20
limx, limy = (-0.1, 1.1), (-0.1, 1.1)

for n in range(1, count + 1):
    p = Spread(n)
    # p = chebyshevt(n, x)
    # p = chebyshevu(n, x)
    p = p.as_poly()

    #  display((sp.Indexed('T', n), p))
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

#  ax.xlim = limx
#  ax.ylim = limy
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
#  display(s1_pts)

#  plots.show()

    #  ax.clear()
    #  ax_btm.clear()

    #  ax.axis('off')
    #  ax_btm.axis('off')
    #  ax.set_aspect('equal')
    #  plt.tight_layout()

    #  title = f'G E O M E T O R • pappus • perm: {perm_id}'
    #  fig.suptitle(title, fontdict={'color': '#960', 'size':'small'})

    #  folder = f'{NAME}/{perm_id}'
    #  print_log('\nPlot Sequence')
    #  build_sequence(folder, ax, ax_btm, history, bounds)

    #  print_log('\nPlot Harmonic Ranges')

    #  print_log(f'\nPERM: {perm_id}')
    #  print_log(f'    elements: {len(elements)}')
    #  print_log(f'    points:   {len(pts)}')



#  # ANALYZE ***************************
#  print_log(f'\PLOT: ALL')

#  ax.clear()
#  title = f'G E O M E T O R • pappus • all'
#  ax.set_title(title, fontdict={'color': '#960', 'size':'small'})
#  ax.axis(False)

#  folder = f'{NAME}/all'
#  print_log('\nPlot Sequence')
#  build_sequence(folder, ax, ax_btm, history, bounds)

#  print_log('\nPlot Harmonic Ranges')
#  #  folder += '/ranges'
#  plot_ranges(folder, ax, ax_btm, history, harmonics, bounds)
#  plot_all_ranges(folder, ax, ax_btm, history, harmonics, bounds)

#  print_log(f'\nCOMPLETE: {NAME}')
#  print_log(f'    elements: {len(elements)}')
#  print_log(f'    points:   {len(pts)}')
#  print_log(f'    ranges:  {len(harmonics)}')
#  plt.show()
