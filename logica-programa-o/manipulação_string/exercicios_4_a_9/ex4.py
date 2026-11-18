vetor = str(input("insira sua palavra: "))

#lista das vogais 
vogais = ["a", "e", "i", "o", "u"]

#lista onde vai ficar as consoantes 
consoantes = []

# a estrutura de repetição que vai repetir cada letra da palavra
for letra in vetor:
    # condição pra saber se a letra que a gente quer é uma vogal ou não
    if letra not in vogais:
        # adição da letra na consoante após a condição dar true ou false    
        consoantes.append(letra)

# print da resposta
print(f"as suas consoantes foram: {consoantes}")


