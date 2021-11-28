from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

class Itens(BoxLayout):
    pass

class Pop(Popup):
    def itens(self):
        return Itens()

class Rodando(BoxLayout):
    
    def solto(self, botao):
        pop = Pop()
        pop.open()
    
class Roda(App):
    def build(self):
        return Rodando()

Roda().run()              