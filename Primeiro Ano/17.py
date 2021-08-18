print("Digite a quantidade de votos validos para o candidato A: " )
A= int(input())
print("Digite a quantidade de votos validos para o candidato B: " )
B= int(input())
print("Digite a quantidade de votos validos para o candidato C: " )
C= int(input())
print("Digite a quantidade de votos nulos: " )
Nulos= int(input())
print("Digite a quantidade de votos branco: " )
Brancos= int(input())
votovalido = A + B + C
totalEleitor=votovalido + Nulos + Brancos
percTot_valido = (votovalido * 100) / totalEleitor
percValido_A = (A * 100) / totalEleitor
percValido_B = (B * 100) / totalEleitor
percValido_C = (C * 100) / totalEleitor
percNulo = (Nulos * 100) / totalEleitor
percBranco = (Brancos * 100) / totalEleitor 
percTot_valido="{:.2f}".format(percTot_valido)
percValido_A="{:.2f}".format(percValido_A)
percValido_B="{:.2f}".format(percValido_B)
percValido_C="{:.2f}".format(percValido_C)
percNulo="{:.2f}".format(percNulo)
percBranco="{:.2f}".format(percBranco)
print("O candidato A teve: "+ str(A)+" de votos")
print("O candidato B teve: "+ str(B)+" de votos")
print("O candidato C teve: "+ str(C)+" de votos")
print("A quantidade de votos nulos foi de: "+ str(Nulos))
print("A quantidade de votos brancos foi de: "+ str(Brancos))
print("Nessa eleição teve: "+ str(totalEleitor)+" de votos")
print("Nessa eleição teve: "+ str(percTot_valido)+"%"+" de votos validos")
print("Nessa eleição o candidato A teve: "+ str(percValido_A)+"%"+" de votos validos")
print("Nessa eleição o candidato B teve: "+ str(percValido_B)+"%"+" de votos validos")
print("Nessa eleição o candidato C teve: "+ str(percValido_C)+"%"+" de votos validos")
print("Nessa eleição teve: "+ str(percNulo)+"%"+" de de votos nulos")
print("Nessa eleição teve :"+ (str(percBranco))+"%"+" de de votos brancos")


