from abc import ABC,abstractmethod
import random
import time


class Entity(ABC):
    def __init__(self,name,hp,speed,power,armor_rating):
        self.name = name
        self.hp = hp
        self.speed = speed
        self.power = power
        self.armor_rating = armor_rating
    
    @abstractmethod    
    def speak(self):
        pass
    
    @abstractmethod
    def attack(self):
        pass
    
class Player(Entity):
    def __init__(self, name, hp, speed, power, armor_rating,profession):
        super().__init__(name, hp, speed, power, armor_rating)
        self.profession = profession
        
        if self.profession == 'healer':
            self.hp += 10
        else:
            self.power += 2
        
    def speak(self):
        print(f"hi, i'm {self.name}")
    
    def roll_dice(self,sides):
        return random.randint(1,sides)
    
    def attack(self,deffendr):
        attack = self.speed + self.roll_dice(20)
        attack = self.attack()
        print(f'the attack is {attack}')
        time.sleep(1.5)
        
        if attack > deffendr.armor_rating:
            print('hit!')
            
            # calculating damage
            damage = self.power + self.roll_dice(6)
            print(f' the damage is {damage}')
            time.sleep(1.5)
            
            # reducing deffender hp
            deffendr.hp -= damage
            print(f' current deffender hp  is {deffendr.hp}')
            print()
            time.sleep(1.5)





        