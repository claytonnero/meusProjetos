"""
16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros

quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3

metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.

Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout 
from kivy.core.window import Window 

Window.clearcolor=(.2,.75,.976,1)

class Pintura(BoxLayout):
    
    def calcula(self, Button):
        
        alt = self.ids.altura.text
        larg = self.ids.largura.text
        lab = self.ids.lab
        
        if larg == "":
            larg = 0.0
        else:
            larg = float(larg)
        
        if alt == "":
            alt = 0.0
        else:
            alt = float(alt)
        
        area = alt * larg
        cobertura = 18 * 3
        resultado = area // cobertura
        preco = resultado * 80
        sobra = area % cobertura
        if sobra != 0:
            resultado += 1
            preco = resultado * 80
        else:
            resultado = resultado
        
        tela = """
        
Para pintar uma área de {:.2f} \n    metros quadrados 
        
Precisará de de {:.2f} latas \n    de tinta de 18 litros
        
E isso lhe custará \n    R${:.2f} Reais

Obrigado pela preferência
        
        """.format(area, resultado, preco)
        lab.text = tela
        

class Tinta(App):
    def build(self):
        return Pintura()

Tinta().run()