class GameStateManager:
    
    __events = []
    
    instance = None
    
#-------------------- Game States ------------------
    MAIN_MENU = 1
    
    GAMEPLAY = 10
    PAUSED = 11
    
    __currentGameState = None
   
    def __init__(self):
        from Core.Scene.SceneManager import SceneManager
                
        if(self.instance == None):
            GameStateManager.instance = self
            SceneManager.onSceneChange(self.sceneChangeHandler)
    
    def changeGameState(self, gameState):
        self.__currentGameState = gameState
        self.onChangeHandler()        
    
    def onChange(self, func):
        self.events.append(func)
    
    def onChangeHandler(self):
        for event in self.__events:
            event(self.__currentGameState)
    
    def sceneChangeHandler(self, fromScene, toScene):
        self.__events = []