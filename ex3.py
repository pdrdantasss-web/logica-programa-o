lista = []
soma = 0

for i in range(0, 4):
    nota = float(input("insira uma nota: "))
    lista.append(nota)

print(lista)
media = sum(lista)/4
print(f"{media:.2}")



