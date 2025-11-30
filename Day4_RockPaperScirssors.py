import random

def print_scissor():
    print("""
        _______
    ---'   ____)__
            ______)
        __________)
        (____)
    ---.__(___)
    """)

def print_paper():
    print("""
        _______
    ---'    ____)
            ______)
            _______)
            _______)
    ---.__________)
    """)

def print_rock():
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)


print("What do you choose?\n Type [0] for Rock, [1] for Paper and [2] for Scissors.\n")
choice_player = input()
choice_comp = random.randint(0,2)

if choice_player == 0:
    print_rock()
    print("Computer chose:")
    if choice_comp == 0:
        print_rock()
        print("It's a draw")
    elif choice_comp == 1:
        print_paper()
        print("You lose!")
    else: 
        print_scissor()
        print("You win!")
elif choice_player == 1:
    print_paper()
    print("Computer chose:")
    if choice_comp == 0:
        print_rock()
        print("You win!")
    elif choice_comp == 1:
        print_paper()
        print("It's a draw.")
    else: 
        print_scissor()
        print("You lose!")
else:
    print_scissor()
    print("Computer chose:")
    if choice_comp == 0:
        print_rock()
        print("You lose!")
    elif choice_comp == 1:
        print_paper()
        print("You win!")
    else: 
        print_scissor()
        print("It's a draw!")


