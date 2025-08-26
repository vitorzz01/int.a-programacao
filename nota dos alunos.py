alunos = 10
for i in range(alunos):
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))  
    n3 = float(input("Digite a terceira nota: "))
    media = (n1 + n2 + n3) / 3
    print("A média do aluno", i + 1, "é:", media)