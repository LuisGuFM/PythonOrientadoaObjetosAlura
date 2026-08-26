from desafio5 import Livro
livro_biblioteca = Livro('Abacate', 'Luís', 2026)
print(f"Antes de emprestar (biblioteca): Livro disponível? {livro_biblioteca.disponivel}")
livro_biblioteca.emprestar()
print(f"Depois de emprestar (biblioteca): Livro disponível? {livro_biblioteca.disponivel}")
ano_especifico = 2020
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
print(f'Livros disponíveis em {ano_especifico}: {livros_disponiveis_ano}')