"""2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 
from kivy.core.window import Window 

Window.clearcolor = (0,0,1,1)

class Rodando(BoxLayout):
    
    def apertado(self, botao):
        num = self.ids.ent.text
        nota = ""
        if num == "":
            num = 0
        if float(num) < 0:
            nota = "{} é negativo".format(num)
            Window.clearcolor = (1,0,0,1)
        else:
            nota = "{} é positivo".format(num)
            Window.clearcolor = (0,1,0,1)
            self.ids.lab.color = (0,0,0,1)
        
        self.ids.lab.text = nota
        
class Roda(App):
    def build(self):
        return Rodando()

Roda().run()