from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, id_produto, nome,
                tipo_bebida: str,tamanho: str, preco: float | int):
        super().__init__(id_produto, nome, preco)
        self._tipo_bebida = tipo_bebida
        self._tamanho = tamanho

    def __str__(self) -> str:
        return (f'\
        \nID da Bebida: {self.id_produto}\
        \nBebida: {self.nome}\
        \nTipo: {self.tipo_bebida}\
        \nTamanho: {self.tamanho}\
        \nPreço: {self.preco}\
        ')

    @property
    def tipo_bebida(self) -> str:
        return self._tipo_bebida

    @property
    def tamanho(self) -> str:
        return self._tamanho