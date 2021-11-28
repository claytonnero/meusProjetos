# este é o quinto programa da lista de exercicios oficiais no site python Brasil ele converte metros em centímetros
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Converte(BoxLayout):
    pass
    def converte(self, Button):
        self.ids.lab.text = "{} centímetros".format(float(self.ids.ent.text)* 100)
    
class Conv(App):
    def build(self):        
        return Converte()
        
Conv().run()