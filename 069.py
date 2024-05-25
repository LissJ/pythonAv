# escreva um programa que crie um dicionário com as
# informações de 5 livros, como
# título,
# autor,
# ano de lançamento e
# número de páginas.
# em seguida,
# exiba apenas
# os autores dos livros

biblioteca = {'livro1': ['No Seu Olhar', 'Nicholas Sparks', 2015, 432],
              'livro2': ['A Hora da Estrela', 'Clarice Lispector', 1977, 224],
              'livro3': ['O Morro dos Ventos Uivantes', 'Emily Brontë', 1847, 416],
              'livro4': ['Dom Casmurro', 'Machado de Assis', 1899, 256],
              'livro5': ['1984', 'George Orwell', 1949, 328]}

for chave in biblioteca:
    print(biblioteca[chave][1])