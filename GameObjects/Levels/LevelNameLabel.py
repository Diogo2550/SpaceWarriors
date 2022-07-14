#coding=utf-8
from Core.Game import Game
from GameObjects.Levels.LevelManager import LevelManager

from GameObjects.UI._Text import UIText


class LevelNameLabel(UIText):
    def __init__(self, name):
        super().__init__()
        self.__text = name
        self.__timer = 5
        
    def _start(self):
        super()._start()
        from Core.Vector import Vector2
        
        self.text.setText(self.__text)
        
        self.setPosition(Game.getWindowCenter() - Vector2(len(self.__text) * self.getFontSize() / 2, self.getFontSize() / 2))
        
    def _update(self):
        super()._update()
        self.__timer -= Game.DELTA_TIME
        
    def _afterUpdated(self):
        if self.__timer <= 0:
            LevelManager.instance.getCurrentLevel().start()
            Game.findGameObjectWithName('timer_hub').play()
            self.destroy()