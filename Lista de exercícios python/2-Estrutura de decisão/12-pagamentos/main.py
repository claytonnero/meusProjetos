"""12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são
do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o
Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a
empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas
no mês. 

• Desconto do IR: 

• Salário Bruto até 900 (inclusive) - isento 

• Salário Bruto até 1500 (inclusive) - desconto de 5% 

• Salário Bruto até 2500 (inclusive) - desconto de 10% 

• Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações
"""
 
from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout 
from kivy.core.window import Window 
import random

class Girando(BoxLayout):
       
    def cinco(self, salario):
       return (salario * 5) / 100
    
    def dez(self, salario):
        return (salario * 10) / 100
    
    def vinte(self, salario):
        return (salario * 20) / 100
        
    def solto(self, botao):
        
        hor = self.ids.preco.text
        tem = self.ids.tempo.text
        
        if not hor:
            hor = 0.0
        if not tem:
            tem = 0.0
            
        salario = int(hor) * float(tem)
        
        sind = (salario * 3) / 100
        fgts = (salario * 11) / 100

        ir = ""
        total_d = ""
        
        if salario > 0 and salario <= 900:
            ir = 0.0
            total_d = "{}".format(sind)
            Window.clearcolor = 0, 1, 0, 1
            
        if salario > 900 and salario <= 1500:
            Window.clearcolor = 1,1,1,1
            self.ids.lab.color = 0,0,0,1
            self.ids.nome.color = 0,0,0,1
            self.ids.nome.text = "5% de desconto"
            desc = self.cinco(salario)
            ir = "{}".format(self.cinco(salario))
            total_d = desc + sind
        
        if salario > 1500 and salario <= 2500:
            Window.clearcolor = random.random(),0,random.random(),1
            desc = self.dez(salario)
            ir = "{}".format(self.dez(salario))
            total_d = desc + sind
            self.ids.nome.text = "10% de desconto"
            
        if salario > 2500:
            Window.clearcolor = 1, random.random(), random.random(),1
            desc = self.vinte(salario)
            ir = "{}".format(self.vinte(salario))
            total_d = desc + sind
            self.ids.nome.text = "20% de desconto"
        
        else:
            if salario == 0:
                self.ids.lab.text = "Insira um valor"
                return
           
        tela = """
        Salário bruto                  R$   {:.2f}
        -IR                                    R$  {}
        -Sindicato 3%                 R$ {}
        Fgts 11% (isento)          R$ {}
        Total de descontos       R$ {}
        Salário líquido                R$ {:.2f}
        """.format(salario, ir, sind, fgts, total_d, (salario - float(total_d)))
        self.ids.lab.text = tela

class Gira(App):
    def build(self):
        return Girando()
Gira().run()        