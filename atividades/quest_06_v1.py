import os 

os.system('cls')

alunos = []
media = 0
status = ''
notas_str = ''

while True:
    nome = input('Aluno(a): ')
    notas = []

    i = 0
    while i < 4:
        nota = float(input(f'{i + 1}º nota: '))

        if nota < 0 or nota > 10:
            print('Nota invalida! Informe uma nota entre 0 a 10')
            continue
        notas.append(nota)
        notas_str += str(nota) + ' '
        i += 1 # i = i + 1


    media = sum(notas) / len(notas)
    notas_str = notas_str.strip()

    if media >= 7.0:
        status = 'Aprovado(a)'
    elif media < 5.0:
        status = 'Reprovado(a)'
    else:
        status = 'Em recuperação'
    
    #dicionario com dados de UM aluno
    aluno = {
        'Nome': nome,
        'Notas': notas_str,
        'Media': media,
        'Status': status
    }

    notas_str = ''

    alunos.append(aluno)


    os.system('cls')
    print('Aluno(a) cadastrado com sucesso')
    print('Cadastrar novo(a) aluno(a)? S/N')
    
    continuar = input('Digite "S" para sim ou "N" para não:')

    if continuar != "S":
        break

os.system('cls')

for a in alunos:
    print(f'Aluno: {a['Nome']}')
    print(f'Aluno: {a['Notas']}')
    print(f'Aluno: {a['Media']}')
    print(f'Aluno: {a['Status']}')
    print ('-' * 30)

