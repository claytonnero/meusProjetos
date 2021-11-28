"""17. Faça um Programa que peça um número correspondente a um determinado ano e em seguida
informe se este ano é ou não bissexto.
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button 
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder

Window.clearcolor = .3, .4, .6, 1

kv = """
<Rodando>:
    orientation:"vertical"
    padding:20
    Label:
        id:lab
        text:"Deu Certo"
    TextInput:
        id:ent
        size_hint_y:None
        height:"40dp"
        hint_text:"Digite o ano a ser verificado"
        input_filter:"int"    
        multiline:False           
    Widget:                    
    GridLayout:
        size_hint_y:None
        height:"60dp"
        cols:3
        Widget:
        Button:
            text:"Calcular"
            on_release:root.apertado(self)
        Widget:            
"""

class Rodando(BoxLayout):
    
    def bisexto(self, ano):
        if int(ano) % 4 == 0:
            if int(ano) % 100 != 0:
                Window.clearcolor = 0,0,1,1
                return "{} é Bisexto".format(ano)
            if int(ano) % 400 == 0:
                self.ids.lab.color = 0,0,0,1
              
                Window.clearcolor = 0,1,0,1
                return "{} é Bisexto".format(ano)
            else:
                return "{} não é Bisexto".format(ano)
        else:
            Window.clearcolor = 1,0,0,1
            return "{} não é bisexto".format(ano)
            
    def apertado(self, x):
                   
        lab = self.ids.lab
        ent = self.ids.ent.text
        
        if ent == "":
            ent = 0
        resp = self.bisexto(ent)
        
        lab.text = str(resp)
        
class Roda(App):

    Builder.load_string(kv)

    def build(self):
        return Rodando()

if __name__ == "__main__":
    Roda().run()