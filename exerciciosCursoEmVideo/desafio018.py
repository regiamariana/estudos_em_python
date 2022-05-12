import math

n1 = int(input('Digite um ângulo de 1 a 360: '))

c1 = math.radians(n1)

seno = math.sin(c1)
cos = math.cos(c1)
tan = math.tan(c1)

print(f'O Seno de {n1} é igual a {seno:.10f}')
print(f'O Cosseno de {n1} é igual a {cos:.10f}')
print(f'A Tangente de {n1} é igual a {tan:.10f}')
