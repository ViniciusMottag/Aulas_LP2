'''
════════════════════════════════════════════════════════════════════════════════
 Instituição   :  Faculdade Impacta Tecnologia
 Curso         :  Análise e Desenvolvimento de Sistemas
 Disciplina    :  Linguagem de Programação 2
 Turma         :  2A (manhã)
 Professor     :  Lucio Nunes de Lira
 Aluno (1)     :  
 Aluno (2)     :  
 Matrícula (1) :  
 Matrícula (2) :  
 Entrega       :  10/10/2018
════════════════════════════════════════════════════════════════════════════════
 Programa      :  AC7 (Herança e polimorfismo)
════════════════════════════════════════════════════════════════════════════════
'''

'''
────────────────────────────────────────────────────────────────────────────────
Com base no arquivo gerado nas aulas de 03/10/2018, 10/10/2018 e na codificação 
a seguir, faça o que se pede:

1) Crie os métodos get() e set() para os atributos da classe disciplina.
2) Crie os métodos get_disciplina() e set_disciplina() para adicionar uma
   disciplina para um aluno.
   Obs.: Note que o atributo do set_disciplina() é um objeto do tipo Disciplina;
3) Coloque alguns testes criando disciplinas e alunos que recebem essas discipl-
   nas.

ATENÇÃO: (a) Os códigos deste arquivo não deverão ser apagados, suas instruções
         devem ser colocadas e adaptadas ao código já existente.
────────────────────────────────────────────────────────────────────────────────
'''

class Pessoa:
    def __init__(self, n, e, c):
        self.nome = n
        self.email = e
        self.celular = c

    def get_nome(self):
        return 'caro(a) %s' % self.nome
    def get_email(self):
        return self.email
    def get_celular(self):
        return self.celular

    def set_nome(self, nome):
        self.nome = nome
    def set_email(self, email):
        self.email = email
    def set_celular(self, celular):
        self.celular = celular

class Aluno(Pessoa):
    def __init__(self, n, e, c, s, m, r, d=[]):
        super().__init__(n, e, c)
        self.sigla = s
        self.disciplinas = d
        self.mensalidade = m
        self.ra = r

    def __repr__(self):
        return 'Aluno: %s | Sigla: %s | Disciplina: %s' % \
               (self.nome,self.sigla,self.disciplinas)

    # "GETANDO" OS ATRIBUTOS (DEVOLVENDO OS VALORES DELES).
    def get_sigla(self):
        return '%c.%c.%c.' % (self.sigla[0],\
                              self.sigla[1],\
                              self.sigla[2])
    def get_mensalidade(self):
        return 'R$ %.2f' % self.mensalidade
    def get_ra(self):
        return self.ra
    def get_disciplinas(self):
        # devolva as disciplinas (a lista delas)
        return self.disciplinas
    # "SETANDO" OS ATRIBUTOS (DANDO VALOR A ELES).
    def set_sigla(self, sigla):
        self.sigla = sigla
    def set_mensalidade(self, mensalidade):
        self.mensalidade = mensalidade
    def set_ra(self, ra):
        self.ra = ra
    def set_disciplinas(self, nova):
        # coloque um append para as disciplinas
        self.disciplinas.append(nova)
        print(self.disciplinas,'\n')
    # n (string) | c (inteiro)

class Disciplina:
    def __init__(self, n, c):
        self.nome = str(n)
        self.carga = int(c)

    def __repr__(self):
        return 'Curso: %s | Carga horaria: %s' % \
               (self.nome,self.carga)
    
    def get_nome(self):
        return get_nome
    def get_carga(self):
        return get_carga
    def set_nome(self, n):
        self.nome = n
    def set_carga(self, c):
        self.carga = c


d1 = Disciplina('IOT',80) #Criando a disciplina e atribuindo a variavel d1
d2 = Disciplina('Matematica Aplicatica',120)

aluno = Aluno('Maria','m@g.com',1234514,'ADS',123.00,12312455) #instanciando a classe Aluno 
print('ANTES ==== ',aluno) #apresentando o objeto instanciado com o representation 
aluno.set_disciplinas(d1) #Incluindo a disciplina da variavel d1 ao objeto instanciado aluno
aluno.set_disciplinas(d2)

print ('DEPOIS ====',aluno) #apresentando o objeto instanciado com a disciplina incluida





 
