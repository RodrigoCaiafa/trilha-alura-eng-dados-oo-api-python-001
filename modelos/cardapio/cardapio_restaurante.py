from excecoes.cardapio_exceptions import ErroCadastroProduto
from modelos.cardapio.item_cardapio import ItemCardapio
from modelos.cardapio.item_factory import ProdutoFactory


class CardapioRestaurante:

    def __init__(self):
        self._relacao_produtos = {}
        self._set_ids_produtos = set()
        self._set_nomes_produtos = set()

    def _valida_produto(self, id_item: str, nome_item: str):
        id_validacao = False
        nome_validacao = False
        status_validacao = False

        if id_item not in self._set_ids_produtos:
            id_validacao = True

        if nome_validacao not in self._set_nomes_produtos:
            nome_validacao = True

        if id_validacao and nome_validacao:
            status_validacao = True

        return id_validacao, nome_validacao, status_validacao

    def _cadastrar_produto(self, item: ItemCardapio):
        id_validacao, nome_validacao, staus_validacao = (
            self._valida_produto(item.id_produto, item.nome))

        if staus_validacao:
            self._relacao_produtos[item.id_produto] = item
            self._set_ids_produtos.add(item.id_produto)
            self._set_nomes_produtos.add(item.nome)

            print(f'Produto {item.nome} criado com sucesso!')
        else:
            raise ErroCadastroProduto(f'Erro no cadastro: ID válido {id_validacao} Nome válido {nome_validacao}')

    def criar_produto(self, tipo: str, *args, **kwargs):
        produto = ProdutoFactory.criar_produto(tipo, *args, **kwargs)
        self._cadastrar_produto(produto)

    def buscar_produto(self, id_produto: str) -> ItemCardapio | None:
        return self._relacao_produtos.get(id_produto)
