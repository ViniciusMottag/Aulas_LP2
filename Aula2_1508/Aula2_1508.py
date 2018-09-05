dic = {123 :"Jade",1234:"Paola",12345:"Alexandre"}

print(len(dic))
print(dic)

dic[123] = "vinicius" #altera valor do 123 para aaa
print(dic)


dic['a']= 1

del dic[123] #deleta o 123
print(dic)
print("123 não está em dic = ",123 in dic) #verificar se o 123 está em dic // not in para verificar se NÃO está.

if 123 not in dic:
    print('Não está')
else:
    print(dic[123])

for chave,valor in dic.items():
    print(chave,valor)