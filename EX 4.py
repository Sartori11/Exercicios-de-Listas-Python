# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

cons = []
contcons = 0
vogal = ['a','e','i','o','u']

for i in range(5):
    x = input("Digite uma letra: ")
    if x not in vogal:
        contcons += 1
        cons.append(x)

print(f"Foram digitadas {contcons} consoantes, {cons}")