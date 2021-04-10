import time
import sys
import random


def delay_print(message):
    print(message)
    time.sleep(2)


def fight(choice):
    if choice == 1:
        delay_print("You have died while fighting the " + enemy)
        print("Game Over!")
    elif choice == 2:
        delay_print("You got eaten alive by the " + enemy + "," +
                    "but saved 4 lives.")
        print("Game Over!")


def run(choice):
    if choice == 1:
        delay_print("You were successful in running " +
                    "away from the """ + enemy + "!")
        delay_print("You found a " + weapon + " while " +
                    "you were running away from the " + enemy + "!")
        delay_print("You come back and fought the " + enemy + " and " +
                    "killed it with your " + weapon + "!")
        delay_print("You win!")
    elif choice == 2:
        delay_print("You encountered a " + enemy + " while evacuating")
        delay_print("You have no other option than to fight it!")
        delay_print("You use your " + weapon + " to shoot the " + enemy)
        if weapon == "shotgun" or weapon == "rifle":
            delay_print("The " + enemy + " dies due to immense pain")
            print("You win!")
        elif weapon == "glock":
            delay_print("The " + enemy + " doesn't even " +
                        "feel the bullets, and eats you alive")
            print("Game Over!")


def choice_input():
    while True:
        try:
            choice = int(input("What would you like to do? "))
            if choice < 3:
                break
            print("Invalid Choice")
        except Exception:
            print("Invalid Choice")
    return choice


while True:
    enemy_list = ["dragon", "monster", "shark"]
    random_number_one = random.randint(0, len(enemy_list)-1)
    enemy = enemy_list[random_number_one]

    weapon_list = ["shotgun", "glock", "rifle"]
    random_number_two = random.randint(0, len(weapon_list)-1)
    weapon = weapon_list[random_number_two]

    delay_print("You are in a ship between a huge ocean")
    delay_print("It looks like a storm is starting to occur")
    delay_print("There is also a huge " + enemy + " which was " +
                "spotted in the ocean sometime ago!")
    delay_print("Enter 1 to start returning to the shore")
    delay_print("Enter 2 to continue sailing")

    choice = choice_input()

    if choice == 1:
        delay_print("On your way back on the shore, you " +
                    "encounter the HUGE " + enemy + "!")
        delay_print("To fight it, Enter 1")
        delay_print("To run away, Enter 2")

        choice1 = choice_input()

        if choice1 == 1:
            fight(choice)
        elif choice1 == 2:
            run(choice)

    elif choice == 2:
        delay_print("You sail for a few hours, but soon spot the " +
                    enemy + " approaching you")
        delay_print("The " + enemy + " starts damaging your boat, " +
                    "and it cracks. You are nowhere near the shore,")
        delay_print("so you have to evacuate the boat in safety jackets.")
        delay_print("But during the evactuation, people are still stuck in" +
                    "the boat, and the " + enemy + " is creeping up on them")
        delay_print("To save people by fighting the " + enemy + ", Enter 1")
        print("To evacuate alone, Enter 2")

        choice2 = choice_input()

        if choice2 == 1:
            fight(choice)
        if choice2 == 2:
            run(choice)

    while True:
        restart = input("Do you want to play again? (y/n): ")
        if restart == "n":
            sys.exit()
        elif restart == "y":
            break
        else:
            print("Invalid Input. Please try again!")
