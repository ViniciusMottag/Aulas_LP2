contador=0
lista=[]
resp1=str(input("Telefonou para a vitima? "))
lista.append(resp1)
if resp1=="sim" or resp1=="SIM":
    contador=contador+1
resp2=str(input("Esteve no local do crime? "))
lista.append(resp2)
if resp2=="sim" or resp2=="SIM": 
    contador=contador+1
resp3=str(input("Mora perto da vitima? "))
lista.append(resp3)
if resp3=="sim" or resp3=="SIM":
    contador=contador+1
    
resp4=str(input("Devia para a vitima? "))
lista.append(resp4)
if resp4=="sim" or resp4=="SIM":
    contador=contador+1
resp5=str(input("Já trabalhou para a vitima? "))
lista.append(resp5)
if resp5=="sim" or resp5=="SIM":
    contador=contador+1

if contador<=1:
    print(lista,"INOCENTE")
if contador==2:
    print(lista,"SUSPEITO")
if contador==(3,4):
    print(lista,"CUMPLICE")
if contador==5:
    print(lista,"ASSASINA")