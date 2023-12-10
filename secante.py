import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve
from sympy import symbols, Eq, solve
from tabulate import tabulate

def secant_method(f, x_minus1, x_0, tolerance=None, max_iterations=None):
    results = []

    for iteration in range(max_iterations) if max_iterations else range(1, 1000):
        f_x0 = f(x_0)
        f_x_minus1 = f(x_minus1)

        x_1 = x_0 - (f_x0 * (x_minus1 - x_0)) / (f_x_minus1 - f_x0)
        error_relative = abs((x_1 - x_0) / x_1) * 100 if x_1 != 0 else 0

        results.append([iteration, f_x0, f_x_minus1, x_1, error_relative])

        if tolerance and error_relative < tolerance:
            break

        x_minus1, x_0 = x_0, x_1

    return results

def print_table(results, decimal_places):
    headers = ["Iteración", "f(x_i)", "f(x_(i-1))", "x_i", "Error Relativo"]
    formatted_results = [[f"{val:.{decimal_places}f}" for val in row] for row in results]

    print(tabulate(formatted_results, headers=headers, tablefmt="grid"))

def main():
    # Definir la función
    def f(x):
        return 2*x**3-11.7*x**2+17.7*x-5

    # Obtener parámetros del usuario
    x_minus1 = float(input("Ingrese el valor inicial de x_(-1): "))
    x_0 = float(input("Ingrese el valor inicial de x_0: "))
    decimal_places = int(input("Ingrese la cantidad de cifras significativas: "))

    method_option = input("¿Desea iterar por cantidad de iteraciones (I) o por Error Relativo (E)? ").upper()

    if method_option == "I":
        max_iterations = int(input("Ingrese la cantidad de iteraciones: "))
        results = secant_method(f, x_minus1, x_0, max_iterations=max_iterations)
    elif method_option == "E":
        tolerance = float(input("Ingrese el valor de Error Relativo deseado: "))
        results = secant_method(f, x_minus1, x_0, tolerance=tolerance)
    else:
        print("Opción no válida.")
        return

    # Imprimir resultados
    print_table(results, decimal_places)

if __name__ == "__main__":
    main()