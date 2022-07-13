from polynumbers import *

PLOT = True
ANALYZE = False
POINTS = True
ZOOM = False
DIVISOR = 2**12

#  colors = ['#F906', '#90F6', '#0F96']
colors = ['#F906', '#90F6']

def main():

    count = 2**3

    folder = 'polynumbers/goldens'
    folder += input(f'\nsession folder: {folder}')
    log_init(folder)
    start_time = timer()

    results = []

    print('Generate:')
    polys = golden_polys(count)
    #  polys = spread_polys(count)

    for n, p in enumerate(polys):
        expr = p.expr
        print('------------------------------')
        print(n)
        print(expr)

        cfs = []
        if hasattr(p, 'coeffs'):
            cfs = p.all_coeffs()
            cfs.reverse()
            results.append(cfs)

        for i, cf in enumerate(cfs):
            print(f'    {i}: {cf}')


        print('    roots: ')
        root_points(p)

        print('    vertices: ')
        vertex_points(p)

        # find meets with previous curves
        for p_prev in polys[:-1]:
            print('    meet: ', p_prev)
            meet_points(p, p_prev)

    if ANALYZE:
        print('GOLDENS:')
        x_points = set()
        for pt in pts:
            x_points.add(point(pt.x, 0))
        x_points = sort_points(x_points)

        golden_sections = analyze_golden_pts(x_points)
        print('x series:', len(golden_sections))
        for g in golden_sections:
            print(g)
        
        y_points = set()
        for pt in pts:
            y_points.add(point(0, pt.y))
        y_points = sort_points(y_points)

        golden_sections = analyze_golden_pts(y_points)
        print('y series:', len(golden_sections))
        for g in golden_sections:
            print(g)
        

    if PLOT:
        print('PLOT')
        limx, limy = get_limits_from_points(pts, margin=.0625)
        bounds = set_bounds(limx, limy)

        fig, ax = ax_prep_full(bounds)
        ax.set_aspect('equal')

        #add start points and baseline
        A = point(0, 0, classes=['start'])
        B = point(1, 0, classes=['start'])
        baseline = line(A, B)
        highlight_points(ax, [A, B])
        plot_points(ax, [A, B])
        plot_line(ax, baseline, bounds)
        
        plot_polys(folder, ax, polys, limx, limy, DIVISOR)

        print('number of curves:', len(polys))
        print('resolution:', DIVISOR)

        print('points: ', len(pts))
        plot_points(ax, pts)
        snapshot(folder, f'summary.png')

        plt.show()

if __name__ == '__main__':
    main()
