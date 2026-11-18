# // LISTAS //

#são estruturas de dados utilizadas para armazenar vários valores dentro de uma única variável.

# EXEMPLO:

# frutas = variável da lista
# [] = função da lista
# e o que tem dentro da lista são chamado de elementos

frutas = ["banana", "goiaba", "abacaxi", "maçã"]

# // VETORES E ÍNDICES //

# vetor = sequência de elementos que podem ser acessados individualmente
# índice = as posições onde os elementos estão, UM ÍNDICE COMEÇA EM ZERO

#EXEMPLO:

notas = [8, 7, 9, 6, 10]

#variável notas: é o vetor
# 8, 7, 9, 6 e 10 são os elementos, onde cada elemento tem uma posição, que são chamadas de índices

print(notas[2])
# o [2] seria a posição do elemento que eu quero imprimir


# // FATIAMENTO DE LISTAS (SLICING)

numeros = [10, 20, 30, 40, 50, 60]

print(numeros[1:4])

# o : escolhe elementos de acordo com o índice
# índice inicial: 1
#índice final onde o mesmo não conta: 4

# resultado: [20,30,40]



#pegar do inicio até determinada posição se usa:

numeros[:3]

#resultado: [10, 20, 30]

#pegar de determinada posição até o final:

numeros[3:]

#resultado: [30, 40, 50, 60]



# copiar a lista inteira:

numeros[:]

# resultado: [10, 20, 30, 40, 50, 60]

