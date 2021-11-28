#medida da escala musical
class Casas():	
	def __init__(self, pole):
		pole = float(pole)	
		self.cons = 17.8171540
		self.ref = 25.40
		self.pol = pole
		self.pole = self.pol
		self.tamanhoCm = self.pol * self.ref
		self.atual = self.tamanhoCm
	def casas(self, casas):
		casas = casas		
		lista = []
		cons = self.cons
		atual = self.atual
		for i in range(0, casas):
			var = atual / cons
			atual = atual - var 
			lista.append(var)
		return lista	
	def mostraCasas(self,lista):
		ini = 1
		num = 1
		for i in lista:
			num = "{:.3f}".format(i)
			#print(ini, num)
			ini += 1
		return num
	def escalaGeral(self,lista):	
		ini = 1
		num = 0
		result = []
		for i in lista:
			num += i
			result.append(num)
			ini += 1
		return result
"""
ini = Casas(34.5)
casas = ini.casas(19)
seq = ini.escalaGeral(casas)
print(seq)
"""
