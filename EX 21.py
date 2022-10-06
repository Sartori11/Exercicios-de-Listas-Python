
# Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, 
# quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:



modelo = ["Fusca","Gol","Uno","Vectra","Peugeout"]

consumo = [7,10,12.5,9,14.5] # quilômetros com um litro de combustível.

menorconsumo = 1000
modelominconsumo = 0

for i in range(len(modelo)):
    if (1000 / consumo[i]) < menorconsumo  :
        menorconsumo = 1000 / consumo[i]
        modelominconsumo = i
    print(f"Veículo {i+1}\nNome: {modelo[i]}\nKm por litro: {consumo[i]}\n")
    print(f"Relátorio Final\n{i+1} - {modelo[i]} -  {consumo[i]} -  {1000/consumo[i]} litros --   R$ {(1000/consumo[i])*2.25}")
    print(f"O menor consumo é do {modelo[modelominconsumo]}")




