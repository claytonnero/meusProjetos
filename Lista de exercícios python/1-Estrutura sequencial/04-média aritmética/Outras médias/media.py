from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 

#esta é uma série de programas gráficos simples com intuito de acessar os widgets de diferentes maneiras
 
#programa gráfico para calcular a média entre dois números 


class Corpo(BoxLayout):
    #A classe Corpo faz uma herança da classe BoxLayout que é um widget que organiza os widgets graficamente
#módulo importado na segunda linha deste software!

    def __init__(self, **kwargs):
        """Função que inicia a classe Corpo"""
        
        super().__init__(**kwargs)
               
    def acontece(self, Button):
        """Função disparada quando o botão é apertado!
        ela calcula a média entre as duas entradas
        e sobescreve o texto do label com id:lab"""
        
        #captura as entradas do usuário
        entr1 = self.ids.ent1.text
        entr2 = self.ids.ent2.text
        #em modo gráfico
        
        #calcula a média entre as duas entradas
        media = (int(entr1) + float(entr2)) /2
        
        #faz a mudança do texto do
        #label através do id criado no kv
        self.ids.lab.text = "A média solicitada é "+str(media)

class Media(App):
    #A classe Media, é a que cria a aplicaçao, através de seu metodo run()
    def build(self):
        """A função build cria os elementros gráficos na tela de seu dispositivo, e chama a classe Corpo()"""
        return Corpo()

#o programa começa a rodar por aqui, a classe Media que faz uma herança da classe App importada na primeira linha deste programa!
Media().run()