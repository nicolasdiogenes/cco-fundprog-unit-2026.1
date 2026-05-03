alunos = int(input("Digite a quantidade de alunos da turma: "))

# Inicio da contagem:
aprovados = 0
reprovados = 0
recuperacao = 0

for i in range(1, alunos + 1):
    media = float(input("Digite a média do {1}° aluno: "))

    if media >= 7:
        aprovados += 1
    elif media >= 4:
        recuperacao += 1
    else: 
        reprovados += 1

print(f"\nTotal de aprovados: {aprovados}")
print(f"\nTotal em recuperação: {recuperacao}")
print(f"\nTotal de reprovados: {reprovados}")