import time
import json

DATAPATH = 'selection_sort/db/grupo_13_selection_sort.json'

def selection_sort(lista: list[dict], chave: str) -> list[dict]:
    n = len(lista)
    inicio = time.time()
    
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):

            valor_j = lista[j][chave]
            valor_min = lista[min_index][chave]

            if valor_j < valor_min:
                min_index = j

        lista[i], lista[min_index] = lista[min_index], lista[i]

    fim = time.time()
    print(f"Tempo de execução do Selection Sort: {fim - inicio:.2f} segundos")
    return lista

def ler_json(DATAPATH: str) -> list[dict]:
    try:
        with open(DATAPATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{DATAPATH}' não foi encontrado.")
        return []
    except json.JSONDecodeError:
        print("Erro: O arquivo JSON está mal formado.")
        return []

def salvar_json(dados: list[dict], DATAPATH: str) -> None:
    try:
        with open(DATAPATH, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
        print(f"Dados salvos com sucesso em {DATAPATH}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo JSON: {e}")

def main():

    dados = ler_json(DATAPATH)
    
    if not dados:
        return 
    
    dados_ordenados = selection_sort(dados, 'renda_mensal')
    
    salvar_json(dados_ordenados, DATAPATH)

main()
