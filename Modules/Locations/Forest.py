from random import choice

from ..NPCs import Bandit
from .Location import Location

class Forest(Location):
    
        
    def __init__(self, player_level: int):
        posible_encounters = {
            Bandit:2
            }
        super().__init__(player_level, posible_encounters)
        