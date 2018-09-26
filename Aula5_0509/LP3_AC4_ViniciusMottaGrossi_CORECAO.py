'''
╔══════════════════════════════════════════════════════════════════════════════╗
║ Instituição   :  Faculdade Impacta Tecnologia                                ║
║ Curso         :  Análise e Desenvolvimento de Sistemas                       ║
║ Disciplina    :  Linguagem de Programação 2                                  ║
║ Turma         :  2A (manhã)                                                  ║
║ Professor     :  Lucio Nunes de Lira                                         ║
║ Aluno         :  Vinicius Motta Grossi                                       ║
║ Matrícula     :  1800842                                                     ║
║ Entrega       :  07/09/2018                                                  ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ Programa      :  AC4 (construtor com parâmetros default, atributos privados, ║
║                  métodos get() e set()).                                     ║
╚══════════════════════════════════════════════════════════════════════════════╝
'''

'''
────────────────────────────────────────────────────────────────────────────────
Com base no arquivo criado na AC3, faça o que se pede a seguir:

Faça com que a classe Aluno fique com os seguintes atributos:
    - Nome          (string) - público
    - Matrícula     (int)    - público
    - Nota de AC    (float)  - público
    - Nota de Prova (float)  - público
    - Média         (float)  - privado
    - Faltas        (int)    - privado

Faça com que a classe Aluno fique com os seguintes métodos:
    - def __init__(Parâmetro "self" e parâmetros para todos os atributos
                   definidos, exceto "média", e com "Nota de AC", "Nota de
                   Prova" e "Faltas" com valor default zerado).
                   Obs.: Todos os atributos definidos em __init__ devem ser
                   inicializados com os valores dos parâmetros, exceto a média
                   que será inicializada com a fórmula 60% nota de AC + 40%
                   nota de prova.
    - def aprovado(<apenas com o parâmetro self>)
                   Devolve um valor booleano indicando se o aluno está aprovado
                   com base na média, que deve ser maior ou igual a 6, e
                   faltas, que deve ser menor ou igual a 4.
    - def abona_faltas(<com o parâmetro self e o número N de faltas abonadas>)
                   Reduz as faltas do aluno em N unidades, se for possível.
                   Caso o valor de N seja superior ao número de faltas do aluno,
                   não reduzir e exibir uma mensagem indicando a falha.
    - def get_media(<apenas com o parâmetro self>)
                   Devolve a média do aluno.
    - def get_faltas(<apenas com o parâmetro self>)
                   Devolve o número de faltas do aluno.

Faça os seguintes testes no programa principal:
    a) Crie um objeto aluno passando os dados como parâmetros, exceto os default;
    b) Altere o nome;
    c) Abone um número de faltas;
    d) Exiba a média;
    e) Exiba a quantidade de faltas;
    f) Exiba a situação de aprovação do aluno;
    g) Abone um número de faltas de modo que garanta aprovação;
    h) Altere a nota de AC e a nota de prova de modo que garantam aprovação;
    i) Repita as instruções d), e) e f);
    j) Entenda o que aconteceu, será indagado em aula.
────────────────────────────────────────────────────────────────────────────────
'''
class Aluno:
    def __init__(self,nome,matricula,notaac=0,notaprova=0,faltas=0):
        self.Nome = nome
        self.Matricula = matricula
        self.NotaAC = notaac
        self.NotaProva = notaprova
        self.__Media = self.NotaAC*0.6+self.NotaProva*0.4
        self.__Faltas = faltas
    def aprovado(self):
        if self.__Media >=6 and self.__Faltas <=4:
            return True
        else:
            return False
    def abona_faltas(self,n):
        if n <= self.__Faltas:
            self.__Faltas -=n
            return self.__Faltas
        else:
            print('Numero de faltas superior existente')
    def get_media(self):
        return  self.__Media

    def get_faltas(self):
        return self.__Faltas
    def set_Nota_AC(self,n):
        self.NotaAC=n
        self.__Media=self.NotaAC*0.6+self.NotaProva*0.4
        
    def set_Nota_Prova(self,n):
        self.NotaProva=n
        self.__Media=self.NotaAC*0.6+self.NotaProva*0.4
    def set_faltas(self,n):
        self.__Faltas=n

#A)
aluno = Aluno('Vinicius',123121)#Mantendo os default 0

#B)
aluno.Nome = 'Alexandre'

#C)
aluno.abona_faltas(10)

#D)
print('Media: ',aluno.get_media())

#E)
print('Faltas: ',aluno.get_faltas())

#F)
print('Aprovado: ',aluno.aprovado())

#G)
aluno.set_Nota_AC(8)
aluno.set_Nota_Prova(8)
aluno.set_faltas(4)

#H)
print('Media: ',aluno.get_media())

#I)
print('Faltas: ',aluno.get_faltas())
print('Aprovado: ',aluno.aprovado())







