

# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . 
# Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.


import random


lado = int(input("Quantos lados tem o dado: "))

dado = [0]*lado

for i in range(100):
    dado[random.randint(0,(lado-1))] += 1



for i  in range(len(dado)):
    print(f"O lado {i+1} foi sorteado {dado[i]} vezes\n ")