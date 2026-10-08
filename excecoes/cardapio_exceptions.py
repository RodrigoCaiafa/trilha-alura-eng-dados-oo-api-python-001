class ErroCardapio(Exception):
    def __init__(self, msg = "Erro de cardapio"):
        self.msg = msg

class ErroCadastroProduto(ErroCardapio):
    def __init__(self, msg = "Erro no cadastro do produto"):
        self.msg = msg

class ErroCadastroPrato(ErroCadastroProduto):
    def __init__(self, msg = "Erro no cadastro do prato"):
        self.msg = msg

class ErroCadastroBebida(ErroCadastroProduto):
    def __init__(self, msg = "Erro no cadastro da bebida"):
        self.msg = msg