from core.player import Entity

class Goblin(Entity):
    def __init__(self, name, hp, speed, power, armor_rating,weapon):
        super().__init__(name, hp, speed, power, armor_rating)
        self.type = 'goblin'
        self.weapon = weapon
        
    def speak(self):
        print(f"i'm the orc {self.name}")
        
    def attack(self):
        pass
