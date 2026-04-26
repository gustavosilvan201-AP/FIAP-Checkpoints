# ====================================== EX01 ======================================
# Crie um programa em Python que verifique se uma pessoa pode entrar em um evento 
# se for maior de 18 anos.

idade = int(input('Para entrar no evento digite sua idade: '))

if idade >= 19:
    print(f'Pode entrar, você tem {idade} anos de idade.')
elif idade == 18:
    print(f'Pode entrar, foi por pouco!')
else:
    print(f'Você é menor de idade, não pode entrar!')
    
# ==================================== FIM EX01 ====================================