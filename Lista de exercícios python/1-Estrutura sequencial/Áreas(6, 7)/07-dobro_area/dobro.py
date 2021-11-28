#este é o  sétimo programa da lista de exercicios oficiais

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Area(BoxLayout):
    pass

class Dobro(App):
    def build(self):
        return Area()

Dobro().run()