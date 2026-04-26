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
print()
# ====================================== EX02 ======================================
# Crie um programa em Python que compare dois números, peça ao usuario os numeros e
# compare se eles são iguais.

num1 = int(input('\nColoque o primeiro número para comparação: '))

num2 = int(input('Coloque o segundo número para comparação: '))

if num1 == num2:
    print(f'\nOs números digitados são iguais.')
else:
    print(f'\nOs números não são iguais, tente novamente!')

# ==================================== FIM EX02 ====================================
print()
# ====================================== EX03 ======================================
# Crie um programa em Python que registre 3 notas de um aluno e determine 
# sua situação na disciplina, peça ao usuario as 3 notas e salve em uma lista, tire 
# a media e se for 7 ou maior ele passou na materia.

nota1 = float(input('Digite a 1ª nota do Aluno: '))

nota2 = float(input('Digite a 2ª nota do Aluno: '))

nota3 = float(input('Digite a 3ª nota do Aluno: '))

listanotas  = [nota1, nota2, nota3]

notasfinais = float(nota1 + nota2 + nota3)/3
if notasfinais > 10:
    print(f'\nAs notas digitadas estão incorretas, tente novamente!\n')
elif notasfinais >= 7:
    print(f'\nParabéns você passou! \nSua média é: {notasfinais:.1f}\n')
elif notasfinais > 0:
    print(f'\nVocê está reprovado! \nSua média é: {notasfinais:.1f}\n')
else:
    print(f'\nAs notas digitadas estão incorretas, tente novamente!\n')

# ==================================== FIM EX03 ====================================
print()
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
print()
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
print()
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
print()
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
print()
# ====================================== EX08 ======================================
# Crie um programa em Python que registre 3 notas de alunos, garantindo que 
# cada nota seja válida, use as estruturas de laço for e while.

notas = []

print('Digite as notas do aluno')
print()

for i in range(3):
    while True:
        nota = float(input(f'Digite a nota {i+1}ª nota: '))
        print()
        
        if 0 <= nota <= 10:
            notas.append(nota)
            break
        else:
            print('Nota inválida, Digite novamente!')

print()
print(f'Notas do aluno: {notas}')

# ==================================== FIM EX08 ====================================
print()
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
print()
# ====================================== EX10 ======================================
# Crie um programa em Python que registre as notas de 3 alunos em 4 provas usando
# uma matriz (lista de listas), calcule a media de cada aluno.
# Use seu conhecimento de laços para cumprir a tarefa.

notas = []

aluno = 3
prova = 4

print('Digite as notas do aluno')
print()

for i in range(aluno):
    linha = []
    print(f'\nAluno {i+1}')
    print()

    for j in range (prova):
        nota = float(input(f'Digite a nota da prova{j+1}: '))
        linha.append(nota)

    notas.append(linha)

print(f'\nNotas dos alunos:')

for i in range(aluno):
    print(f'Aluno {i+1} notas: {notas[i]}')
print()

for i in range(aluno):
    soma = 0

    for j in range(prova):
        soma += notas[i][j]

    media = soma / prova
    print(f'A média do aluno {i+1}: {media:.1f}')

# ==================================== FIM EX10 ====================================