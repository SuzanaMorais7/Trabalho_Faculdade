def busca_binaria(lista, alvo): 
    esquerda, direita = 0, len(lista) - 1 # começa e onde termina a busca.
    while esquerda <= direita:  #enquanto, continua procurando
        meio = (esquerda + direita) // 2 
        if lista[meio] == alvo:  #compara o numero procurado
            return meio 
        elif lista[meio] < alvo: 
            esquerda = meio + 1 
        else: 
            direita = meio - 1 
    return -1

