from configuracoes.matricial import Matriz
from configuracoes.ingredientes import Ingredientes
from configuracoes.cardapio import Cardapio

def main():
    print("""
        1 - Mostrar Cardápio
        2 - Alterar Item do Lanche
        3 - Mostrar Preço dos Ingredientes
        4 - Alterar Preço dos Ingredientes
        5 - Mostrar Tabela de Preços
    """)
    try:
        value = int(input("Escolha uma opção\n>>> "))
        match value:
            case 1:
                print("\n" * 100) 
                Cardapio().impressao_cardapio()
            case 2:
                print("\n" * 100) 
                try:
                    lanche = input("Digite o nome do lanche: ")
                    item = input("Digite o item: ")
                    value = int(input("Digite o valor: "))
                    print('')
                    Cardapio().alterar_item_lanche(lanche, item, value)
                except:
                    print('')
                    print("Formato inválido")
            case 3:
                print("\n" * 100) 
                Ingredientes().monstrar_items()
            case 4:
                print("\n" * 100)
                try:
                    ingrediente = input("Digite o nome do ingrediente: ")
                    mercado = input("Digite o nome do mercado: ")
                    value = float(input("Digite o valor: "))
                    print('')
                    Ingredientes().alterar_preco_ingrediente(ingrediente, mercado, value)
                except:
                    print('')
                    print("Formato inválido")
            case 5:
                print("\n" * 100) 
                Matriz().impressao_custo()
                print('\n'*2)
                Matriz().impressao_custo_taxa()
            case _:
                print("Valor inválido.")
    except:
        print('Apenas Numeros')

if __name__ == "__main__":
    while True:
        main()

