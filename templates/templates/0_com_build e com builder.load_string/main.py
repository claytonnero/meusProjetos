"""

"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang.builder import Builder

Window.clearcolor = .3, .4, .6, 1

kv = """
<Rodando>:
    Label:
        text:"Deu Certo"
"""

class Rodando(BoxLayout):
    pass

class Roda(App):

    Builder.load_string(kv)

    def build(self):
        return Rodando()

if __name__ == "__main__":
    Roda().run()
