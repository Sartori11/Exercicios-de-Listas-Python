#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
#  cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.


v1= [1,3,5,7,9,11,13,15,17,19]
v2 = [2,4,6,8,10,12,14,16,18,20]
vt = []

cont = 0

for i in range(1,11):
    vt.append(v1[cont])
    vt.append(v2[cont])
    cont += 1

print(vt)