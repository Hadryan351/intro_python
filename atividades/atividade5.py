import random, os
os.system('cls')

print('''Tenta adivinhar o número sorteado entre 1 e 10,
Você tem 3 tentativas...''')

numero_sorteado = random.randrange(1, 11)
tentativas = 3

palpite = int(input('Qual o seu palpite para o número sorteado? '))

while tentativas > 0:
    tentativas -= 1
    if palpite == numero_sorteado:
        print == ('Bingo!! Você acertou o número sorteado')
        break #encerra imediatamente a execução do laço
    elif palpite < numero_sorteado:
        print ('Seu Palpite foi menor que o número sorteado')
    else:
        print('Sei palpite foi maior que o número sorteado ')
    
    palpite = int(input(f'Você ainda tem {tentativas} tentativas. Tente novamente: '))

print('************ FIM DO SCRIPT **************')