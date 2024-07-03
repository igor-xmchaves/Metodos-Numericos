import math

class MetodoNewtonRhapson:
    def __init__(self, c, q0, tol, max_iter=100):
        """
        Inicializa o método de ponto fixo.
        """
        self.c = c
        self.q0 = q0
        self.tol = tol
        self.max_iter = max_iter

    def funcaoObjetivo(self, c, q):
        return c * math.exp(q) - 4 * pow(q, 2)

    def funcaoDerivada(self, c, q):
        return c * math.exp(q) - 8 * q

    def funcaoIteracao(self, c, q):
        return q - self.funcaoObjetivo(c, q)/self.funcaoDerivada(c, q)
