"""4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante"""

from kivy.app import App
from kivy.lang import Builder 
from kivy.uix.boxlayout import BoxLayout 
#from kivy.core.window import Window 

#Window.clearcolor= (0,1,0.6,1)

Builder.load_string("""
<Gira>:
    orientation:"vertical"
    Label:
        text:"Vogais ou consoantes"
        color:0,0,0,1
    TextInput:
        id:ent
        size_hint_y:None
        heigth:"30dp"
        multiline:False
        hint_text:"Digite uma letra"
    Widget:
    Label:
        id:lab
        text:"Resultado"
        font_size:35
        color:0,0,0,1
    Widget:  
    Button:
        text:"Calcula"
        on_release:root.apertado(self)
""")

class Gira(BoxLayout):
   def apertado(self, botao):
       
       vogais = ("a", "e", "i", "o", "u")
       
       texto = ""
       imp = self.ids.ent.text
       menor =imp.lower()
       
       if menor == "":
           texto = "Por favor, digite alguma letra"
       
       if menor.isalpha():
                        
           if menor  in vogais:
               texto = "A letra digitada é uma Vogal"
           else:
               if len(menor) > 1:
                   texto = "nao existe letra com mais de um caractere"
               else:    
                   texto = "A letra digitada é uma consoante"
       else:
           if menor.isalnum():
               texto = "O caractere digitado é alfanumérico"
           else:
               texto = "O caractere digitado nao faz parte do alfabeto"
                 
       self.ids.lab.text = texto
       
class App(App):
    def build(self):
        return Gira()
App().run()       
