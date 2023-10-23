import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify

# Define the parameter
t = symbols('t')

# Define the parametric equations
x_expr = t
y_expr = t**2 - t**1 - 1

# Lambdify the expressions
x_func = lambdify(t, x_expr, "numpy")
y_func = lambdify(t, y_expr, "numpy")

# Generate t values
t_values = np.linspace(-3, 3, 400)

# Compute x and y values
x_values = x_func(t_values)
y_values = y_func(t_values)

# Plotting
plt.plot(x_values, y_values, label='Curve: y = x^3 - x^2 - x')
plt.title('Plot of the Curve')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.show()

