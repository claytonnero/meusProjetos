"""14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar orendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que oestabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar umamulta de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia avariável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na variávelexcesso e na variável multa o valor da multa que João deverá pagar. Caso contrário mostrartais variáveis com o conteúdo ZERO.
"""
from kivy.app import App 
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout

class Calculando(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def processa(self, Button):
        
        self.multa = 4.00
        self.limite = 50.00
        self.ent = self.ids.peso.text 
        if self.ent == "":
            self.ent = "0.00"
        else:
            self.ent = float(self.ids.peso.text)
            
        self.excesso = float(self.ent) - self.limite
        self.multa_valor = self.excesso * self.multa
        
        lab = """
        O total pescado é Kg{}
        houve de excesso 
        Kgs{}
        multa sobre excesso
         de R${}
        """.format(self.ent, self.excesso, self.multa_valor)
        
        self.ids.resultado.text = lab
    
class Pescado(App):
    def build(self):
        return Calculando()

Pescado().run()