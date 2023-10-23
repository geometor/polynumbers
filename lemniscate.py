import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sin, cos, lambdify

# Define the parameter
t = symbols('t')

# Define the parametric equations
x_expr = sin(t)
y_expr = sin(t) * cos(t)

# Lambdify the expressions
x_func = lambdify(t, x_expr, "numpy")
y_func = lambdify(t, y_expr, "numpy")

# Generate t values
t_values = np.linspace(-2*np.pi, 2*np.pi, 400)

# Compute x and y values
x_values = x_func(t_values)
y_values = y_func(t_values)

# Plotting
plt.plot(x_values, y_values, label='Lemniscate: x=sin(t), y=sin(t)cos(t)')
plt.title('Plot of the Lemniscate')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.legend()
plt.axis('equal')
plt.show()

