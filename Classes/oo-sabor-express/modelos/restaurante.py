class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'


restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast-Food'



restaurantes = [restaurante_praca, restaurante_pizza]

print(restaurante_praca.nome)

nomedorestaurente = restaurante_praca.nome

if restaurante_praca.ativo:
    print('O restaurante esta ativo')
else:
    print('O restaurante esta inativo')

categoria = Restaurante.categoria

restaurante_praca.nome = 'Bistrô'

if restaurante_pizza.categoria == 'Fast-Food':
    print('A categoria é fast food')
else:
    print('A categoria não é fast food')

restaurante_pizza.ativo = True

print(f'Nome do Restaurante: {restaurante_praca.nome} Categoria do Restaurante: {restaurante_praca.categoria}')
