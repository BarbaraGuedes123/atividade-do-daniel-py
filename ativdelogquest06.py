import os


c:str
compra:float;cv:float;cp:float;ct:float

compra=0
cv=0
cp=0
c=""

for n in range(1,3):
    print(f'Dados da {n}ª venda')

    c=input('Digite o código de compra(V - à vista ou P - a prazo): ').upper()

    while(c != "V" and c != "p") :
        c=input("digite o código da compra(V - à vista ou p - a prazo):").upper()
        if c == "V":
           compra=float(input("digite o valor da compra: R$ "))
           cv=cv+compra
        elif c == "":
           compra=float(input("Digite o valor da compra: R$ "))
           cp= cp + compra
     

    os.system("cls")


print(f"O valor total á vista: R${cv: .2f}")
print(f"O valor total á prazo: R${cp: .2f}")
print(f"O valor total das compras: R${cp + cv: .2f}")
print(f"O valor da primeira pestação das compras á prazo junntas: R${cp /3: .2f}")


