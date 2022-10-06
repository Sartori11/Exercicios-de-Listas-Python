#Foram anotadas as idades e alturas de 30 alunos. 
# Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.


idade = []

altura = []

totalaltura = 0
media = 0
resp = 0
for c in range(30):
    for i in range(1):
        idade.append(int(input(f"Pessoa {c+1}\nDigite a sua idade:")))
        x = float(input(f"Pessoa {c+1}\nDigite a sua altura:"))
        altura.append(x)
        
        
        totalaltura += x 
        media = totalaltura/4


for i in range(30):
    if idade[i] > 13 and altura[i] < media:
        resp +=1


print(f"Idades: {idade}")
print(f"Alturas: {altura}")

print(resp)