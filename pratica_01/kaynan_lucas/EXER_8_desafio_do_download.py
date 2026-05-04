print("Digite o tamanho do arquivo (MB):")
tamanho_mb = float(input())

print("Digite a velocidade da internet (Mbps):")
velocidade_mbps = float(input())

tempo_segundos = tamanho_mb / (velocidade_mbps / 8)

minutos_inteiros = int(tempo_segundos // 60)
segundos_restantes = int(tempo_segundos % 60)

print(f"{minutos_inteiros} minutos e {segundos_restantes} segundos")