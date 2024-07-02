import math

class MetodoSecante:
    def __init__(self, c, q0, q1, tol=1e-4, max_iter=100):
        """
        Inicializa o método de ponto fixo.
        """
        self.c = c
        self.q0 = q0
        self.q1 = q1
        self.tol = tol
        self.max_iter = max_iter

    def funcaoObjetivo(self, c, q):
        return c * math.exp(q) - 4 * pow(q, 2)

    def funcaoIteracao(self, c, q0, q1):
        return q1 - self.funcaoObjetivo(c, q1)/(self.funcaoObjetivo(c, q1) - self.funcaoObjetivo(c, q0)) * (q1 - q0)
