# coding= utf-8
from Core.Component import *
from Core.PPlay.sprite import *

from .Abstracts.DrawingComponent import *

# Adicionará sprites aos gameobjects
class SpriteComponent(DrawingComponent):
    def __init__(self, spritePath):
        super().__init__()
        self.sprite = Sprite(spritePath)
    
    def _update(self):
        pass
    
    def setGameObject(self, gameObject):
        super().setGameObject(gameObject)
        self.gameObject.setSize(self.sprite.width, self.sprite.height)  

    def draw(self):
        self.sprite.x = self.gameObject.x
        self.sprite.y = self.gameObject.y
        
        self.sprite.draw()
