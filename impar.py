lista=[1,2,3,4,5]
final=0
for num in lista:
    for num2 in lista:
        if num<num2:
            final=final+num
        else:
            final=final
print(final)
