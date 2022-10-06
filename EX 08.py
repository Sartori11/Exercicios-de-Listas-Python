#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
# Imprima a idade e a altura na ordem inversa a ordem lida.

idade = []

altura = []

for c in range(5):
    for i in range(1):
        idade.append(int(input(f"Pessoa {c+1}\nDigite a sua idade:")))
        altura.append(float(input(f"Pessoa {c+1}\nDigite a sua altura:")))

idade.reverse()
altura.reverse()

print(f"Idades: {idade}")
print(f"Alturas: {altura}")


