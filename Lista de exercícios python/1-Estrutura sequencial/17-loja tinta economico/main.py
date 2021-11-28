"""
17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros

quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6

metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em

galões de 3,6 litros, que custam R$ 25,00. 

• Informe ao usuário as quantidades de tinta a serem compradas e os respectivos

preços em 3 situações: 

• comprar apenas latas de 18 litros; 

• comprar apenas galões de 3,6 litros; 

• misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga

e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""
from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window 

Window.clearcolor = (0, 0.6, 0.8, 1)
class Tela(BoxLayout):
    
    def calculo(self, Button):
        
        lab = self.ids.lab.text
        alt = self.ids.altura.text
        larg = self.ids.largura.text
        but = self.ids.but
        
        if alt == "":
            alt = 0.0          
        else:
            alt = float(alt)       
        if larg == "":
            larg = 0.0           
        else:
            larg = float(larg)
        
        area = larg  *  alt
        percentual = (area * 10) / 100  
        
        cobertura_lata = 18 * 6
        cobertura_galao = 3.6 * 6
        
        apenas_latas = (area + percentual) / cobertura_lata 
        apenas_galoes = (area + percentual) / cobertura_galao
            
        latas = int(apenas_latas)
        galoes = 0
        area_lata = latas * cobertura_lata
        resto = (area + percentual) - area_lata
        galoes = resto / cobertura_galao
        
        if galoes > 3:
            latas = latas + 1
            galoes = 0
        if galoes > int(galoes):
            galoes = int(galoes) + 1
        
            
        if apenas_latas > int(apenas_latas):
            apenas_latas = int(apenas_latas) + 1           
        else:
            apenas_latas = int(apenas_latas)
            
        if apenas_galoes > int(apenas_galoes):
            apenas_galoes = int(apenas_galoes) + 1
        else:
            apenas_galoes = int(apenas_galoes)
                                        
        tela="""
        Área {} metros quadrados
        
        Necessario {} latas 18 litros 
        com o custo de R${} Reais
        
        Precisa de {} galoes de 3.6 litros
        com o custo de R${} Reais
        
        misturando {} latas e {} galões
        com o custo de R${}
        """.format(area, apenas_latas, apenas_latas * 80.00, apenas_galoes,  apenas_galoes * 25.00, latas,galoes,((latas * 80.00)+ (galoes * 25.00)))
        self.ids.lab.text = tela
    
class Economico(App):
    def build(self):
        return Tela()
Economico().run()