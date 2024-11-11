def bubble_sort(lista: list[dict[str, any]], chave: str) -> list[dict[str, any]]:
    n = len(lista)
    for i in range(n):
        trocou = False
        for j in range(0, n-i-1):
            if lista[j][chave] > lista[j+1][chave]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                trocou = True
        if not trocou:
            break
    return lista