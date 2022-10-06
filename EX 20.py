
# As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. 
# Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.

salario = []
total = 0
listabono = []
tabono = 0
abonomin = 0

def abono (x):
    y = x*0.2
    if y <100:
        return 100
    else:
        return y 


while True:
    x = float(input("Informe 0 caso queira SAIR\nInforme o salário: "))
    if x == 0:
        break
    elif x < 0:
        print("Digite um valor válido")
        continue
    else:
        salario.append(x)
        listabono.append(abono(x))
        if abono(x) == 100:
            abonomin +=1
        total += 1
        tabono += abono(x)


print("Projeção de Gastos com Abono\n====================")
for i in range(len(salario)):
    print(f"Salário: {salario[i]}\n")
print("\n")

print("Salário     -Abono")
for i in range(len(salario)):
    print(f"R$ {salario[i]}      -R$ {listabono[i]}    \n")


print(f"Foram processados {total} colaboradores\nTotal gasto com abonos: R$ {sum(listabono)}\nValor minimo pago a {abonomin} colaboradores\nMaior valor de abono pago: R${max(listabono)}")

