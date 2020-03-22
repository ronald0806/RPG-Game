#Ronald Chatelier
#A turn based Role Playing Game (RPG) by using text
#Sources: W3Schools, Python Fiddle, Class, and Professor
#Links: https://www.w3schools.com/ , https://snakify.org/ , http://pythonfiddle.com/

#Introduction
print("Welcome to Delta Quest")
print("This is where you'll explore across various lands and encounter unique monsters!")

#User
p1 = "player 1"

#Selecting options (different inputs) 
yes = "accept"
no = "decline"

#Different Classes
class_one = "Brawler"
class_two = "Lancer"
class_three = "Gunner"

#Different Areas
area_one = "Iceland"
area_two = "Dragon Ditch"
area_three = "Tropical Tropes"
area_four = "Onion Ocean"

#Different Enemies 
enemy_one = "Mimic Mushroom"
enemy_two = "Jade Ant"
enemy_three = "Cactus Dragon"
enemy_four = "Brass Bird"

#Usable Items
item_one = "Bandage: Gives 10% of Health Points"
item_two = "Star Fruit: Gives an increased critical hit chance by a pinch"
item_three = "Smoke Bomb: Gives a 100% run rate"
item_four = "Cloak: Gives a 30% evasion rate"
item_five = "Net: Used to capture the enemy"

#Materials
material_one = "Wood"
material_two= "Iron"
material_three = "Water"
material_four = "Cloth"

#Picking a class
class_choice_not_valid = True
while class_choice_not_valid:    
    print ("1: Brawler; with high damage output, medium accuracy, and low stamina")
    print ("2: Lancer; with high stamina, medium damage output, and low accuracy")
    print ("3: Gunner; with high accuracy, medium stamina, and low damage output")
    class_choice = int(input("Please choose a number that's for a class (1, 2, or 3)"))
    if class_choice == 1 or class_choice == 2 or class_choice == 3:
        class_choice_not_valid = False

#Final class decision
no_accept = True
while no_accept:
    print("Alright, you have chosen that class")
    accept = input("Are you ready to choose an area to go to? [type either yes or no]")
    if accept == yes:
        no_accept = False

#Picking a location
lost_location = True
while lost_location:
    print("Now it's time to pick a location")
    areas = [area_one, area_two, area_three, area_four]
    print(areas)
    location = input("Go on ahead and choose one")
    if location == 'Iceland' or location == 'Dragon Ditch' or location == 'Tropical Tropes' or location == 'Onion Ocean':
        lost_location = False

#Enemy encounter
def encounter():
    print("Yikes, a...")
    import random
    print random.choice([enemy_one, enemy_two, enemy_three, enemy_four])
    print("has decided to pick for a fight")
encounter()

#Amount of Health Points an enemy has
import random
print('The enemy has...')
print(random.randrange(220,550,100))
print('Health points')

#Getting ready for combat
print("It's time to engage in combat!")
engage = raw_input("Type engage")
print(p1 + ' ' + "is" + engage)

#Doing an attack
import random
def attack_option(attack):
    print(attack + ' ' + "does...")
    print(random.randrange(30,80,10))
    print("Overall damage output")
attack_option('strike')
print("The enemy has gotten weakened, what shall you do next?")

#Option to run away from battle
no_run = True
while no_run:
    print("Would you like to run away?")
    run = input("Go on ahead and type either yes or no")
    if run == yes or run == no:
        no_run = False

#Options on which item to use
no_item = True
while no_item:
    print("Which item would you like to use")
    items = [item_one, item_two, item_three, item_four, item_five]
    print(items)
    use_item = input("Go on ahead and choose an item!")
    if use_item == "Bandage" or use_item == "Star Fruit" or use_item == "Smoke Bomb" or use_item == "Cloak" or use_item == "Net":
        no_item = False

#End of battle and experience points earned
print("Great, the battle is now over")
import random
print(random.randrange(15,20,40))
print("Experience points has been gained")

#Currency gained
import random
print(random.randrange(45,50,80))
print("silver has been gained")

#Leveling up
import random
def level_up(level):
    print("You've gained" + ' ' + level + ' ')
    print(random.randrange(1,2,5))
level_up("this level:")

#Material earned
def material_gained():
    print("You got...")
    import random
    print random.choice([material_one, material_two, material_three, material_four])
    print(" used for crafting")
material_gained()
