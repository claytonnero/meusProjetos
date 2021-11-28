"""10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou
V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa
Noite!" ou "Valor Inválido!", conforme o caso"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 
from kivy.core.window import Window 

class Rodando(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def manha(self):
        self.ids.lab.text = "Bommmm Diiiiiiiaaaa!"
        
    def tarde(self):
        self.ids.lab.text = "Boa tarde, pode fazer calor hein!"   
    
    def noite(self):
        self.ids.lab.text = "Boa noite, leva um casaco??"
    def outro(self):
        self.ids.lab.text = "Este valor é inválido"
        
class Roda(App):
    
    def build(self):
        return Rodando()
        
Roda().run()