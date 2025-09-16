contagem=0
maiormedi=0
menormedi=9999
qtdeaprov=0
qtderep=0
while contagem!=3:
    contagem+=1
    n1 = float(input("nota 1 bimestre"))
    n2 = float(input("nota 2 bimestre"))
    n3 = float (input("nota 3 bimestre"))
    media = (n1+n2+n3) / 3
    if media>maiormedi:
        maiormed=media 
    if media<menormedi:
      menormedi=media
    if media>=6:
        qtdeaprov+=1
        print("a maior media é",maiormedi)
        print("a menor média é",menormedi)
        print("a quantidade de alunos aprovados é",qtdeaprov)
        print("a quantidade de alunos reprovados é",qtderep)
            