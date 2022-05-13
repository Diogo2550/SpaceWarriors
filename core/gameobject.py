# coding= utf-8
from .pplay.gameobject import GameObject as GameObjectP
from .component import Component
from .vector import Vector2

# Classe customizada para manipula��o de gameobjects
class GameObject(GameObjectP):
    def __init__(self):
        super().__init__()
        self.components = []


#------------------------COMPONENTS METHODS-------------------------------
    def addComponent(self, component):
        if(isinstance(component, Component)):
            component.setGameObject(self)
            self.components.append(component)
        else:
            raise Exception(f"Instancia da classe {component.__class__} nao pertence ao tipo Component.")

    def getComponent(self, componentType):
        for component in self.components:
            if(isinstance(component, componentType)):
                return component


#------------------------LIFECICLE METHODS OF GAMEOBJECTS-------------------------------
    def awake(self):
        self._awake()

    def start(self):
        for component in self.components:
            component.start()
        self._start()

    def update(self):
        for component in self.components:
            component.update()

        self._update()
        self._afterUpdated()


#------------------------POSITION METHODS-------------------------------
    def setPosition(self, position):
        self.x = position.x
        self.y = position.y
        
    def getPosition(self):
        return Vector2(self.x, self.y)

    def translate(self, position):
        self.x += position.x
        self.y += position.y
    

#------------------------SIZE METHODS-------------------------------
    def setSize(self, witdh, height):
        self.width = witdh
        self.height = height


#------------------------LIFECICLE METHODS OF INSTANCES-------------------------------        
    def _awake(self):
        pass

    def _start(self):
        pass

    def _update(self):
        pass
	
    def _afterUpdated(self):
        pass