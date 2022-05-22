# coding= utf-8
from Core.PPlay.window import *
from Core.Components.Abstracts.DrawingComponent import *
from Core.PPlay.gameimage import *
from Core.Vector import Vector2


class Game:

    # Configurações da janela
    WINDOW_TITLE = 'Pong'
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 600
    DELTA_TIME = 0

    SPEED_MULTIPLIER = 1

    window = None

    def __init__(self):
        self.gameObjects = []
        self.player = None
        self.__bootstrap()

    def addGameObject(self, gameObject):
        ''' Adiciona uma nova instância de um gameobject para fazer parte do Game '''
        self.gameObjects.append(gameObject)

    def setBackground(self, backgroundPath):
        ''' Adiciona um background para o Game '''
        self.background = GameImage(backgroundPath)

    def setPlayer(self, player):
        ''' Seta o jogador para que o mesmo possa ser visto globalmente '''
        self.player = player
    
    def getWindowCenter():
        ''' Obtém o ponto central da janela do jogo '''
        return Vector2(
            Game.WINDOW_WIDTH / 2, 
            Game.WINDOW_HEIGHT / 2
        )

    def start(self):
        for gameObject in self.gameObjects:
            gameObject.awake()

        for gameObject in self.gameObjects:
            gameObject.start()

        self.__gameLoop()

    def getKeyboard():
        ''' Obtém a atual instância do teclado sendo utilizada '''
        return Game.window.get_keyboard()

    def getMouse():
        ''' Obtém a atual instância do mouse sendo utilizada '''
        return Game.window.get_mouse()

    def __bootstrap(self):
        window = Window(Game.WINDOW_WIDTH, Game.WINDOW_HEIGHT)
        window.set_title(Game.WINDOW_TITLE)

        Game.window = window
        
    def __gameLoop(self):
        while(True):
            Game.DELTA_TIME = self.window.delta_time()

            # Inputs


            # Update
            for gameObject in self.gameObjects:
                gameObject.update()

            # Desenho
            try:
                self.background.draw()
            except Exception:
                Game.window.set_background_color((0, 0, 0))                

            for gameObject in self.gameObjects:
                drawingComponent = gameObject.getComponent(DrawingComponent)
                if(drawingComponent != None):
                    drawingComponent.draw()

            Game.window.update()