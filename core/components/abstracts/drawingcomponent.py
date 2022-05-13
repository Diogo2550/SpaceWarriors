# coding= utf-8
from core.component import *
from core.pplay.sprite import *

# Classe base para componentes que precisam ser desenhados na tela
class DrawingComponent(Component):
    def __init__(self):
        super().__init__()

    def draw(self):
        raise NotImplementedError(f'O método draw() da classe {self.__class__} deve ser implementado');
