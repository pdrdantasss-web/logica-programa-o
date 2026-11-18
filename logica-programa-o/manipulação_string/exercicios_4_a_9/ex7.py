numeros = []

for i in range(0, 5):
    vetor = int(input(f"insira um número {i + 1}: "))
    numeros.append(vetor)


soma = sum(numeros)

print("os números são: ", numeros)
print("a soma dos numeros são: ", soma)