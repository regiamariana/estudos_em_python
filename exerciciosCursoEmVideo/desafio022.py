r1 = str(input('Digite seu nome completo: ')).strip()

print('O seu nome com todas as letras maiúsculas é: ', r1.upper())
print('O seu nome com todas as letras minúsculas é: ', r1.lower())
print('O seu nome com a fonte capitalizada é: ', r1.title())



# tirando os espaços do meio
teste = r1.replace(" ", "")
print('1. O seu nome seu sobrenome, juntos, têm', len(teste), "letras") #len conta os caracteres tbm


#outra forma de fazer
m1 = len(r1)-r1.count(' ')
print(f'2. Seu nome tem ao todo {m1} letras')



teste2 = r1.split()
print('1. O seu primeiro nome, sozinho, tem', len(teste2[0]), 'letras')


#outra forma de fazer
m2 = r1.find(' ') #ele simplesmente procurou onde está o único espaço, que obviamente fica entre o primeiro e o segundo nome, e me trouxe a posição que o caractere está
print(f'2. Seu primeiro nome tem {m2} letras')

