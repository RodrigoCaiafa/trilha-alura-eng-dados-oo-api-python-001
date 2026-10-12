from modelos.restaurantes_credenciados import RestaurantesCredenciados
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato


def main():
    base_restaurantes = RestaurantesCredenciados()
    base_restaurantes.criar_restaurante(id_restaurante='0000001',
                                        nome_restaurante='Restaurante do Zé',
                                        categoria_restaurante='comida brasileira')

    base_restaurantes.criar_restaurante(id_restaurante='0000002',
                                        nome_restaurante='Restaurante do Rio',
                                        categoria_restaurante='comida brasileira')

    base_restaurantes.criar_restaurante(id_restaurante='0000003',
                                        nome_restaurante='Japa Fast',
                                        categoria_restaurante='comida japonesa')

    base_restaurantes.listar_restaurantes()

    base_restaurantes.remover_restaurante('Restaurante do Rio', '0000002')

    base_restaurantes.listar_restaurantes()

    bebida_refri = Bebida(id_produto='0000001',
                          nome='CocaCola',
                          tipo_bebida='Refrigerante',
                          tamanho='500ml',
                          preco=15.0)
    prato_hamburguer = Prato(id_prato='0000002',
                             nome='Hamburguer',
                             tipo_prato='Sanduiches',
                             preco=10.0)

    bebida_refri = ['0000001', 'CocaCola', 'Refrigerante', '500ml', 15.0]
    prato_hamburguer = ['0000002', 'Hamburguer', 'Sanduiches', 10.0]
    sobremesa_pudim = ['0000003', 'Pudim de leite', 'Sobremesas', 'fatia', 'Sobremesa gelada', 8.0]

    cardapio_do_ze = base_restaurantes \
        .buscar_restaurante(id_restaurante='0000001') \
        .cardapio_restaurante

    cardapio_do_ze.criar_produto('bebida', *bebida_refri)
    cardapio_do_ze.criar_produto('prato', *prato_hamburguer)
    cardapio_do_ze.criar_produto('sobremesa', *sobremesa_pudim)

    #print(cardapio_do_ze._relacao_produtos['0000001'])

    for _, produto in cardapio_do_ze._relacao_produtos.items():
        print(produto)

    cardapio_do_ze.buscar_produto('0000001').aplicar_desconto()
    cardapio_do_ze.buscar_produto('0000002').aplicar_desconto()
    cardapio_do_ze.buscar_produto('0000003').aplicar_desconto()



if __name__ == '__main__':
    main()
