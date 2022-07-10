from Core.Builders.GameObjectBuilder import GameObjectBuilder
from Core.Scene.Scene import Scene
from Core.Vector import Vector2
from Core.Game import Game

def build(name):
    scene = createScene(name)
    addChangeEvent(scene)
    return scene

def onActiveScene():
    from Core.GameStateManager import GameStateManager
    GameStateManager.instance.changeGameState(GameStateManager.GAMEPLAY)

def addChangeEvent(scene):
    scene.onActiveScene = onActiveScene
    
def createScene(name):
    from GameObjects.Player import Player
    from GameObjects.UI.LivesDisplay import LivesDisplay
    
    scene = Scene(name)
    
    # Player
    player = Player()
    player.setPosition(
        Vector2(Game.WINDOW_WIDTH / 2, Game.WINDOW_HEIGHT) -
		Vector2(player.width / 2, player.height)
    )
    
    # Display de vida
    lives_hub = LivesDisplay()
    
    scene.addGameObject(player)
    scene.addGameObject(lives_hub)
    
    return scene