n1 = float(input('O preço inicial é: R$'))
n2 = float(input('De quantos % será o desconto?: '))

# funciona para 5%
# desconto = n1 * 0.05
# novoValor = n1 * 0.95

desconto = n1 * (n2/100)
novoValor = n1 - desconto

print(f'O valor de R${n1} com {n2}% de desconto fica R${novoValor},')
print(f'tendo a diminuição de R${desconto}')
