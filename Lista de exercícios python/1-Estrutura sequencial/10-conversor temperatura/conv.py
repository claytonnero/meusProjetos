from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 

class Faz(BoxLayout):
    pass

class Conv(App):
    def build(self):
        return Faz()
        
Conv().run()