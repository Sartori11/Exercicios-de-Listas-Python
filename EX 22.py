

# Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. 
# A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.


total = 0
situacao = ['Necessita da esfera ','Necessita de limpeza ','Necessita troca do cabo ou conector','Quebrado ou inutilizado']
quantidade = [0]*(len(situacao))

print("1- Necessita da esfera\n2- Necessita de limpeza\n3- Necessita troca Cabo\n4- Quebrado ou inutilizado  ")
while True:
    x = int(input("Informe 0 para Finalizar\nDigite o problema do mouse: "))
    if x == 0:
        break
    elif x < 0 or x > 4:
        print("Digite um valor válido")
        continue

    else:
        quantidade[x-1] +=1
        total += 1


def percentual (votos,total):
    return (votos*100)/total


print(f"Quantidade de mouses: {total}\nSituação            Quantidade               Percentual")


for i in range(len(situacao)):
    print(f"{i+1}- {situacao[i]}    {quantidade[i]}     {percentual(quantidade[i],total)}% " )


