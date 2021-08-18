print("Digite o salario mensal: ")
variável_SM= float(input())
print("Digite o percentual de reajuste: ")
variável_PR= float(input())
variável_NS=variável_SM/100*variável_PR
variável_NS="{:.2f}".format(variável_NS)
print("O novo salário será de: "+ str(variável_NS))

