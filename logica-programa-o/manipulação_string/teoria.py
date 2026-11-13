# // FUNÇÕES //

#DEF


#saudacao é a variável 
def saudacao():
# o print é o texto que vai ser imprimido
    print("olá")

#chamada de função
saudacao()

#DEF COM IF E ELSE E PARAMETRO

def verificar_idade(idade):

#variável atribuída para o uso nas condições
    idade = 18

#condições
    if idade <= 17:
        print("idade baixa!")
    else:
        print("pode passar!")

#chamada de função
verificar_idade()

#DEF COM RETURN 

#função, onde preco e quantidade seria os parametros
def calcular_preco(preco, quantidade):

#variável atribuída para a resolução das situações abaixo
    total = preco * quantidade

#retorno da variável
    return total

# variável de resultados, onde calcular preço é a chamada de função, e os número entre parênteses são os parâmetros da função
resultado1 = calcular_preco(15 * 3)
resultado2 = calcular_preco(20 * 3)

print(f"o valor do produto 1 é {resultado1} e o valor do produto 2 é {resultado2}")

