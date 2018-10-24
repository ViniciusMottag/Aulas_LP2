# Esse é o nosso Façade
class Organizador_eventos:
    def __init__(self):
        print('Organizador: Falarei com o pessoal')

    def organizar(self):
        self.hoteleiro = Hoteleiro()
        self.hoteleiro.reserva_hotel()

        self.fornecedor = Fornecedor()
        self.fornecedor.set_cozinha()

        self.florista = Florista()
        self.florista.set_requisitor_flor()

        self.musico = Musico()
        self.musico.set_tipo_musica()

#Subsistema 1
class Hoteleiro:
    def __init__(self):
        print('Organizando o Hotel para um casamento? ')
    def __esta_disponivel(self):
        print('O hotel está livre para o evento este dia?')
        return True
    def reserva_hotel(self):
        if self.__esta_disponivel():
            print('Registrou a reserva')

#Subsistema 2
class Florista:
    def __init__(self):
        print('Decoração de flores para o evento?')
    def set_requisitor_flor(self):
        print('Rosas e lirios serão usadas')

#Subssistema 3

class Fornecedor:
    def __init__(self):
        print('Organização da comida para o evento?')
    def set_cozinha(self):
        print('Comida chinesa e regional sera servida')

#Subssitema 4

class Musico:
    def __init__(self):
        print('Organização de musica para o evento')
    def set_tipo_musica(self):
        print('Rock e musica pop sera tocada')

#Cliente
class Voce:
    def __init__(self):
        print('Voce é o responsável pelo casamento')
    def pergunte_organizador_eventos(self):
        print('Vamos ligar para o Organizador de Eventos')
        org_eventos = Organizador_eventos()
        org_eventos.organizar()
    
    def __del__(self):
        print('Obrigado organizar de eventos, deu tudo certo')

vc = Voce()
vc.pergunte_organizador_eventos()