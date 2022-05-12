pergunta = input('Seu valor é em Celsius ou Fahrenheit? ')
n1 = float(input(f'Digite o valor em {pergunta}: '))

cF = (n1 * 1.8) + 32
fC = (n1 - 32) / 1.8

if pergunta == 'celsius':
    print(f'O valor {n1}°C convertido em Fahrenheit é {cF}°F')
else:
    print(f'O valor {n1}°F convertido em Celsius é {fC}°C')
