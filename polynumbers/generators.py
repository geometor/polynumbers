'''
polynomial generators
'''
from geometor.utils import *
from geometor.model import *
from geometor.render import *

def Spread(n):
    n = sp.Integer(n)
    p = sp.Integer(0)
    for k in range(1, n+1):
        k = sp.Integer(k)
        p += sp.Poly(((-4)**(k-1))/(n+k) * sp.binomial(n+k,2*k) * x**k)
    return 2*n*p

