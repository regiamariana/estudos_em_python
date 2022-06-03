info = int(input('Digite um ano qualquer: '))

conta = info % 4 #conta para ver se vai sobrar resto com o valor obtido dividido por quatro

if conta == 0: #se não tiver resto, é bissexto, se tiver, não eh
    print('esse ano eh bissexto')
else:
    print('não é bissexto')