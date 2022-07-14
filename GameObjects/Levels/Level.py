#coding=utf-8

from Core.GameObject import GameObject
from Core.PPlay.sound import Sound
from GameObjects.Spawner import Spawner

class Level(GameObject):
    def __init__(self):
        super().__init__()
        self.soundtrack = None
        self.__spawners = []
    
    def setSoundTrack(self, music: Sound):
        self.soundtrack = music
    
    def addSpawner(self, spawner: Spawner):
        self.__spawners.append(spawner)
    
    def active(self):
        self.soundtrack.play()
        
        for spawner in self.__spawners:
            spawner.deactive()
        
    
    def deactive(self):
        self.soundtrack.stop()
        
        for spawner in self.__spawners:
            spawner.deactive()
            
    def onLevelChanges(self, level):
        if(level == self):
            print('sou eeeeu')
            
    def getSpawnerWithName(self, name):
        for gameObject in self.__spawners:
            if(gameObject.getName() == name):
                return gameObject
        return None