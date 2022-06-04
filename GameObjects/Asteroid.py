# coding= utf-8
from Core.GameObject import GameObject
from Core.Game import Game

from Core.Components.KineticsComponent import KineticsComponent
from Core.Components.SpriteComponent import SpriteComponent

class Asteroid(GameObject):
    ''' Classe de gameobject que representará um inimigo genérico '''
    def __init__(self):
        super().__init__()
        self.addComponent(KineticsComponent())
        self.addComponent(SpriteComponent('assets/images/sprites/meteors/meteor_brown_big1.png'))

    def _awake(self):
        self.kinetics = self.getComponent(KineticsComponent)
        self.sprite = self.getComponent(SpriteComponent)

    def _start(self):
        self.move_speed = Game.moveSpeedBase
        self.kinetics.disableGravity()

    def _update(self):
        pass