import os
#Declaração de variáveis
alunos = []
notas = []
status = ''

saida = ''

os.system('cls')

#entrada
while True:
    alunos.append(input('Aluno: '))
    qtd_notas = int(input('Quantidade de notas: '))

    for i in range(qtd_notas):
        notas.append(float(input(f'{i + 1}º nota: ')))

    os.system('cls')

    #processamento
    media = sum(notas) / len(notas)

    if media >= 7:
        status = 'Aprovado(a)'
    elif media < 5:
        status = 'Reprovado(a)'
    else:
        status= 'Em Recuperação'

    #saída
    #saida += f'Aluno: {nome_aluno}\n'
    saida += 'Notas: '

    for nota in notas:
        saida += f'{str(notas)}'

    saida += f'\n Média: {media}:.2f\n'
    saida += f'Situação: {status}'
    saida += "-" * 40
    print(saida) 