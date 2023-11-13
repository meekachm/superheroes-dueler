import random
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
            abilities: List
            armors: List
            name: String
            starting_health: Integer
            current_health: Integer
        '''
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0
  
    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        if not self.abilities and not opponent.abilities:
            print("Draw")
            return

        while self.is_alive() and opponent.is_alive():
            self.take_damage(opponent.attack())
            if not opponent.is_alive():
                opponent.add_death(1)
                self.add_kill(1)
                print(f"{self.name} won!")
                return opponent

            opponent.take_damage(self.attack())
            if not self.is_alive():
                self.add_death(1)
                opponent.add_kill(1)
                print(f"{opponent.name} won!")
                return self

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)
    
    def attack(self):
        '''Calculate the total damage from all ability attacks.
            return: total_damage:Int
        '''
        total_damage = 0

        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage
   
    def add_armor(self, armor):
        '''Add armor to self.armors
        Armor: Armor Object
        '''
        self.armors.append(armor)

    def defend(self):
        '''Calculate the total block amount from all armor blocks.
        return: total_block:Int
        '''
        total_block = 0  

        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.'''
        total_defense = self.defend()
        damage_taken = damage - total_defense

        if damage_taken < 0:
            damage_taken = 0 
        
        self.current_health -= damage_taken 

    def is_alive(self):  
        '''Return True or False depending on whether the hero is alive or not.
        '''
        if self.current_health <= 0:
            return False 
        else:
            return True 
    
    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        self.abilities.append(weapon)

    def add_kill(self, num_kills):
        ''' Update self.kills by num_kills amount'''
        self.kills += num_kills

    def add_death(self, num_deaths):
        ''' Update deaths with num_deaths'''
        self.deaths += num_deaths

       
if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
