from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, id_produto: str,
                 nome: str, preco: float):
        self._id_produto = id_produto
        self._nome = nome
        self._preco = preco

    @abstractmethod
    def aplicar_desconto(self, desconto: float | int):
        pass

    @property
    def id_produto(self):
        return self._id_produto

    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco
