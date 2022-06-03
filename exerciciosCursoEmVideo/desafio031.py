info1 = int(input('Digite a kilometragem da sua viagem: '))

if info1 <= 200:
    conta = 0.50 * info1
    print(f'Você vai pagar {conta} reais nessa viagem')
else:
    conta2 = 0.45 * info1
    print(f'Você vai pagar {conta2} reais nessa viagem')


