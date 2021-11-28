"""15. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os
valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é:
equilátero, isósceles ou escaleno. 
• Dicas: 
• Três lados formam um triângulo quando a soma de quaisquer dois lados for maior
que o terceiro; 
• Triângulo Equilátero: três lados iguais;
• Triângulo Isósceles: quaisquer dois lados iguais;
• Triângulo Escaleno: três lados diferentes
"""
from kivy.base import runTouchApp
from kivy.core.window import Window 
from kivy.lang.builder import Builder 
from kivy.uix.boxlayout import BoxLayout

Window.clearcolor = .7, .8, .3, 1

kv = """
#:set azul 0, 0, 1, 1
#:import rand random.random
#:set cor_r rand(), rand(), rand(), 1

BoxLayout:
    orientation:"vertical"
    Rodando:
        
<Rodando>:
    orientation:"vertical"
    Label:
        id:lab
        text:"Deu Certinho sô!"
        color:azul
    GridLayout:
        cols:3
        spacing:15
        Widget:
            size_hint_x:.3
        TextInput:
            id:ent1
            size_hint_y:None
            heigth:"30dp"
            multiline:False
            input_filter:"float"
            hint_text:"Digite um lado para o triangulo"
        Widget:
            size_hint_x:.3
        Widget:
            size_hint_x:.3
        TextInput:
            id:ent2
            size_hint_y:None
            heigth:"30dp"
            multiline:False
            input_filter:"float"
            hint_text:"Digite outro lado para o triangulo"
        Widget:
            size_hint_x:.3
        Widget:
            size_hint_x:.3
        TextInput:
            id:ent3
            size_hint_y:None
            heigth:"30dp"
            multiline:False
            input_filter:"float"
            hint_text:"Digite o ultimo lado do triangulo"
        Widget:
            size_hint_x:.3
    GridLayout:
        cols:4
        spacing:20,0
        Widget:
        Button:
            text:"Verificar"
            size_hint_y:None
            heigth:"60dp"
            on_release:root.solto(self)
        Widget:
"""
class Rodando(BoxLayout):
    
    def triangulo(self, x, y, z):
                  
        if (x + y) < z or (x + z) < y or (y + x) < z or (y + z) < x or (z + x) < y or (z + y) < x or x == y == z == 0:
            return "Triangulo não aceito"
            
        elif x == y == z:
            return self.equilatero()
        
        elif x == y != z or x == z != y or y == x != z or y == z != x or z == x != y or z == y != x:
            return self.isosceles() 
            
        else:
            return self.escaleno()      
        
    def equilatero(self):        
        return "Triângulo equilátero"
    
    def escaleno(self):        
        return "Triângulo escaleno"
        
    def isosceles(self):        
        return "Triângulo isósceles"
        
    def compara(self, x, y, z):
        
        x = int(x)
        y = int(y)
        z = int(z)
        
        teste = self.triangulo(x, y, z)
        return teste
        
                     
    def solto(self, botao):
        
        lado1 = self.ids.ent1.text
        lado2 = self.ids.ent2.text
        lado3 = self.ids.ent3.text
        
        msn = ""
        
        if lado1 == "":
            lado1 = 0
        if lado2 == "":
            lado2 = 0
        if lado3 == "":
            lado3 = 0
            
        msn = self.compara(lado1, lado2, lado3)          
        self.ids.lab.text = str(msn)

runTouchApp(Builder.load_string(kv))