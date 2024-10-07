import json

class Matriz():
    def __init__(self, taxa=None) -> None:
        self.taxa = taxa or 70
        self.path_cardapio = "./Informacoes/cardapio.json"
        self.path_ingredientes = "./Informacoes/ingredientes.json"
        self.cardapio = {}
        self.ingredientes = {}
    
    def _open_informacoes(self):
        with open(self.path_cardapio, 'r') as f:
            self.cardapio = json.load(f)

        with open(self.path_ingredientes, 'r') as f:
            self.ingredientes = json.load(f)
    
    def multiplicacao_possivel(self, lanche):
        if len(self.cardapio[lanche]) != len(self.ingredientes):
            raise ValueError("O número de colunas da Matriz A deve ser igual ao número de linhas da Matriz B.")
    
    def multiplicacao_matriz(self):
        self._open_informacoes()

        custos = { "Covabra": {}, "Savegnago": {} }

        for lanche, items in self.cardapio.items():
            self.multiplicacao_possivel(lanche)
            for fornecedor in custos.keys():
                total = 0
                for ingrediente, quantidade in items.items():
                    total += quantidade * self.ingredientes[ingrediente][fornecedor]
                custos[fornecedor][lanche] = total

        return custos
    
    def impressao_custo(self):
        custos_totais = self.multiplicacao_matriz()
        print('Total sem Taxa\n')
        print(f"{'Lanche':<12} {'Covabra':<10} {'Savegnago':<10}")
        print("-" * 32)
        for lanche in custos_totais["Covabra"]:
            print(f"{lanche:<12} R$ {custos_totais['Covabra'][lanche]:.2f}     R$ {custos_totais['Savegnago'][lanche]:.2f}")
    
    def impressao_custo_taxa(self):
        custos_totais_taxa = self.multiplicacao_matriz()
        print(f'Total com Taxa de {self.taxa}%\n')
        print(f"{'Lanche':<12} {'Covabra':<10} {'Savegnago':<10}")
        print("-" * 32)
        for lanche in custos_totais_taxa["Covabra"]:
            print(f"{lanche:<12} R$ {custos_totais_taxa['Covabra'][lanche]*(1+(self.taxa/100)):.2f}     R$ {custos_totais_taxa['Savegnago'][lanche]*(1+(self.taxa/100)):.2f}")
