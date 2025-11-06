from core.player import Entity
class Boss(Entity):
    def __init__(self, name, hp, speed, power, armor_rating,weapon):
        super().__init__(name, hp, speed, power, armor_rating)
        self.type = 'orc'
        self.weapon = weapon
        
    def heal(self):
        if self.hp < 11:
            self.hp += 30
        
    def speak(self):
        print(f"i'm the orc {self.name}")
        
    def attack(self):
        pass