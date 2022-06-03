velocidade = int(input())

if velocidade > 80:
    multa = 7 * (velocidade - 80)
    print(f'Você foi multado! Terá que pagar {float(multa)} reais')
elif velocidade == 80:
    print('Se liga hein, fica ligado')
else:
    print('Tudo certo por aqui :)')
