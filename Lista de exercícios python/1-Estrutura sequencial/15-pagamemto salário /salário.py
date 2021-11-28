"""15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que
são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça
um programa que nos dê: 

• salário bruto. 

• quanto pagou ao INSS. 

• quanto pagou ao sindicato. 

• o salário líquido. 

• calcule os descontos e o salário líquido, conforme a tabela abaixo: 

+ Salário Bruto : R$

- IR (11%) : R$

- INSS (8%) : R$

- Sindicato ( 5%) : R$

= Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido."""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.clearcolor=(0,0,0.5,1)

class Recebimento(BoxLayout):            
    
    def salario(self, botao):
        
        self.lab = self.ids.lab.text
        self.horas = self.ids.horas.text
        self.valor = self.ids.valor.text
        self.butao = self.ids.but    
          
        if self.horas == "":
            self.horas = 0.0
        else:
            self.horas = float(self.horas)
            
        if self.valor == "":
            self.valor = 0.0
        else:
            self.valor = float(self.valor)
        
        salario = float(self.horas) * float(self.valor)
        imposto = (salario * 11) / 100
        inss = (salario * 8) / 100
        sindicato = (salario * 5) / 100
        salario_liquido = salario - imposto - inss - sindicato 
        
        
        self.tela = """
        Salário Bruto : R$ {:.2f}

        - IR (11%) : R$ {:.2f}

        - INSS (8%) : R$ {:.2f}

        - Sindicato ( 5%) : R$ {:.2f}

        = Salário Liquido : R$ {:.2f}
        """.format(salario, imposto, inss, sindicato, salario_liquido)
        self.ids.lab.text = self.tela
        
class Salario(App):
    def build(self):
        return Recebimento()
        
Salario().run()