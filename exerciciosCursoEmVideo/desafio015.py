# carro custa 60 reais por dia
# 0,15 centavos por km rodado

resposta1 = float(input('Quantos KM rodou?: '))
resposta2 = int(input('Quantos dias foi usado??: '))

custoDias = resposta2 * 60
custoKm = resposta1 * 0.15
soma = custoKm + custoDias

print(f'O preço a pagar é R${soma}')

