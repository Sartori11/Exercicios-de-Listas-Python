
#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

n = [0]*4

for i in range(4):
    n[i] = float(input(f"Digite a nota {i+1}: "))

media = sum(n)/4

print(f"As notas foram {n} e a média = {media}")