KM_LITRO = 12

print("Informe o tempo gasto na viagem em horas: ")
vTempo= float(input())
print("Informe a velocidade média em KM/H: ")
vVelMedia= float(input())
vDistancia= vTempo*vVelMedia
vConsumo=vDistancia / KM_LITRO
vDistancia="{:.2f}".format(vDistancia)
vConsumo="{:.2f}".format(vConsumo)
print("A distancia percorida foi de:"+ str(vDistancia)+"KM.")
print("O consumo foi de:"+ str(vConsumo)+"litros")



