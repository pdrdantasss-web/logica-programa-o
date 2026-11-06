n1 = int(input("um número: "))
n2 = int(input("digite um segundo número: "))


soma = 0


for i in range (n1, n2 + 1):
    print(i)

    soma = soma + i
    print(soma)

print("a soma é: ", soma)
