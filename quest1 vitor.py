somapos = 0
contaneg=0
for i in range(20):
    valor=int(input("digite o valor: "))
    if valor>=0:
        somapos+=valor
    else:
        contaneg+=1
        print("a soma dos numeros positivos é",somapos)
        print("a quantidade de numero negativo é",contaneg)