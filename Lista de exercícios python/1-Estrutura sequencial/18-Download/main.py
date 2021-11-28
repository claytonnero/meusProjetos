"""18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a
velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de
download do arquivo usando este link (em minutos)"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.clearcolor = (1,0,1,1)

class Calcular(BoxLayout):
    
    Bits = 1
    Bytes = 8
    Kb = 1024 * Bytes
    Mb = 1024 * Kb
    Gb = 1024 * Mb
    Tb = 1024 * Gb
    Pb = 1024 * Tb
    Hb = 1024 * Pb
    
    dicio = {}
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        
    def tamanho(self):
        
        tam = self.ids.tamanho.text
        self.esco = self.ids.megas.text
        
        if tam == "":
            tam = 0
        
        if self.esco == "Bits":
            return float(tam) * self.Bits
        if self.esco == "Bytes":
            return float(tam) * self.Bytes 
        if self.esco == "Kb":
            return float(tam) * self.Kb
        if self.esco == "Mb":
            return float(tam) * self.Mb
        if self.esco == "Gb":
            return float(tam) * self.Gb
        if self.esco == "Tb":
            return float(tam) * self.Tb
        if self.esco == "Pb":
            return float(tam) * self.Pb
        if self.esco == "Hb": 
            return float(tam) * self.Hb
        
    def velocidade(self):        
        vel = self.ids.velocidade.text
        self.esco1 = self.ids.velo.text
        
        if vel == "":
            vel = 0
       
        if self.esco1 == "Kbps":
           return float(vel) * self.Kb
        if self.esco1 == "Mbps":
           return float(vel) * self.Mb
        if self.esco1 == "Gbps":
           return float(vel) * self.Gb
           
    def verifica(self, numero):
        
        if numero < self.Bytes:
            return numero // self.Bits
        if numero < self.Kb:
            return numero //  self.Bytes
        if numero < self.Mb:
            return numero // self.Kb
        if numero < self.Gb:
            return numero // self.Mb
        if numero < self.Tb:
            return numero // self.Gb
        if numero < self.Pb:
            return numero // self.Tb
        if numero < self.Hb:
            return numero // self.Pb
       
    def tempo(self, numero):
                 
         if numero < 60:
             return "{:.2f} segundos".format(numero / 1)
         if numero < (60*60):
             return "{:.2f} minutos".format(numero / 60)
         if numero < (60*60*24):
             return "{:.2f} horas".format( numero / (60*60))
         if numero < (60*60*24*7):
             return "{:.2f} dias".format(numero / (60*60*24))
         if numero < (60*60*24*7*4):
             return "{:.2f} semanas".format(numero / (60*60*24*7))
         if numero < (60*60*24*7*4*12):
             return "{:.2f} meses".format(numero / (60*60*24*7*4))  
         if numero < (60*60*24*7*4*12*10):
             return "{:.2f} anos".format(numero / (60*60*24*7*4*12))
         if numero < (60*60*24*7*4*12*10*100):
             return "{:.2f} décadas".format(numero / (60*60*24*7*4*12*10)) 
         if numero < (60*60*24*7*4*12*10*100*1000):
             return "{:.2f} céculos".format(numero / (60*60*24*7*4*12*10*100))  
         if numero < (60*60*24*7*4*12*10*100*1000*10000):
             return "{:.2} milênios".format(numero / (60*60*24*7*4*12*10*100*1000))     
         
         
    def apertado(self, botao):
        
        tam= self.tamanho()
        vel = self.velocidade()
        tempo = 0
        
        if tam == 0:
            pass
        if vel == 0:
            pass
        else:
            tempo = tam // vel
                
        tela = """
        
        Tamanho a baixar  em bits ({})
        
        Tamanho  da velocidade do\n
        
        Download por segundo ({})
        
        Tempo real ({})
        
        Para baixar um arquivo de {} {}
        
        Será nescessário ({})
        
        """.format(tam, vel, tempo, self.verifica(tam), self.esco, self.tempo(tempo))
        self.ids.lab.text = tela
        self.ids.lab.font_size = 30
          
class Download(App):
    def build(self):
        return Calcular()

Download().run()