import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify

# Define the symbol
t = symbols('t')

# Generate t values
t_values = np.linspace(-2, 2, 400)

# Creating a figure to plot the curves
plt.figure()

# Looping through polynomial degrees from 2 to 5
for degree in range(2, 6):
    # Defining the parametric equations
    x_expr = t
    y_expr = sum([t**i for i in range(degree+1)]) - t - 1
    
    # Lambdifying the expressions
    x_func = lambdify(t, x_expr, "numpy")
    y_func = lambdify(t, y_expr, "numpy")
    
    # Computing x and y values
    x_values = x_func(t_values)
    y_values = y_func(t_values)
    
    # Plotting
    plt.plot(x_values, y_values, label=f'Degree {degree} Polynomial')

# Adding titles and labels
plt.title('Plot of the Curves')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.axis('equal')  # Setting the aspect ratio to be equal
plt.axis([-2, 2, -10, 10])  # Adjust the axis limits if necessary
plt.show()

