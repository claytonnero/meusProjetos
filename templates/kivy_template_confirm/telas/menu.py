from kivy.uix.button import Button
from kivy.lang import Builder 
from kivy.uix.screenmanager import Screen 

from kivy.core.audio import SoundLoader
from kivy.core.window import Window 

from uteis.confirm import Confirma

loc = "/storage/emulated/0/Music/sons/"

entSom = SoundLoader.load(loc+"bell.wav")

popSom = SoundLoader.load(loc+"pop.wav")

class Menu(Screen):
    
    Builder.load_file("kvs/menu.kv")
    
    pop = Confirma()
    
    def on_pre_enter(self):
        Window.bind(on_request_close=self.confirmacao)
        
    def confirmacao(self, *args, **kwargs):
        
        self.pop.open()
        global popSom
        popSom.play()
        return True
        
    def on_enter(self):
        global entSom
        entSom.play()