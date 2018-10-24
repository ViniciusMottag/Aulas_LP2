class Pessoa:
    def __init__(self, nome, email, celular):
        self.nome = nome
        self.email = email
        self.celular = celular

    def get_nome(self):
        return f"Caro(a) {self.nome}"
    def get_email(self):
        return(self.email)
    def get_celular(self):
        return(self.celular)

    def set_nome(self, nome):
        self.nome = nome
    def set_email(self, email):
        self.email = email
    def set_celular(self, celular):
        self.celular = celular

class Aluno(Pessoa):
    def __init__(self, nome, email, celular, sigla, m, r, d=[]):
        super().__init__(nome, email, celular)
        self.sigla = sigla
        self.mensalidade = m
        self.ra = r
        self.disciplina = d

    def __repr__(self):
        return 'Aluno: %s | Curso: %s' %(self.nome,self.sigla)

###Getando os atrigutos  (Devolvendo os valores deles)

    def get_sigla(self):
        return(f"{self.sigla[0]},{self.sigla[1]},{self.sigla[2]}")

    def get_mensalidade(self):
        return 'R$ %.2f' %self.mensalidade

    def get_ra(self):
        return self.ra
    
    def get_disciplina(self):
        return self.disciplina
    
#### setando os atributos ( Dando valor a eles.)
    def set_disciplina(self, m):
        self.disciplina.append(m)

    def set_mensalidade(self, mensalidade):
        self.mensalidade = mensalidade

    def set_sigla(self, sigla):
        self.sigla = sigla
    
    def set_ra(self, ra):
        self.ra = ra

class Professor(Pessoa):
    def __init__(self, nome, email, celular, v):
        super().__init__(nome, email, celular)
        self.valor_hora = float(v)

    def __repr__(self):
        return 'Prof: %s ' %(self.nome)
    
    def get_nome(self):
        return f"Mestre {self.nome}"

    def get_valor_hora(self):
        return self.valor_hora    
   
    def set_valor_hora(self, valor):
        self.valor_hora = float(valor)


aluno = Aluno("tuiu","tuius@hotmail.com",11961015070,"ADS",690.00,1800648)
print(aluno)
print(aluno.get_nome())
aluno.set_nome("Ricardo Martins")
print(aluno.get_nome())


aluno1 = Aluno("tuiu","tuius@hotmail.com",11961015070,"ADS",690.00,1800648,["logica","matematica"])
print(aluno1.get_disciplina())
aluno1.set_disciplina("aleluia")
print(aluno1.get_disciplina())


prof = Professor("ilana","ilana@gmail.com",156,150)
print (prof)
print(prof.get_nome())
