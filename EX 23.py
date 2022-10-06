

# A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. 
# Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":




def conversao (x):
    return (x / (1000000))


def percentual (x,y):
    return (x*100)/y

usuario = []
espaco = []

while True:
    x = input("Pressione ENTER para FINALIZAR\nInforme o Nome do usuário: ")
    if x == "":
        break 
    y = float(input("Espaço ocupado(B): "))
    usuario.append(x)
    espaco.append(y)

print("ACME Inc.              Uso do espaço em disco pelos usuários\n------------------------------------------------")

print("Nr. Usuário          Espaço utilizado         % do uso")

for i in range(len(usuario)):
    print(f"{i+1} {usuario[i]}    {conversao(espaco[i])}       {percentual(espaco[i],sum(espaco))}")

print(f"Espaço total ocupado: {conversao(sum(espaco))}\nEspaço médio ocupado: {conversao((sum(espaco))/len(espaco))}")


