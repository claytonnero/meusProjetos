"""13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-
Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window 

class Rodando(BoxLayout):
    
    def testa(self, botao):
            lab = self.ids.lab
            nom = self.ids.nome
            nome = botao.text
            
            lab.text = nome
            
            if nome == "*":
                lab.text = "Uai jefim, asterístico nao né! Doido!"
            elif nome == "#":
                lab.text = "Uai doido, vái jogar com essa véia então doido, uai!"
            elif int(nome) == 1:
                lab.text = "Domingão né Jefim!...né, tomá bavaria..., né?!"
            elif int(nome) == 2:
                tela = """
                Oh jefim, bruta 
                segunda-feira doido?
                ah não doido vô largá
                dessa vida doido, 
                gúento mais não doido!!
                """
                lab.text = tela
            elif int(nome) == 3:
                lab.text = "jefim já é terça"
            elif int(nome) == 4:
                lab.text = "Quarta-feira, doido, vô dá depressão doido!"
            elif int(nome) == 5:
                tela = """
                Poxa quinta feira!, oh doido, 
                traz aí um remédio pra anciedade doido,
                jefim, num guento mais de vontade de 
                tomá umas bavária doido!"
                """
                lab.text = tela            
            elif int(nome) == 6:
                tela = """
                Nossa doido hoje é sexta, 
                amanhã o pau quebra né 
                jefim?!!"
                """
                lab.text = tela
            elif int(nome) == 7:
                lab.text = "Sabadão né doido, pegá umas mina né doido!"
            else:
                lab.text = "Ficou doido? doido..., {} É inválido doido".format(nome)
            
    
class Roda(App):
    def build(self):
        return Rodando()

Roda().run()
