# coding=utf-8
from Core.GameObject import GameObject

class SceneManager:

    __scenes = {}
    __currentScene = None
    __onSceneChangeEvent = []

    @classmethod
    def addScene(cls, scene):
        cls.__scenes[scene.getSceneName()] = scene

    @classmethod
    def getSceneByIndex(self, index: int):
        sceneName = list(self.__scenes.keys())[index]
        return self.__scenes[sceneName]

    @classmethod
    def changeScene(cls, sceneName: str):
        newScene = cls.__scenes[sceneName]
        
        last_scene = cls.getCurrentScene()
        cls.__currentScene = newScene
        cls.sceneChangeHandler(last_scene, newScene)
        
    @classmethod
    def addGameObjectToCurrentScene(cls, gameObject: GameObject):
        cls.getCurrentScene().addGameObjectToScene(gameObject)

    @classmethod
    def getCurrentScene(cls):
        return cls.__currentScene

    @classmethod
    def onSceneChange(cls, function):
        cls.__onSceneChangeEvent.append(function)

    @classmethod
    def sceneChangeHandler(cls, fromScene, toScene):
        for event in cls.__onSceneChangeEvent:
            event(fromScene, toScene)
