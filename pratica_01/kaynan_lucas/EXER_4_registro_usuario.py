nome = input("Digite seu nome: ")
ano = int(input("Digite seu ano de nascimento: "))
altura = float(input("Digite sua altura (ex: 1,75): ").replace(",", "."))

idade = 2026 - ano

altura = str(round(altura, 2)).replace(".", ",")

print("Olá,", nome + "! Você tem", idade, "anos e sua altura é de", altura + "m. Registro concluído.")