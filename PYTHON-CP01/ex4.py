# ====================================== EX04 ======================================
# Crie um programa em Python que registre 5 produtos comprados em um mercado. 
# Use Listas, laço for e inputs.

produtos = []

print('\n----------------Bem-Vindo a mercearia do Zé----------------\n')

for i in range(5):
    produto = input(f'Escolha os seus produtos {i+1}: ')
    produtos.append(produto)

print(f'\nVocê escolheu esses produtos: {produtos}\n')
# ==================================== FIM EX04 ====================================
