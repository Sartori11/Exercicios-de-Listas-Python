#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

v = []
mult = 1  
for i in range(5):
    x = int(input("Digite um número: "))
    v.append(x)
for i in range (5):
    mult *= v[i] 

print(f"vetor:{v}\nsoma:{sum(v)}\nmultiplicação:{mult} ")