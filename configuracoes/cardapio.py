import json

class Cardapio:
    def __init__(self) -> None:
        self.path = "./Informacoes/cardapio.json"
        self._dict_lanches = self._open_cardapio()

    def _open_cardapio(self):
        # Abre o arquivo JSON e carrega os dados em um dicionário
        with open(self.path) as files:
            return json.loads(files.read())

    def impressao_cardapio(self):
        # Imprime o cardápio formatado com os ingredientes de cada lanche
        print(f"{'Lanche':<12} {'Bacon':<10} {'Hamburguer':<10} {'Queijo':<10} {'Ovo':<10} {'Pão':<10}")
        print("-" * 60)
        
        for lanche, ingredientes in self._dict_lanches.items():
            print(f"{lanche:<12} {ingredientes.get('Bacon', 0):<10} {ingredientes.get('Hamburguer', 0):<10} "
                f"{ingredientes.get('Queijo', 0):<10} {ingredientes.get('Ovo', 0):<10} "
                f"{ingredientes.get('Pão', 0):<10}")

    def alterar_item_lanche(self, lanche, item, valor):
        # Altera o valor de um item específico em um lanche e salva as alterações
        try:
            if lanche not in self._dict_lanches:
                print(f"Lanche '{lanche}' não encontrado.")
                return

            if item not in self._dict_lanches[lanche]:
                print(f"Item '{item}' não encontrado no lanche '{lanche}'.")
                return

            self._dict_lanches[lanche][item] = valor
            self._salvar_alteracoes()
            print("Item alterado com sucesso.")
        except Exception as e:
            print(f"Ocorreu um erro ao alterar o item: {e}")

    def _salvar_alteracoes(self):
        # Salva as alterações feitas no dicionário de lanches de volta no arquivo JSON
        with open(self.path, "w") as files:
            json.dump(self._dict_lanches, files, ensure_ascii=False, indent=4)
