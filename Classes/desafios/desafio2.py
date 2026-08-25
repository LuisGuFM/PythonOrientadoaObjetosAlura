class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
meu_carro = Carro(modelo = 'Fusca', cor = 'Preto', ano = 1989)

class Restaurante:
    def __init__(self, nome, categoria, capacidade = 0, nota_avaliacao = 0.0, ativo = False):
        self.nome = nome
        self.categoria = categoria
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao
        self.ativo = ativo
    def __str__(self):
        return f'{self.nome} | {self.categoria}'    
novo_restaurante = Restaurante(nome = 'Santa Marmita', categoria = 'Marmitas')
print(novo_restaurante)


class Cliente:
    def __init__(self, nome, idade, email, telefone, forma_pagamento):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
        self.forma_pagamento = forma_pagamento
    def __str__(self):
        return f'{self.nome} | {self.idade} | {self.email} | {self.telefone} | {self.forma_pagamento}'

cliente1 = Cliente(nome='Alice', idade=25, email='alice@gmail.com', telefone='123-456-7890', forma_pagamento = 'Dinheiro')
cliente2 = Cliente(nome='Bob', idade=30, email='bob@gmail.com', telefone='987-654-3210', forma_pagamento = 'Cartao de Credito')
cliente3 = Cliente(nome='Charlie', idade=22, email='charlie@gmail.com', telefone='555-123-4567', forma_pagamento = 'Cartao de Debito')
print(cliente1)
print(cliente2)
print(cliente3)