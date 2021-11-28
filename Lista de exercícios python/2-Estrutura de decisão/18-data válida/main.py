"""18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é
uma data válida"""

from kivy.base import runTouchApp
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang.builder import Builder

Window.clearcolor = 0, .6, .3, 1

kv = """
BoxLayout:
    #orientation:"vertical"
    Rodando:

<Rodando>:
    orientation:"vertical"
    Label:
        id:lab
        canvas:
            Color:
                rgba:.2,1,1,.1
            Rectangle:
                size:self.size
                pos:self.pos
        text:"Deu Certo"
    GridLayout:
        cols:3
        size_hint_y:.2
        Widget:
            canvas:
                Color:
                    rgba:1,.3,1,.2
                Rectangle:
                    size:self.size
                    pos:self.pos
        TextInput:
            id:imp
            multiline:False
            hint_text:"Digite a data"
            size_hint_y:None
            height:"40dp"
            #input_filter:"int"
        Widget:
            canvas:
                Color:
                    rgba:1,1,.3,.1
                Rectangle:
                    size:self.size
                    pos:self.pos
    Widget:
        canvas:
            Color:
                rgba:1,1,1,.3
            Rectangle:
                size:self.size
                pos:self.pos
    GridLayout:
        cols:3
        size_hint_y:None
        height:"60dp"
        Widget:
        Button:
            on_release:root.solto(self)
            text:"calcule"
            background_color:1,0,0,1
        Widget:
"""

class Rodando(BoxLayout):
    
    def valido(self):
        entrada = self.ids.imp.text
        teste = entrada.replace("/", ",")
        return teste
        
    def solto(self, x):        
        self.ids.lab.text = str(type(self.valido()))
        self.ids.lab.color = 0,0,0,.3

runTouchApp(Builder.load_string(kv))