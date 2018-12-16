import random


class Creature:
    def __init__(self, name, level):
        self.level = level
        self.name = name

    def __repr__(self):
        return "Creature {} of level {}".format(self.name, self.level)

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):
    def attack(self, creature):
        print("The wizard {} attacks {}!".format(self.name, creature.name))

        my_roll = self.get_defensive_roll()
        creature_roll = creature.get_defensive_roll()

        print("You roll {}...".format(my_roll))
        print("Creature roll {}...".format(creature_roll))

        if my_roll >= creature_roll:
            print("The wizard has handily triumphed over {}".format(creature))
            return True
        else:
            print("The wizard has been DEFEATED!!!")
            return False


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_role = super().get_defensive_roll()
        return base_role / 2


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name, level)
        self.breaths_fire = breaths_fire
        self.scaliness = scaliness
        self.level = level

    def get_defensive_roll(self):
        base_role = super().get_defensive_roll()
        fire_modifier = 5 if self.breaths_fire else 1
        scale_modifier = self.scaliness / 10

        return base_role * fire_modifier * scale_modifier
