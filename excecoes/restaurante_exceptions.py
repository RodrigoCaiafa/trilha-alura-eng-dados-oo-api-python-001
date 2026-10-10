class ErroRestaurante(Exception):
    def __init__(self, msg = 'Erro de restaurantes'):
        self.msg = msg

class ErroCriacaoRestaurante(ErroRestaurante):
    def __init__(self, msg = 'Erro na criação do restaurante'):
        self.msg = msg

class ErroRemocaoRestaurante(ErroRestaurante):
    def __init__(self, msg= 'Erro na remoção do restaurante'):
        self.msg = msg




