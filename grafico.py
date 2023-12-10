import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve
from sympy import symbols, Eq, solve
# Generar datos para la gráfica
x_values = np.linspace(-3, 3, 400)  # Ajusta el rango de valores para incluir todo el plano cartesiano
y_values = f(x_values)

# Encontrar puntos de intersección con el eje x
roots_fsolve = fsolve(f, [-2, -1, 1])

# Imprimir las raíces encontradas con fsolve
print("Raíces encontradas con fsolve:", roots_fsolve)

# Crear la gráfica
plt.plot(x_values, y_values, label=f'f(x) = {str(f(x_sym))}')  # Utiliza la representación simbólica
plt.scatter(roots_fsolve, [0, 0, 0], color='red', label='Puntos de intersección')

# Marcar los puntos de intersección en la gráfica
for root in roots_fsolve:
    plt.annotate(f'({root:.2f}, 0)', (root, 0), textcoords="offset points", xytext=(0,10), ha='center')

# Configurar límites del eje x e y para mostrar todo el plano cartesiano
plt.xlim([min(x_values), max(x_values)])
plt.ylim([min(y_values), max(y_values)])

# Activar la cuadrícula
plt.grid(True)

plt.title('Método Gráfico')
plt.xlabel('x')
plt.ylabel('f(x)')

# Mostrar la leyenda
plt.legend()

# Mostrar la gráfica
plt.show()