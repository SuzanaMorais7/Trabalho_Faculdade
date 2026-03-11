def imprimir_pares_e_soma(lista):
    # Bloco 1: imprime cada elemento
    for i in range(len(lista)): # percorre a lista uma vez 
        print(lista[i])
    # Bloco 2: imprime todos os pares
    for i in range(len(lista)):   # tem dois loops um dentro do outro
        for j in range(len(lista)):
            print(lista[i], lista[j])
