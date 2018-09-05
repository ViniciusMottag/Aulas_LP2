class Televisao:
    def __init__(self,mini=None,maxi=None):#metodo __init__ reservado
        self.ligada= False
        self.canal= 2
        if mini !=None:
            self.__cmini = mini
        if maxi != None:
            self.__cmaxi = maxi
    def get_cmini(self):#metodo cmini que retorna um valor reservado para o principal
        return self.__cmini

tv_sala = Televisao(2,50)
tv_sala.__cmini = 777
#print('Minimo',tv_sala.__cmini)#cmini com o __ ficou reservado, logo é possível usar fora da classe
print('Minimo',tv_sala.get_cmini())#usando o metodo que puxa o valor reservado
#print('Máximo',tv_sala.cmaxi)#cmini com o __ ficou reservado, logo é possível usar fora da classe

tv_quarto = Televisao(1,180)
#print('Minimo',tv_quarto.cmini)
#print('Máximo',tv_quarto.cmaxi)
