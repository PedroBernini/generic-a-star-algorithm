from utilities import *

# Algoritmo do A*
def aStar(estadoInicial, estadoFinal, heuristica):

    # O algoritmo deve começar pelo estado inicial
    estadoAtual = estadoInicial

    # Listas para os nós da árvore
    listaFechada = []
    listaAberta = []

    # Passo 1 - O algoritmo começa agora: Crie aqui o primeiro nó (raiz da árvore) com G, H e F. Coloque o nó dentro da listaAberta:
    custo_G = 0
    heuristica_H = heuristica(estadoAtual, estadoFinal)
    total_F = custo_G + heuristica_H
    novo_no = No(estadoAtual, total_F, custo_G, heuristica_H, None)
    listaAberta.append(novo_no)
    # Fim do passo 1

    # Repete até que o estadoAtual seja a estadoFinal
    while estadoAtual != estadoFinal:
        # Passo 2 - Crie uma lista de Expansão para o estadoAtual (funcao "expandir"):
        listaExpansao = expandir(estadoAtual, listaAberta, listaFechada)
        # Fim do passo 2

        # Passo 3 - Preencha a listaAberta com a lista de Expansão do passo anterior:
        listaAberta = preencherListaAberta(listaExpansao, estadoInicial, estadoFinal, estadoAtual, listaAberta, listaFechada, heuristica)
        # Fim do passo 3

        # Passo 4 - Remova o primeiro nó da listaAberta (posição[0]) e adicione-o na listaFechada
        no = listaAberta[0]
        listaFechada.append(no)
        listaAberta.remove(no)
        # Fim do passo 4

        # Passo 5 - Ordene a listaAberta
        listaAberta = ordenarNoPorHeuristica(listaAberta)
        # Fim do passo 5
        
        # Passo 6 - Crie uma condição: Se a listaAberta não estiver vazia -> troque o valor do estadoAtual para o estado do primeiro nó da listaAberta (posicao[0]). Se não, não há mais saídas.
        if len(listaAberta) != 0:
            estadoAtual = listaAberta[0].estado
        # Fim do passo 6
    # Fim do While

    # Passo 7 - Adicione o primeiro nó da listaAberta na listaFechada (que é o nó final)
    listaFechada.append(listaAberta[0])
    # Fim do passo 7

    # Passo 8 (Último) - retorne a melhor caminho utilizando o estadoAtual, estadoInicial e listaFechada:
    return getMelhorCaminho(estadoAtual, estadoInicial, listaFechada)
    # Fim do passo 8