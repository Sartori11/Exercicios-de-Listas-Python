#Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. 
# O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. 
# Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, 
# ou seja, um total de $470. 
# Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
# $200 - $299
# $300 - $399
# $400 - $499
# $500 - $599
# $600 - $699
# $700 - $799
# $800 - $899
# $900 - $999
# $1000 em diante
# Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.



valores = [[200,299],[300,399],[400,499],[500,599],[600,699],[700,799],[800,899],[900,999],] 
contagem = [0]*9
salario = []
resp = True
while resp == True:
    print("Digite um número NEGATIVO caso queira sair")
    x = float(input("Digite o valor de venda bruta:  "))
    if x < 0:
        resp = False
    
    else:
        salario = (x*0.09) + 200
        if salario < 1000:
            for i in range(len(valores)):
                if salario >= valores[i][0] and salario < valores [i][1]:
                    contagem[i] +=1
        else:
            contagem[8] += 1

for i in range(len(valores)):
    print("Entre R$",valores[i][0],valores[i][1],":",contagem[i])

print("Salários maiores que 1000: ",contagem[8])