from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 

class Acontece(BoxLayout):
    
    def calcula(self, Button):
        
        ent1 = int(self.ids.ent1.text)
        ent2 = int(self.ids.ent2.text)
        ent3 = float(self.ids.ent3.text)
        
        solução1 = (2*ent1) + (ent2 / 2)
        solução2 = (3 * ent1) + ent3
        solução3 = ent3 ** 3
        
        str1 = "O dobro de {} + 1/2 de {} é {}".format(ent1, ent2, solução1)
        str2 = "A soma do triplo de {} + {} é {}".format(ent1, ent3, solução2)
        str3 = "{} elevado ao cubo é {:.2f}".format(ent3, solução3)
        
        letras = """
        {}
        {}
        {}
        """.format(str1, str2, str3)
        self.ids.lab.text = letras

class Calcula(App):
    def build(self):
        return Acontece()
Calcula().run()