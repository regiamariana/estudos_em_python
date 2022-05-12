n1 = float(input('O salário atual do funcionário é: R$'))
n2 = float(input('Você quer aumentar quantos %? '))

# dentro do parentese se calcula o número para ele virar decimal
aumento = n1 * (n2/100)
novoSalario = n1 + aumento

print(f'O salário do funcionário era de R${n1}, e subiu {n2}%')
print(f'Portanto, houve um acrescimo de R${aumento:.2f}, e o novo salário é R${novoSalario:.2f}')

