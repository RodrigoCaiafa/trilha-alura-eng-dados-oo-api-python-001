from modelos.cardapio.item_cardapio import ItemCardapio
from typing import override


class Prato(ItemCardapio):
    def __init__(self, id_prato: str,
                 nome: str, tipo_prato: str, preco: float):
        super().__init__(id_prato, nome, preco)
        self._tipo_prato = tipo_prato

    def __str__(self) -> str:
        return (f'\
        \nID do Prato: {self.id_produto}\
        \nPrato: {self.nome}\
        \nTipo: {self.tipo_prato}\
        \nPreço: R${self.preco}\
        ')

    @override
    def aplicar_desconto(self, desconto=0.5):
        if 0 < desconto <= 1:
            print(f'Valor liquido {self.nome} R${self.preco - (self.preco * desconto)}\nDesconto {100 * desconto}%')


    @property
    def tipo_prato(self) -> str:
        return self._tipo_prato
