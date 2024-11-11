'''import json
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

with open('bubble_sort.json', 'r') as arquivo:
    pessoas = json.load(arquivo)
bubble_sort(pessoas, 'nome')
with open('bubble_sort.json', 'w') as arquivo:
    json.dump(pessoas, arquivo, indent=4)'''


import json
from bubble import bubble_sort  # Certifique-se de que bubble.py está no mesmo diretório

def main():
    try:
        # Carregar dados do arquivo JSON
        with open('bubble_sort.json', 'r') as arquivo:
            pessoas = json.load(arquivo)

        # Ordenar a lista de dicionários pela chave 'nome'
        pessoas_ordenadas = bubble_sort(pessoas, 'nome')

        # Salvar a lista ordenada de volta no arquivo JSON
        with open('bubble_sort.json', 'w') as arquivo:
            json.dump(pessoas_ordenadas, arquivo, indent=4)

        print("Ordenação concluída com sucesso!")

    except FileNotFoundError:
        print("Erro: O arquivo 'bubble_sort.json' não foi encontrado.")
    except json.JSONDecodeError:
        print("Erro: O arquivo JSON está mal formado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()

