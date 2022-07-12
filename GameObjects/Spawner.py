#coding=UTF-8
from Core.GameObject import GameObject
from Core.Game import Game

class Spawner(GameObject):
    def __init__(self):
        super().__init__()
        self.__pool_size = 10
        self.__pool_enemies = []
        
        self.__respawn_delay = 3
        self.__respawn_ticks = 0
        
        self.__spawner_level = 1
        
        self.__timer = None
    
    def _start(self):
        self.__timer = Game.findGameObjectWithName('timer_hub')
        print(self.__timer)
    
    def _update(self):
        self.doTick()
        
    def doTick(self):
        self.__respawn_ticks += Game.DELTA_TIME
        if(self.__respawn_ticks >= self.__respawn_delay):
            self.__respawn_ticks = 0
            self.__spawnEnemy()
            
            # total - 1
            # 0     - 10
            self.__spawner_level = self.__timer.timer_current - self.__timer.timer_total // 10
        
    def __spawnEnemy(self):
        print(self.__spawner_level)