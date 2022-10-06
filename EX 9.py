#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

v = []

for i in range(10):
    x = int(input("Digite um número: "))
    v.append(x*x)

print(sum(v))

