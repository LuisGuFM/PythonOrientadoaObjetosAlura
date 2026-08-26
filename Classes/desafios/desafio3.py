class Pessoa:
    def __init__(self, nome = '', idade = 0, profissao = ''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
    def __str__(self):
        return f'{self.nome.title()},{self.idade} anos, {self.profissao}.'
    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, sou {self.nome}! Trabalho como {self.profissao}.'
        else:
            return f'Olá, sou {self.nome}.'
    def aniversario(self):
            self.idade += 1            
pessoa1 = Pessoa(nome = 'Luís', idade = 21, profissao = 'Programador')
pessoa2 = Pessoa(nome = 'Gabriela', idade = 21, profissao = 'Psicologa')
pessoa3 = Pessoa(nome = 'Clarencio', idade = 10)

print('Informações Iniciais:')
print(pessoa1)
print(pessoa2)
print(pessoa3)
print()

pessoa1.aniversario()
pessoa3.aniversario()

print('Informações após aniversário:')
print(pessoa1)
print(pessoa3)

print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)