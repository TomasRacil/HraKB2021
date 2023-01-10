from random import randrange

from NPCs import *

class Encounter:
    def __init__(self, player_level):
        self.location = None #TODO get location from locations
        self.NPCs = []
        for number in randrange(2):
            