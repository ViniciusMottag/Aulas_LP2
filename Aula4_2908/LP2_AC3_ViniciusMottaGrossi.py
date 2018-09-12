'''
╔══════════════════════════════════════════════════════════════════════════════╗
║ Instituição   :  Faculdade Impacta Tecnologia                                ║
║ Curso         :  Análise e Desenvolvimento de Sistemas                       ║
║ Disciplina    :  Linguagem de Programação 2                                  ║
║ Turma         :  2A (manhã)                                                  ║
║ Professor     :  Lucio Nunes de Lira                                         ║
║ Aluno         :  Vinicius Motta Grossi                                       ║
║ Matrícula     :  -------                                                     ║
║ Entrega       :  05/09/2018                                                  ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ Programa      :  AC3 (Classes, objetos, atributos e métodos)                 ║
╚══════════════════════════════════════════════════════════════════════════════╝
'''

'''
────────────────────────────────────────────────────────────────────────────────
Crie a classe Aluno com os seguintes atributos:
    - Nome      (string)
    - Matrícula (int)
    - Média     (real)
    - Faltas    (int)
e com os seguintes métodos:
    - def __init__(<apenas com o parâmetro self>)
    - def aprovado(<apenas com o parâmetro self>)
      devolve um valor booleano indicando se o aluno
      está aprovado com base na nota e no número de faltas.
    - abona_faltas(<Com o parâmetro self e o número N de faltas abonadas>)
      remove N faltas do aluno (considere que não ficará negativo).
────────────────────────────────────────────────────────────────────────────────
'''

class Aluno:
    def __init__(self,mediaac=None,mediaprova=None):
        self.nome = 'Vinicius'
        self.matricula = 173801
        self.media = 6.0
        self.faltas = 7
    def aprovado(self):
        #if self.media >=6 and self.faltas <=4:
            #return True
        #else:
            #return False
        return self.media >=6 and self.faltas <=4  #Retorna True ou False Bol
    def abona_faltas(self,n):
        self.faltas -=n
        if self.faltas >0:
            print(self.faltas)
        else:
            print(0)

valores = Aluno()
print('Aprovado: ',valores.aprovado())
n = int(input('Quantas faltas abonadas?: '))
valor = valores.abona_faltas(n)
print('Faltas abonadas: ',n,'Faltas atual:',valor,'Aluno aprovado?',valores.aprovado())