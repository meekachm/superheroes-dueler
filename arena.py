from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        self.team_one = Team("Team One")
        self.team_two = Team("Team Two")

    def create_ability(self):
        '''Prompt for Ability information.
        return Ability with values from user Input
        '''
        name = input("What is the ability name?  ")
        max_damage = input(
            "What is the max damage of the ability?  ")

        return Ability(name, max_damage)


    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        name = input("What is the weapon name?  ")
        max_damage = input(
            "What is the max damage of the weapon?  ")
    
        return Weapon(name, max_damage)
  
    def create_armor(self):
        '''Prompt user for Armor information
        return Armor with values from user input.
        '''
        name = input("What is the armor name?  ")
        max_block = input(
            "What is the max defense of the armor?  ") 
        return Armor(name, max_block)

    def create_hero(self):
        '''Prompt user for Hero information
        return Hero with values from user input.
        '''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                ability = self.create_ability()
                hero.add_ability(ability)
            elif add_item == "2":
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
            elif add_item == "3":
                armor = self.create_armor()
                hero.add_armor(armor)
        return hero

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        '''Prompt the user to build team_two'''
        numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        self.team_one.attack(self.team_two)

    def show_stats(self):
        '''Prints team statistics to terminal.'''
        print("\n")
        print(f"{self.team_one.name} statistics: ")
        self.team_one.stats()
        print("\n")
        print(f"{self.team_two.name} statistics: ")
        self.team_two.stats()
        print("\n")

        self.calculate_kd(self.team_one)
        self.calculate_kd(self.team_two)

        self.surviving_heroes(self.team_one)
        self.surviving_heroes(self.team_two)

    def calculate_kd(self, team):
        '''Calculate and print the average K/D ratio for the given team.'''
        team_kills = sum(hero.kills for hero in team.heroes)
        team_deaths = sum(hero.deaths for hero in team.heroes)

        if team_deaths == 0:
            team_deaths = 1  

        print(f"{team.name} average K/D was: {team_kills/team_deaths}")

    def surviving_heroes(self, team):
        '''List and print the heroes from the given team that survived.'''
        for hero in team.heroes:
            if hero.is_alive():
                print(f"Survived from {team.name}: {hero.name}")


if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()