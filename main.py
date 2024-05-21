from metodos.metodo_ponto_fixo import MetodoPontoFixo

def main():
    metodo = MetodoPontoFixo(c=1, q0=0.5)

    metodo.executar()

if __name__ == "__main__":
    main()