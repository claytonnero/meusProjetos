from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from scalaInstrumentos import Casas
import random

class Gerente(ScreenManager):
	pass

class Rodando(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
					
	def calcule(self, botao):
		App.get_running_app().root.current = "calcula"
		
class Calcula(Screen):
		
	def on_enter(self):
		app = App.get_running_app().root.get_screen("rodando")
		med = app.ids.medida.text
		cas = app.ids.casas.text
		if med == "":
			med = 0
		if cas == "":
			cas = 0
					
		ini = Casas(med)
		seq = ini.casas(int(cas))
		lista = ini.escalaGeral(seq)
		mostra = self.ids.mostra
		cont = 1
		
		for i in lista:
			info = """        casa {}
Medida => {:.4f}""".format(cont, i)
			cor = (random.randint(1, 10), random.random(), random.random(), 1)
			mostra.add_widget(Label(text = info, size_hint_y = None, height=220, font_size=80, color=cor))
			cont += 1
		
	def voltar(self, botao):
		app = App.get_running_app().root.current = "rodando"
	
class Roda(App):
	pass

Roda().run()