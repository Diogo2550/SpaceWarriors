#coding=UTF-8
from Core.GameObject import GameObject
from Core.Game import Game

class Spawner(GameObject):
    def __init__(self):
        super().__init__()
        self.__pool_size = 10
        self.__pool_enemies = []
        self.__max_pool_difficulty = 0
        
        self.__respawn_delay = 3
        self.__respawn_ticks = 0
        
        self.__spawner_level = 1
        
        self.__timer = None
    
    def _start(self):
        self.__timer = Game.findGameObjectWithName('timer_hub')
    
    def _update(self):
        self.doTick()
        
    def addEnemy(self, enemy):
        if(len(self.__pool_enemies) > 0):
            # Como esse método é chamado pouquíssimas vezes não há problema fazer um método mais custoso como este
            position = [ index for index in range(len(self.__pool_enemies)) if self.__pool_enemies[index].difficulty > enemy.difficulty ]
            if(len(position) > 0):
                self.__pool_enemies.insert(position[0], enemy)
            else:
            	self.__pool_enemies.append(enemy)
        else:
            self.__pool_enemies.append(enemy)
        
        if(enemy.difficulty > self.__max_pool_difficulty):
            self.__max_pool_difficulty = enemy.difficulty
    
    def doTick(self):
        self.__respawn_ticks += Game.DELTA_TIME
        if(self.__respawn_ticks >= self.__respawn_delay):
            self.__respawn_ticks = 0
            self.__spawnEnemy()
            
            # total - 1
            # 0     - 10
            self.__spawner_level = self.__timer.timer_total // 10 - self.__timer.timer_current // 10
        
    def __spawnEnemy(self):
        horizontal_offset = 100
        vertical_offset = 40
        
        enemy_to_spawn = self.__chooseEnemy()
        enemy_to_spawn.configure_spawn(horizontal_offset, vertical_offset)
        
        self.addChild(enemy_to_spawn)
        self._dispatchEvent('onSpawn', enemy_to_spawn)
        
    def __chooseEnemy(self):
        from random import randint
        
        difficulty = randint(0, self.__max_pool_difficulty)
        
        # Esse método é chamado apenas uma vez a cada tick de spawn. Por isso, não terá um impacto tão grande
        # fazer desta forma mais custosa
        index_bigger_aux = [ index for index in range(len(self.__pool_enemies)) if self.__pool_enemies[index].difficulty >= difficulty ]
        index_bigger = len(self.__pool_enemies) - 1
        if(len(index_bigger_aux)):
            index_bigger = index_bigger_aux[0]
        
        previous_enemy = self.__pool_enemies[index_bigger - 1] if index_bigger > 0 else self.__pool_enemies[0]
        next_enemy = self.__pool_enemies[index_bigger]
        
        enemy = None
        # Seleciona o inimigo com a dificuldade mais próxima do número sorteado
        if(difficulty - previous_enemy.difficulty < difficulty - next_enemy.difficulty):
            enemy = previous_enemy
        else:
            enemy = next_enemy
        
        return enemyFactory(type(enemy))
    
def enemyFactory(enemy_type):
    enemy = enemy_type()
    
    return enemy