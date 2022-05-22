# coding= utf-8

from Core.Components.KineticsComponent import *
from Core.Components.SpriteComponent import *
from Core.Game import *
from GameObjects.Ball import Ball
from Core.Builders.GameObjectBuilder import GameObjectBuilder

game = Game()

ball = GameObjectBuilder\
    .startBuild(Ball())\
    .addComponent(KineticsComponent())\
    .addComponent(SpriteComponent('assets/images/ball.png'))\
    .setName('koe')\
    .build()

# Inserção dos gameobjects no jogo
game.addGameObject(ball)

# Iniciação do game loop
game.start()