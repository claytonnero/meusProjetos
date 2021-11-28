"""5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve
calcular a média alcançada por aluno e apresentar: 
• A mensagem "Aprovado", se a média alcançada for maior ou igual a sete; 
• A mensagem "Reprovado", se a média for menor do que sete; 
• A mensagem "Aprovado com Distinção", se a média for igual a dez"""

from kivy.app import App 
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.clearcolor = 1,1,0,1

kv = Builder.load_string("""
<Rodando>:
    orientation:"vertical"
    padding:("20dp", "30dp")
    
    Label:
        text:"Media e Aprovaçao"
        color:0,0,0,1
        
    Widget:
        
    TextInput:
        id:nota1
        hint_text:"Nota 1"
        size_hint_y:None
        height:"40dp"
        input_filter:"float"
        
    TextInput:       
        id:nota2
        hint_text:"Nota 2"
        size_hint_y:None
        height:"40dp"
        input_filter:"float"
        
    Widget:
        
    Label:
        id:lab
        text:"Resultado"
        color:0,0,0,1
        
    Widget:
        
    Button:
        text:"Calcula"
        on_release:root.apertado(self)
        size_hint_y:None
        height:"60dp"
""")

class Rodando(BoxLayout):
        
    def apertado(self, botao):
        
        nota1 = self.ids.nota1.text.lower()
        nota2 = self.ids.nota2.text
        res = self.ids.lab.text
        
        msn = ""
        
        if nota1 == "":
            nota1 = 0.01
        if nota2 == "":
            nota2 = 0.01
            
        media = (float(nota1) + float(nota2)) / 2
        
        if media <= 70:
            msn = "Reprovado"
            Window.clearcolor = 1,0,0,1
        
        if media > 70 and media < 100 :
            msn = "Aprovado" 
            Window.clearcolor = 0,0,1,1   
        
        if media >= 100:
            msn = "Aprovado com destinção"
            Window.clearcolor = 0,1,0,1
            
        tela = """
        A média é  {}
        
        
        O aluno foi  {}
        """.format(media, msn)        
        self.ids.lab.text = tela

class Roda(App):
    kv
    def build(self):
        return Rodando()
    
Roda().run()