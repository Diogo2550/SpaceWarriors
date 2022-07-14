#coding=utf-8

from Core.GameObject import GameObject
from Core.PPlay.sound import Sound
from Core.Game import Game
from Core.Scene.SceneManager import SceneManager

from GameObjects.Spawner import Spawner
from GameObjects.UI._Text import UIText

class Level(GameObject):
    def __init__(self, time, name, pool_size, respawn_delay_base):
        super().__init__()
        self.soundtrack: Sound = None
        self.__spawners = []
                
        self.__pool_size = pool_size
        self.__respawn_delay_base = respawn_delay_base

        self.__time = time
        self.__name = name
        
    
    def setSoundTrack(self, music_name):
        self.soundtrack = Sound(music_name)
    
    def addSpawner(self, spawner: Spawner):
        spawner.setRespawnDelay(self.__respawn_delay_base)
        spawner.setPoolSize(self.__pool_size)
        self.__spawners.append(spawner)
    
    def active(self):
        from GameObjects.Levels.LevelNameLabel import LevelNameLabel
        
        timer = Game.findGameObjectWithName('timer_hub')
        timer.setTimer(self.__time)
        
        level_label = LevelNameLabel(self.__name)
        SceneManager.addGameObjectToCurrentScene(level_label)
    
    def start(self):
        self.soundtrack.play()
        
        for spawner in self.__spawners:
            spawner.active()        
    
    def deactive(self):
        self.soundtrack.stop()
        
        for spawner in self.__spawners:
            spawner.deactive()
            
    def onLevelChanges(self, level):
        if(level == self):
            print('sou eeeeu')
            
    def findSpawnerWithName(self, name):
        for gameObject in self.__spawners:
            if(gameObject.getName() == name):
                return gameObject
        return None