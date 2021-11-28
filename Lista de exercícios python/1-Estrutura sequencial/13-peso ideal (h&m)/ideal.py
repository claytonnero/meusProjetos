"""13. Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que
calcule seu peso ideal, utilizando as seguintes fórmulas: 

• Para homens: (72.7*h) - 58 

• Para mulheres: (62.1*h) - 44.7 (h = altura) 

• Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.
"""
from kivy.app import App
#from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button 

#Window.clearcolor = 0, .4, .3, 1

class Verifica(BoxLayout):
    def calculando(self, Button):
        """
        Para homens: (72.7*altura) - 58 

        Para mulheres: (62.1*altura) - 44.7 
        """
        self.sexo = None
        self.tog = self.ids.but_tog
        self.lab = self.ids.lab
        
        #info = self.ids.peso
        self.alt = self.ids.imp.text
        self.but = self.ids.but
        self.inform = self.ids.info
        
        if self.alt == "":
            self.alt = 0.0 
        else:
            self.alt = float(self.alt)
                                    
        if self.tog.state == "down":
            self.tog.text = "Mulher"
            self.sexo = "mulher"            
        else:
            self.tog.text = "Homem"
            self.sexo = "homem"
            
        if self.sexo:
            if self.sexo == "mulher":
                 self.lab.text = "O peso ideal\npara uma mulher é\n{:.2f}".format(self.mulheres(self.alt))
            else:
                self.lab.text = "O peso ideal \npara um homem é\n{:.2f}".format(self.homens(self.alt))
                       
    def mulheres(self, altura):
          
          ideal = altura * 62.1 - 44          
          return ideal
          
    def homens(self, altura):
         
         ideal = altura * 72.7 - 58
         return ideal
         
    def executa(self, botao):
        if self.sexo == "homem":
            homem_ideal = "{:.2f}".format(self.homens(self.alt))
            if float(self.imp2.text) < float(homem_ideal):
                self.inform.text = "Você está abaixo do peso ideal"
            elif float(self.imp2.text)> float(homem_ideal):
                self.inform.text = "Você está acima do peso  ideal"
            elif float(self.imp2.text) == float(homem_ideal):
                self.inform.text = "Você está com o peso ideal"
        else:
            mulher_ideal = "{:.2f}".format(self.mulheres(self.alt))
            if float(self.imp2.text) < float(mulher_ideal):
                self.inform.text = "Você está abaixo do peso ideal"
            elif float(self.imp2.text) > float(mulher_ideal):
                self.inform.text = "Você está acima do peso ideal"
            elif float(self.imp2.text) == float(mulher_ideal):
                self.inform.text = "Você está com o peso ideal"
         
        self.pop.dismiss()
        
    def calcula(self, botao):
          box = BoxLayout(orientation="vertical", padding="20dp", spacing="10dp")
          
          self.imp2 = TextInput(size_hint_y=None, height="40dp", hint_text="Digite seu peso atual", multiline=False, input_filter="float")
          
          box.add_widget(self.imp2)
          box.add_widget(Button(text="Pronto", size_hint_y=None, height="60dp", on_release=self.executa))
          
          self.pop = Popup(title="Defina seu peso", content=box, size_hint=(None, None), size=("300dp", "200dp"))
          self.pop.open()
          
class Processa(App) :    
    def build(self):
        return Verifica()
        
Processa().run()
