def porcentagem(valor,taxa):
    if taxa >100 or taxa <0:
        return -1
    else:
        return valor *taxa /100
print(porcentagem(1000,5))

class MinhaExcecao(Exception):
    pass

def funcao(x):
    if x<0 or x>100:
        raise MinhaExcecao("Valor invalido") #Um problema criado pelo programador com uma linguagem mais "FACIL"
    if x % 2 == 0:
        #raise MinhaExcecaozinha("Par não!") #Minhaexcecaozinha não foi definido
        raise MinhaExcecao("Par Não!")


def divide(a,b):
    if b== 0:
        raise MinhaExcecao("Não dividiras por zero")
    c = a/b
    return c

print(divide(8,4))

def divide2(a,b):
    try:
        c = a/b
    except MinhaExcecao as e:
        print("Assim não da!Zero não!!",e)
    return c

def divide3(a,b):
    try:
        c = a/b
        return c
    except MinhaExcecao as e:
        print("Ocorreu o seguinte erro: ",e)

#print(divide3(16,0))

from math import sqrt
#print(sqrt(-9))
def divide4(a,b):
    try:
        c = a/b
        return c
    except ZeroDivisionError: #Ficar atento pois o Exception é generico e geralmente vem primeiro
        print("Divisao por zero NÃO!")
    except ValueError:
        print("Erro de valor")
    except Exception:
        print("Vixi, a nota abaixo")
    finally:
        print("Opa cá estou finally")

divide4(10,4)
