"""8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato"""

from kivy.base import runTouchApp
from kivy.core.window import Window
from kivy.lang.builder import Builder 

Window.clearcolor = 1, .5, 1, 1

runTouchApp(Builder.load_string("""
#:import f func

#:set azul 0,0,1,1
#:set vermelho 1,0,0,1

BoxLayout:
    orientation:"vertical"
    BoxLayout:
        Label:
            id:lab
            text:"Resultado"
            font_size:35
            color:vermelho
    GridLayout:
        cols:3
        padding:20
        spacing:10
        TextInput:
            id:valor1
            text:"0.0"
            multiline:False 
            input_filter:"float"
            hint_text:"primeiro valor"
            size_hint_y:None
            height:"40dp"            
        TextInput:
            id:valor2
            text:"0.0"
            multiline:False 
            input_filter:"float"
            hint_text:"segundo valor"
            size_hint_y:None
            height:"40dp"
        TextInput:
            id:valor3
            text:"0.0"
            multiline:False 
            input_filter:"float"
            hint_text:"terceiro valor"
            size_hint_y:None
            height:"40dp"              
    GridLayout:
        cols:3
        padding:20
        Widget:
        Button:
            text:"Calcule"
            size_hint:None, None
            height:"60dp"
            width:"100dp"
            on_release:lab.text = "{} é o menor número".format(f.economiza(valor1.text, valor2.text, valor3.text))
        Widget:
"""))