from kivy.app import App
from kivy.uix.label import Label

class Roda(App):
    def build(self):
        return Label(text="deu certo")

Roda().run()
