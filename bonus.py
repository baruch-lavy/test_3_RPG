from core.player import Player
from core.orc import Orc
from core.goblin import Goblin
import random
import time

class Game:
    def __init__(self,name):
        self.name = name
        
    def show_menu(self):
        while True:
            choose = input('enter your choose please (battle,exit): ')
            if choose.lower() in ['battle','exit']:
                break
        return choose
    
    def start(self):
        user_choose = self.show_menu()
        if user_choose == 'exit':
            print('bye bye')
            return
        else:
            print('the buttle is about to begin')
            palyer = self.create_player()
            monster = self.choose_random_monster()
            self.battle(palyer,monster)
    
    def create_player(self):
        professions = ['healer','warrior']
        random_num = random.randint
        speed = random_num(5,10)
        power = random_num(5,10)
        armor_rating = random_num(5,15)
        profession = professions[random_num(0,1)]
        
        #creating and returning player
        player = Player('baruch',50,speed,power,armor_rating,profession)
        return player
    
    def choose_random_monster(self):
        monster = ['orc','goblin'][random.randint(0,1)]
        if monster == 'orc':
            return self.create_orc()
        else:
            return self.create_goblin()
    
    def create_orc(self):
        random_num = random.randint
        weapon = ['sword','dagger','axe'][random_num(0,2)]
        
        return Orc('priest',50,random_num(0,5),random_num(10,15),random_num(2,8),weapon)
    
    def create_goblin(self):
        random_num = random.randint
        weapon = ['sword','dagger','axe'][random_num(0,2)]
        
        return Goblin('monk',20,random_num(5,10),random_num(5,10),1,weapon)
    
    def roll_dice(self,sides):
        return random.randint(1,sides)
        
    playing_in_maze = True
    def maze_buttle(self,attacker:Orc | Goblin,deffendr:Orc | Goblin):
        playing = True
          
        while playing:
            print(f'the attacker is {attacker.name}')  
            print(f'the deffender is {deffendr.name}')  
            time.sleep(2) 
            
            # attach logic
            attack = attacker.speed + self.roll_dice(20)
            print(f'the attack is {attack}')
            time.sleep(1.5)
            
            if attack > deffendr.armor_rating:
                print('hit!')
                
                # calculating damage
                damage = attacker.power + self.roll_dice(6)
                
                # checking is the attacker is monster
                if hasattr(attacker,'type'):
                    if attacker.weapon == 'dagger':
                        damage *= 0.5
                    elif attacker.weapon == 'sword':
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
                
                # checking winner/looser
                if deffendr.hp <= 0:
                    print(f'game over ,winner: {attacker.__dict__}, looser: {deffendr.__dict__}')
                    playing = False
                    Game.playing_in_maze = False
                    
                if attacker.hp <= 0:
                    print(f'game over ,winner: {deffendr.__dict__}, looser: {attacker.__dict__}')
                    playing = False
                    Game.playing_in_maze = False
                    
            
            # swap attacker/deffender      
            else:
                attacker,deffendr = deffendr,attacker

        
    def battle(self,player:Player,monster:Orc | Goblin):
        
        # rolling dice
        player_result = self.roll_dice(6)
        monster_result = self.roll_dice(6)
        
        # starting game and check starter
        if player_result >= monster_result:
            attacker = player
            deffendr = monster
        else:
            attacker = monster
            deffendr = player
        
        playing = True
          
        while playing:
            print(f'the attacker is {attacker.name}')  
            print(f'the deffender is {deffendr.name}')  
            time.sleep(2) 
            
            # attach logic
            attack = attacker.speed + self.roll_dice(20)
            print(f'the attack is {attack}')
            time.sleep(1.5)
            
            if attack > deffendr.armor_rating:
                print('hit!')
                
                # calculating damage
                damage = attacker.power + self.roll_dice(6)
                
                # checking is the attacker is monster
                if hasattr(attacker,'type'):
                    if attacker.weapon == 'dagger':
                        damage *= 0.5
                    elif attacker.weapon == 'sword':
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
                
                if hasattr(deffendr,'type'):
                    if deffendr.type == 'goblin' and 0 < deffendr.hp < 10:
                        print('entering maze')
                        maze = [None for _ in range(8)]
                        for i in range(len(maze)):
                            random_num = random.randint(1,2)
                            if i % random_num == 0:
                                maze[i] = self.create_orc()
                            else:
                                maze[i] = self.create_goblin()
                        
                        for monster in maze:
                            if Game.playing_in_maze:
                                self.maze_buttle(deffendr,monster)
                
                # checking winner/looser
                if deffendr.hp <= 0:
                    print(f'game over ,winner: {attacker.__dict__}, looser: {deffendr.__dict__}')
                    playing = False
                    
                if attacker.hp <= 0:
                    print(f'game over ,winner: {deffendr.__dict__}, looser: {attacker.__dict__}')
                    playing = False
            
            # swap attacker/deffender      
            else:
                attacker,deffendr = deffendr,attacker
                        
                    
            

