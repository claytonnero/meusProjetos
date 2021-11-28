"""6. Faça um Programa que leia três números e mostre o maior deles."""

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang.builder import Builder 
from kivy.core.window import Window 

Window.clearcolor = 0,1,1,1
kv = """
<Rodando>:
    
    TextInput:
        id:num1
        size_hint:None, None
        height:"40dp"
        width:"80dp"
        hint_text:"numero 1"
        pos:(300, 900)
        input_filter:"int"
    TextInput:
        id:num2
        size_hint:None, None
        height:"40dp"
        width:"80dp"
        hint_text:"numero 2"
        pos:(300, 800)
        input_filter:"int"
    TextInput:
        id:num3
        size_hint:None, None
        height:"40dp"
        width:"80dp"
        hint_text:"numero 3"
        pos:(300, 700)
        input_filter:"int"
        
    Label:
        id:lab
        text:"Resultado"
        pos:(20, 600)
        color:0,0,0,1
        font_size:30
        
    Button:
        text:"Verifica"
        size_hint:None, None
        height:"60dp"
        width:"80dp"
        pos:(300, 100)
        on_release:root.apertado(self)
"""
class  Rodando(FloatLayout):
    
    def processa(self, x, y, z):
        
        if x > y:
            if x > z:
                return "O {} é o maior número".format(x)
            else:
                return "{} é o maior número digitado".format(z)
        
        elif y > x:
            if y > z:
                return "Sim {} é o número maior".format(y)
            else:
                return "{} é o maior".format(z)
                
        elif z > x:
            if z > y:
                return "Neste caso, {} é o maior número".format(z)
            else:
                return "{} é maior".format(y)
        else:
            return "Os números são iguais"
    
    def apertado(self, botao):
        
        num1 = int(self.ids.num1.text)
        num2 = int(self.ids.num2.text)
        num3 = int(self.ids.num3.text)
        
        if num1 == "":
            num1 = 0
        if num2 == "":
            num2 = 0
        if num3 == "":
            num3 = 0.0
            
        tela = self.processa(num1, num2, num3)
            
        self.ids.lab.text = tela

class Roda(App):
    
    Builder.load_string(kv)
    
    def build(self):
        return Rodando()

Roda().run()   