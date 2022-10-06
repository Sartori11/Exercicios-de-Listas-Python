#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".


resp = []
suspeita = 0
print("Responda com S/N")

a = input("Telefonou para a vítima?: ")
a = a.upper()
resp.append(a)


b = input("Esteve no local do crime?: ")
b = b.upper()
resp.append(b)

c = input("Mora perto da vítima?: ")
c = c.upper()
resp.append(c)


d = input("Devia para a vítima?: ")
d = d.upper()
resp.append(d)

e = input("Já trabalhou com a vítima?: ")
e = e.upper()
resp.append(e)


for i in range(5):
    if resp[i] == 'S':
        suspeita +=1

if suspeita == 2:
    print('Suspeita')

elif suspeita == 3 or suspeita == 4:
    print("Cúmplice")

elif suspeita == 5:
    print("Assasino")

else:
    print("Inocente")