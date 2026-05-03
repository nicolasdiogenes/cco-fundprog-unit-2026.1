total_fatias = int(input("Quantas fatias de pizza temos no total? "))
total_programadores = int(input("Quantos programadores vão comer? "))

#//realizar a divisão inteira(fatias inteiras para cada um)
fatias_por_pessoa = total_fatias // total_programadores 
#calcular o resto da divisão (fatias restantes)
resto_fatias = total_fatias % total_programadores

print(f"\nCada programador receberá {fatias_por_pessoa} fatias inteiras.")
print(f"Fatias que sobraram na caixa: {resto_fatias}.")
