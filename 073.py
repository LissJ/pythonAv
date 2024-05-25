# crie um programa que leia o 
# nome, 
# sexo e 
# idade de vários alunos, 
# guardando os dados de cada aluno 
# em um dicionário e 
# todos os dicionários em uma lista. 
# no final mostre:
# quantas pessoas foram cadastradas
# a média de idade do grupo
# uma lista com todas as pessoas com idade acima da média
# uma lista com todas as mulheres
  
'''alunos = []
total_cadastrados = 0
soma_idades = 0

while True:
    try:
        print('--------------------------------------------------------')
        nome = input('Digite o nome do aluno (ou "sair" para encerrar): ')

        if nome.lower() == 'sair':
            break

        sexo = input('Digite o sexo do aluno (M/F): ').upper()
        idade = int(input('Digite a idade do aluno: '))

        aluno = {'nome': nome, 'sexo': sexo, 'idade': idade}
        alunos.append(aluno)

        total_cadastrados += 1
        soma_idades += idade
    except:
        print('ERRO.')

media_idade = soma_idades / total_cadastrados

mulheres = [aluno['nome'] for aluno in alunos if aluno['sexo'] == 'F']
acima_media = [aluno['nome'] for aluno in alunos if aluno['idade'] > media_idade]

print('--------------------------------------------------------')
print(f'Quantidade de pessoas cadastradas: {total_cadastrados}')
print(f'Média de idade do grupo: {media_idade:.2f}')
print('Lista de todas as mulheres:', mulheres)
print('Lista de pessoas com idade acima da média:', acima_media)'''

# outra resolução

alunos = []

while True:
    try:
        nome = input('Digite o nome [sair para encerrar]: ')

        if nome == 'sair':
            break

        sexo = input('Sexo [M/F]: ').upper().strip()
        idade = int(input('Digite sua idade: '))

        alunos.append({'nome': nome,
                       'sexo': sexo,
                       'idade': idade})
    except:
        print('Erro. Você digitou algo errado.')

# numero de cadastros
num_cadastros = len(alunos)

# calculo da media de idade do grupo
soma_idade = sum(aluno['idade'] for aluno in alunos)
media_idade = soma_idade / num_cadastros

# criar uma lista com todas as mulheres
mulheres = [aluno['nome'] for aluno in alunos if aluno['sexo'] == 'F']

# criar uma lista com pessoas acima da média de idade
acima_media = [aluno['nome'] for aluno in alunos if aluno['idade'] > media_idade]

# exibir
print(f'Número de pessoas: {num_cadastros}'
      f'\nMédia de idade: {media_idade}'
      f'\nLista de mulheres: {mulheres}'
      f'\nLista de pessoas acima da média de idade: {acima_media}')