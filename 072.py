# crie um programa que leia
# nome,
# ano de nascimento e
# carteira de trabalho e
# cadastre-os (com idade)
# em um dicionário,
# se por acaso a Carteira de trabalho
# for diferente de zero.
# o Dicionário receberá também o
# ano de contratação e o
# saláro.
# calcule e apresente, além da
# idade,
# com quantos anos a pessoa vai se aposentar

'''resposta = ''
cadastros = {}

while resposta != 'N':
    try:
        print('--------------------------------------------------------')
        nome = input('Digite o nome: ')
        nascimento = int(input('Digite o seu ano de nascimento: '))
        carteira_de_trabalho = input('Possui carteira de trabalho?[S/N] ').upper()

        cadastro_individual = {'nascimento': nascimento, 'carteiraTrabalho': carteira_de_trabalho}

        if carteira_de_trabalho == 'S':
            ano_contratacao = int(input('Qual o ano de contratação? '))
            salario = float(input('Qual o salário? R$'))

            idade = 2024 - nascimento
            anos_contribuicao = 2024 - ano_contratacao
            anos_ate_aposentadoria = max(0, 65 - idade)

            cadastro_individual['ano_contratacao'] = ano_contratacao
            cadastro_individual['salario'] = salario
            cadastro_individual['idade'] = idade
            cadastro_individual['anos_contribuicao'] = anos_contribuicao
            cadastro_individual['anos_ate_aposentadoria'] = anos_ate_aposentadoria

        cadastros[nome] = cadastro_individual

        resposta = input('Deseja continuar? [S/N] ').strip().upper()
    except:
        print('ERRO.')

print('----------------------- CADASTRO -----------------------')

for nome, info in cadastros.items():
    print('--------------------------------------------------------')
    print(f'Nome: {nome}')
    print(f'Nascimento: {info["nascimento"]}')
    print(f'Carteira de trabalho: {info["carteiraTrabalho"]}')
    if info['carteiraTrabalho'] == 'S':
        print(f'Ano de contratação: {info["ano_contratacao"]}')
        print(f'Salário: R${info["salario"]}')
        print(f'Idade: {info["idade"]} anos')
        print(f'Anos de contribuição: {info["anos_contribuicao"]}')
        print(f'Anos até aposentadoria: {info["anos_ate_aposentadoria"]}')'''

# outra resolução

from datetime import datetime

funcionarios = []

while True:
    try:
        nome = input('Digite o nome: ')

        if nome == 'sair':
            break

        ano_nascimento = int(input('Digite o ano de nascimento: '))
        carteira_trabalho = int(input('Digite a carteira de trabalho [0 para não e 1 para sim]: '))

        if carteira_trabalho != 0:
            ano_contratacao = int(input('Digite o ano de contratação do funcionário: '))
            salario = float(input('Digite o salário do funcionário: '))
            idade = datetime.now().year - ano_nascimento
            aposentadoria = ano_contratacao + 35 - ano_nascimento

            funcionarios.append({'nome': nome,
                                 'idade': idade,
                                 'carteira_trabalho': carteira_trabalho,
                                 'ano_contratacao': ano_contratacao,
                                 'salario': salario,
                                 'aposentadoria': aposentadoria})

        else:
            idade = datetime.now().year - ano_nascimento
            funcionarios.append({'nome': nome,
                                 'idade': idade,
                                 'carteira_trabalho': carteira_trabalho})
    except:
        print('Erro. Você digitou algo errado.')

for f in funcionarios:
    print(f'Nome: {f["nome"]}'
          f'\nIdade: {f["idade"]}')
    if f['carteira_trabalho']:
        print(f'Carteira de trabalho: {f["carteira_trabalho"]}'
              f'\nAno de contratação: {f["ano_contratacao"]}'
              f'\nSalário: R${f["salario"]}'
              f'\nAposentadoria: {f["aposentadoria"]}')