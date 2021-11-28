"""9. Faça um Programa que leia três números e mostre-os em ordem decrescente"""

from kivy.base import runTouchApp 
from kivy.core.window import Window 
from kivy.lang.builder import Builder 

Window.clearcolor = 1,.4,.6,1

runTouchApp(Builder.load_string("""
#:import f funcoes

<pop@Popup>:
    id:pop
    size_hint:None, None
    size:(300, 400)
    BoxLayout:
        Label:
            text:f.autor()    
            
FloatLayout:
    ActionBar:
        pos_hint:{"top":1}
    BoxLayout:
        orientation:"vertical"
        size_hint:None, None
        height:"80dp"
        width:"150dp"
        pos_hint:{"top":.7}
        pos:(150, 500)
        
        TextInput:
            id:num1
            #text:"0.0"
            size_hint:None, None
            height:"40dp"
            width:"250dp"
            multiline:False
            input_filter:"int"
            hint_text:"Digite o primeiro número"
        TextInput:
            id:num2
            #text:"0.0"
            size_hint:None, None
            height:"40dp"
            width:"250dp"
            multiline:False
            input_filter:"int"
            hint_text:"Digite o segundo número"
        TextInput:
            id:num3
            #text:"0.0"
            size_hint:None, None
            height:"40dp"
            width:"250dp"
            multiline:False
            input_filter:"int"
            hint_text:"Digite o terceiro número"
                        
    Label:
        id:lab
        text:"Resultado"
    Button:
        size_hint: .5, .1
        text:"calcula"
        pos:root.width/4, 1
        on_release:lab.text = 'Menor {} Médio {} Maior {}'.format(f.verifica(num1.text, num2.text, num3.text, tipo="maior"), f.verifica(num1.text, num2.text, num3.text, tipo="medio"), f.verifica(num1.text, num2.text, num3.text, tipo="menor"))

"""))

    