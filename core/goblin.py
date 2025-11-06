from core.player import Entity
import random
import time

class Goblin(Entity):
    def __init__(self, name, hp, speed, power, armor_rating,weapon):
        super().__init__(name, hp, speed, power, armor_rating)
        self.type = 'goblin'
        self.weapon = weapon
        
    def speak(self):
        print(f"i'm the orc {self.name}")
    
    def roll_dice(self,sides):
        return random.randint(1,sides)
        
    def attack(self,deffendr):
         # attach logic
        attack = self.speed + self.roll_dice(20)
        print(f'the attack is {attack}')
        time.sleep(1.5)
        
        if attack > deffendr.armor_rating:
            print('hit!')
            
            # calculating damage
            damage = self.power + self.roll_dice(6)
            
            # checking is the self is monster
            if hasattr(self,'type'):
                if self.weapon == 'dagger':
                    damage *= 0.5
                elif self.weapon == 'sword':
                    damage *= 1
                else:
                    damage *= 1.5
            print(f' the damage is {damage}')
            time.sleep(1.5)
            
            # reducing deffender hp
            deffendr.hp -= damage
            print(f' current deffender hp  is {deffendr.hp}')
            print()
            time.sleep(1.5)
