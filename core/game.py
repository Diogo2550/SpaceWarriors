# coding= utf-8
from core.pplay.window import *
from core.components.abstracts.drawingcomponent import *
from core.pplay.gameimage import *


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
        self.gameObjects.append(gameObject)

    def setBackground(self, backgroundPath):
        self.background = GameImage(backgroundPath)

    def setPlayer(self, player):
        self.player = player

    def start(self):
        for gameObject in self.gameObjects:
            gameObject.awake()

        for gameObject in self.gameObjects:
            gameObject.start()

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

    def getKeyboard():
        return Game.window.get_keyboard()

    def getMouse():
        return Game.window.get_mouse()

    def __bootstrap(self):
        window = Window(Game.WINDOW_WIDTH, Game.WINDOW_HEIGHT)
        window.set_title(Game.WINDOW_TITLE)

        Game.window = window
