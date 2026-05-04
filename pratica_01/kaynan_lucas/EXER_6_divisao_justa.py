fatias = int(input("Número total de fatias: "))
pessoas = int(input("Número de programadores: "))

por_pessoa = fatias // pessoas
sobra = fatias % pessoas

print("Fatias por pessoa:", por_pessoa)
print("Fatias que sobraram:", sobra)
