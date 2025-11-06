from core.player import Entity
import random
import time
class Orc(Entity):
    def __init__(self, name, hp, speed, power, armor_rating,weapon):
        super().__init__(name, hp, speed, power, armor_rating)
        self.type = 'orc'
        self.weapon = weapon
        
    def speak(self):
        print(f"i'm the orc {self.name}")
    
    def roll_dice(self,sides):
        return random.randint(1,sides)
      
    def attack(self):
        pass