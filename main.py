from modelos.restaurantes_credenciados import RestaurantesCredenciados
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

def main():
    base_restaurantes = RestaurantesCredenciados()
    restaurante_01 =  base_restaurantes.criar_restaurante(id_restaurante='0000001',
                                 nome_restaurante= 'Restaurante do Zé',
                                 categoria_restaurante= 'comida brasileira')

    restaurante_02 = base_restaurantes.criar_restaurante(id_restaurante='0000002',
                                 nome_restaurante= 'Restaurante do Rio',
                                 categoria_restaurante= 'comida brasileira')

    restaurante_03 = base_restaurantes.criar_restaurante(id_restaurante='0000003',
                                 nome_restaurante= 'Japa Fast',
                                 categoria_restaurante= 'comida japonesa')

    base_restaurantes.listar_restaurantes()

    base_restaurantes.remover_restaurante('Restaurante do Rio', '0000002')

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