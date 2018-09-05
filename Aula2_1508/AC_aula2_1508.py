
def dicionario(f):
    dicionario_final={}
    for letra in frase:
        if letra in dicionario_final:
            dicionario_final[letra] +=1
        else:
            dicionario_final[letra] =1
    return dicionario_final
    
frase = input('frase: ')
print(dicionario(frase))
    
