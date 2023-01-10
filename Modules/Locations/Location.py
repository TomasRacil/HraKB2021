from abc import ABC, abstractmethod
from random import choice


from ..Utils import get_text_by_id

class Location(ABC):
    
    def get_NPCs(self, player_level:int, posible_encounters:dict)->list:
        
        rand_choice = choice(list(posible_encounters.keys()))
        return [rand_choice(player_level) for i in range(posible_encounters[rand_choice])]
    
    @abstractmethod
    def __init__(self, player_level:int, posible_encounters: dict):
        
        self._name = get_text_by_id(self.__class__.__name__.lower()+"_name")
        self._description = get_text_by_id(self.__class__.__name__.lower()+"_description_"+str(player_level)) #TODO accessing different descriptions
        
        self._items = None
        self._NPCs = self.get_NPCs(player_level, posible_encounters)
        
    
    
    