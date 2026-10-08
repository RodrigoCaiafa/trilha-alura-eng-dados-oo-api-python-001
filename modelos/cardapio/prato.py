from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
   def __init__(self, id_prato: str,
                 nome: str, preco: float, tipo_prato:str):
       super().__init__(id_prato, nome, preco)
       self._tipo_prato = tipo_prato

   def __str__(self) -> str:
        return f"""
        ID do Prato: {self.id_produto} 
        Prato: {self.nome}
        Tipo: {self.tipo_prato}
        Preço: {self.preco}
        """

   @property
   def tipo_prato(self) -> str:
       return self._tipo_prato