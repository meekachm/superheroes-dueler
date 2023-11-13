import random  # Import the random module
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        '''Instance properties:
            abilities: List
            armors: List
            name: String
            starting_health: Integer
            current_health: Integer
        '''
        # abilities and armors don't have starting values,
        # and are set to empty lists on initialization
        self.abilities = list()
        self.armors = list()
        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
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

        # We use the append method to add ability objects to our list.
        self.abilities.append(ability)
    
    def attack(self):
        '''Calculate the total damage from all ability attacks.
            return: total_damage:Int
        '''

        # start our total out at 0
        total_damage = 0
        # loop through all of our hero's abilities
        for ability in self.abilities:
            # add the damage of each attack to our running total
            total_damage += ability.attack()
            # return the total damage
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
        total_block = 0  # Initialize the total block to zero

        # Iterate through the armor objects and calculate their block amounts
        for armor in self.armors:
            total_block += armor.block()

        return total_block

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.'''
        total_defense = self.defend()  # Calculate the total defense
        damage_taken = damage - total_defense

        if damage_taken < 0:
            damage_taken = 0  # Make sure damage taken cannot be negative
        
        self.current_health -= damage_taken # Update current health after subtracting defense

    def is_alive(self):  
        '''Return True or False depending on whether the hero is alive or not.
        '''
        # TODO: Check the current_health of the hero.
        # if it is <= 0, then return False. Otherwise, they still have health
        # and are therefore alive, so return True
        if self.current_health <= 0:
            return False  # The hero is not alive
        else:
            return True  # The hero is alive
    
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
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
