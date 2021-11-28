"""11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e
lhe contraram para desenvolver o programa que calculará os reajustes. 
• Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
seguinte critério, baseado no salário atual: 
• salários até R$ 280,00 (incluindo) : aumento de 20% 
• salários entre R$ 280,00 e R$ 700,00 : aumento de 15% 
• salários entre R$ 700,00 e R$ 1500,00 : aumento de 10% 
• salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado,
informe na tela: 
• o salário antes do reajuste; 
• o percentual de aumento aplicado; 
• o valor do aumento; 
• o novo salário, após o aumento"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window 
import random as ran

cor = ran.random(), ran.random(), ran.random(), 1

Window.clearcolor = cor

class Rodando(BoxLayout):
   
    def apertado(self, botao):
        
        Window.clearcolor = cor
        self.sal = self.ids.sal.text
        self.res = self.ids.lab
        
        if self.sal == "":
            self.sal = 0
        
        self.sal = int(self.sal)

        salario = 0
        self.perc = 5

        if self.sal > 0 and self.sal <= 280:
            salario = self.duz()
            self.ids.lab1.text = ""
            Window.clearcolor = .7, 0, .3, 1

        elif self.sal > 280 and self.sal <= 700:
            salario = self.sete()
            self.ids.lab1.text = ""
            Window.clearcolor = .2, .4, .3, 1
        
        elif self.sal > 700 and self.sal <= 1500:
            salario = self.mil()
            self.ids.lab1.text = ""
            

        else:
            
            if self.sal == 0:
                self.perc = 0
                self.ids.lab1.text = "Zerado"
                self.ids.lab1.color = cor
            else:
                self.ids.lab1.text = ""
                Window.clearcolor = 1,1,1,1
            
            salario = self.acima()
            Window.clearcolor = 0,.7,1,1
            
            if self.sal > 5000:
                Window.clearcolor = 1, .5, 1, 1
                self.ids.lab1.text = "Nossa como você é salarudo!"
                self.ids.lab1.color = cor
                self.ids.lab1.font_size = 40
        
        tela = """
        salario Atual            {:>12}
        Percentual de aumento    {:>2}% 
        Valor do aumento         {:>8}
        salario Final            {:>15}
        """.format(self.sal, self.perc, self.porc(self.sal, self.perc), self.sal+self.porc(self.sal, self.perc))

        self.res.text = tela
        
    def porc(self, total, quant):
        return (total * quant) / 100
    
    def duz(self):
        self.perc = 20
        return float(self.porc(self.sal, 20))
    
    def sete(self):
        self.perc = 15
        return float(self.porc(self.sal, 15))
          
    def mil(self):
        self.perc = 10
        return float(self.porc(self.sal, 10))
           
    def acima(self):
        self.perc = 5
        return float(self.porc(self.sal, 5))
        
class Roda(App):
    def build(self):
        return Rodando()
        
Roda().run()
