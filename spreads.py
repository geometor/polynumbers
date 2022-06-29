from polynumbers import *

from IPython.display import display
#  plt.rcParams['image.cmap'] = 'copper'
#  plt.set_cmap('copper')
from cycler import cycler

#  plt.rcParams['axes.prop_cycle'] = cycler('color', mp.cm.get_cmap('gray').colors)


count = 10
print('count:', count)

NAME = 'polynumbers/spread'
NAME += input(f'\nsession folder: {NAME}')

results = []
polys = []


for n in range(1, count + 1):
    p = Spread(n)
    #  p = p.as_poly()

    if hasattr(p, 'expr'):
        polys.append(p)
        #  display(p.expr)
    if hasattr(p, 'coeffs'):
        cfs = p.all_coeffs()
        cfs.reverse()
        #  print(cfs)
        results.append(cfs)
    #  print('-----------------------')


#  def SpreadPoly(n):
    #  p = []
    #  for k in range(1,n+1):
        #  p += [Fraction(-n * comb(n+k,n-k) * (-4)**k, (2*(n+k)))]
    #  return p[::-1]

#  def PolyEval(p, x):
    #  r = Fraction(0,1)
    #  for k in range(len(p)):
        #  i = p[k]
        #  r = x * (i + r)
    #  return r

#  def getPoints(n, density):
    #  p = SpreadPoly(n)
    #  i = Fraction(1, density)
    #  k = Fraction(-1,density)
    #  x, y = [], []
    #  for j in range(density+1):
        #  k += i
        #  x.append(k)
        #  y.append(PolyEval(p, k))
    #  return x, y


limx, limy = (-0.1, 1.1), (-0.1, 1.1)

fig, (ax, ax_btm) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [10, 1]})
ax.axis('off')
ax_btm.axis('off')
bounds = set_bounds(limx, limy)

plt.tight_layout()
ax_prep(ax, ax_btm, bounds, "spread polynomials")

#  xs = np.arange(limx[0], limx[1], .001)
xs = []
# starting point in the range
xs.append(sp.Rational(-1, 8))

# division across the unit
divisions = 2**12
span = sp.Rational(5, 4)
k = sp.Rational(1, divisions)

steps = span / k

print('division:', divisions)
print('k:', k)
print('span:', span)
print('steps:', steps)

for _ in range(steps):
    #  xs.append(sp.simplify(xs[-1] + k))
    xs.append(xs[-1] + k)

print(xs)

#  xsf = [float(sp.evalf(x_val)) for x_val in xs]
xsf = [float(x_val) for x_val in xs]

#  float(sp.evalf(x_val)) for x_val in xs]

exprs = [p.expr for p in polys]
for i, poly in enumerate(polys):
    expr = poly.expr
    print('---')
    print(i)
    print(expr)
    
    f = sp.lambdify(x, expr)
    ys = [f(x_val) for x_val in xs]
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
    snapshot(f'{NAME}', f'{i:0>3}.png')
#  plots.save('spread_polynomials.png')

goldens = analyze_golden_pts(pts)
print('GOLDENS:', len(goldens))
for g in goldens:
    print(g)

plot_points(ax, pts)
snapshot(f'{NAME}', f'summary.png')
plt.show()
