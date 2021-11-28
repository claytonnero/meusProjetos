"""1. Faça um Programa que peça dois números e imprima o maior deles.
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.clearcolor = 1,1,1,1

class Calcula(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None
        self.height = "50dp"
        
    def calcula(self, botao):
        num1 = self.ids.num1.text
        num2 = self.ids.num2.text
        result = 0
        
        if num1 > num2:
            result = num1
        else:
            result = num2
            
        self.ids.lab.text = "O maior numero é {}".format(result)
        
class Maior(App):
    pass
        
app = Maior()
app.run()    