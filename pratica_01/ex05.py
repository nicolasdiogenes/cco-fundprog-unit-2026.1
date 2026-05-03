tamanho_arquivo = float(input("Digite o tamanho do arquivo em MB: "))
velocidade_internet = float(input("Digite a velocidade da internet em Mbps: "))

tempo_segundos = tamanho_arquivo / (velocidade_internet / 8) 
minutos_inteiros = int(tempo_segundos // 60)
segundos_restantes = int(tempo_segundos % 60)

print(f"{minutos_inteiros} minutos e {segundos_restantes} segundos para fazer o download do arquivo. ")

