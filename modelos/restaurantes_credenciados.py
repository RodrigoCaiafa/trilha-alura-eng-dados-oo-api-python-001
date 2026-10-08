from excecoes.restaurante_exceptions import ErroCriacaoRestaurante


class RestaurantesCredenciados:

    def __init__(self):
        self._relacao_restaurantes = {}
        self._set_ids_restaurantes = set()
        self._set_nomes_restaurantes = set()

    _instancia_lista = None

    def __new__(cls):
        if cls._instancia_lista is None:
            cls._instancia_lista = super().__new__(cls)
        return cls._instancia_lista

    def _valida_restaurante(self, id_restaurante: str, nome_restaurante: str):
        id_validacao = False
        nome_validacao = False
        status_validacao = False

        if id_restaurante not in self._set_ids_restaurantes:
            id_validacao = True

        if nome_restaurante not in self._set_nomes_restaurantes:
            nome_validacao = True

        if id_validacao and nome_validacao:
            status_validacao = True

        return id_validacao, nome_validacao, status_validacao

    def listar_restaurantes(self, status=True):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)}|{'Status'}')
        for restaurante in self._relacao_restaurantes.values():
            if restaurante.ativo == status:
                print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')

    def cadastrar_restaurante(self, restaurante):
        id_validacao, nome_validacao, status_validacao = (
            self._valida_restaurante(restaurante.id_restaurante, restaurante.nome))

        if status_validacao:
            self._relacao_restaurantes[restaurante.id_restaurante] = restaurante
            self._set_ids_restaurantes.add(restaurante.id_restaurante)
            self._set_nomes_restaurantes.add(restaurante.nome)
            print(f'Cadastro efetuado com sucesso: {restaurante}')
        else:
            raise ErroCriacaoRestaurante(f'Erro no cadastro: ID válido {id_validacao} Nome válido {nome_validacao}')

    def remover_restaurante(self, nome_restaurante: str, id_restaurante = ""):
        id_validacao, nome_validacao, status_validacao = self._valida_restaurante(id_restaurante, nome_restaurante)
