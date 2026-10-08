from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, id_produto, nome,
                 preco, tipo_bebida: str, tamanho: str):
        super().__init__(id_produto, nome, preco)
        self._tipo_bebida = tipo_bebida
        self._tamanho = tamanho

    def __str__(self) -> str:
        return f"""
        ID da Bebida: {self.id_produto}
        Bebida: {self.nome}
        Tipo: {self.tipo_bebida}
        Tamanho: {self.tamanho}
        Preço: {self.preco}
        """

    @property
    def tipo_bebida(self) -> str:
        return self._tipo_bebida

    @property
    def tamanho(self) -> str:
        return self._tamanho