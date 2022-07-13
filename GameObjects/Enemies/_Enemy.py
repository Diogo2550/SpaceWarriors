# coding= utf-8
import math

from Core.GameObject import GameObject
from Core.Game import Game
from Core.Vector import Vector2

from Core.Components.KineticsComponent import KineticsComponent
from Core.Components.SpriteComponent import SpriteComponent
from Core.Components.CollisionComponent import CollisionComponent

class EnemyBase(GameObject):
    ''' Classe de gameobject que representará um inimigo genérico '''
    def __init__(self):
        super().__init__()
        self.difficulty = 1 # Dificuldade do inimigo. Usado para definir sua frequência de spawn
        self.move_speed = None # Setadp durante o Start
        self.score_base = 100
        self.lives = 1
        self.vector_direction = None
        self._fire_delay = 2
        self._reload_time = 0        

    def _awake(self):
        self.addComponent(KineticsComponent())
        self.addComponent(SpriteComponent('assets/images/sprites/enemies/enemy_black_1.png'))
        self.addComponent(CollisionComponent())

    def _start(self):
        self.kinetics = self.getComponent(KineticsComponent)
        self.sprite = self.getComponent(SpriteComponent)
        self.collision = self.getComponent(CollisionComponent)
        
        self.move_speed = Game.SPEED_BASE
        self.kinetics.disableGravity()
        
        self.collision.addCollisionWith(Game.player)

    def _update(self):
        if(self.y > Game.WINDOW_HEIGHT + self.height):
            self.destroy()
        
        if(self._reload_time <= 0):
            self._fire()
            self._reload()
        
    def _afterUpdated(self):
        self._reload_time -= Game.DELTA_TIME
        
    def configure_spawn(self, horizontal_offset = 0, vertical_offset = 0):
        from random import randint

        self.setPosition(Vector2(
            randint(horizontal_offset * -1, Game.WINDOW_WIDTH + horizontal_offset),
            (self.height + vertical_offset) * -1
        ))
        
    def _fire(self):
        print('Atirou')
    
    def _reload(self):
        from random import randint
        
        percentage = int(self._fire_delay * 0.7)
        self._reload_time = self._fire_delay + randint(-percentage, int(percentage / 2))
    
    def _faceToPlayer(self):
        ''' Vira a rotação do gameobject em direção ao player '''
        playerPosition = Game.player.getPosition()
        position = self.getPosition()
        vector_distance = playerPosition - position

        angle = 0
        if(vector_distance.x == 0):
            pass
        else:
            angle = math.atan(vector_distance.x/vector_distance.y)
            angle = angle * (180/math.pi)
        self.transform.rotate(angle)
        
    def _followPlayer(self):
        playerPosition = Game.player.getPosition()
        position = self.getPosition()
        
        vector_distance = playerPosition - position
        self.vector_direction = vector_distance.normalize()
        
        self.kinetics.setVelocity(self.vector_direction * self.move_speed)
        
    def _tookDamage(self):
        Game.score += self.score_base
        self.lives -= 1
        
        if(self.lives <= 0):
            self.destroy()
        
    # Função executada quando ocorre uma colisão com o player
    def onCollided(self, gameObject):
        from GameObjects.Player import Player
        from GameObjects.GunFire import GunFire
        
        if(isinstance(gameObject, Player)):
            Game.player.damage()
        elif(isinstance(gameObject, GunFire)):
            # Diminui em 1 a vida do inimigo e mata caso a vida zere
            self._tookDamage()