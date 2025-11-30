import sys
print("*******************************************************************************")
print("          |                   |                  |                     |")
print(" _________|________________.=\"\"_;=.______________|_____________________|_______")
print("|                   |  ,-\"_,=\"\"     `\"=.|                  |")
print("|___________________|__\"=._o`\"-._        `\"=.______________|___________________")
print("          |                `\"=._o`\"=._      _`\"=._                     |")
print(" _________|_____________________:=._o \"=._.\"_.-=\"\'\"=.__________________|_______")
print("|                   |    __.--\" , ; `\"=._o.\" ,-\"\"\"-._ \".   |")
print("|___________________|_._\"  ,. .` ` `` ,  `\"-._\"-._   \". '__|___________________")
print("          |           |o`\"=._` , \"` `; .\". ,  \"-._\"-._; ;              |")
print(" _________|___________| ;`-.o`\"=._; .\" ` '`.\"\` . \"-._ /_______________|_______")
print("|                   | |o;    `\"-.o`\"=._``  '` \" ,__.--o;   |")
print("|___________________|_| ;     (#) `-.o `\"=.`_.--\"_o.-; ;___|___________________")
print("____/______/______/___|o;._    \"      `\".o|o_.--\"    ;o;____/______/______/____")
print("/______/______/______/_\"=._o--._        ; | ;        ; ;/______/______/______/_")
print("____/______/______/______/__\"=._o--._   ;o|o;     _._;o;____/______/______/____")
print("/______/______/______/______/____\"=._o._; | ;_.--\"o.--\"_/______/______/______/_")
print("____/______/______/______/______/_____\"=.o|o_.--\"\"___/______/______/______/____")
print("/______/______/______/______/______/______/______/______/______/______/[TomekK]")
print("*******************************************************************************")

print("Welcome to Treasure Island. Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
print("\tType \"left\" or \"right\"")
choice = input()

if (choice == "left"): 
    print("You've come to a lake. There is an island in the middle of the lake.")
else: 
    print("You fall into a hole and broke your neck. Game over.")
    sys.exit()

choice = input("Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")

if choice == "wait":
    print("You arrive at the island unharmed. There is a house with 3 doors.\n\tOne red, one yellow and one blue. Which colour do you choose?")
else: 
    print("The hungry trouts surrounded you and killed you. You died. Game over")
    sys.exit()

choice = input()

if choice == "red":
    print("As you enter the red door, a surge of fire burst out an burned you alive. Game over.")
elif choice == "yellow":
    print("You opened the door and behind it is a treasure chest filled to the brim with gold. Congratulation! You win!")
elif choice == "blue":
    print("A hungry beast hides behind the door. The moment you opened the door, the bast pounced on you and killed you. Game over")
else: 
    print("You decided that the journey is too tiring to your body and you decided to just turn away and go home without the treasure.")

    

