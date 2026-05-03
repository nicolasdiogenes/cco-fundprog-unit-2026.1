numero = int(input("Digite um número para verificar a tabuada: "))
print(f"\nTabuada do {numero}: ")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} * {i} = {resultado}")
    
    