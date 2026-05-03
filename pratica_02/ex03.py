numero = int(input("Digite um número de 1 a 20: "))

if numero in range(1, 21):
   if numero % 2 == 0:
    print(f"{numero} é par.")
   else:  
    #0
    print(f"{numero} é ímpar.")
else: 
  # Se NÃO estver no intervalo de 1 a 20, aparecerá a mensagem abaixo
    print("O número está fora do intervalo de 1 a 20.")
