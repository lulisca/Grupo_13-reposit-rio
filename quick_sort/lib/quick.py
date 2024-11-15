import json
import random
import time

DATAPATH = 'quick_sort/db/grupo_13_quick_sort.json'

def quick_sort(lista: list[dict], chave: str) -> list[dict]:
    if len(lista) <= 1:
        return lista
    else:
        pivo = random.choice(lista)[chave]
        menores = [x for x in lista if x[chave] < pivo]
        maiores = [x for x in lista if x[chave] > pivo]
        pivos = [x for x in lista if x[chave] == pivo]
        return quick_sort(menores, chave) + pivos + quick_sort(maiores, chave)
    
def main():
    try:
        inicio = time.time()

        with open(DATAPATH, 'r', encoding='utf-8') as f:
            dados = json.load(f)
        
        dados_ordenados = quick_sort(dados, "nome")
        
        with open(DATAPATH, 'w', encoding='utf-8') as f:
            json.dump(dados_ordenados, f, ensure_ascii=False, indent=4)

        fim = time.time()
        duracao = fim - inicio

        print(f"Dados ordenados com sucesso!")
        print(f"Tempo de execução: {duracao:.4f} segundos")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{DATAPATH}' não foi encontrado.")
    except json.JSONDecodeError:
        print("Erro: O arquivo JSON está mal formado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

main()
