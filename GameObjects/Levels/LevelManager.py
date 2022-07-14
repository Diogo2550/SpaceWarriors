#coding=utf-8

from Core.GameObject import GameObject
from GameObjects.Levels.Level import Level

class LevelManager(GameObject):
    def __init__(self):
        super().__init__()
        self.__levels = []
        self.__current_level = 1
        
    @classmethod
    def addLevel(self, level: Level):
        self.__levels.append(level)
        self.addEventListener('onLevelChanges', level.onLevelChanges)
        
    @classmethod    
    def onLevelChange(self):
        self.__current_level += 1
        
        if self.__current_level >= len(self.__levels):
            self.endGame()
            self._dispatchEvent('onGameEnds')
        else:
            self._dispatchEvent('onLevelChanges', self.getCurrentLevel())
            
    @classmethod
    def getCurrentLevel(self):
        return self.__levels[self.__current_level]
    
    @classmethod
    def findSpawnerWithName(self, name):
        return self.getCurrentLevel().findGameObjectWithName(name)
    
    @classmethod
    def endGame(self):
        print('Jogo terminou')
        self.__levels[-1].deactive()