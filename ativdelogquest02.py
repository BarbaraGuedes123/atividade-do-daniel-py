precoIngre:float
despesas:float
lucro:float
qtdIngre:float

precoIngre=5.00
qtdIngre=120
despesas=200.00

while precoIngre >= 1.00:
      lucro=qtdIngre* precoIngre- despesas
      print(f"preco: (t)t|r${precoIngre: .2f} ")
      print(f"lucro: (t)t|r${lucro: .2f} ")
      print(f"ingressos vendidos: (t)t|{qtdIngre: } ")
      print("--------------------------------")
      precoIngre=precoIngre- 0.50
      qtdIngre=qtdIngre+ 26
