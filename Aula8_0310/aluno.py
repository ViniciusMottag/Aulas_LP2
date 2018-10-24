#nome, celular, email, sigla,RA
class Aluno:
    def __init__(self,n,e,c,s,m,r):
        self.nome = n
        self.email = e
        self.celular = c
        self.sigla = s
        #self.disciplinas = d
        self.mensalidade = m
        self.ra = r

    def __repr__(self):
        return 'Aluno: %s | Curso: %s' % \
        (self.nome,self.sigla)

    def get_nome(self):
        return 'Mestre %s'% self.nome
    def get_email(self):
        return self.email
    def get_celular(self):
        return self.celular
    def get_sigla(self):
        return '%c.%c.%c' % (self.sigla[0],self.sigla[1],self.sigla[2])
    #def get_disciplinas(self):
        #return self.disciplinas
    def get_mensalidade(self):
        return 'R$ %.2f' % self.mensalidade
    def get_ra(self):
        return self.ra
    def set_nome(self,nome):
        self.nome = nome
    def set_email(self,email):
        self.email = email
    def set_celular(self,celular):
        self.celular = celular
    def set_sigla(self,sigla):
        self.sigla = sigla
    def set_ra(self,ra):
        self.ra = ra
    
class Professor:
    def __init__(self,n,e,c,v):
        self.nome = n
        self.email = e
        self.celular = c
        #self.disciplinas = d
        self.valor_hora=float(v)

    def __repr__(self):
        return 'Aluno: %s ' % \
        (self.nome)
    def get_nome(self):
        return 'Mestre %s'% self.nome
    def get_email(self):
        return self.email
    def get_celular(self):
        return self.celular
    def get_valor_hora(self):
        return self.valor_hora
    def set_nome(self,nome):
        self.nome = nome
    def set_email(self,email):
        self.email = email
    def set_celular(self,celular):
        self.celular = celular
    def set_valor_hora(self,valor):
        self.valor = float(valor)
