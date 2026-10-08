from modelos.restaurante import Restaurante
from modelos.restaurantes_credenciados import RestaurantesCredenciados
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

def main():
    base_restaurantes = RestaurantesCredenciados()
    restaurante_01 = Restaurante(id_restaurante='0000001',
                                 nome= 'Restaurante do Zé',
                                 categoria= 'comida brasileira',
                                 lista_restaurantes= base_restaurantes)

    restaurante_02 = Restaurante(id_restaurante='0000002',
                                 nome= 'Restaurante do Rio',
                                 categoria= 'comida brasileira',
                                 lista_restaurantes= base_restaurantes)

    base_restaurantes.listar_restaurantes()

    bebida_refri = Bebida(id_produto="0000001",
                          nome="CocaCola",
                          tipo_bebida="Refrigerante",
                          tamanho="500ml",
                          preco=15.0)
    prato_hamburguer = Prato(id_prato="0000002",
                             nome="Hamburguer",
                             tipo_prato="Sanduiches",
                             preco=10.0)

    print(bebida_refri)
    print(prato_hamburguer)


if __name__ == '__main__':
    main()