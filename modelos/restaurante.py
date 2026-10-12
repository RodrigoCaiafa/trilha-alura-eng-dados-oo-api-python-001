from modelos.cardapio.cardapio_restaurante import CardapioRestaurante


class Restaurante:
    def __init__(self, id_restaurante: str, nome: str,
                 categoria: str, ativo=True):
        self._id_restaurante = id_restaurante
        self._nome = nome.upper().strip()
        self._categoria = categoria.upper().strip()
        self._ativo = ativo
        self._cardapio = CardapioRestaurante()

    def __str__(self) -> str:
        return f'\
        \nID do Restaurante: {self.id_restaurante}\
        \nRestaurante: {self.nome}\
        \nCategoria: {self.categoria}\
        \nStatus: {self.ativo}\
        '

    @property
    def id_restaurante(self):
        return self._id_restaurante

    @property
    def nome(self):
        return self._nome

    @property
    def categoria(self):
        return self._categoria

    @property
    def ativo(self):
        return self._ativo

    @property
    def cardapio_restaurante(self) -> CardapioRestaurante:
        return self._cardapio

    def ajustar_status(self, ativo: bool) -> None:
        self._ativo = ativo
        if ativo:
            print('Status ajustado para: ativo!')
        else:
            print('Status ajustado para: inativo!')
