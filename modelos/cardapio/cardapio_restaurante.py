from bebida import Bebida
from prato import Prato
from item_cardapio import ItemCardapio


class CardapioRestaurante:

    def __init__(self):
        self._relacao_produtos = {}

    def _valida_novo_produto(self, id_item: str, nome_item: str):
        id_validacao = False
        nome_validacao = False
        staus_validacao = False

        for key, item in self._relacao_produtos.items():
            if key == id_item:
                id_validacao = True
            if item ==


    def cadastrar_produto(self, item: ItemCardapio):
        self._valida_novo_produto(item.id_produto, item.nome)
