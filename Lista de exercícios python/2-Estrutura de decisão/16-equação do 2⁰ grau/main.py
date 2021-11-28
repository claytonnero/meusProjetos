"""16. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 +
bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando
ao usuário nas seguintes situações: 
• Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o
programa não deve fazer pedir os demais valores, sendo encerrado; 
• Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao
usuário e encerre o programa; 
• Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-
a ao usuário; 
• Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang.builder import Builder

Window.clearcolor = 0, .6, .3, 1

kv = """
BoxLayout:
    Rodando:

<Rodando>:
    orientation:"vertical"
    Label:
        text:"Calcular equação do segundo grau "
    GridLayout:
        cols:3
        size_hint_y:None
        height:"100dp"
        spacing:8
        #input1
        Wid:
        TextInput:
            id:ent1
            hint_text:"Informe o valor de A"
            input_filter:"int"
            multiline:False
        Wid:
            
        #input2
        Wid:
        TextInput:
            id:ent2
            hint_text:"Informe o valor de B"
            input_filter:"int"
            multiline:False
        Wid:
        
        #input3
        Wid:
        TextInput:
            id:ent3
            hint_text:"Informe o valor de C"
            input_filter:"int"
            multiline:False
        Wid:
    Label:
        id:lab
        text:"Deu Certo"
    Widget:
    GridLayout:
        cols:3
        size_hint_y:None
        height:"60dp"
        Wid:
        Button:
            id:but
            text:"Calcule"
            on_release:root.solto(self)
        Wid:

#personalizando o widget        
<Wid@Widget>:
    size_hint_x:.5
"""


class Rodando(BoxLayout):   
    
    def deltaNeg(self, delta, a,b,c):
        raizD = delta**0.5
        
        x1 = (-b+raizD) / (2*a)
        x2 = (-b-raizD) / (2*a)
        return """A equação nao possue raizes reais
delta {}
X1= {:.2f}
X2= {:.2f}""".format(delta,x1, x2)
     
    def deltaZero(self, delta, a,b,c):
        raizD = delta**0.5
        
        x1 = (-b+raizD) / (2*a)
        x2 = (-b-raizD) / (2*a)
        return """delta {}
X1= {:.2f}
X2= {:.2f}""".format(delta,x1, x2)
        
    def  deltaPos(self, delta,a,b,c):
        
        raizD = delta**0.5
        
        x1 = (-b+raizD) / (2*a)
        x2 = (-b-raizD) / (2*a)
        return """delta {}
X1= {:.2f}
X2= {:.2f}""".format(delta,x1, x2)
        
    def solto(self, botao):
        self.ids.lab.color = 1,0,0,1
        
        lab = self.ids.lab 
        A = self.ids.ent1.text
        B = self.ids.ent2.text
        C = self.ids.ent3.text
        
        msn =""
        
        if A == "":
            A = 0
        if B == "":
            B = 0
        if C == "":
            C = 0
        
        A = int(A)
        B = int(B)
        C = int(C)
        
        if A == 0:
            lab.text = "A equação não é do segundo grau"
            return Roda().stop()
            
        delta = (B**2) - (4*A*C)
            
        if delta < 0:
            msn = self.deltaNeg(delta,A,B,C)
            
        elif delta == 0:
            msn = self.deltaZero(delta, A,B,C)
            
        else:
            msn = self.deltaPos(delta,A,B,C)
        
        lab.text = str(msn)

class Roda(App):   
    
    def build(self):
        Builder.load_string(kv)
        return Rodando()
        
if __name__ == "__main__":
    Roda().run()    