resp=[]
resp.append(input("Telefonou para a vitima? "))
resp.append(input("Esteve no local do crime? "))
resp.append(input("Mora perto da vitima? "))
resp.append(input("Devia para a vitima? "))
resp.append(input("Já trabalhou para a vitima? "))
cont_sim=0
for r in resp:
    if r =='sim':
        cont_sim=cont_sim+1
        #cont_sim += 1 mesma coisa que a de cima ^

if cont_sim<=1:
    print(resp,"INOCENTE")
if cont_sim<=2:
    print(resp,"SUSPEITO")
if cont_sim<=4:
    print(resp,"CUMPLICE")
if cont_sim==5:
    print(resp,"ASSASINA")

    