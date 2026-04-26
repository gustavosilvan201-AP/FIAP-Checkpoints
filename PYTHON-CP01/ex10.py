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