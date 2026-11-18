
# lista onde as notas ficarão armazenadas 
nomes = []

for alunos in range (10):

    notas = []

    vetor1 = input(f"insira o nome dos {alunos + 1}: ")

    nomes.append(vetor1)

    for i in range(0, 4):
        vetor2 = int(input(f"insira a {i + 1}° nota: "))

        notas.append(vetor2)
    media = sum(notas) / 4

    print("média de notas: ", media)
    print("alunos: ", nomes)

        







#o que falta?


#aplicar média
#colocar essa lógica pra 10 alunos 
# 
    


   

        
    

    
        