"""3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra
escrever: F - Feminino, M - Masculino, Sexo Inválido"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window 

Window.clearcolor = 1, 1, 0,1

class Roda(BoxLayout):
    
    def apertado(self, botao):
       
        ent = self.ids.ent.text
        min = ent.lower()
        
        fem = ["f", "mulher", "fêmea", "femea", "ela"]
        mach = ["h", "m","macho", "ele", "homem"]
        
        m = "Sexo Femenino"
        h = "Sexo Mascolino"
        
        resp = ""
        
        if min in fem:
            resp = m
            Window.clearcolor = 1,0,0,1
        if min in mach:
            resp = h
            Window.clearcolor = 0,0,1,1
        if resp == "":
            resp = "Sexo Inválido"
            Window.clearcolor = 0,0,0,1
        
        self.ids.lab.text = resp
        

class App(App):
    def build(self):
        return Roda()
        
App().run()        