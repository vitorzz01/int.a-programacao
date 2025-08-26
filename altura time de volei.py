jogadores = 0
somAltura = 0
jogadores = int(input("digite o numero de jogadores"))
for i in range(jogadores):
    altura = float(input("digite a altura dos jogadores"))
    somAltura += altura
print("altura media do elenco", somAltura/jogadores)
