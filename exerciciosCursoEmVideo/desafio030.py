info = int(input('Digite um número qualquer: '))

conta = info % 2

if conta == 0:
    print(f'O número {info} é par')
else:
    print(f'O número {info} é impar')
