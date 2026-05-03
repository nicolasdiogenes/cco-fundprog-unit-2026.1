contador_positivos = 0

for i in range(10):
    numero = float(input(f"Digite o {i+1}° número: "))
    if numero > 0:
        contador_positivos = contador_positivos + 1
        print(f"Você digitou {contador_positivos} números positivos.")
        

