#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.


v1= [1,3,5,7,9,11,13,15,17,19]
v2 = [2,4,6,8,10,12,14,16,18,20]
v3 = [21,22,23,24,25,26,27,28,29,30]
vt = []

cont = 0

for i in range(1,11):
    vt.append(v1[cont])
    vt.append(v2[cont])
    vt.append(v3[cont])
    cont += 1

print(vt)