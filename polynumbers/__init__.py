from geometor.utils import *
from geometor.model import *
from geometor.render import *
from .generators import *
from .render import *

def meet_points(p1, p2):
    meet_pts = []
    p_sub = p1 - p2
    f = sp.lambdify(x, p1.expr)
    print('        sub: ', p_sub)
    for root in p_sub.real_roots():
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


def root_points(p):
    root_pts = []
    f = sp.lambdify(x, p.expr)
    for root in p.all_roots():
        root_x = root.simplify()
        if root_x.is_algebraic:
            root_y = sp.simplify(f(root_x))
            print(f'        x: {root_x}')
            print(f'        y: {root_y}')
            print()
            pt = point(root_x, root_y)
            #  print(pt)
            pt = add_point(pt)
            root_pts.append(pt)
        else:
            print(f'        x: {root_x}')
            print(f'        NOT ALGEBRAIC')
            print(f'        x: {float(root_x)}')
            print(f'        y: {f(float(root_x))}')
            print()
    return root_pts


def vertex_points(p):
    vertex_pts = []
    p_d = p.diff()
    f = sp.lambdify(x, p.expr)
    for root in p_d.all_roots():
        root_x = root.simplify()
        if root_x.is_algebraic:
            root_y = sp.simplify(f(root_x))
            print(f'        x: {root_x}')
            print(f'        y: {root_y}')
            print()
            pt = point(root_x, root_y)
            #  print(pt)
            pt = add_point(pt)
            vertex_pts.append(pt)
        else:
            print(f'        x: {root_x}')
            print(f'        NOT ALGEBRAIC')
            print(f'        x: {float(root_x)}')
            print(f'        y: {f(float(root_x))}')
            print()
    return vertex_pts


def find_conic_from_pts(five_pts):
    '''Function that takes a list of 5 points and returns the conic equation
    that corresponds to those points

    Returns
    -------
    Sympy equation of the conic

    '''

    # We assume the equation to be A*x**2+B*y**2+C*x*y+D*x+E*y+1=0

    d = sp.Matrix()

    for i, pt in enumerate(five_pts):
        p_x, p_y = pt.x,  pt.y
        d = d.row_insert(i, sp.Matrix([[p_x**2, p_y**2, p_x * p_y, p_x, p_y]]))

    d_det = d.det()
    coeff = []
    #  breakpoint()
    for i in range(len(five_pts)):
        d_coeff = d.copy()
        d_coeff.col_del(i)
        d_coeff = d_coeff.col_insert(i, sp.Matrix([-1, -1, -1, -1, -1]))
        coeff.append(d_coeff.det() / d_det)

    expr =  coeff[0] * x**2 + coeff[1] * y**2 + coeff[2] * x * y + coeff[3] * x + coeff[4] * y + 1
    print(expr)
    #  breakpoint()
    return expr
    #  return sp.Eq(coeff[0] * x**2 + coeff[1] * y**2 + coeff[2] * x * y + coeff[3] * x + coeff[4] * y + 1, 0)
