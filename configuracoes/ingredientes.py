import json

class Ingredientes:
    def __init__(self) -> None:
        self.path = "./Informacoes/ingredientes.json"
        self._list_produto = self._open_ingredientes()

    def _open_ingredientes(self):
        # Abre o arquivo JSON e carrega os dados dos ingredientes em uma lista
        with open(self.path) as files:
            return json.loads(files.read())
    
    def monstrar_items(self):
        # Exibe os ingredientes e seus preços em dois mercados diferentes
        print(f"{'Ingrediente':<12} {'Covabra':<10} {'Savegnago':<10}")
        print("-" * 32)
        
        for ingrediente, precos in self._list_produto.items():
            print(f"{ingrediente:<12} R$ {precos['Covabra']:.2f}     R$ {precos['Savegnago']:.2f}")

    def alterar_preco_ingrediente(self, ingrediente, mercado, valor):
        # Altera o preço de um ingrediente em um mercado específico e salva a alteração
        try:
            if ingrediente not in self._list_produto:
                print(f"'{ingrediente}' não encontrado.")
                return

            if mercado not in self._list_produto[ingrediente]:
                print(f"'{mercado}' não encontrado. '{ingrediente}'.")
                return

            self._list_produto[ingrediente][mercado] = valor
            self._salvar_alteracoes()
            print("Item alterado com sucesso.")
        except Exception as e:
            print(f"Ocorreu um erro ao alterar o item: {e}")

    def _salvar_alteracoes(self):
        # Salva as alterações feitas no dicionário de ingredientes de volta no arquivo JSON
        with open(self.path, "w") as files:
            json.dump(self._list_produto, files, ensure_ascii=False, indent=4)
