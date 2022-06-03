#daria para fazer assim, mas o código quebra quando o usuário digita menos de 4 números
# r1 = str(input('Digite um número de 1 a 9999: ')[:4])
# m1 = list(r1)
# print(f'Seu número foi {r1} e a unidade é {m1[3]}, a dezena é {m1[2]}, a centena é {m1[1]} e o milhar é {m1[0]}')

#o correto seria
num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número de {num}')
print(f'Sua unidade é {u}')
print(f'Sua dezena é {d}')
print(f'Sua centena é {c}')
print(f'E o milhar é {m}')

