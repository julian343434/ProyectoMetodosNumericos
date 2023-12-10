import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve
from sympy import symbols, Eq, solve
def bisection_method(func, a, b, error_estimated):
    iter_count = 0
    error_approx_prev = None

    print("")
    print("-----------------------------------------------------------Metodo de Bisección--------------------------------------------------------- ")
    print("{:<5} {:<10} {:<10} {:<10} {:<15} {:<15} {:<15} {:<15}".format("Iter", "xl", "xu", "xr", "f(xl)", "f(xu)", "f(xr)", "ErrorAproximado"))

    while True:
        c = (a + b) / 2
        f_a = func(a)
        f_b = func(b)
        f_c = func(c)

        iter_count += 1

        if iter_count == 1:
            error_approx = None
        else:
            error_approx = abs((c - error_approx_prev) / c) * 100

        if error_approx is None:
            print("{:<5} {:<10.6f} {:<10.6f} {:<10.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15}".format(iter_count, a, b, c, f_a, f_b, f_c, ""))
        else:
            print("{:<5} {:<10.6f} {:<10.6f} {:<10.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f}".format(iter_count, a, b, c, f_a, f_b, f_c, error_approx))

        if f_c == 0 or (error_approx is not None and error_approx < error_estimated):
            return c, iter_count

        if np.sign(f_c) == np.sign(f_a):
            a = c
        else:
            b = c

        error_approx_prev = c

#Método de bisección
root_bisection, iterations = bisection_method(f, lower_limit, upper_limit, error_estimated)

# Imprimir la raíz encontrada con el método de bisección
print("\nMétodo de Bisección:")
print(f"Raíz encontrada: {root_bisection:.6f}")
print(f"Iteraciones necesarias: {iterations}")