# escreva um programa que leia diversos alunos,
# crie um dicionário com as notas de dele em três disciplinas:
# matemática,
# português e
# história.
# em seguida, exiba a
# média das notas do aluno

'''resposta = ''
alunos = {}

while resposta != 'N':
    try:
        print('--------------------------------------------------------')
        nome = input('Digite o nome do aluno: ')

        n_matematica = float(input('Digite a nota dele/a em matemática: '))
        n_portugues = float(input('Digite a nota dele/a em português: '))
        n_historia = float(input('Digite a nota dele/a em história: '))

        resposta = input('Deseja continuar? [S/N] ').strip().upper()

        alunos[nome] = {'mat': n_matematica, 'port': n_portugues, 'hist': n_historia}
    except:
        print('ERRO.')

for ele in alunos:
    media = (alunos[ele]['mat'] + alunos[ele]['port'] + alunos[ele]['hist']) / 3
    print(f'-----------------------------------'
          f'\nEstudante: {ele}'
          f'\nMédia: {media}')'''

# outra resolução

alunos = {}

while True:
    try:
        nome = input('Digite o nome do aluno [sair para encerrar]')

        if nome == 'sair':
            break

        matematica = float(input('Digite a nota em matemática: '))
        portugues = float(input('Digite a nota em português: '))
        historia = float(input('Digite a nota em história: '))

        alunos[nome] = {'mat': matematica, 'port': portugues, 'hist': historia}

    except ValueError:
        print('Digite apenas números.')

for nome, notas in alunos.items():
    media_aritmetica = sum(notas.values()) / len(notas)
    print(f'A média de {nome} é de: {media_aritmetica}')