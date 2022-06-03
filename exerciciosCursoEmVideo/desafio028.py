import random

n1 = random.randint(1, 5)
n2 = int(input('Escolha um número de 1 a 5: '))

if n2 == n1:
    print(f'O computador escolheu {n1}')
    print('Parabéns, você acertou o número que o computador escolheu')
elif n2 > 5:
    print('número inválido, tente novamente')
else:
    print(f'O computador escolheu {n1}')
    print('Que pena, quem sabe na próxima')
