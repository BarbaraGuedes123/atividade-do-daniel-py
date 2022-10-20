faixa1:int
faixa2:int
faixa3:int
faixa4:int
faixa5:int

faixa1=0
faixa2=0
faixa3=0
faixa4=0
faixa5=0

for n in range(1,9):
    idade=int(input("digite idade: "))
    if idade <= 15:
        faixa1 += 1
    elif idade > 15 and idade <= 30:
        faixa2 += 1
    elif idade > 30 and idade <= 45:
        faixa3 += 1
    elif idade > 45 and idade <= 60:
        faixa4 += 1
    else:
        faixa5 +=1

print(f"faixa etaria01(ate15): {faixa1} ")
print(f"faixa etaria01(de15 a 30): {faixa2} ")
print(f"faixa etaria01(de30 a 45): {faixa3} ")
print(f"faixa etaria01(de45 a 60): {faixa4} ")

print(f"porcentagem da 1faixa: {faixa1/8*100}%")
print(f"porcentagem da ultima: {faixa1/8*100}%")


