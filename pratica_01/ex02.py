valor_hora = float(input("Quanto você ganha por hora?: "))
horas_estimadas = float(input("Em quantas horas o projeto deverá ser concluído?: " ))

valor_bruto = valor_hora * horas_estimadas
impostos = valor_bruto * 0.15
valor_liquido = valor_bruto - impostos

print("-"  * 30)
print(f"Valor bruto: R${valor_bruto: .2f}")
print(f"Impostos (15%): R${impostos: .2f}")
print(f"Valor Líquido final: R${valor_liquido: .2f}")
print("-" * 30)

