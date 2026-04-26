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