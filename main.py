# coding= utf-8

from Core.Game import *
from Core.Builders.GameObjectBuilder import GameObjectBuilder

from GameObjects.Player import Player
from GameObjects.Enemy import Enemy
from GameObjects.Asteroid import Asteroid

from Core.Scene.Scene import Scene

game = Game()
game.setBackground('assets/images/backgrounds/blue_resized.jpg')

# Instanciação de gameobjects
player = GameObjectBuilder\
    .startBuild(Player())\
    .setName('Player1')\
    .setPosition(Vector2(
        Game.WINDOW_WIDTH / 2 - GameObjectBuilder.instance.width / 2,
        Game.WINDOW_HEIGHT - GameObjectBuilder.instance.height
    ))\
    .build()

enemy1 = GameObjectBuilder.startBuild(Enemy())\
    .setName('Enemy1')\
    .setPosition(Vector2(20, 30))\
    .build()

enemy2 = GameObjectBuilder.startBuild(Enemy())\
    .setName('Enemy2')\
    .setPosition(Vector2(Game.WINDOW_WIDTH - 120, 60))\
    .build()

asteroid1 = GameObjectBuilder.startBuild(Asteroid())\
    .setName('Asteroid1')\
    .setPosition(Game.getWindowCenter())\
    .build()

gameScene = Scene('gameplay')
gameScene.addGameObject(player)
gameScene.addGameObject(enemy1)
gameScene.addGameObject(enemy2)
gameScene.addGameObject(asteroid1)

gameScene = Scene('gameplay2')
gameScene.addGameObject(player)
gameScene.addGameObject(enemy1)
gameScene.addGameObject(enemy2)
gameScene.addGameObject(asteroid1)


# Iniciação do game loop
game.setPlayer(player)

game.developmentMode()
game.start()