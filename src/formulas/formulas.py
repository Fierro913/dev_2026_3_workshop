class Formulas:
    """
    Clase con ejercicios de fórmulas de física, finanzas y álgebra.
    """

    def velocidad_media(self, distancia, tiempo):
        velocidad_media = distancia / tiempo
        return velocidad_media
        """
        Calcula la velocidad media de un recorrido.

        Args:
            distancia (float): Distancia recorrida (metros)
            tiempo (float): Tiempo empleado (segundos)

        Returns:
            float: Velocidad media (metros/segundo)

        Fórmula: v = d / t

        Ejemplo:
            velocidad_media(100, 10) -> 10.0
        """
        return distancia / tiempo

    def mruv_posicion(self, posicion_inicial, velocidad_inicial, aceleracion, tiempo):
        posicion_final = (
            posicion_inicial + velocidad_inicial * tiempo + (1 / 2) * aceleracion * tiempo**2
        )
        return posicion_final
        """
        Calcula la posición de un móvil con aceleración constante (MRUV).

        Args:
            posicion_inicial (float): Posición inicial (metros)
            velocidad_inicial (float): Velocidad inicial (metros/segundo)
            aceleracion (float): Aceleración constante (metros/segundo^2)
            tiempo (float): Tiempo transcurrido (segundos)

        Returns:
            float: Posición final

        Fórmula: x = x0 + v0*t + (1/2)*a*t^2

        Ejemplo:
            mruv_posicion(0, 2, 1, 3) -> 10.5
        """
        pass

    def mruv_velocidad(self, velocidad_inicial, aceleracion, tiempo):
        velocidad_final = velocidad_inicial + aceleracion * tiempo
        return velocidad_final
        """
        Calcula la velocidad final de un móvil con aceleración constante (MRUV).

        Args:
            velocidad_inicial (float): Velocidad inicial (metros/segundo)
            aceleracion (float): Aceleración constante (metros/segundo^2)
            tiempo (float): Tiempo transcurrido (segundos)

        Returns:
            float: Velocidad final

        Fórmula: v = v0 + a*t

        Ejemplo:
            mruv_velocidad(2, 1, 3) -> 5.0
        """
        pass

    def fuerza_newton(self, masa, aceleracion):
        fuerza = masa * aceleracion
        return fuerza
        """
        Calcula la fuerza según la segunda ley de Newton.

        Args:
            masa (float): Masa del objeto (kg)
            aceleracion (float): Aceleración (m/s^2)

        Returns:
            float: Fuerza (Newtons)

        Fórmula: F = m * a

        Ejemplo:
            fuerza_newton(10, 2) -> 20.0
        """
        pass

    def energia_cinetica(self, masa, velocidad):
        energia_cinetica = (1 / 2) * masa * velocidad**2
        return energia_cinetica
        """
        Calcula la energía cinética de un objeto en movimiento.

        Args:
            masa (float): Masa del objeto (kg)
            velocidad (float): Velocidad del objeto (m/s)

        Returns:
            float: Energía cinética (Joules)

        Fórmula: Ec = (1/2) * m * v^2

        Ejemplo:
            energia_cinetica(2, 3) -> 9.0
        """
        pass

    def energia_potencial(self, masa, altura, gravedad=9.8):
        energia_potencial = masa * gravedad * altura
        return energia_potencial
        """
        Calcula la energía potencial gravitatoria de un objeto.

        Args:
            masa (float): Masa del objeto (kg)
            altura (float): Altura sobre el suelo (metros)
            gravedad (float): Aceleración de la gravedad (m/s^2), por defecto 9.8

        Returns:
            float: Energía potencial (Joules)

        Fórmula: Ep = m * g * h

        Ejemplo:
            energia_potencial(2, 5) -> 98.0
        """
        pass

    def ley_ohm_voltaje(self, corriente, resistencia):
        voltaje = corriente * resistencia
        return voltaje
        """
        Calcula el voltaje usando la ley de Ohm.

        Args:
            corriente (float): Corriente eléctrica (Amperios)
            resistencia (float): Resistencia (Ohmios)

        Returns:
            float: Voltaje (Voltios)

        Fórmula: V = I * R

        Ejemplo:
            ley_ohm_voltaje(2, 5) -> 10.0
        """
        pass

    def ley_ohm_corriente(self, voltaje, resistencia):
        corriente = voltaje / resistencia
        return corriente
        """
        Calcula la corriente usando la ley de Ohm.

        Args:
            voltaje (float): Voltaje (Voltios)
            resistencia (float): Resistencia (Ohmios)

        Returns:
            float: Corriente (Amperios)

        Fórmula: I = V / R

        Ejemplo:
            ley_ohm_corriente(10, 5) -> 2.0
        """
        pass

    def interes_simple(self, capital, tasa, tiempo):
        interes = capital * tasa * tiempo
        return interes
        """
        Calcula el interés generado por un capital a interés simple.

        Args:
            capital (float): Capital inicial
            tasa (float): Tasa de interés anual (en decimal, ej. 0.05 para 5%)
            tiempo (float): Tiempo en años

        Returns:
            float: Interés generado

        Fórmula: I = C * r * t

        Ejemplo:
            interes_simple(1000, 0.05, 2) -> 100.0
        """
        pass

    def interes_compuesto(self, capital, tasa, tiempo, n=1):
        interes = capital * (1 + tasa / n) ** (n * tiempo)
        return interes
        """
        Calcula el monto final de un capital a interés compuesto.

        Args:
            capital (float): Capital inicial
            tasa (float): Tasa de interés anual (en decimal, ej. 0.05 para 5%)
            tiempo (float): Tiempo en años
            n (int): Número de capitalizaciones por año, por defecto 1

        Returns:
            float: Monto final

        Fórmula: M = C * (1 + r/n)^(n*t)

        Ejemplo:
            interes_compuesto(1000, 0.05, 2) -> 1102.5
        """
        pass

    def discriminante(self, a, b, c):
        discriminante = b ** 2 - 4 * a * c
        return discriminante
        """
        Calcula el discriminante de una ecuación cuadrática ax^2 + bx + c = 0.

        Args:
            a (float): Coeficiente cuadrático
            b (float): Coeficiente lineal
            c (float): Término independiente

        Returns:
            float: Discriminante

        Fórmula: D = b^2 - 4*a*c

        Ejemplo:
            discriminante(1, -3, 2) -> 1
        """
        pass

    def raices_cuadraticas(self, a, b, c):
        discriminante= (b ** 2 - 4 * a * c)
        if discriminante < 0:
            raise ValueError("El discriminante es negativo, la ecuacion no tiene raices reales")
        raiz1 = (-b + discriminante ** 0.5) / (2 * a)
        raiz2 = (-b - discriminante ** 0.5) / (2 * a)
        return raiz1, raiz2
        """
        Calcula las raíces reales de una ecuación cuadrática ax^2 + bx + c = 0
        usando la fórmula general. Si el discriminante es negativo, lanza ValueError.

        Args:
            a (float): Coeficiente cuadrático (distinto de cero)
            b (float): Coeficiente lineal
            c (float): Término independiente

        Returns:
            tuple: (raiz1, raiz2) las dos raíces reales

        Fórmula: x = (-b ± sqrt(b^2 - 4ac)) / (2a)

        Ejemplo:
            raices_cuadraticas(1, -3, 2) -> (2.0, 1.0)
        """
        pass

    def imc(self, peso, altura):
        imc = peso / altura ** 2
        return imc
        """
        Calcula el Índice de Masa Corporal (IMC).

        Args:
            peso (float): Peso en kilogramos
            altura (float): Altura en metros

        Returns:
            float: Índice de Masa Corporal

        Fórmula: IMC = peso / altura^2

        Ejemplo:
            imc(70, 1.75) -> 22.86
        """
        pass

    def hipotenusa_pitagoras(self, cateto1, cateto2):
        return (cateto1 ** 2 + cateto2 ** 2) ** 0.5
        """
        Calcula la longitud de la hipotenusa de un triángulo rectángulo.

        Args:
            cateto1 (float): Longitud del primer cateto
            cateto2 (float): Longitud del segundo cateto

        Returns:
            float: Longitud de la hipotenusa

        Fórmula: h = sqrt(cateto1^2 + cateto2^2)

        Ejemplo:
            hipotenusa_pitagoras(3, 4) -> 5.0
        """
        pass
