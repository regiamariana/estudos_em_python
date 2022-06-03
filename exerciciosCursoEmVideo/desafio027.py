info = input('Digite seu nome completo: ').title()

info2 = info.split()
print(f'Seu primeiro nome é {info2[0]} e o último é {info2[-1]}') #o -1 encontra o último item da lista
print(info2)
# print(f'Seu primeiro nome é {info2[0]} e o último é {info2.pop()}') #o pop mostra o último elemento de uma lista e EXCLUI ELE DA LISTA
# print(info2)