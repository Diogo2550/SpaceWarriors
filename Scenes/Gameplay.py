from Core.Builders.GameObjectBuilder import GameObjectBuilder
from Core.Scene.Scene import Scene
from Core.Vector import Vector2
from Core.Game import Game

from Core.Components.SpriteComponent import SpriteComponent

from GameObjects.Enemy import Enemy
from GameObjects.Asteroid import Asteroid
from GameObjects.Player import Player

def build(name):
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
        
    gameScene = Scene(name)
    gameScene.addGameObject(enemy1)
    gameScene.addGameObject(enemy2)
    gameScene.addGameObject(asteroid1)
