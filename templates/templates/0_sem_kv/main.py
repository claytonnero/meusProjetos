"""

"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor = .5, .5, .5, 1

class Rodando(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text = "Deu Certo"))

class Roda(App):
    def build(self):
        return Rodando()

if __name__ == "__main__":
    Roda().run()
