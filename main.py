import json
from bubble import bubble_sort



def main():

    try:
        with open('bubble_sort.json', 'r', encoding='utf-8') as a:
            idade = json.load(a)

        idade_ordenadas = bubble_sort(idade, 'idade') #!!!!!!!!

        with open('bubble_sort.json', 'w', encoding='utf-8') as arquivo:
            json.dump(idade_ordenadas, arquivo, indent = 4, ensure_ascii = False)
        print("Ordenação concluída com sucesso!")

    except FileNotFoundError:
        print("Erro: O arquivo 'bubble_sort.json' não foi encontrado.")
    except json.JSONDecodeError:
        print("Erro: O arquivo JSON está mal formado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    
print(main())