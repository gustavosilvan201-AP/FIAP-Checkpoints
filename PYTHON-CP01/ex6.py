# ====================================== EX06 ======================================
# Crie um programa em Python que peça números ao usuário e some todos eles.
# Use o laço while e receba numeros ate que uma condição seja atendida.

print('\nDigite os números para somar ou digite 0 para parar\n')
  
usernum = []

resultado = 0

while True: 

    usernum = int(input('\nDigite os números (ou 0 para parar): '))

    if usernum == 0:
        break

    resultado += usernum
    print(f'\nA soma de todos os números digitados é: {resultado}')

# ==================================== FIM EX06 ====================================