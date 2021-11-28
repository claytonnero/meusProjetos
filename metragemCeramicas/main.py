import os
#os.environ['KIVY_GL_BACKEND'] = 'sdl2'

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import StringProperty, ObjectProperty

Window.clearcolor = .4, .6, .3, 1

class Rodando(BoxLayout):
	
	lab = ObjectProperty(None)
	alt = ObjectProperty(None)
	larg = ObjectProperty(None)
	but = ObjectProperty(None)
	quant = ObjectProperty(None)
	val = ObjectProperty(None)
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)		
		
		#referencia ao label
		self.lab.text = "inserido do python"
		
		#referencias aos inputs
		self.alt.hint_text = "largura"
		self.larg.hint_text = "altura"
		self.quant.hint_text = "Peças"
				
		#referencia ao botao
		self.but.text = "Calcule"
		self.but.on_release = self.apertado
		
	def apertado(self, *args):
		
		if self.alt.text == "":
			self.alt.text = "0.0"
		if self.larg.text == "":
			self.larg.text = "0.0"
		if self.quant.text == "":
			self.quant.text = "0.0"
		if self.val.text == "":
			self.val.text = "0.0"
		
		area_individual = float(self.alt.text) * float(self.larg.text)
		area_total = float(area_individual) * float(self.quant.text)
		preço = area_total * float(self.val.text)
		
		stri = """
A área unitária 
é {:.2f} Mtrs²

A área total 
assentada é 
{:.2f} Mtrs²

Esta produção por {} 
o metro lhe renderá 
{:.2f} R$
""".format(area_individual, area_total, self.val.text, preço)
		
		self.lab.text = stri
		self.lab.font_size = dp(35)
		
		if preço <=130:
			Window.clearcolor = (1,0,0,1)
		elif preço >=131 and preço <=150:
			Window.clearcolor = (1,0,1,1)
		else:
			Window.clearcolor = (0,.6,0,1)
			

class Roda(App):
    def build(self):
        return Rodando()

if __name__ == "__main__":
    Roda().run()