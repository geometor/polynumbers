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
    roots = p_sub.real_roots()
    roots = {root:roots.count(root) for root in roots}
    #  for root in p_sub.real_roots():
    for root in roots:
        root_x = root.simplify()
        count = roots[root]
        print(f'    count: {count}')
        if root_x.is_algebraic:
            root_y = sp.simplify(f(root_x))
            print(f'        x: {root_x}')
            print(f'        y: {root_y}')
            print()
            pt = point(root_x, root_y, classes=['meet'])
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
    roots = p.real_roots()
    roots = {root:roots.count(root) for root in roots}
    #  for root in p.real_roots():
    for root in roots:
        root_x = root.simplify()
        count = roots[root]
        print(f'    count: {count}')
        if root_x.is_algebraic:
            root_y = sp.simplify(f(root_x))
            print(f'        x: {root_x}')
            print(f'        y: {root_y}')
            print()
            pt = point(root_x, root_y, classes=['root'])
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
    roots = p_d.real_roots()
    roots = {root:roots.count(root) for root in roots}
    #  for root in p_d.real_roots():
    for root in roots:
        root_x = root.simplify()
        count = roots[root]
        print(f'    count: {count}')
        if root_x.is_algebraic:
            root_y = sp.simplify(f(root_x))
            print(f'        x: {root_x}')
            print(f'        y: {root_y}')
            print()
            pt = point(root_x, root_y, classes=['vertex'])
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

    d = sp.Matrix([[x**2,x*y,y**2,x,y,1]])

    for i, pt in enumerate(five_pts):
        p_x, p_y = pt[0], pt[1]
        d = d.row_insert(i+1, sp.Matrix([[p_x**2, p_x * p_y, p_y**2, p_x, p_y,1]]))
    
    #  expr = sp.Eq(d.det(),0)
    expr = sp.simplify(d.det())
    
    print(expr)

    return expr
    
