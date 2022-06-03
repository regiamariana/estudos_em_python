info = str(input('Escreva sua cidade: ').title().strip())  # trad: recolhendo a info, colocando numa variável e deixando tudo capitalizado e sem espaço extra
separandoLista = info.split()  # trad: transformando a informação em lista
info2 = 'Santo' in separandoLista[0]  # trad: há "santo" no item 0 dessa lista lista?

if info2 == True : # condicional que analisa se a resposta de info2 vai ser True ou False
    print('O primeiro nome da sua cidade é Santo') #se for true, ele vai imprimir isso aq na tela
else: #mas se for falso,
    print(f'O pimeiro nome da sua cidade é {separandoLista[0]}')#ele identifica qual que é o primeiro item da lista (o primeiro nome da cidade) e imprime
