#Ronald Chatelier
#A turn based Role Playing Game (RPG) by using text
#Sources: W3Schools
#Links: https://www.w3schools.com/ , https://snakify.org/

print ("Welcome to Delta Quest")

#Different Classes
class_one = Brawler

class_two = Lancer

class_three = Gunner

#Different Areas
area_one = Iceland

area_two = Dragon_Ditch

area_three = Tropical_Tropes

area_four = Onion_Ocean

#Different Enemies 
#enemy_one = Mimic Mushroom

#enenmy_two = Jade Ant

#enemy_three = Cactus Dragon

#enemy_four = Brass Bird

enem

#print ("Lancer, Gunner, or Brawler")
#description of each class' stats/ability

print ("Brawler; with high damage output, medium accuracy, and low stamina")

print ("Lancer; with high stamina, medium damage output, and low accuracy")

print ("Gunner; with high accuracy, medium stamina, and low damage output")

choice = int(input())

#planned attacks and skills against enemies
#focusAttack = 100 + attackBuff
#focusGuard = 100 + 
#focusSnipe = 100
#poke = 25
#jab = 50
#bigBang = 35 + high crit chance

#accepting or declining an option
#y = accept
#n = decline
#picking a class
class = input("Please pick your class:") 
#confirming your class to go with on your adventure
print("So, are going for the" + choice + "?")

area = input("Which area would you like to go to:")

#Different areas
print("Are ready to adeventure on and go to" + b + "?")

#if y:
#    print("then let's get going")
#else: n
#    print("Where do you want to go then")

#print ("If so then it's time to go beat some monsters")

#Different monsters that will be used with random number generation battles

#Battle System
#battle = input("Something has jumped out of the grass")
#playerTurn = input("It's your turn!"
#enenmyTurn = input("It's the enemy turn!"

import random

enemies = ["Mimic Mushroom",  "Jade Ant", "Cactus Dragon", "Brass Bird"]
random.shuffle(enemies)

print(enemies)
