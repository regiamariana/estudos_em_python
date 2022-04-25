respostaUsuario = input('soma ou subtração?')


if respostaUsuario == 'soma' :
    primeiroValorSoma = input('Primeiro Valor: ')
    segundoValorSoma = input('Segundo Valor: ')
    print('seu resultado é: ', int(primeiroValorSoma) + int(segundoValorSoma))
else:
    primeiroValorSubtracao = input('Primeiro Valor: ')
    segundoValorSubtracao = input('Segundo Valor: ')
    print("seu resultado é: ", int(primeiroValorSubtracao) - int(segundoValorSubtracao))
