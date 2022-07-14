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
    from GameObjects.Obstacles._Obstacle import ObstacleBase
    from GameObjects.Levels.Level import Level
    from GameObjects.Levels.LevelManager import LevelManager
    
    scene = Scene(name)
    
    # Player
    player = Player()
    player.setPosition(
        Vector2(Game.WINDOW_WIDTH / 2, Game.WINDOW_HEIGHT) -
		Vector2(player.width / 2, player.height)
    )
    
    # ------------------------------- HUBS --------------------------------
    # Display de vida
    lives_hub = LivesDisplay()
    lives_hub.setName('liver_hub')
    
    score_hub = ScoreDisplay()
    score_hub.setName('score_hub')
    
    timer_hub = TimerDisplay()
    timer_hub.setName('timer_hub')
    
    
    
    
    # ------------------------------- SPAWNS --------------------------------
    enemy_spawner = Spawner()
    enemy_spawner.setName('enemy_spawner')
    
    enemy_1 = EnemyDefault()
    enemy_2 = EnemyDefault()
    enemy_2.difficulty = 4
    enemy_3 = EnemyDefault()
    enemy_3.difficulty = 8
    
    enemy_spawner.add(enemy_1)
    enemy_spawner.add(enemy_2)
    enemy_spawner.add(enemy_3)
    
    
    obstacle_spawner = Spawner()
    obstacle_spawner.setName('obstacle_spawner')
    obstacle_spawner.active()
    
    meteor_1 = ObstacleBase()
    
    obstacle_spawner.add(meteor_1)
    
    
    
    
    # ------------------------------- LEVELS --------------------------------
    level_manager = LevelManager()
    
    level_1 = Level()
    level_1.setSoundTrack('assets/songs/soundtrack/fase01.mp3')
    level_1.addSpawner(enemy_spawner)
    
    level_manager.addLevel(level_1)
    
    
    
    
    # ------------------------------- ADICIONAR A CENA --------------------------------
    scene.addGameObject(player)
    scene.addGameObject(lives_hub)
    scene.addGameObject(score_hub)
    scene.addGameObject(timer_hub)
    scene.addGameObject(obstacle_spawner)
    scene.addGameObject(level_manager)
    
    return scene