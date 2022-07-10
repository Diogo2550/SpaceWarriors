# coding= utf-8
from Core.GameObject import GameObject
from Core.Game import Game
from Core.Vector import Vector2

from Core.Components.KineticsComponent import KineticsComponent
from Core.Components.SpriteComponent import SpriteComponent

from Core.Builders.GameObjectBuilder import GameObjectBuilder

from GameObjects.GunFire import GunFire
from Core.Components.ClickableComponent import ClickableComponent

class Player(GameObject):
    ''' Classe de GameObject que será controlada pelo jogador '''
    def __init__(self):
        super().__init__()
        self.addComponent(KineticsComponent())
        self.addComponent(SpriteComponent('assets/images/sprites/player_ship2_blue.png'))
        
        self.__lastFire = 0
        self.fireReload = 0

    def _awake(self):
        self.kinetics = self.getComponent(KineticsComponent)
        self.sprite = self.getComponent(SpriteComponent)
        
        Game.setPlayer(self)

    def _start(self):
        self.addComponent(ClickableComponent())
        self.move_speed = Game.SPEED_BASE
        self.kinetics.disableGravity()
        
        self.fireReload = .5 / Game.GAME_DIFFICULTY

    def _update(self):
        keyboard = Game.getKeyboard()
        
        # Movimentação
        velocity = Vector2.zero()
        if(keyboard.key_pressed('W') and self.getPosition().y > 0):
            velocity.y = -1
        elif(keyboard.key_pressed('S') and self.getPosition().y < Game.WINDOW_HEIGHT - self.height):
            velocity.y = 1
            
        if(keyboard.key_pressed('A') and self.getPosition().x > 0):
            velocity.x = -1
        elif(keyboard.key_pressed('D') and self.getPosition().x < Game.WINDOW_WIDTH - self.width):
            velocity.x = 1
        
        self.kinetics.setVelocity((velocity.normalize()) * Game.SPEED_BASE)
        # Fim movimento
        
        # Tiro
        self.__lastFire -= Game.DELTA_TIME 
        
        if(keyboard.key_pressed('SPACE') and self.__lastFire < 0):
            self.fire()
        # Fim tiro
        
    def _afterUpdated(self):
        if(not Game.elementOnWindow(self)):
            self.translate(self.kinetics.velocity.normalize() * Game.SPEED_BASE)
            self.kinetics.setVelocity(Vector2.zero())
            
    def fire(self):
        self.__lastFire = self.fireReload

        fire = GameObjectBuilder.startBuild(GunFire())\
                .setPosition(self.getPosition() + Vector2(self.width / 2, 0))\
                .build()

        self.addChild(fire)
        
    def onClick(self):
        from Core.Scene.SceneManager import SceneManager
        
        current = SceneManager.getCurrentScene().getSceneName()
        SceneManager.changeScene('gameplay2' if current == 'gameplay' else 'gameplay')