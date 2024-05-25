# escreva um programa que crie um dicionário com as informações de
# 5 países, como
# nome,
# capital,
# população e
# idioma oficial.
# em seguida, permita que o usuário
# digite o nome de um país e
# exiba suas informações

paises = {'brasil': ['Brasil', 'Brasília', '215.3 milhões de pessoas', 'Português-BR'],
          'china': ['China', 'Pequim', '1.412 bilhão de pessoas', 'Mandarim'],
          'argentina': ['Argentina', 'Buenos Aires', '45.6 milhões de pessoas', 'Espanhol'],
          'alemanha': ['Alemanha', 'Berlim', '83.3 milhões de pessoas', 'Alemão'],
          'jamaica': ['Jamaica', 'Kingston', '2.827 milhões de pessoas', 'Inglês'],}

try:
    qual_pais = input('Qual país você gostaria de saber mais? ').lower()

    print(paises[qual_pais])
except KeyError:
    print('Não existe. Digite um país válido.')