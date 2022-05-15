# coding= utf-8
from Core.Vector import *
from Core.Game import *


class TransformComponent(Component):
    ''' Componente que representa uma coordenada no espaço e um container de objetos '''
    def __init__(self):
        super().__init__()
        self.position = Vector2(0, 0)
        self.parent = None
        self.children = []

    def _update(self):
        self.gameObject.x = self.position.x
        self.gameObject.y = self.position.y
        
    def addChild(self, child):
        child.parent = self
        self.children.append(child)
        
    def getChildByType(self, childType):
        for child in self.children:
            if(isinstance(child, childType)):
                return child
        return None
    
    def getChildByName(self, childName):
        for child in self.children:
            if(self.name == childName):
                return child
        return None
    
    def setName(self, name):
        self.name = name
        
    def setPosition(self, position):
        self.position = position
        
    def translate(self, translate):
        ''' Move o objeto, a partir da posição atual, o vetor translate dado '''
        self.position += translate * Game.DELTA_TIME
                