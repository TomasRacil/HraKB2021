from abc import ABC, abstractmethod
from ..Utils import get_text_by_id


class NPC(ABC):
    
    @abstractmethod
    def __init__(self, level:int, type:str, vitality:int, strength:int, speed:int, magicka:int, endurance:int):
        
        self._name = get_text_by_id(self.__class__.__name__.lower()+"_name")
        self._description = get_text_by_id(self.__class__.__name__.lower()+"_description_"+str(level)) #TODO accessing different descriptions
        
        self._level = level
        self._type = type
        self._vitality = vitality
        self._strength = strength
        self._speed = speed
        self._magicka = magicka
        self._endurance =endurance
        
        #TODO Balance values
        self._HP = level*vitality*10
        self._stamina = level*endurance
        self._mana = level*magicka*10
        self._carry_weight = level*(magicka/2+strength+endurance/2)*10
    
    def __repr__(self) -> str:
        representation = f"""
        {self._name}
        {self._description}
        """
        return representation
    
    def get_stats(self)-> str:
        pass
    
    def getName(self):
        return self._name
    
    def getDescription(self):
        return self._description