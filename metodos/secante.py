import math
import pandas as pd
import matplotlib.pyplot as plt

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
        return q1 - self.funcaoObjetivo(self.c, q1)/(self.funcaoObjetivo(self.c, q1) - self.funcaoObjetivo(self.c, q0)) * (q1 - q0)

    def tabela(self, k, q_next, e):
        """
        Formata o output para uma tabela
        """
        pd.options.display.float_format = '{:.15f}'.format
        table_data = {'k': ['Iteração'], 'Q2': ['Q2'], 'Q1': ['Q1'], 'Q': ['Q'], 'Erro': ['Erro'], 'f(Q2)': ['f(Q2)']}
        table_data['k'][0] = k
        table_data['Q2'][0] = q_next
        table_data['Q1'][0] = self.q1
        table_data['Q'][0] = self.q0
        table_data['Erro'][0] = e
        table_data['f(Q2)'][0] = self.funcaoObjetivo(self.c, q_next)
        table = pd.DataFrame(table_data)
        print(table.to_string(index=False, header=True))

    def executar(self):
        """
        Executa o método de ponto fixo até que o critério de parada seja atingido.
        """
        if abs(self.funcaoObjetivo(self.c, self.q0)) < self.tol:
            return print("Raiz: ", self.q0)
        if (
            abs(self.funcaoObjetivo(self.c, self.q1)) < self.tol 
            or abs(self.q1-self.q0) < self.tol
        ):
            return print("Raiz: ", self.q1) 

        ### Plota um gráfico iterativo da convergência do método
        iters = []
        values = []
        plt.ion()
        fig, ax = plt.subplots()
        line,  = ax.plot(iters, values, "b-")
        ax.set_title("Convergência da Secante")
        ax.set_xlabel("Iteração")
        ax.set_ylabel("Valor de Q")

        for k in range(self.max_iter):
            q_next = self.funcaoIteracao(self.c, self.q0, self.q1)
            e = q_next - self.q1
            iters.append(k)
            values.append(q_next)

            self.tabela(k, q_next, e)

            line.set_xdata(iters)
            line.set_ydata(values)
            ax.relim()
            ax.autoscale_view()
            plt.draw()
            plt.pause(0.4)

            if (
                abs(self.funcaoObjetivo(self.c, q_next)) < self.tol
                or abs(e) < self.tol
                or k >= self.max_iter
            ):
                plt.ioff()
                plt.show() 
                return print("Raiz: ", q_next)
                
            self.q0 = self.q1
            self.q1 = q_next

        raise ValueError("O método de ponto fixo não convergiu após o número máximo de iterações.")
