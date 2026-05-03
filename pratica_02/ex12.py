total = 0

while True:
    valor = float(input("Digite o valor da compra: "))
    total += valor
    resposta = input("Deseja continuar? (S/N): ").upper()
    
    if resposta == 'N':
        break  
print(f"Programa encerrado. Total das compras: R${total:.2f}")
