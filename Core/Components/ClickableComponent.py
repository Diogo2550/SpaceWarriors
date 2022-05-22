# coding= utf-8
from Core.Vector import *
from Core.Game import *

class ClickableComponent(Component):
    ''' Componente que injeta os eventos de click do mouse no GameObject. 
    Apenas o LMB será levado em consideração ''' 
 
    def __init__(self):
        super().__init__()
        self.keyPressed = False
        self.dataKeyPressed = {
			'start': None,
			'finish': None
		}
        self.mouse = Game.getMouse()
        
    def update(self):
        if(self.mouse.is_button_pressed(1)):
            if(self.mouse.is_over_object(self.gameObject) and not self.keyPressed):
                self.__onKeyDown()
                
            self.__onKeyPressed()
        else:
            if(self.keyPressed):
                self.__onKeyUp()
                
    def clickDeltaTime(self):
        ''' Obtém o tempo ocorrido entre o início e o fim do click. Retorna -1 se o DeltaTima não estiver definido '''
        if(self.dataKeyPressed['start'] and self.dataKeyPressed['finish']):
            return self.dataKeyPressed['finish'] - self.dataKeyPressed['start']
        return -1
        
    def __onClick(self):
        self.gameObject.onClick()
    
    def __onKeyDown(self):
        self.keyPressed = True
        self.dataKeyPressed['start'] = Game.window.time_elapsed()
        self.dataKeyPressed['finish'] = None
        self.gameObject.onKeyDown()
    
    def __onKeyPressed(self):
        self.gameObject.onKeyPressed()
    
    def __onKeyUp(self):
        self.dataKeyPressed['finish'] = Game.window.time_elapsed()
        self.keyPressed = False
        
        self.gameObject.onKeyUp()
        