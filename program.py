import algorithms
from heuristics import getHeuristic

if __name__ == "__main__":
    # Defina o estado inicial e o estado final
    estadoInicial = None
    estadoFinal = None

    # Defina qual heuristica utilizar
    heuristica = getHeuristic

    # A*
    print("Algoritmo A*...")
    caminho = algorithms.aStar(estadoInicial, estadoFinal, heuristica)
    for estado in caminho:
        print('Estado:', estado, 'Heurística:', heuristica(estado, estadoFinal))
    print("Quantidade de Movimentos:", len(caminho))