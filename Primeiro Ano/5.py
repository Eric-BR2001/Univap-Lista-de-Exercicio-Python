print("Digite o valor:")
valor= float(input())
print("Digite o valor da taxa: ")
taxa= float(input())
print("Digite o tempo: ")
tempo= float(input())
prestacao=valor+(valor*taxa/100)*tempo
prestacao="{:.2f}".format(prestacao)
print("Prestacao R$:"+ str(prestacao))
print("O consumo foi de:"+ str(vConsumo)+"litros")

