valor_inicial = -1 

while valor_inicial != 0:
    print("\n--- MENU DE OPERAÇÕES ---")
    print("1 - Somar")
    print("2 - Subtrair")
    print("0 - sair")

    valor_inicial = int(input("Escolha uma opção: "))

    if valor_inicial == 1:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(f"Reseultado da soma: {num1 + num2}")
    elif valor_inicial == 2:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(f"Resultado da subtração: {num1 - num2}")
    elif valor_inicial == 0:
        print("Saindo do menu.")
    else:
        print("Opção inválida! Tente novamente.")
        
