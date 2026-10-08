from prato import Prato
from bebida import Bebida
from item_cardapio import ItemCardapio
from excecoes.cardapio_exceptions import ErroCadastroProduto


class ProdutoFactory:
    _produto_factory = {
        "prato": Prato,
        "bebida": Bebida
    }

    @classmethod
    def criar_produto(cls, tipo: str, *args, **kwargs) -> ItemCardapio:
        classe = cls._produto_factory.get(tipo.lower())
        if not classe:
            raise ErroCadastroProduto()
        return classe(*args, **kwargs)
