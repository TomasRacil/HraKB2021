from abc import ABC, abstractmethod


class NPC(ABC):
    
    @abstractmethod
    def __init__(self):
        self._description = "Defaultni popis NPC"
        self._name = "Defaultni jmeno"
        
    @abstractmethod 
    def getName(self):
        return self._name
    @abstractmethod
    def getDescription(self):
        return self._description