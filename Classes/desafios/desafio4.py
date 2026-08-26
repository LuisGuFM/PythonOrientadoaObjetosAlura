class ContaBancaria:
    def __init__(self, titular = '', saldo = 0):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False
    def __str__(self):
        return f'Ola, {self.titular.title()}! Seu saldo é {self.saldo}'
    def ativar_conta(self):
        self._ativo = True        


conta1 = ContaBancaria(titular = 'Cleber', saldo = 350)
conta2 = ContaBancaria(titular = 'Ana', saldo = 1000)  

print(conta1)
print(conta2)

conta3 = ContaBancaria("Carlos", 200)
print(f"Antes de ativar: Conta ativa? {conta3._ativo}")
conta3.ativar_conta()
print(f"Depois de ativar: Conta ativa? {conta3._ativo}")

class ContaBancariaPythonica:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
    @property
    def titular(self):
        return self._titular
    @property
    def saldo(self):
        return self._saldo
    @property
    def ativo(self):
        return self._ativo
    def ativar_conta(self):
        self._ativo = True

conta4 = ContaBancariaPythonica('Pericles', 10000000)
print(f'Titular da conta 4: {conta4.titular}')

class ClienteBanco:
    def __init__(self, nome, idade, endereco, cpf, profissao):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.profissao = profissao
    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancariaPythonica(titular, saldo_inicial)
        return conta    
cliente1 = ClienteBanco("Ana", 30, "Rua A", "123.456.789-01", "Backend")
cliente2 = ClienteBanco("Luiza", 25, "Rua B", "987.654.321-01", "Estudante")
cliente3 = ClienteBanco("Vinny Neves", 40, "Rua C", "111.222.333-44", "Frontend")

conta_cliente1 = ClienteBanco.criar_conta('Ana', 500)
print(f'Conta de {conta_cliente1.titular} criada com sucesso! Saldo inicial de R${conta_cliente1.saldo}')