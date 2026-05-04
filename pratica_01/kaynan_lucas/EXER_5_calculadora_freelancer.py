valor_hora = float(input("Valor por hora: ").replace(",", "."))
horas = float(input("Horas: ").replace(",", "."))

bruto = valor_hora * horas
imposto = bruto * 0.15
liquido = bruto - imposto

print("Valor bruto:", bruto)
print("Imposto:", imposto)
print("Valor liquido:", liquido)