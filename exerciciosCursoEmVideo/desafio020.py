import random

m1 = input('cadastre um nome: ')
m2 = input('cadastre um nome: ')
m3 = input('cadastre um nome: ')
m4 = input('cadastre um nome: ')

teste = list((m1, m2, m3, m4))

# também funfa
# random.shuffle(teste)

print(f'A ordem de apresentação será {random.sample(teste, 4)}')
