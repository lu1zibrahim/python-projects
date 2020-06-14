print("\n******************* Python Calculator *******************")

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

qualFuncao = int(input("Digite sua opção(1/2/3/4):"))

if qualFuncao <= 0 and qualFuncao < 5:
    print("Opção Inválida")
else:
    primeironumero = int(input("Digite o primeiro número:"))
    segundonumero = int(input("Digite o segundo número:"))
    if qualFuncao == 1:
        total = primeironumero + segundonumero
        print("\n")
        print(f"{primeironumero} + {segundonumero} = {total}")
        print("\n")
    elif qualFuncao == 2:
        total = primeironumero - segundonumero
        print("\n")
        print(f"{primeironumero} + {segundonumero} = {total}")
        print("\n")
    elif qualFuncao == 3:
        total = primeironumero * segundonumero
        print("\n")
        print(f"{primeironumero} + {segundonumero} = {total}")
        print("\n")
    else:
        total = primeironumero/segundonumero
        print("\n")
        print(f"{primeironumero} + {segundonumero} = {total}")
        print("\n")
