#Faça um programa que leia um número indeterminado de valores, correspondentes a notas, 
# encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;

contmaiormedia = 0
contmenorsete = 0
notas = []
resp = True
while resp == True:
    x = float(input("Digite -1 caso queira sair\nInforme o valor da nota: "))
    if x != -1:
        notas.append(x)
    elif x == -1:
        resp = False
        print("Fim")


media = sum(notas)/len(notas)
for i in range(len(notas)):
    if notas[i] > media:
        contmaiormedia +=1

for i  in range(len(notas)):
    if notas [i] < 7:
        contmenorsete += 1



print(f"{len(notas)} notas foram lidos")

print(notas)

notas.reverse()
print(notas)

print(sum(notas))

print(media)

print(f'{contmaiormedia} são maiores que a média')

print(f'{contmenorsete} menores que sete')