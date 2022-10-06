#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
# Imprima os três vetores.
v = []
vp = []
vi = []

for i in range(20):
    x = int(input("Digite um número inteiro: "))
    v.append(x)
    if x %2 == 0:
        vp.append(x)
    else:
        vi.append(x)

print(f"VetorTotal: {v}\nVetorPar:{vp}\nVetorImpar:{vi}")
