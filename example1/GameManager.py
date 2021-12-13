class GameManager:
    def __init__(self):
        self.currentMap = None
        self.renderableObjects = []
        
    def setCurrentMap(self, map):
        self.currentMap = map 
    