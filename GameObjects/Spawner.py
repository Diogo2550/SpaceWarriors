#coding=UTF-8
from Core.GameObject import GameObject
from Core.Game import Game

class Spawner(GameObject):
    def __init__(self):
        __pool_size = 10
        __pool_enemies = []
        
        __respawn_delay = 3
        __respawn_ticks = 0        
    
    def _awake(self):
        pass
    
    def _start(self):
        pass
        
    def _update(self):
        doTick()
        
    def doTick(self):
        __respawn_ticks += Game.DELTA_TIME
        if(__respawn_ticks >= __respawn_delay):
            __respawn_ticks = 0
            self.__spawnEnemy()
        
    def __spawnEnemy():
        pass