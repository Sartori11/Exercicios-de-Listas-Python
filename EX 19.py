
# Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações

print("Qual o melhor Sistema Operacional para uso em servidores?\nAs possíveis respostas são:\n1- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outro")

total = 0
votos = [0]*6
sistemas = ["Windows Server","Unix",'Linux','Netware','Mac Os','Outro']
while True:
    x = int(input("Digite a resposta: "))
    if x ==0:
        break
    elif x < 0 or x > 6:
        print("Digite um valor válido")
        continue
    else:
        total +=1
        votos [x-1] +=1

def percentual (votos,total):
    return (votos*100)/total

print("Sistema Operacional   Votos   %")
print("-------------------------------------")
for i in range(6):
    print(f"{sistemas[i]}            {votos[i]}   {percentual(votos[i],total)}%\n")
    if votos [i] == max(votos):
        melhor = i


print(f"O Sistema Operacional mais votado foi o  {[sistemas[melhor]]}, com {votos[melhor]}, correspondendo a {percentual(votos[melhor],total)} % ")