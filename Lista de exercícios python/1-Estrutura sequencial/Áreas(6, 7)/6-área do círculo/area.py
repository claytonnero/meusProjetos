from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 

from math import pi

class Circulo(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def calcula(self, Button):
        
        raio = float(self.ids.ent.text)
        area = ((pi) * (raio * raio))
        self.ids.lab.text = "A área do círculo  é\n{:.2f}".format(area)
        self.ids.lab.font_size = 70
        
class Area(App):
    def build(self):
        return Circulo()
        
Area().run()