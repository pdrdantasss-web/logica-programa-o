vetor = int(input("digite seu número: "))

impar = []

par = []

for numero in range(0, 21):
    if numero % 2 == 0:
        par.append(numero)

    else:
        impar.append(numero)

print(f"os números ímpar foram {impar} e os números pares foram {par}")