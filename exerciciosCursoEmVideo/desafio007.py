n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))

# soma = n1 + n2 + n3
# divisao = soma / 3

media = (n1 + n2 + n3) / 3

if media < 7.0:
    print(f'A média é {media} e infelizmente o aluno está retido :(')
else:
    print(f'A média é {media} e aluno está promovido ao próximo ano :)')
