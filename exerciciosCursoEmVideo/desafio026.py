info = input('Digite uma frase: ').lower()
info1 = info.replace('á', 'a')
info2 = info.replace('ã', 'a')
info3 = info.replace('à', 'a')
info4 = info.count('a')

info5 = info.find('a') + 1
info6 = info.rfind('a') + 1
# print(info4, info5, info6)
print(f'A letra "a" aparece {info4} vezes, e a primeira posição que ocupa é no {info5} e a última {info6}')
