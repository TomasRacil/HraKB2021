from .NPC import NPC

class Bandit(NPC):
    def __init__(self, level:int, type = "Enemy", vitality:int = 4, strength:int = 3, speed:int =2, magicka:int = 0, endurance:int = 2):
        super().__init__(
            level = level,
            type = type,
            vitality= vitality,
            strength=strength,
            speed=speed,
            magicka=magicka,
            endurance=endurance
        )
    
    