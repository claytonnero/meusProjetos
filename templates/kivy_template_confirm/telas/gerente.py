from kivy.uix.screenmanager import ScreenManager as Sc
from telas.menu import Menu
from telas.tela import Tela

class Gerencia(Sc):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Menu(name="menu"))
        self.add_widget(Tela(name="tela"))