"""

"""
from kivy.base import runTouchApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

Window.clearcolor = 0, .6, .3, 1

class Rodando(BoxLayout):
    pass

kv = """
BoxLayout:
    Rodando:

<Rodando>:
    Label:
        text:"Deu Certo"
"""
runTouchApp(Builder.load_string(kv))
