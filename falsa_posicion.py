import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve
from sympy import symbols, Eq, solve

def false_position_method(func, a, b, error_estimated):
    iter_count = 0
    error_approx_prev = None

    print("")
    print("----------------------------------------Metodo de Falsa Posición--------------------------------------------------------------------- ")
    print("{:<5} {:<10} {:<10} {:<10} {:<15} {:<15} {:<15} {:<15}".format("Iter", "xl", "xu", "xr", "f(xl)", "f(xu)", "f(xr)", "ErrorAproximado"))

    while True:
        f_a = func(a)
        f_b = func(b)
        
        xr = b - (f_b * (a - b)) / (f_a - f_b)
        f_xr = func(xr)

        iter_count += 1

        if iter_count == 1:
            error_approx = None
        else:
            error_approx = abs((xr - error_approx_prev) / xr) * 100

        if error_approx is None:
            print("{:<5} {:<10.6f} {:<10.6f} {:<10.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15}".format(iter_count, a, b, xr, f_a, f_b, f_xr, ""))
        else:
            print("{:<5} {:<10.6f} {:<10.6f} {:<10.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f}".format(iter_count, a, b, xr, f_a, f_b, f_xr, error_approx))

        if f_xr == 0 or (error_approx is not None and error_approx < error_estimated):
            return xr, iter_count

        if np.sign(f_xr) == np.sign(f_a):
            a = xr
        else:
            b = xr

        error_approx_prev = xr

# Método de falsa posición
root_false_position, iterations_fp = false_position_method(f, lower_limit, upper_limit, error_estimated)

# Imprimir la raíz encontrada con el método de falsa posición
print("\nMétodo de Falsa Posición:")
print(f"Raíz encontrada: {root_false_position:.6f}")
print(f"Iteraciones necesarias: {iterations_fp}")