info1 = int(input('Informe um número inteiro: '))
info2 = int(input('Informe um número inteiro: '))
info3 = int(input('Informe um número inteiro: '))

if info1 > info2:
    print(f'o maior número é {info1}')
elif info2 > info3:
    print(f'o maior número é {info2}')
else:
    print(f'o maior número é {info3}')

if info1 < info2:
    print(f'O menor número é {info1}')
elif info2 < info3:
    print(f'O menor número é {info2}')
else:
    print(f'O menor número é {info3}')

