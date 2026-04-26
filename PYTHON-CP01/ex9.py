# ====================================== EX09 ======================================
# Crie um programa em Python que registre números digitados pelo usuário e 
# conte quantos são positivos. Use o laço while para registrar todas as entradas
# depois use o laço for para percorrer toda a lista e fazer a contagem.

usernum = []

contador = 0

print("Digite números (digite 0 para parar):")
print()

while True:
    num = int(input('Digite o número desejado (digite 0 para parar): '))
    if num == 0:
        break
    usernum.append(num)
    print()

for n in usernum:
    if n > 0:
        contador += 1
print()

print(f'Quantidade de números positivos {contador}\n')

print(f'Os números digitados pelo usuário são: {usernum}\n')

# ==================================== FIM EX09 ====================================