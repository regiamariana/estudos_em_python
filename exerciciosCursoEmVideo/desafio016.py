from math import trunc

n1 = float(input('Insira um valor: '))
# arredonda p cima
# conta = math.ceil(n1)
# retorna o valor positivo
# conta = math.fabs(n1)
# retorna a parte fracionada E a parte inteira
# conta = math.modf(n1)

conta = trunc(n1)
print(f'O valor de {n1} sem a parte fracionada é {conta}')