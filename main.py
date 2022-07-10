# coding= utf-8
from Core.Game import *
from Core.Builders.GameObjectBuilder import GameObjectBuilder

from GameObjects.Player import Player
from GameObjects.Enemy import Enemy
from GameObjects.Asteroid import Asteroid

from Core.Scene.Scene import Scene
from Scenes.Menu import build as bsMenu
from Scenes.Gameplay import build as bsGameplay

game = Game()
Game.setBackground('assets/images/backgrounds/blue_resized.jpg')

# Instanciação de gameobjects
player = GameObjectBuilder\
    .startBuild(Player())\
    .setName('Player1')\
    .setPosition(Vector2(
        Game.WINDOW_WIDTH / 2 - GameObjectBuilder.instance.width / 2,
        Game.WINDOW_HEIGHT - GameObjectBuilder.instance.height
    ))\
    .build()
    
menu = bsMenu('menu')
gameplay = bsGameplay('gameplay')

# Iniciação do game loop
game.setPlayer(player)

game.developmentMode()
game.start()