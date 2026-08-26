from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praca', 'Gourmet')
restaurante_praca.receber_avaliacao('Luís', 10)
restaurante_praca.receber_avaliacao('Gabi', 9)
restaurante_praca.receber_avaliacao('Mateus', 10)

def main():
    Restaurante.listar_restaurantes()
if __name__ == '__main__':
    main()