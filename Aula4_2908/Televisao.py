class Televisao:
    def __init__(self):
        self.ligada = False #Dado atributo ao metodo criado na classe televisão
        self.cor = 'black piano'
        self.canal = 6 
    def aumenta_canal(self):
        #tv = Televisao()
        #tv.canal +=1
        
        self.canal +=1
        print('Aumentar canal',self.canal)   


    def diminui_canal(self):
        #tv = Televisao()
        #tv.canal -=1
        self.canal -=1
        print('Diminuir canal',self.canal)
        

