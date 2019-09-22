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
      self.abilities = []
      self.armors = []

    def add_ability(self, ability):
      ''' Add ability to abilities list '''
      # TODO: Add ability object to abilities:List
      self.abilities.append(ability)

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

    def add_armor(self, armor):
        '''Add armor to self.armors
        Armor: Armor Object
        '''
        # TODO: Add armor object that is passed in to `self.armors`
        self.armors.append(armor)

    def defend(self, damage_amt):
        '''Runs `block` method on each armor.
            Returns sum of all blocks
        '''

  # TODO: This method should run the block method on each armor in self.armors
        total = 0
        for armor in self.armors:
            total += armor.block()
            print("total " + str(total))
        return total - damage_amt

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        # TODO: Create a method that updates self.current_health to the current
        # minus the the amount returned from calling self.defend(damage).
  



if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    armor = Armor("Strong",100 )
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    hero.add_armor(armor)
    #print(hero.attack())
    #print("block "+ str(armor.block()))
    print("defend " + str(hero.defend(30)))
