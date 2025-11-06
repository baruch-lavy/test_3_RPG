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
    
    def attack(self):
       pass





        