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
      return total

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        # TODO: This method will append the weapon object passed in as an
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
            #print("total " + str(total))
        return abs(total - damage_amt)
        #return total

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        # TODO: Create a method that updates self.current_health to the current
        # minus the the amount returned from calling self.defend(damage).
        remains = damage - self.defend(damage)
        self.current_health = self.current_health - remains

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.
        '''
        # TODO: Check whether the hero is alive and return true or false
        return  self.current_health > 0


    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
  # TODO: Fight each hero until a victor emerges.
  # Print the victor's name to the screen.
        while self.is_alive() and opponent.is_alive():
            # if ability lists are empty https://stackoverflow.com/questions/53513/how-do-i-check-if-a-list-is-empty
            if not self.abilities and not opponent.abilities:
                print("Draw")
                return

            a1 = self.attack()
            a2 = opponent.attack()
            #d1 = self.defend(a2)
            #d2 = opponent.defend(a1)

                # break
            opponent.take_damage(a1)
            if not opponent.is_alive():
                #num_kills += 1
                #num_deaths += 1
                self.add_kill(1)
                opponent.add_deaths(1)
                print(self.name +" won")
                return

            self.take_damage(a2)
            if not self.is_alive():
                opponent.add_kill(1)
                self.add_deaths(1)
                print(opponent.name +" won")
                return
                # break
            # if self.is_alive() == True and opponent.is_alive() == False:
            #     print(self.name + " won")
            # #elif self.is_alive() == False and opponent.is:
            # else:
            #     print(opponent.name + " won")

class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        # TODO: Use what you learned to complete this method.
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
        # TODO: Add the Hero object that is passed in to the list of heroes in
        # self.heroes
        self.heroes.append(hero)

    def attack(self, other_team):
        ''' Battle each team against each other.'''
        # TODO: Randomly select a living hero from each team and have
        # them fight until one or both teams have no surviving heroes.
        # Hint: Use the fight method in the Hero class.
        self_alive = []
        other_alive = []

        for hero1 in self.heroes:
            if hero1.is_alive():
                self_alive.append(hero1)
            else:
                return "All self hero dead"

        team1 = random.choice(self_alive)

            #while self.heroes.is_alive() or other_team.heroes.is_alive():
                # team1 = random.choice(self.heroes)
        for hero2 in other_team.heroes:
            if hero2.is_alive():
                other_alive.append(hero2)
            else:
                return "All other team hero dead"

        team2 = random.choice(other_team.heroes)

        Hero.fight(team1, team2)

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        # TODO: This method should reset all heroes health to their
        # original starting value.
        for hero in self.heroes:
            hero.current_health = health

    def stats(self):
        '''Print team statistics'''
        # TODO: This method should print the ratio of kills/deaths for each
        # member of the team to the screen.
        # This data must be output to the console.
        # Hint: Use the information stored in each hero.
        for hero in self.heroes:
            print(int(hero.kills/hero.deaths))

class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        # TODO: create instance variables named team_one and team_two that
        # will hold our teams.
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        # TODO: This method will allow a user to create an ability.
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
        # TODO: This method will allow a user to create a weapon.
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
        # TODO:This method will allow a user to create a piece of armor.
        #  Prompt the user for the necessary information to create a new armor
        #  object.
        #
        #  return the new armor object with values set by user.
        name = input("Add an armor for the hero: ")
        max_block = int(input("Add the maximum block for the hero: "))
        armor = Armor(name, max_block)
        return armor

    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        # TODO: This method should allow a user to create a hero.
        # User should be able to specify if they want armors, weapons, and
        # abilities.
        # Call the methods you made above and use the return values to build
        # your hero.
        #
        # return the new hero object
        name = input("Enter a hero name: ")
        health = input("Enter starting health: ")
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
        # TODO: This method should allow a user to create team one.
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
        # TODO: This method should allow a user to create team two.
        # Prompt the user for the number of Heroes on team two
        # call self.create_hero() for every hero that the user wants to add to team two.
        #
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
        # TODO: This method should battle the teams together.
        # Call the attack method that exists in your team objects
        # for that battle functionality.

        self.team_one.attack(self.team_two)

    def show_stats(self):
        '''Prints team statistics to terminal.'''
        # TODO: This method should print out battle statistics
        # including each team's average kill/death ratio.
        # Required Stats:
        #     Declare winning team
        #     Show both teams average kill/death ratio.
        #     Show surviving heroes.

        for hero in team_one:
            if hero.is_alive():
                print(f"{self.team_one.name} wins!")
            else:
                print(f"{self.team_two.name} wins!")

        self.team_one.stats()
        self.team_two.stats()
        for hero in team_one:
            if hero.is_alive():
                print(hero)
            else:
                print("all team 1 dead")
        for hero in team_two:
            if hero.is_alive():
                print(hero)
            else:
                print("all team 2 dead")

        #print('surviving heroes')

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.
    # ability = Ability("Great Debugging", 50)
    # another_ability = Ability("Smarty Pants", 90)
    # armor = Armor("Strong",100 )
    # hero = Hero("Grace Hopper", 200)
    # hero.add_ability(ability)
    # hero.add_ability(another_ability)
    # hero.add_armor(armor)
    # #print(hero.attack())
    # #print("block "+ str(armor.block()))
    # print("defend " + str(hero.defend(30)))
    # hero = Hero("Grace Hopper", 200)
    # shield = Armor("Shield", 50)
    # hero.add_armor(shield)
    # hero.take_damage(50)
    # print(hero.current_health)
    # hero = Hero("Grace Hopper", 200)
    # hero.take_damage(150)
    # print(hero.is_alive())
    # hero.take_damage(15000)
    # print(hero.is_alive())
    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")
    # ability1 = Ability("Super Speed", 300)
    # ability2 = Ability("Super Eyes", 130)
    # ability3 = Ability("Wizard Wand", 80)
    # ability4 = Ability("Wizard Beard", 20)
    # hero1.add_ability(ability1)
    # hero1.add_ability(ability2)
    # hero2.add_ability(ability3)
    # hero2.add_ability(ability4)
    # hero2.fight(hero1)
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    print(arena.team_one.heroes[0])
    arena.team_battle()
    arena.show_stats()
