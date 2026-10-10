class Restaurante:
    def __init__(self, id_restaurante: str,  nome: str,
                 categoria: str, ativo = True):
        self._id_restaurante = id_restaurante
        self._nome = nome.upper().strip()
        self._categoria = categoria.upper().strip()
        self._ativo = ativo


    def __str__(self) -> str:
        return f"""
        ID do Restaurante: {self.id_restaurante}
        Restaurante: {self.nome}
        Categoria: {self.categoria}
        Status: {self.ativo}
        """

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

    def ajustar_status(self, ativo: bool) -> None:
        self._ativo = ativo
        if ativo:
            print('Status ajustado para: ativo!')
        else:
            print('Status ajustado para: inativo!')