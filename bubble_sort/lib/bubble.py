import time
import json

DATAPATH = 'bubble_sort/db/grupo_13_insertion_sort.json'

def bubble_sort(lista: list[dict[str, any]], chave: str) -> list[dict[str, any]]:

    inicio = time.time()
    n = len(lista)

    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            if lista[j][chave] > lista[j + 1][chave]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
        if not trocou:
            break
        
    fim = time.time()
    duracao = fim - inicio 
    print(f"Tempo de execução do bubble_sort: {duracao//60:.3f} minutos")

    return lista

def main():
    try:

        with open(DATAPATH, 'r', encoding='utf-8') as a:
            idade = json.load(a)
        idade_ordenadas = bubble_sort(idade, 'idade')

        with open(DATAPATH, 'w', encoding='utf-8') as arquivo:
            json.dump(idade_ordenadas, arquivo, indent = 4, ensure_ascii=False)

        print("Ordenação concluída com sucesso!")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{DATAPATH}' não foi encontrado.")
    except json.JSONDecodeError:
        print("Erro: O arquivo JSON está mal formado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

main()