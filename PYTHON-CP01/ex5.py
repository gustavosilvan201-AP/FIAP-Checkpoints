# ====================================== EX05 ======================================
# Crie um programa em Python que registre 5 números digitados pelo usuário e 
# depois mostre algumas informações sobre eles, use laço For.
# 1 - A lista completa de números
# 2 - O maior número
# 3 - O menor número
# 4 - A soma de todos os números

numeros = []

for i in range(5):
    num = int(input(f'\nDigite os números desejados: '))
    numeros.append(num)

print(f'\nEsses são os números digitados: {numeros}\n')

maior = max (numeros)
print(f'O maior número digitado é: {maior}\n')

menor = min (numeros)
print(f'O menor número digitado é: {menor}\n')

soma = 0

for n in numeros:
    soma += n
    print(f'Esse é o resultado se somarmos todos os números: {soma}\n')

# ==================================== FIM EX05 ====================================