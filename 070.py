# escreva um programa que crie um dicionário com os
# nomes e
# preços de
# 5 produtos.
# em seguida, exiba o
# produto mais barato e o
# mais caro

'''maior = 0
menor = 0

produtos = {'produto': ['Caneta', 'Lápis', 'Borracha'],
            'valor': [2.50, 1.35, 1.90]}

mais_caro = produtos['produto'][produtos['valor'].index(max(produtos['valor']))]
mais_barato = produtos['produto'][produtos['valor'].index(min(produtos['valor']))]

print(f'O produto mais caro é o/a {mais_caro}.')
print(f'O produto mais barato é o/a {mais_barato}.')'''

# outra resolução com input

produtos = {}
produto = []
preco = []

try:
    for x in range(5):
        produto.append(input('Digite o produto: '))
        preco.append(float(input('Digite o preço: R$')))

    produtos['Nome'] = produto[:]
    produtos['Preco'] = preco[:]

    print(f'O produto mais caro é: {produtos["Nome"][produtos["Preco"].index(max(produtos["Preco"]))]}.'
          f'\nO produto mais barato é: {produtos["Nome"][produtos["Preco"].index(min(produtos["Preco"]))]}.')

except ValueError:
    print('Erro. Digite apenas números.')