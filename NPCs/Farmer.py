from .NPC import NPC

class Farmer(NPC):
    def __init__(self):
        super().__init__()
        self._name="Farmar 1"
        self._description="Toto je framar"
    
    def getName(self):
        return super().getName()

    def getDescription(self):
        return super().getDescription()
    
    def searchForWomen(self):
        answer = input("")
        return answer