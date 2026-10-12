from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
   def __init__(self, id_prato: str,
                 nome: str, tipo_prato:str, preco: float):
       super().__init__(id_prato, nome, preco)
       self._tipo_prato = tipo_prato

   def __str__(self) -> str:
        return (f'\
        \nID do Prato: {self.id_produto}\
        \nPrato: {self.nome}\
        \nTipo: {self.tipo_prato}\
        \nPreço: {self.preco}\
        ')

   @property
   def tipo_prato(self) -> str:
       return self._tipo_prato