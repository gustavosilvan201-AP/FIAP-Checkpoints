# ====================================== EX07 ======================================
# Crie um programa em Python que simule um sistema simples de login.
# Usar um primeiro laço while para pedir o nome de usuário até que 
# o usuário digite o valor correto, faça o mesmo para a senha.

login = ('admin')

print('\nDigite seu login e senha')
print()

while True:
    username = input('Digite o login de usúario ou digite 0 para desistir: ')
    print()
    if login == username:
        print('--------Usuário encontrado!--------')
        break
    elif username == 0:
        break
    else:
        print('usúario não encontrado, tente novamente!\n')

senha = 1234

while True:
    password = int(input('\nDigite sua senha ou digite 0 para desistir: '))
    if senha == password:
        print(f'\n--------Bem-Vindo {login}--------')
        print()
        break
    elif password == 0:
        break
    else:
        print('\nsenha incorreta, tente novamente!')

# ==================================== FIM EX07 ====================================