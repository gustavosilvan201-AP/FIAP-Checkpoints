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