from Core.Builders.GameObjectBuilder import GameObjectBuilder
from Core.Scene.Scene import Scene
from Core.Vector import Vector2
from Core.Game import Game

from Core.Components.SpriteComponent import SpriteComponent

from GameObjects.UI._Button import UIButton
from GameObjects.UI._Text import UIText

def build(name):
    scene = createScene(name)
    addChangeEvent(scene)
    return scene

def startGame():
    from Core.Scene.SceneManager import SceneManager
    
    SceneManager.changeScene('gameplay')

def continueGame():
    print('Funcionalidade não implementada!')

def closeGame():
    Game.window.close()

def settings():
    print('Funcionalidade não implementada!')

def onActiveScene():
    from Core.GameStateManager import GameStateManager
    GameStateManager.instance.changeGameState(GameStateManager.MAIN_MENU)

def addChangeEvent(scene):
    scene.onActiveScene = onActiveScene

def createScene(name):
    scene = Scene(name)
    
    # Start button
    start_button = GameObjectBuilder().startBuild(UIButton())\
        .addComponent(SpriteComponent('assets/images/sprites/ui/button_green.png'))\
        .setName('start_button')\
        .setPosition(Game.getWindowCenter() - GameObjectBuilder().instance.getObjectCenter())\
        .build()
    start_button.onClick = startGame
    start_button.setText('Novo Jogo')
    
    # Continue button
    continue_button = GameObjectBuilder().startBuild(UIButton())\
        .addComponent(SpriteComponent('assets/images/sprites/ui/button_blue.png'))\
        .setName('continue_button')\
        .setPosition(
			Game.getWindowCenter() - 
			GameObjectBuilder().instance.getObjectCenter() + 
			Vector2(0, GameObjectBuilder.instance.getSize().y + 20)
		)\
        .build()
    continue_button.onClick = continueGame
    continue_button.setText('Continuar')
    
    # Settings button
    settings_button = GameObjectBuilder().startBuild(UIButton())\
        .addComponent(SpriteComponent('assets/images/sprites/ui/button_yellow.png'))\
        .setName('settings_button')\
        .setPosition(
			Game.getWindowCenter() - 
			GameObjectBuilder().instance.getObjectCenter() + 
			Vector2(0, GameObjectBuilder.instance.getSize().y * 2 + 20 * 2)
		)\
        .build()
    settings_button.onClick = settings
    settings_button.setText('Opções')
        
    # Close button
    close_button = GameObjectBuilder().startBuild(UIButton())\
        .addComponent(SpriteComponent('assets/images/sprites/ui/button_red.png'))\
        .setName('close_button')\
        .setPosition(
			Game.getWindowCenter() - 
			GameObjectBuilder().instance.getObjectCenter() + 
			Vector2(0, GameObjectBuilder.instance.getSize().y * 3 + 20 * 3)
		)\
        .build()
    close_button.onClick = closeGame
    close_button.setText('Sair')
    
    # Game Title
    title = Game.WINDOW_TITLE
    game_title = GameObjectBuilder().startBuild(UIText())\
        .setName('game_title')\
        .setPosition(
			Game.getWindowCenter() -
			Vector2(len(title) * 24, Game.WINDOW_HEIGHT / 3)
		).build()
    game_title.configureText(120, (24, 42, 168))
    game_title.setText(title)
    
    # Adição dos objetos na cena
    scene\
        .addGameObject(start_button)\
        .addGameObject(continue_button)\
        .addGameObject(settings_button)\
        .addGameObject(close_button)\
        .addGameObject(game_title)
    return scene