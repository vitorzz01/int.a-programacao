numero=int(input("digite um número"))
cont=0
divisor=1
while divisor<=numero:
    if numero%divisor==0:
        cont+=1
        divisor+=1
        if cont==2:
            print("o numero é primo")
        else:
            print("o numero nao é primo")
    