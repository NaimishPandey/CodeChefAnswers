def game(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    else:
        if you == 's':
            return False
        elif you == 'w':
            return True
import random
print("Computer's Turn")
randNo = random.randint(1,3)
if randNo == 1:
    comp = "s"
elif randNo == 2:
    comp = "w"
else:
    comp = "g"
you = input('Enter snake(s), water(w) or gun(g)?')
print(f'Computer chose {comp}')
gameWin = game(comp, you)
if gameWin == None:
    print('The Game is a tie')
elif gameWin == True:
    print("You won the game")
else:
    print('You lose the game')