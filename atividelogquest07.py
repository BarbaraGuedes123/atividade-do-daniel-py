import os
idade = 0
idade50 = 0
idade1020 = 0

for n in range(1,6):
    idade = int(input("Informe idade: "))
    altura = float(input("Informe altura: "))
    peso = float(input("Informe peso: "))
    os.system("cls")
    if idade > 50:
        idade50 += 1
    elif idade >= 10 and idade < 20:
        idade1020 += 1
        