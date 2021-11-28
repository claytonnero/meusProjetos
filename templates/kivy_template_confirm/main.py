from kivy.app import App

import sys

caminho = '/storage/emulated/0/Progamar/python3/nero_modules/kivy/'
sys.path.append(caminho)

from cores import escolha as esc
#modulos internos
from uteis.botao import Botao

from uteis.barra import Barra
from telas.gerente import Gerencia

import os
path = os.path.dirname(os.path.abspath(__file__))
os.chdir(path)
    
class Tela(App):
    def build(self):
        return Gerencia()
        
if __name__ ==    "__main__":
    Tela().run()