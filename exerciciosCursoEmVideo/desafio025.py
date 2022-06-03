info = input('Digite seu nome: ').strip().title()
info2 = 'Silva ' in info

if info2:
    print('Ei, há Silva no seu nome :)')
else:
    print('Pelo visto, você não tem "Silva" no nome')
