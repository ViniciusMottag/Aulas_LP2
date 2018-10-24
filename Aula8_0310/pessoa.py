class Pessoa:
    def __init__(self,n,e,c):
        self.nome = n
        self.email = e
        self.celular = c
    def get_nome(self):
        return 'Caro(a) %s'% self.nome
    def get_email(self):
        return self.email
    def get_celular(self):
        return self.celular
    
    def set_nome(self,nome):
        self.nome = nome
    def set_email(self,email):
        self.email = email
    def set_celular(self,celular):
        self.celular =celular 

class Aluno(Pessoa): #Com isso voce herda a classe pessoa, não sendo necessário ficar repetindo
    def __init__(self,n,e,c,s,m,r,d=[]):
        super().__init__(n,e,c)
        self.sigla = s
        self.disciplinas = d
        self.mensalidade = m
        self.ra = r

    def __repr__(self):
        return 'Aluno: %s | Curso: %s | Disciplina: %s' % \
        (self.nome,self.sigla,self.disciplinas)
    
    def get_sigla(self):
        return '%c.%c.%c' % (self.sigla[0],self.sigla[1],self.sigla[2])
    
    def get_disciplinas(self):
        return self.disciplinas
    
    def get_mensalidade(self):
        return 'R$ %.2f' % self.mensalidade
    
    def get_ra(self):
        return self.ra
    def set_sigla(self,sigla):
        self.sigla = sigla
    def set_ra(self,ra):
        self.ra = ra
        
    def set_disciplinas(self,valor):
        self.disciplinas.append(valor)
        
class Professor(Pessoa):
    def __init__(self,n,e,c,v):
        super().__init__(n,e,c)
        #self.disciplinas = d
        self.valor_hora=float(v)

    def __repr__(self):
        return 'Prof: %s ' % \
        (self.nome)

    def get_nome(self): #Sobrecarga no metodo pois já existe na classe PESSOA E ELE SUBSCREVE
        return 'mestre: %s' % self.nome
        
    def get_valor_hora(self):
        return self.valor_hora
    
    def set_valor_hora(self,valor):
        self.valor = float(valor)
