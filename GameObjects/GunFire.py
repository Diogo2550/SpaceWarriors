# coding= utf-8
from Core.Components.KineticsComponent import KineticsComponent
from Core.Components.SpriteComponent import SpriteComponent
from Core.GameObject import *
from Core.Vector import Vector2
from Core.Game import *
from Core.Builders.GameObjectBuilder import GameObjectBuilder

# Classe responsável por representar a bola do Pong
class GunFire(GameObject):
    def __init__(self):
        super().__init__()

    def _awake(self):
        self.addComponent(SpriteComponent('assets/images/sprites/effects/fire01.png'))
        self.addComponent(KineticsComponent())
        self.addComponent(CollisionComponent())

    def _start(self):
        self.spawn = Game.findGameObjectWithName('spawner')
        self.setPosition(self.getPosition() - Vector2(self.width / 2, 0))
        
        self.collision = self.getComponent(CollisionComponent)
        self.kinetics = self.getComponent(KineticsComponent)
        self.kinetics.disableGravity()
        self.moveSpeedBase = Game.SPEED_BASE * 2 * Game.GAME_DIFFICULTY
        
        self.kinetics.setVelocity(Vector2(0, -self.moveSpeedBase))

    def _afterUpdated(self):
        if(self.y < 0):
            self.destroy()
    
    def destroy(self):
        super().destroy()
        self.spawn.removeEventListener('onSpawn', self._addColisionWith)
    
    def addCollisionWithEnemies(self):
        enemies_alive = self.spawn.transform.children
        
        for enemy in enemies_alive:
            self._addColisionWith(enemy)
        
        self.spawn.addEventListener('onSpawn', self._addColisionWith)
        
    def addCollisionWithPlayer(self):
        self._addColisionWith(Game.player)
    
    def _addColisionWith(self, gameObject):
        self.collision.addCollisionWith(gameObject)
        
    def onCollided(self, gameObject):
        from GameObjects.Enemies._Enemy import EnemyBase
        from GameObjects.Player import Player
        
        if(isinstance(gameObject, EnemyBase)):
            self.destroy()
        if(isinstance(gameObject, Player)):
            gameObject.damage()
            self.destroy()