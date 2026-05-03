salario = float(input("Digite o salário atual: "))

if salario <= 1500:
    percentual = 15
    novo_salario = salario * 1.15
elif salario <= 3000:
    percentual = 10
    novo_salario = salario * 1.10
else:
    percentual = 5
    novo_salario = salario * 1.05
print(f"Aumento de {percentual}% aplicado. Novo salário: R$ {novo_salario:.2f}")
