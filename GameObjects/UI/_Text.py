# coding= utf-8
from Core.GameObject import GameObject
from Core.Vector import Vector2
from Core.Game import Game

from Core.Components.ClickableComponent import ClickableComponent
from Core.Components.TextComponent import TextComponent

class UIText(GameObject):
    def __init__(self):
        super().__init__()
        self.text_string = ''

    def _awake(self):
        self.text = TextComponent()
        self.addComponent(self.text)
        
        self.configureText()
        
    def _start(self):
        self.text.setText(self.text_string)
        
        if(self.transform.parent):
            self.setLocalPosition(
            	self.transform.parent.gameObject.getObjectCenter() -
            	Vector2(len(self.text_string) * 5, 14)
			)
        
    def setText(self, text):        
        self.text_string = text
        
    def configureText(self, size = 22, color = (64, 64, 64), family = 'arial'):
        self.text\
            .setFontColor(color)\
            .setFontSize(size)