from kivy.app import App
from kivy.lang import Builder
from kivy.utils import get_color_from_hex as hex

kv = """
#:import hex kivy.utils.get_color_from_hex
<Lab@Label>:
    canvas.before:
        Color:
            rgba:hex("#00BFFF")
        Rectangle:
            size:self.size
            pos:self.pos
    id:nero
    
Lab:
    text:app.apresenta
    color:app.cor
"""
class Roda(App):
    
    apresenta = "texto no python"
    cor = hex("#00FF00")
    
    def build(self):
        return Builder.load_string(kv)

Roda().run()