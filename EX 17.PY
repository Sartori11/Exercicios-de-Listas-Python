# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
# O resultado do atleta será determinado pela média dos cinco valores restantes.
# Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, 
# os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. 
# A saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Rodrigo Curvêllo
 
# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m

# Resultado final:
# Atleta: Rodrigo Curvêllo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dos saltos: 5.9 m

nome = ""
notas = []
media = 0

while True :
    x = input("Caso queira sair aperte enter\nDigite nome do atleta: ")
    nome = x
    if x == "":
        break
    for i in range(5):
        y = float(input("Digite a nota: "))
        notas.append(y)
    
    media = (sum(notas))/5

    print(f"Atleta: {nome}\n")
    
    print(f"Primeiro Salto: {notas[0]}\nSegundo Salto: {notas[1]}\nTerceiro Salto: {notas[2]}\nQuarto Salto: {notas[3]}\nQuinto Salto: {notas[4]}\n")

    print(f"Resultado final:\nAtleta: {nome}\nSaltos: {notas}\nMédia dos saltos: {media}")


