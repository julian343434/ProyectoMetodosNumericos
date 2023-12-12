import math

class MetodosNumericos:
    def __init__(self, ecuacion):
        self.ecuacion = ecuacion

    def funcion(self, x):
        # Evalúa la ecuación con el valor de x proporcionado
        try:
            resultado = eval(self.ecuacion, {'x': x, 'sin': math.sin, 'cos': math.cos, 'tan': math.tan, 'exp': math.exp})
            return resultado
        except:
            print("Error al evaluar la función. Asegúrese de que la ecuación sea válida.")
            return None

    def derivada_aproximada(self, x, h=1e-8):
        # Aproximación numérica de la derivada usando diferencia central
        return (self.funcion(x + h) - self.funcion(x - h)) / (2 * h)

    def biseccion(self, limite_inferior, limite_superior, tolerancia_error, max_iteraciones):
        iteracion = 0
        xr = 0.0
        error_aproximado = 100.0

        while error_aproximado >= tolerancia_error and iteracion < max_iteraciones:
            xrold = xr
            xr = (limite_inferior + limite_superior) / 2
            fr = self.funcion(xr)
            iteracion += 1

            if xr != 0:
                error_aproximado = abs((xr - xrold) / xr) * 100

            test = self.funcion(limite_inferior) * fr

            if test < 0:
                limite_superior = xr
            elif test > 0:
                limite_inferior = xr
            else:
                error_aproximado = 0

        return xr

    def falsa_posicion(self, limite_inferior, limite_superior, tolerancia_error, max_iteraciones):
        iteracion = 0
        xr = 0.0
        error_aproximado = 100.0
        fl = self.funcion(limite_inferior)
        fu = self.funcion(limite_superior)
        il = 0
        iu = 0

        while error_aproximado >= tolerancia_error and iteracion < max_iteraciones:
            xrold = xr
            xr = limite_superior - fu * (limite_inferior - limite_superior) / (fl - fu)
            fr = self.funcion(xr)
            iteracion += 1

            if xr != 0:
                error_aproximado = abs((xr - xrold) / xr) * 100

            test = fl * fr

            if test < 0:
                limite_superior = xr
                fu = self.funcion(limite_superior)
                iu = 0
                il += 1
                if il >= 2:
                    fl = fl / 2
            elif test > 0:
                limite_inferior = xr
                fl = self.funcion(limite_inferior)
                il = 0
                iu += 1
                if iu >= 2:
                    fu = fu / 2
            else:
                error_aproximado = 0

            if error_aproximado < tolerancia_error or iteracion >= max_iteraciones:
                break

        return xr
    
    def secante(self, x0, x1, es, imax):
        iteracion = 0
        ea = 100.0

        while ea >= es and iteracion < imax:
            xr = x1 - (self.funcion(x1) * (x0 - x1)) / (self.funcion(x0) - self.funcion(x1))
            x0 = x1
            x1 = xr
            iteracion += 1

            if xr != 0:
                ea = abs((xr - x0) / xr) * 100

            # Verificar si f'(x) es cercano a cero
            if abs(self.funcion(x1) - self.funcion(x0)) < 1e-10:
                print("Alerta: f'(x) podría ser igual a cero. Revise la función y elija otros valores iniciales.")
                break

        return xr
    
    def newton_raphson_mejorado(self, x0, tolerancia_error, max_iteraciones):
        iteracion = 0
        ea = 100.0

        while ea >= tolerancia_error and iteracion < max_iteraciones:
            x1 = x0 - self.funcion(x0) / self.derivada_aproximada(x0)
            x2 = x1 - self.funcion(x1) / self.derivada_aproximada(x1)
            xr = x2 - ((x1 - x2) ** 2) / (self.funcion(x0) - 2 * self.funcion(x1) + self.funcion(x2))
            iteracion += 1

            if xr != 0:
                ea = abs((xr - x2) / xr) * 100

            x0 = x1
            x1 = xr

        return xr

if __name__ == '__main__':
    # Solicitar al usuario la ecuación
    ecuacion = input("Ingrese la ecuación (en términos de x, puedes usar sin, cos, tan, exp, etc.): ")

    # Crear una instancia de la clase MetodosNumericos
    metodos_numericos = MetodosNumericos(ecuacion)

    # Solicitar al usuario el método a utilizar
    metodo_elegido = input("Elija el método (B/F/S/N): ").upper()

    # Resolver y obtener la raíz aproximada según el método elegido
    if metodo_elegido == "B":
        # Solicitar las condiciones iniciales específicas para el método de bisección
        limite_inf = float(input("Ingrese el límite inferior del intervalo: "))
        limite_sup = float(input("Ingrese el límite superior del intervalo: "))
        tolerancia_error = float(input("Ingrese la tolerancia para el error relativo: "))
        max_iteraciones = int(input("Ingrese el número máximo de iteraciones: "))
        raiz_aproximada = metodos_numericos.biseccion(limite_inf, limite_sup, tolerancia_error, max_iteraciones)
        print(f"La raíz aproximada (bisección) es: {raiz_aproximada}")
    elif metodo_elegido == "F":
        # Solicitar las condiciones iniciales específicas para el método de falsa posición
        limite_inf = float(input("Ingrese el límite inferior del intervalo: "))
        limite_sup = float(input("Ingrese el límite superior del intervalo: "))
        tolerancia_error = float(input("Ingrese la tolerancia para el error relativo: "))
        max_iteraciones = int(input("Ingrese el número máximo de iteraciones: "))
        raiz_aproximada = metodos_numericos.falsa_posicion(limite_inf, limite_sup, tolerancia_error, max_iteraciones)
        print(f"La raíz aproximada (falsa posición) es: {raiz_aproximada}")
    elif metodo_elegido == "S":
        # Solicitar las condiciones iniciales específicas para el método de la secante
        x0 = float(input("Ingrese el valor inicial x0: "))
        x1 = float(input("Ingrese el valor inicial x1: "))
        tolerancia_error = float(input("Ingrese la tolerancia para el error relativo: "))
        max_iteraciones = int(input("Ingrese el número máximo de iteraciones: "))
        raiz_aproximada = metodos_numericos.secante(x0, x1, tolerancia_error, max_iteraciones)
        print(f"La raíz aproximada (secante) es: {raiz_aproximada}")
    elif metodo_elegido == "N":
        # Solicitar las condiciones iniciales específicas para el método de Newton-Raphson mejorado
        x0_nr_mejorado = float(input("Ingrese el valor inicial para Newton-Raphson mejorado: "))
        tolerancia_error_nr_mejorado = float(input("Ingrese la tolerancia para el error relativo: "))
        max_iteraciones_nr_mejorado = int(input("Ingrese el número máximo de iteraciones: "))
        raiz_aproximada = metodos_numericos.newton_raphson_mejorado(x0_nr_mejorado, tolerancia_error_nr_mejorado, max_iteraciones_nr_mejorado)
        print(f"La raíz aproximada (Newton-Raphson mejorado) es: {raiz_aproximada}")
    else:
        print("Opción no válida. Por favor, elija 'B', 'F', 'S' o 'N'.")
