from Televisao import Televisao

tv = Televisao()
print(tv.canal)
print(tv.ligada)
tv2 = Televisao()
print("Minha teve está ligada? ",tv.ligada)
tv2.ligada = True
print("Minha teve está ligada? ",tv2.ligada)
print("A cor da tv é: ",tv.cor)
print("Canal atual", tv.canal)
tv.aumenta_canal()
print("Canal atual", tv.canal)
tv.diminui_canal()
