import json

class Matriz():
    def __init__(self, taxa=None) -> None:
        self.taxa = taxa or 70  # Define a taxa padrão como 70% se não for especificada
        self.path_cardapio = "./Informacoes/cardapio.json"
        self.path_ingredientes = "./Informacoes/ingredientes.json"
        self.cardapio = {}
        self.ingredientes = {}
    
    def _open_informacoes(self):
        # Abre os arquivos JSON do cardápio e dos ingredientes e carrega seus dados
        with open(self.path_cardapio, 'r') as f:
            self.cardapio = json.load(f)

        with open(self.path_ingredientes, 'r') as f:
            self.ingredientes = json.load(f)
    
    def multiplicacao_possivel(self, lanche):
        # Verifica se a multiplicação de matrizes é possível com base no número de ingredientes
        if len(self.cardapio[lanche]) != len(self.ingredientes):
            raise ValueError("O número de colunas da Matriz A deve ser igual ao número de linhas da Matriz B.")
    
    def multiplicacao_matriz(self):
        # Realiza a multiplicação de matrizes para calcular o custo dos lanches
        self._open_informacoes()

        custos = { "Covabra": {}, "Savegnago": {} }

        for lanche, items in self.cardapio.items():
            self.multiplicacao_possivel(lanche)  # Verifica a compatibilidade das matrizes
            for fornecedor in custos.keys():
                total = 0
                for ingrediente, quantidade in items.items():
                    total += quantidade * self.ingredientes[ingrediente][fornecedor]  # Calcula o custo do ingrediente
                custos[fornecedor][lanche] = total  # Armazena o custo total para cada lanche

        return custos
    
    def impressao_custo(self):
        # Imprime o custo dos lanches sem a taxa adicional
        custos_totais = self.multiplicacao_matriz()
        print('Total sem Taxa\n')
        print(f"{'Lanche':<12} {'Covabra':<10} {'Savegnago':<10}")
        print("-" * 32)
        for lanche in custos_totais["Covabra"]:
            print(f"{lanche:<12} R$ {custos_totais['Covabra'][lanche]:.2f}     R$ {custos_totais['Savegnago'][lanche]:.2f}")
    
    def impressao_custo_taxa(self):
        # Imprime o custo dos lanches com a taxa adicional
        custos_totais_taxa = self.multiplicacao_matriz()
        print(f'Total com Taxa de {self.taxa}%\n')
        print(f"{'Lanche':<12} {'Covabra':<10} {'Savegnago':<10}")
        print("-" * 32)
        for lanche in custos_totais_taxa["Covabra"]:
            # Calcula o custo final com a taxa aplicada
            print(f"{lanche:<12} R$ {custos_totais_taxa['Covabra'][lanche]*(1+(self.taxa/100)):.2f}     R$ {custos_totais_taxa['Savegnago'][lanche]*(1+(self.taxa/100)):.2f}")
