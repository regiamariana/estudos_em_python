import math

n1 = float(input('Digite o valor do Cateto Oposto: '))
n2 = float(input('Digite o valor do Cateto Adjacente: '))

hip = math.hypot(n1, n2)
print(f'O valor da hipotenusa é: {hip:.2f}')
