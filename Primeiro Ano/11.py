print("Digite o valor em Real: ")
real= float(input())
print("Digite a cotacao do Dolar: ")
cotacao= float(input())
dolar=real*cotacao
dolar="{:.2f}".format(dolar)
print("O valor em dolar é: "+ str(dolar))
