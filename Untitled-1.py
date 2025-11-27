totalpreco=0
quantidade_produtos=0
média=0
mais_caro=0
compras=0
preco=0
while compras!=1:
    preco=float(input("preco do produto:"))
    if preco>0:
      totalpreco+=preco
    quantidade_produtos+=1
média+=preco
if mais_caro<preco:
   mais_caro=preco
   print("salvo.")
a=str(input("deseja continuar?(s/n)"))
if a =="n":
   compra=1
else:
   print("digite um valor positivo") 
   print("ficou o total de:",totalpreco,"RS")
print("a quantidade de produtos:",quantidade_produtos)
print("a media de preco foi",media/quantidade_produtos)
print("o produto mais caro foi:",mais_caro,"RS")