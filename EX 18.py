
#  desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos.



total = 0
votos = [0]*23
melhor = 0
while True:
    x = int(input("Digite 0 caso deseja encerrar\nQual foi o melhor jogador: "))
    if x == 0:
        break
    elif x <0 or x >23:
        print("Número inválido")
        continue
    
    else:
        total +=1
        votos [x-1] +=1

def percentual (votos,total):
    return (votos*100)/total

print(f"Resultado da votação:\nForam computados {total} votos")

for i in range(23):
    if votos[i] != 0:
        print(f"Jogador Votos\n{i+1}         {votos[i]}     {percentual(votos[i],total)}% ")
    if votos [i] == max(votos):
        melhor = i

print(f"O melhor jogador foi o número {melhor+1}, com {votos[melhor]}, correspondendo a {percentual(votos[melhor],total)}% ")