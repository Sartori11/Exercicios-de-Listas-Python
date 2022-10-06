#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, 
# imprima o número de alunos com média maior ou igual a 7.0.

vmedia = []
total = 0
aprovado = 0
for c in range(10):
    for i in range(4):
        x = float(input(f"Aluno {c+1}\nDigite a nota {i+1}: "))
        total += x
    media = total/4 
    vmedia.append(media)
    total = 0
    media = 0
for i in range(10):
    if vmedia[i] >= 7:
        aprovado +=1
    
        

print(f"{aprovado} alunos possuem a média maior ou igual a 7")