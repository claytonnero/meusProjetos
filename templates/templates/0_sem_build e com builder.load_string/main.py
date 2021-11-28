"""

"""
from kivy.base import runTouchApp
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang.builder import Builder

Window.clearcolor = 0, .6, .3, 1

kv = """
BoxLayout:
    Rodando:

<Rodando>:
    Label:
        text:"Deu Certo"
"""


class Rodando(BoxLayout):
    pass

runTouchApp(Builder.load_string(kv))
