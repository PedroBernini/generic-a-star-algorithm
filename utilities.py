# Esta classe representa os nós do grafo.
class No:
    def __init__(self, estado, total_F, custo_G, heuristica_H, pai):
        self.estado = estado
        self.total_F = total_F
        self.custo_G = custo_G
        self.heuristica_H = heuristica_H
        self.pai = pai

# Retorna o custo, ou seja, a distancia percorrida do estado inícial até o nó estado atual
def getCusto(estadoInicial, estadoAtual, listaFechada, listaAberta):
    G = 0
    aux = True
    if estadoInicial == estadoAtual:
        return G
    else:
        for no in listaAberta:
            if estadoAtual == no.estado:
                estadoAtual = no.pai
                if estadoAtual == estadoInicial:
                    return G + 1
        while aux:
            for no in listaAberta:
                if estadoAtual == no.estado:
                    estadoAtual = no.pai
            for no in listaFechada:
                if estadoAtual == no.estado:
                    estadoAtual = no.pai
                    G = G + 1
                    if estadoAtual == estadoInicial:
                        aux = False
        return G

# Retorna a mesma lista aberta, porém, os nós em ordem crescente de acordo com a pontuação F(G+H)
def ordenarNoPorHeuristica(listaAberta):
    elementos = len(listaAberta) - 1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if listaAberta[i].total_F > listaAberta[i + 1].total_F:
                listaAberta[i], listaAberta[i + 1] = listaAberta[i + 1], listaAberta[i]
                ordenado = False
    return listaAberta

# Retorna o melhor caminho de acordo com a listaFechada
def getMelhorCaminho(estadoAtual, estadoInicial, listaFechada):
    listaComMelhorCaminho = [estadoAtual]
    chegou = True
    while chegou:
        for no in listaFechada:
            if no.estado == estadoAtual:
                estadoAtual = no.pai
                listaComMelhorCaminho.append(estadoAtual)
                if estadoAtual == estadoInicial:
                    chegou = False
                break
    listaComMelhorCaminho.reverse()
    return listaComMelhorCaminho

# Retorna uma lista com os nós adjacentes que ainda não foram expandidos
def expandir(estadoAtual, listaAberta, listaFechada):
    listaExpansao = []
    adjacents = getAllAdjacents(estadoAtual)
    for adjacent in adjacents:
        valido = True
        for no in listaFechada:
            if no.estado == adjacent:
                valido = False
        for no in listaAberta:
            if no.estado == adjacent:
                valido = False
        if valido == True:
            listaExpansao.append(adjacent)
    return listaExpansao

# Retorna a lista aberta com todos os novos nós expandidos (atribuído dos valores)
def preencherListaAberta(listaExpansao, estadoInicial, estadoFinal, estadoAtual, listaAberta, listaFechada, funcaoHeuristica):
    for estado in listaExpansao:
        custo_G = getCusto(estadoInicial, estadoAtual, listaFechada, listaAberta) + 1
        heuristica_H = funcaoHeuristica(estado, estadoFinal)
        total_F = custo_G + heuristica_H
        novo_no = No(estado, total_F, custo_G, heuristica_H, estadoAtual)
        listaAberta.append(novo_no)
    return listaAberta

def getAllAdjacents(estado):
    ''' -> TODO
    A partir de um estado, retorne uma lista de estados adjacentes de acordo com as regras do ambiente
    '''
    raise Exception('Falta implementação da funcionalidade "getAllAdjacents"!')
