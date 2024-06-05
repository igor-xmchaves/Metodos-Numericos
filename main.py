from metodos.ponto_fixo      import MetodoPontoFixo
from metodos.newton_rhapson  import MetodoNewtonRhapson
from metodos.secante         import MetodoSecante
def main():
    # metodo = MetodoPontoFixo(c=1, q0=0.5)
    # metodo.executar()

    # metodo = MetodoNewtonRhapson(c=1, q0=0.5)
    # metodo.executar()

    metodo = MetodoSecante(c=1, q0=0.4, q1=0.8)
    metodo.executar()

if __name__ == "__main__":
    main()