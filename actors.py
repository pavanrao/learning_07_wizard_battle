import random


class Wizard:
    def __init__(self, name, level):
        self.level = level
        self.name = name

    def attack(self, creature):
        print('The wizard {} attacks {}!'.format(
            self.name, creature.name
        ))

        my_roll = random.randint(1, 12) * self.level
        creature_roll = random.randint(1, 12) * creature.level

        print("You roll {}...".format(my_roll))
        print("Creature roll {}...".format(creature_roll))

        if my_roll >= creature_roll:
            print("The wizard has handily triumphed over {}".format(creature))
            return True
        else:
            print("The wizard has been DEFEATED!!!")
            return False


class Creatures:
    def __init__(self, name, level):
        self.level = level
        self.name = name

    def __repr__(self):
        return "Creature {} of level {}".format(
            self.name,
            self.level
        )


class Human:
    pass
