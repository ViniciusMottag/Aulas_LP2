#nome, celular, email, sigla,RA
class Aluno:
    def __init__(self,n,e,c,s,m):
        self.nome = n
        self.email = e
        self.celular = c
        self.sigla = s
        #self.disciplinas = d
        self.mensalidade = m

    def __repr__(self):
        return 'Nome: %s | Curso: %s' % \
        (self.nome,self.sigla)

    def get_nome(self):
        return 'Meste %s'% self.nome
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
    def set_nome(self,nome):
        self.nome = nome
    def set_email(self,email):
        self.email = email
    def set_celular(self,celular):
        self.celular = celular
    def set_sigla(self,sigla):
        self.sigla = sigla
    
a = Aluno('Jô','jo@gmail.com',190,'ADS',630)
print(a)
