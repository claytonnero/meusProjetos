#este é o quarto programa da lista de exercícios, ele tira a média entre 4 notas bimestrais
from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout

class Calcula(BoxLayout):
    def ___init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def media(self, Button):
            soma = int(self.ids.ent1.text) + int(self.ids.ent2.text) + int(self.ids.ent3.text) + int(self.ids.ent4.text)
            media = "{}".format(soma / 4)
            self.ids.lab.text = "a média entre as notas é {}".format(media)
            
class Media(App):
    def build(self):
        return Calcula()

Media().run()