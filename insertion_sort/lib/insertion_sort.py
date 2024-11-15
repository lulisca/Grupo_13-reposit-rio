import time
import json

DATAPATH = 'insertion_sort/db/grupo_13_insertion_sort.json'

def insertion_sort(lista: list[dict[str, any]], chave: str) -> list[dict[str, any]]:
    tamanho = len(lista)
    inicio = time.time()


    for i in range(1, tamanho): 
        elemento = lista[i] 
        chave_valor = elemento[chave]
        j = i - 1

        while j >= 0 and chave_valor < lista[j][chave]:
            lista[j + 1] = lista[j]  
            j = j - 1

        lista[j + 1] = elemento

    fim = time.time()
    duracao = fim - inicio 
    print(f"Tempo de execução do insertion_sort: {duracao//60:.3f} minutos")

    return lista



def main():
    try:
        with open(DATAPATH, 'r', encoding = 'utf-8') as archive:
            dados_json = json.load(archive)
        
        ra_ordenado = insertion_sort(dados_json, 'idade')
        
        with open(DATAPATH, 'w', encoding = 'utf-8') as arquivo:
            json.dump(ra_ordenado, arquivo, indent = 4, ensure_ascii = False)
        
        print('Tudo feito meu chapa')

    except FileNotFoundError:
        print(f"Erro: O arquivo '{DATAPATH}' não foi encontrado.")
    except json.JSONDecodeError:
        print("Erro: O arquivo JSON está mal formado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
