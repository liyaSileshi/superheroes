import random

class Ability:

    def __init__(self, name, attack_strength):
      '''Create Instance Variables:
          name:String
          max_damage: Integer
       '''
      self.name = name
      self.max_damage = attack_strength

    def attack(self):
      ''' Return a value between 0 and the value set by self.max_damage.'''

      # Return an attack value between 0 and the full attack.
      # Hint: The constructor initializes the maximum attack value.
      return random.randint(0, self.max_damage)

class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        self.name = name
        self.max_block = max_block

    def block(self):
        return random.randint(0, self.max_block)

class Hero:
    def __init__(self, name, starting_health=100):
      '''Instance properties:
          abilities: List
          armors: List
          name: String
          starting_health: Integer
          current_health: Integer
      '''
      self.name = name
      self.starting_health = starting_health
      self.current_health = starting_health
      self.deaths = 0
      self.kills = 0
      self.abilities = []
      self.armors = []


    def add_ability(self, ability):
      ''' Add ability to abilities list '''
      # TODO: Add ability object to abilities:List
      self.abilities.append(ability)

    def add_kill(self, num_kills):
        ''' Update kills with num_kills'''
    # TODO: This method should add the number of kills to self.kills
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        ''' Update deaths with num_deaths'''
    # TODO: This method should add the number of deaths to self.deaths
        self.deaths +=num_deaths

    def attack(self):
      '''Calculate the total damage from all ability attacks.
          return: total:Int
      '''
      # TODO: This method should run Ability.attack() on every ability
      # in self.abilities and returns the total as an integer.
      total = 0
      for ability in self.abilities:
        total += ability.attack()

      #print(total)
      return total

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        # This method will append the weapon object passed in as an
        # argument to self.abilities.
        # This means that self.abilities will be a list of
        # abilities and weapons.
        self.abilities.append(weapon)



    def add_armor(self, armor):
        '''Add armor to self.armors
        Armor: Armor Object
        '''
        # TODO: Add armor object that is passed in to `self.armors`
        self.armors.append(armor)

    #ask for help on this function
    def defend(self, damage_amt=0):
        '''Runs `block` method on each armor.
            Returns sum of all blocks
        '''

  # TODO: This method should run the block method on each armor in self.armors
        total = 0
        for armor in self.armors:
            total += armor.block()

        return abs(total - damage_amt)


    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        # Create a method that updates self.current_health to the current
        # minus the the amount returned from calling self.defend(damage).
        remains = self.defend(damage)
        self.current_health -= remains

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.
        '''
        # Check whether the hero is alive and return true or false
        return self.current_health > 0


    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        # Fight each hero until a victor emerges.
        # Print the victor's name to the screen.
        while self.is_alive() and opponent.is_alive():
            #print(self.current_health)
            #print(opponent.current_health)
            # if ability lists are empty https://stackoverflow.com/questions/53513/how-do-i-check-if-a-list-is-empty
            if not self.abilities and not opponent.abilities:
                print("Draw")
                break

            a1 = self.attack()
            a2 = opponent.attack()



            opponent.take_damage(a1)

            if not opponent.is_alive():

                self.add_kill(1)
                opponent.add_deaths(1)
                print(self.name +" won")
                print(opponent.name + " is dead")


            self.take_damage(a2)
            if not self.is_alive():
                opponent.add_kill(1)
                self.add_deaths(1)
                print(opponent.name +" won")
                print(self.name + " is dead")


class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        #Use what you learned to complete this method.
        return random.randint(self.max_damage//2, self.max_damage)


class Team:
    def __init__(self, name):
        ''' Initialize your team with its team name
        '''
        self.name = name
        self.heroes = []

    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        for name in self.heroes:
            self.heroes.remove(name)
        else:
            return 0

    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
        # Add the Hero object that is passed in to the list of heroes in
        # self.heroes
        self.heroes.append(hero)

    def get_alive(self):
        alive_list = []
        for hero in self.heroes:
            if hero.is_alive():
                alive_list.append(hero)
        return alive_list
    def attack(self, other_team):
        ''' Battle each team against each other.'''
        #  Randomly select a living hero from each team and have
        # them fight until one or both teams have no surviving heroes.

        while len(self.get_alive()) > 0 and len(other_team.get_alive()) > 0:
            rand_hero1 = random.choice(self.get_alive())
            rand_hero2 = random.choice(other_team.get_alive())
            rand_hero1.fight(rand_hero2)

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        # This method should reset all heroes health to their
        # original starting value.
        for hero in self.heroes:
            hero.current_health = health

    def stats(self):
        '''Print team statistics'''
        # This method should print the ratio of kills/deaths for each
        # member of the team to the screen.
        # This data must be output to the console.
        for hero in self.heroes:

                #print(f"kills = {hero.kills} deaths = {hero.deaths}, no ratio since we can't divide by 0")
            #else:
                #print(int(hero.kills/hero.deaths))
            print(f"K/D {hero.kills}/{hero.deaths}")
class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        # Create instance variables named team_one and team_two that
        # will hold our teams.
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        # This method will allow a user to create an ability.
        # Prompt the user for the necessary information to create a new ability object.
        # return the new ability object.
        name = input("Add an ability name for the hero: ")
        attack_strength = int(input("Add the maximum attack strength for the hero: "))
        ability = Ability(name, attack_strength)
        return ability

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        # This method will allow a user to create a weapon.
        # Prompt the user for the necessary information to create a new weapon object.
        # return the new weapon object.
        name = input("Add a weapon name for the hero: ")
        attack_strength = int(input("Add the maximum attack strength for the hero: "))
        weapon = Weapon(name, attack_strength)
        return weapon

    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        # This method will allow a user to create a piece of armor.
        #  Prompt the user for the necessary information to create a new armor
        #  object.
        #
        #  return the new armor object with values set by user.
        name = input("Add an armor name for the hero: ")
        max_block = int(input("Add the maximum block for the hero: "))
        armor = Armor(name, max_block)
        return armor

    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        # This method should allow a user to create a hero.
        # User should be able to specify if they want armors, weapons, and
        # abilities.
        # Call the methods you made above and use the return values to build
        # your hero.
        #
        # return the new hero object
        name = input("Enter a hero name: ")
        health = int(input("Enter starting health: "))
        hero = Hero(name, health)

        choice_armor = input('Would you like to add armors for your hero, Y/N?: ').lower()
        if choice_armor == 'y':
            num = int(input('how many armors? '))
            for i in range(num):
                hero.add_armor(self.create_armor())

        choice_ability = input('Would you like to add abilities for your hero, Y/N?: ').lower()
        if choice_ability == 'y':
            num = int(input('how many abilities?: '))
            for i in range(num):
                hero.add_ability(self.create_ability())

        choice_weapon = input('Would you like to add weapons for your hero, Y/N?: ').lower()
        if choice_weapon == 'y':
            num = int(input('how many weapons?: '))
            for i in range(num):
                hero.add_weapon(self.create_weapon())

        return hero

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        #This method should allow a user to create team one.
        # Prompt the user for the number of Heroes on team one
        # call self.create_hero() for every hero that the user wants to add to team one.
        #
        # Add the created hero to team one.
        name = input('enter name for team 1: ')
        team1 = Team(name)
        num_team1 = int(input('how many heroes do you want on your team 1?: '))
        for i in range(num_team1):
            hero1 = self.create_hero()
            team1.add_hero(hero1)
        self.team_one = team1

    def build_team_two(self):
        """Prompt the user to build team_two"""
        # This method should allow a user to create team two.
        # Prompt the user for the number of Heroes on team two
        # call self.create_hero() for every hero that the user wants to add to team two.
        # Add the created hero to team two.
        name = input('enter name for team 2: ')
        team2 = Team(name)
        num_team2 = int(input('how many heroes do you want on your team 2?: '))
        for i in range(num_team2):
            hero2 = self.create_hero()
            team2.add_hero(hero2)
        self.team_two = team2

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        # This method should battle the teams together.
        # Call the attack method that exists in your team objects
        # for that battle functionality.
        return self.team_one.attack(self.team_two)

    def show_stats(self):
        '''Prints team statistics to terminal.'''
        # This method should print out battle statistics
        # including each team's average kill/death ratio.
        # Required Stats:
        #     Declare winning team
        #     Show both teams average kill/death ratio.
        #     Show surviving heroes.

        if len(self.team_one.get_alive()) > 0:
            print(f"team {self.team_one.name} wins!")
            print(f"Alive {self.team_one.name} heroes: ")
            for hero in self.team_one.get_alive():
                print(hero.name)

        else:
            print(f"team {self.team_two.name} wins!")
            print(f"Alive {self.team_two.name} heroes: ")
            for hero in self.team_two.get_alive():
                print(hero.name)


        print(f"{self.team_one.name} stats")
        self.team_one.stats()
        print(\n)
        print(f"{self.team_two.name} stats")
        self.team_two.stats()

        # if len(self.team_one.get_alive()) > 0:
        #     print(f"{self.team_one.name} wins!"))
        #
        # for hero in self.team_one.heroes:
        #     if hero.is_alive():
        #         print(hero)
        #     else:
        #         print("all team 1 dead")
        # for hero in self.team_two:
        #     if hero.is_alive():
        #         print(hero)
        #     else:
        #         print("all team 2 dead")

        #print('surviving heroes')

if __name__ == "__main__":

    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()

    arena.team_battle()
    arena.show_stats()
