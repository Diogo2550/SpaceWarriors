# coding= utf-8

from Core.Components.KineticsComponent import *
from Core.Components.SpriteComponent import *
from Core.Game import *
from GameObjects.Ball import Ball

game = Game()

# Instanciação de gameobjects
ball = Ball()
ballSprite = SpriteComponent('assets/images/ball.png')
ballKinetics = KineticsComponent()

ball.addComponent(ballSprite)
ball.addComponent(ballKinetics)

# Inserção dos gameobjects no jogo
game.addGameObject(ball)

# Iniciação do game loop
game.start()