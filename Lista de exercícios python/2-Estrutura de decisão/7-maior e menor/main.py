"""
7. Faça um Programa que leia três números e mostre o maior e o menor deles.
"""
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
from kivy.lang.builder import Builder 

Window.clearcolor = 1, 0.6, 1, 1

class Rodando(AnchorLayout):
    
    def menor(self, num1, num2, num3):
        
        num1 = int(num1)
        num2 = int(num2)
        num3 = int(num3)
        
        
        if num1 < num2:
            if num1 < num3:
                return num1
            else:
                return num3
        if num2 < num1:
            if num2 < num3:
               return num2
            else:
               return num3
        if num3 < num1:
            if num3 < num2:
                return num3
            else:
                return num2
                    
        else:
            return  num2
        
                           
    def  maior(self, num1, num2, num3):
        num1 = int(num1)
        num2 = int(num2)
        num3 = int(num3)
        
        if num1 > num2:
            if num1 > num3:
                return num1
            else:
                return num3
                
        if num2 > num1:
            if num2 > num3:
                return num2
            else:
                return num3
        if num3 > num1:
            if num3 > num2:
                return num3
            else:
                return num2
        else:
            return num2
        
    def calcula(self, botao):
        
        texto = self.ids.lab.text
        num1 = self.ids.num1.text
        num2 = self.ids.num2.text
        num3 = self.ids.num3.text
        
        if num1 == "":
            num1 = 0
        if num2 == "":
            num2 = 0
        if num3 == "":
            num3 = 0
        
        maior =  self.maior(num1, num2, num3)
         
        menor = self.menor(num1, num2, num3)     
        
        tela = """O maior é {}
        
Já o menor é {}
        """.format(maior, menor)
        
        self.ids.lab.text = tela
        
class Roda(App):
    Builder.load_file("Roda.kv")
    def build(self):
        return Rodando()

Roda().run()                