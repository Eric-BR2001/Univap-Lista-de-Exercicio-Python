print("Digite o valor em dolar: ")
dolar= float(input())
print("Digite a cotacao do real: ")
cotacao= float(input())
real=dolar/cotacao
real="{:.2f}".format(real)
print("O valor em dolar é: "+ str(real))
