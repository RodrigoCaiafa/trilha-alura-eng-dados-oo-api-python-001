from typing import override

from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, id_produto: str,
                 nome: str, tipo_prato: str, tamanho: str,
                 descricao: str, preco: float):
        super().__init__(id_produto, nome, preco)
        self._tipo_prato = tipo_prato
        self._descricao = descricao
        self._tamanho = tamanho

    def __str__(self) -> str:
        return (f'\
        \nID do Prato: {self.id_produto}\
        \nPrato: {self.nome}\
        \nTipo: {self.tipo_prato}\
        \nTamanho: {self.tamanho}\
        \nDescrição: {self.descricao}\
        \nPreço: {self.preco}\
        ')

    @override
    def aplicar_desconto(self, desconto=0.15):
        if 0 < desconto <= 0.5:
            print(f'Valor liquido {self.nome} R${self.preco - (self.preco * desconto)}\nDesconto {100 * desconto}%')


    @property
    def tipo_prato(self) -> str:
        return self._tipo_prato

    @property
    def tamanho(self) -> str:
        return self._tamanho

    @property
    def descricao(self) -> str:
        return self._descricao


