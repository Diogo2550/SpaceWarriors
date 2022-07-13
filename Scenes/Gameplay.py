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
    from GameObjects.UI.ScoreDisplay import ScoreDisplay
    from GameObjects.UI.TimerDisplay import TimerDisplay
    from GameObjects.Spawner import Spawner
    from GameObjects.Enemies.EnemyDefault import EnemyDefault
    
    scene = Scene(name)
    
    # Player
    player = Player()
    player.setPosition(
        Vector2(Game.WINDOW_WIDTH / 2, Game.WINDOW_HEIGHT) -
		Vector2(player.width / 2, player.height)
    )
    
    # Display de vida
    lives_hub = LivesDisplay()
    lives_hub.setName('liver_hub')
    
    score_hub = ScoreDisplay()
    score_hub.setName('score_hub')
    
    timer_hub = TimerDisplay()
    timer_hub.setName('timer_hub')
    
    spawner = Spawner()
    spawner.setName('spawner')
    
    enemy_1 = EnemyDefault()
    enemy_2 = EnemyDefault()
    enemy_2.difficulty = 4
    enemy_3 = EnemyDefault()
    enemy_3.difficulty = 8
    
    spawner.addEnemy(enemy_1)
    spawner.addEnemy(enemy_2)
    spawner.addEnemy(enemy_3)
    
    scene.addGameObject(player)
    scene.addGameObject(lives_hub)
    scene.addGameObject(score_hub)
    scene.addGameObject(timer_hub)
    scene.addGameObject(spawner)
    
    return scene