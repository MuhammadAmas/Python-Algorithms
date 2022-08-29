import random

# Evaluating results


def gamewin(user, comp):
    if comp == user:
        print("This game is a tie")

    elif comp == 'r':
        if user == 'p':
            return False
        elif user == 's':
            return True

    elif comp == 'p':
        if user == 's':
            return False
        elif user == 'r':
            return True

    elif comp == 's':
        if user == 'r':
            return False
        elif user == 'p':
            return True


user = input("Your Turn: Rock(r) Paper(p) or Scissor(s)?")

# Computer's choice
rand = random.randint(1, 3)
if rand == 1:
    comp = 'r'
elif rand == 2:
    comp = 'p'
else:
    comp = 's'


final = gamewin(comp, user)
# Printing computer's choice
print(f"Computer chose {comp}")
# Printing user's choice
print(f"You chose {user}")


# Printing results
if final == None:
    print("This game is a tie")
elif final == True:
    print("you win")
else:
    print("you lose")
