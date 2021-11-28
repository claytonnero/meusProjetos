"""14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao
longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela
abaixo:
• Média de Aproveitamento Conceito
 Entre 9.0 e 10.0 A
 Entre 7.5 e 9.0 B
 Entre 6.0 e 7.5 C
 Entre 4.0 e 6.0 D
 Entre 4.0 e zero E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a
mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o
conceito for D ou E"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 
from kivy.core.window import Window 

Window.clearcolor = .6, .4, .7, 1

class Rodando(BoxLayout):
    
    def media(self, n1=0, n2=0):
        return (int(n1) + int(n2)) / 2
        
    def decide(self, num=0):
        
        if float(num) > 90.0:
           Window.clearcolor = 0, 1, 0, 1
           if float(num) <=100.0:
               sent = "Aprovado"
               conc = "A"
               lista = [sent, conc]
               return lista
               
        if float(num) > 75.0:
           Window.clearcolor = 0, .7, .4, 1
           if float(num) <= 90.0:
                sent = "Aprovado"
                conc = "B"
                lista = [sent, conc]
                return lista
       
        if float(num) > 60.0:
           if float(num) <= 75.0:
               sent = "Aprovado"
               conc = "C"
               lista = [sent, conc]
               return lista
               
        if float(num) > 40.0:
           Window.clearcolor = .8, .2, 0,1
           if float(num) <= 60.0:
               sent = "Reprovado"
               conc = "D"
               lista = [sent, conc]
               return lista
               
        if float(num) < 40.0:
           Window.clearcolor = 1,0,0,1
           if float(num) >= 0.0:
               sent = "Reprovado"
               conc = "E"
               lista = [sent, conc]
               return lista
              
    def apertado(self, botao):
        
        lab = self.ids.lab 
        nota1 = self.ids.ent.text
        nota2 = self.ids.ent1.text
        
        if nota1 == "":
            nota1 = 0
        if nota2 == "":
            nota2 = 0
        
        med = self.media(nota1, nota2)
        
        nota = self.decide(med)
        
        tela = """
        {}
                    
        Nota 1          {}
        Nota 2          {}
        Média           {}
        Conceito      {}
        """.format(nota[0], nota1, nota2, med, nota[1])
        
        lab.text = tela
        lab.font_size = 35

class Roda(App):
    def build(self):
        return Rodando()

Roda().run()