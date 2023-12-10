import math
from tabulate import tabulate

class ImprovedNewtonRaphson:
    def __init__(self, function, initial_guess, max_iterations=None, tolerance=None):
        self.function = function
        self.initial_guess = initial_guess
        self.max_iterations = max_iterations
        self.tolerance = tolerance
        self.iterations_data = []

    def _derivative(self, x, order=1, h=1e-5):
        if order == 1:
            return (self.function(x + h) - self.function(x)) / h
        elif order == 2:
            return (self._derivative(x + h, order=1) - self._derivative(x, order=1)) / h

    def _calculate_error(self, x_new, x_old):
        return abs((x_new - x_old) / x_new) * 100 if x_new != 0 else 0

    def _round_result(self, value, significant_digits):
        # Redondear el resultado a la cantidad de cifras significativas deseada
        if value == 0:
            return 0.0
        order_of_magnitude = math.floor(math.log10(abs(value)))
        rounded_value = round(value, significant_digits - order_of_magnitude - 1)
        return rounded_value

    def solve(self, significant_digits=4):
        x = self.initial_guess
        iteration = 0

        f_x = self.function(x)
        f_prime_x = self._derivative(x, order=1)
        f_double_prime_x = self._derivative(x, order=2)
        x_new = x - (f_x * f_prime_x) / ((f_prime_x**2) - f_x * f_double_prime_x)

        self.iterations_data.append((iteration, f_x, x, None))

        while True:
            f_x = self.function(x)
            f_prime_x = self._derivative(x, order=1)
            f_double_prime_x = self._derivative(x, order=2)

            x_new = x - (f_x * f_prime_x) / (f_prime_x**2 - f_x * f_double_prime_x)
            x_new_rounded = self._round_result(x_new, significant_digits)
            error = self._calculate_error(x_new_rounded, x)

            self.iterations_data.append((iteration + 1, f_x, x_new_rounded, error))

            if self.max_iterations is not None and iteration >= self.max_iterations - 1:
                break
            if self.tolerance is not None and error < self.tolerance:
                break

            x = x_new
            iteration += 1

    def display_results(self):
        table_header = ["Iteraciones", "f(x)", "x_n", "Error Relativo"]
        table_data = []

        for iteration, f_x, x_n, error in self.iterations_data[1:]:  # Excluye la primera iteración
            table_data.append([iteration, f_x, x_n, error])

        # Mostrar la tabla utilizando tabulate
        print(tabulate(table_data, headers=table_header, tablefmt="grid"))

# Ejemplo de uso con entrada del usuario:
if __name__ == "__main__":
    def my_function(x):
        return x**3 - 5*x**2 + 7*x - 3

    # Solicitar la condición inicial, método de parada y cifras significativas al usuario
    initial_guess = float(input("Ingrese la condición inicial: "))
    method_choice = input("Elija el método de parada ('iter' para iteraciones, 'error' para error estimado): ")

    if method_choice == 'iter':
        max_iterations = int(input("Ingrese el número máximo de iteraciones: "))
        significant_digits = int(input("Ingrese la cantidad de cifras significativas en el resultado: "))
        newton_solver = ImprovedNewtonRaphson(function=my_function, initial_guess=initial_guess, max_iterations=max_iterations)
    elif method_choice == 'error':
        tolerance = float(input("Ingrese el error estimado deseado: "))
        significant_digits = int(input("Ingrese la cantidad de cifras significativas en el resultado: "))
        newton_solver = ImprovedNewtonRaphson(function=my_function, initial_guess=initial_guess, tolerance=tolerance)
    else:
        print("Opción no válida. Se utilizará el método de iteraciones por defecto.")
        significant_digits = int(input("Ingrese la cantidad de cifras significativas en el resultado: "))
        newton_solver = ImprovedNewtonRaphson(function=my_function, initial_guess=initial_guess, max_iterations=5)

    # Resolver y mostrar resultados
    newton_solver.solve(significant_digits)
    newton_solver.display_results()