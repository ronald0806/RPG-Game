# Ronald Chatelier
# A turn based Role Playing Game (RPG) by using text
# Sources: W3Schools, Python Fiddle, Class, and Professor
# Links: https://www.w3schools.com/ , https://snakify.org/ ,
# http://pythonfiddle.com/


import random


# Function Definition
def main():
    # Introduction
    print("Welcome to Delta Quest")
    print("This is where you'll explore across various lands and encounter "
          "unique monsters!")

    # User
    p1 = "player 1"

    # Selecting options (different inputs)
    yes = "accept"
    no = "decline"

    # Different Classes
    class_one = "Brawler"
    class_two = "Lancer"
    class_three = "Gunner"

    # Different Areas
    area_one = "Iceland"
    area_two = "Dragon Ditch"
    area_three = "Tropical Tropes"
    area_four = "Onion Ocean"

    # Different Enemies
    enemy_one = "Mimic Mushroom"
    enemy_two = "Jade Ant"
    enemy_three = "Cactus Dragon"
    enemy_four = "Brass Bird"

    # Usable Items
    item_one = "Bandage: Gives 10% of Health Points"
    item_two = "Star Fruit: Gives an increased critical hit chance by a pinch"
    item_three = "Smoke Bomb: Gives a 100% run rate"
    item_four = "Cloak: Gives a 30% evasion rate"
    item_five = "Net: Used to capture the enemy"

    # Materials
    material_one = "Wood"
    material_two = "Iron"
    material_three = "Water"
    material_four = "Cloth"
    materials = [material_one, material_two, material_three, material_four]
    # Picking a class
    class_choice_not_valid = True
    # Starter Iterative Structures
    while class_choice_not_valid:
        # Print Functions
        print("1: Brawler; with high damage output, medium accuracy, and low "
              "stamina")
        print("2: Lancer; with high stamina, medium damage output, and low "
              "accuracy")
        print("3: Gunner; with high accuracy, medium stamina, and low damage "
              "output")
        class_choice = int(input("Please choose a number that's for a class "
                                 "(1, 2, or 3)"))
        # Starter Iterative Structures
        if class_choice == 1 or class_choice == 2 or class_choice == 3:
            class_choice_not_valid = False

    # Final class decision
    no_accept = True
    # Starter Iterative Structures
    while no_accept:
        # Print Functions
        print("Alright, you have chosen that class")
        accept = input("Are you ready to choose an area to go to? [type "
                       "either yes or no]")
        # Starter Iterative Structures
        if accept == "yes":
            no_accept = False

    # Picking a location
    lost_location = True
    # Starter Iterative Structures
    while lost_location:
        # Print Functions
        print("Now it's time to pick a location")
        areas = ['Iceland', 'Dragon Den', 'Onion Ocean', 'Tropical Tropes']
        print(areas)
        location = input("Go on ahead and choose one")
        # Starter Iterative Structures
        if location in areas:
            lost_location = False

    encounter()

    # Amount of Health Points an enemy has
    # Print Functions
    print('The enemy has...')
    print(random.randrange(200, 550))
    print('Health points')

    # Getting ready for combat
    # Print Functions
    print("It's time to engage in combat!")
    engage = input("Type engage")
    print(p1 + ' ' + "is" + engage)
    attack_option('strike')
    # Print Functions
    print("The enemy has gotten weakened, what shall you do next?")

    # Option to run away from battle
    no_run = True
    # Starter Iterative Structures
    while no_run:
        # Print Functions
        print("Would you like to run away?")
        run = input("Go on ahead and type either yes or no")
        if run == "yes" or run == "no":
            no_run = False

    # Options on which item to use

    no_item = True
    # Starter Iterative Structures
    while no_item:
        # Print Functions
        print("Which item would you like to use (Type the exact name)")
        items = ['Star Fruit', 'Smoke Bomb', 'Cloak', 'Bandage', 'Net']

        print(items)
        use_item = input("Go on ahead and choose an item!")

        if use_item in items:
            no_item = False

    # End of battle and experience points earned
    print("Great, the battle is now over")

    print(random.randrange(15, 40))
    print("Experience points has been gained")

    # Currency gained
    print(random.randrange(45, 80))
    print("silver has been gained")
    level_up("this level:")
    material_gained(materials)


# Enemy encounter
# Function Definition
def encounter():
    print("Yikes, a...")
    enemies = ['Brass Bird', 'Cactus Dragon', 'Jade Ant', 'Mimic Mushroom']
    print(random.choice(enemies))
    print("has decided to pick for a fight!")


# Doing an attack
# Function Definition
def attack_option(attack):
    # Print Functions
    print(attack + ' ' + "does...")
    print(random.randrange(30, 80))
    print("Overall damage output")


# Leveling up
# Parameter passing (write a function that accepts parameters
# Function Definition
def level_up(level):
    print("You've gained" + ' ' + level + ' ')
    print(random.randrange(1, 5))


# Material earned
# Parameter passing (write a function that accepts parameters
# Function Definition
def material_gained(materials):
    print("You got...")
    print(random.choice(materials))
    print("used for crafting")


main()
