from kivy.lang import Builder 
from kivy.uix.screenmanager import Screen 

from kivy.core.audio import SoundLoader

import os
path = os.path.dirname(os.path.abspath(__file__))  

loc = "/storage/emulated/0/Music/sons/"

entSom = SoundLoader.load(loc+"bom.wav")

class Tela(Screen):
    
    Builder.load_file("kvs/tela.kv")
    
    def on_enter(self):
        global entSom
        entSom.play()
        
        