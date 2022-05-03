n1 = float(input('Digite um valor: '))
pergunta = input('Você deseja converter o valor em centímetros ou milimetros? ')


multiplicacao = n1 * 100
multiplicacao2 = n1 * 1000

if pergunta == 'centímetros':
    print(f'O valor de {n1}m convertido em centímetros é {multiplicacao}cm')
else:
    print(f'O valor de {n1}m convertido em milímetros é {multiplicacao2}mm')
