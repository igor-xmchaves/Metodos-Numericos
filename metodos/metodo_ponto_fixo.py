import math
import pandas as pd
import matplotlib.pyplot as plt

class MetodoPontoFixo:
    def __init__(self, c, q0, tol=1e-4, max_iter=100):
        """
        Inicializa o método de ponto fixo.
        """
        self.c = c
        self.q0 = q0
        self.tol = tol
        self.max_iter = max_iter

    def funcaoObjetivo(self, c, q):
        return c * math.exp(q) - 4 * pow(q, 2)

    def funcaoIteracao(self, c, q):
        return math.sqrt(c * math.exp(q) / 4)

    def tabela(self, k, q_next, e):
        """
        Formata o output para uma tabela
        """
        pd.options.display.float_format = '{:.6f}'.format
        table_data = {'k': ['Iteração'], 'Q1': ['Q1'], 'Q': ['Q'], 'Erro': ['Erro'], 'f(Q1)': ['f(Q1)']}
        table_data['k'][0] = k
        table_data['Q1'][0] = q_next
        table_data['Q'][0] = self.q0
        table_data['Erro'][0] = e
        table_data['f(Q1)'][0] = self.funcaoIteracao(self.c, q_next)
        table = pd.DataFrame(table_data)
        print(table.to_string(index=False, header=True))

    def executar(self):
        """
        Executa o método de ponto fixo até que o critério de parada seja atingido.
        """
        if abs(self.funcaoIteracao(self.c, self.q0)) < self.tol:
            return print("Raiz: ", self.q0)

        
        ### Plota um gráfico iterativo da convergência do método
        iters = []
        values = []
        plt.ion()
        fig, ax = plt.subplots()
        line,  = ax.plot(iters, values, "b-")
        ax.set_title("Convergência do Ponto Fixo")
        ax.set_xlabel("Iteração")
        ax.set_ylabel("Valor de Q")

        for k in range(self.max_iter):
            valor = self.funcaoObjetivo(self.c, self.q0)
            q_next = self.funcaoIteracao(self.c, self.q0)
            e = q_next - self.q0
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
                abs(self.funcaoIteracao(self.c, q_next)) < self.tol
                or abs(e) < self.tol
                or k >= self.max_iter
            ):
                plt.ioff()
                plt.show()
                return
                
            self.q0 = q_next

        raise ValueError("O método de ponto fixo não convergiu após o número máximo de iterações.")
