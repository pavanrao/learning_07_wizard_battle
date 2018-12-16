import random
import time

from actors import Wizard, Creature, SmallAnimal, Dragon


def print_header():
    print("-----------------------------------------------------")
    print("------------w i z a r d -- g a m e-------------------")
    print("-----------------------------------------------------")
    print("")


def game_loop():
    creatures = [
        SmallAnimal("Toad", 1),
        Creature("Tiger", 12),
        SmallAnimal("Bat", 3),
        Dragon("Dragon", 50, 30, True),
        Wizard("Evil Wizard", 1000),
    ]

    hero = Wizard("Gandalf", 75)

    while True:

        active_creature = random.choice(creatures)
        print(
            "A {} of level {} has appeared from a dark and foggy forest...".format(
                active_creature.name, active_creature.level
            )
        )

        cmd = input("Do you want to [a]ttack, [r]unaway, [l]ook around or e[x]it?  ")
        if cmd == "a":
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                # print("Game over!")
                print("The wizard hides taking time to recover...")
                time.sleep(5)
                print("The wizard returns revitalized!")
        elif cmd == "r":
            print("The wizard has become unsure of his power and flees!!!")
        elif cmd == "l":
            print("The wizard {} takes in the surroundings and sees:".format(hero.name))
            for creature in creatures:
                print(" * A {} of level {}".format(creature.name, creature.level))
        elif cmd == "x":
            print("exiting the game... bye!")
            break
        else:
            print("I dont understand that, please try again.")

        if not creatures:
            print("You defeated all the creatures!!")
            break


def main():
    print_header()
    game_loop()


if __name__ == "__main__":
    main()
