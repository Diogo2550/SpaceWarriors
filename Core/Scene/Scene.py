# coding=utf-8

from Core.Scene.SceneManager import SceneManager
from Core.Components.Abstracts.DrawingComponent import DrawingComponent
from Core.GameObject import GameObject

class Scene:
    def __init__(self, sceneName):
        # Objetos padrões usados para iniciar a cena, não deverão ser modificados
        self.__gameObjects = []
		# GameObjects que foram iniciados pela cena. Os mesmos podem ser destruídos
        self.__sceneObjects = []

        self.__sceneName = sceneName
        self.__activated = False

        SceneManager.addScene(self)
        SceneManager.onSceneChange(self.__onSceneChangeHandler)
        
# ------------------------- GAMEOBJECT ----------------------
    def addGameObject(self, gameObject: GameObject):
        ''' Adiciona uma gameobject à cena.'''
        self.__gameObjects.append(gameObject)
        return self
    
    def addGameObjectToScene(self, gameObject: GameObject, forceInit = True):
        ''' Adiciona uma gameobject à cena em execução '''
        from copy import deepcopy
        
        gameObject.forceInit()
        
        self.__sceneObjects.append(gameObject.copy())
    
    def removeGameObject(self, gameObject):
        self.__sceneObjects.remove(gameObject)

    def getGameObjects(self):
        return self.__sceneObjects

    def getGameObjectWithName(self, name):
        for gameObject in self.__sceneObjects:
            if(gameObject.getName() == name):
                return gameObject
        return None

# --------------------- MANIPULADORES DE CENA ----------------
    def getSceneName(self):
        return self.__sceneName

    def activeScene(self):
        self.__enableScene()

# ---------------------- LIFE CYCLE ---------------------------
    def play(self):        
        # Update
        for gameObject in self.__sceneObjects:
            gameObject.update()

        # Desenho
        for gameObject in self.__sceneObjects:
            gameObject.draw()

# ------------------------- GAMEOBJECT ----------------------
    def __startGameObjects(self):
        for gameObject in self.__gameObjects:
            self.addGameObjectToScene(gameObject, False)
        
        for gameObject in self.__sceneObjects:
            gameObject.awake()

        for gameObject in self.__sceneObjects:
            gameObject.start()
    
    def __destroyAllGameObjects(self):
        for gameObject in self.__sceneObjects:
            gameObject.destroy()
    
# --------------------- MANIPULADORES DE CENA ----------------
    def __enableScene(self): 
        if(not self.__activated):
            self.__startGameObjects()
            self.__activated = True
        
    def __disableScene(self):
        if(self.__activated):
            self.__destroyAllGameObjects()
            self.__activated = False

# ---------------------- EVENTS ---------------------------
    def onActiveScene(self):
        pass
    
    def __onSceneChangeHandler(self, fromScene, toScene):
        if(toScene.getSceneName() == self.__sceneName):
            self.activeScene()
            self.onActiveScene()
        elif(fromScene and fromScene.getSceneName() == self.__sceneName):
            self.__disableScene()
