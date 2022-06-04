# coding= utf-8
import math

from Core.GameObject import GameObject
from Core.Game import Game

from Core.Components.KineticsComponent import KineticsComponent
from Core.Components.SpriteComponent import SpriteComponent

class Enemy(GameObject):
    ''' Classe de gameobject que representará um inimigo genérico '''
    def __init__(self):
        super().__init__()
        self.addComponent(KineticsComponent())
        self.addComponent(SpriteComponent('assets/images/sprites/enemies/enemy_black_1.png'))

    def _awake(self):
        self.kinetics = self.getComponent(KineticsComponent)
        self.sprite = self.getComponent(SpriteComponent)

    def _start(self):
        self.move_speed = Game.moveSpeedBase
        self.kinetics.disableGravity()

        self.__faceToPlayer()

    def _update(self):
        pass

    def __faceToPlayer(self):
        ''' Vira a rotação do gameobject em direção ao player '''
        playerPosition = Game.player.getPosition()
        position = self.getPosition()
        vectorDistance = playerPosition - position

        angle = 0
        if(vectorDistance.x == 0):
            pass
        else:
            angle = math.atan(vectorDistance.y/vectorDistance.x)
            angle = angle * (180/math.pi)
        self.transform.rotate(angle)