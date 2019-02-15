import random
import time
def menu():
    print(30*"-", "MENU", 30*"-")
    print("[1]", "Blackjack")
    print("[2]", "Coin Flip")
    print("[3]", "Exit")
    
def menuSelection():
    selection = int(input())
    if selection == 1:
        blackjack()
    elif selection == 2:
        coinFlip()
    else:
        print("Farewell.")
def promptContinue():
    print("Do you want to continue? Y/N")
    continuation = input()
    if continuation == ('Y') or continuation == ('y'):
        coinFlip()
    elif continuation == ('N') or continuation == ('n'):
        print("Returning to menu...")
        menu()
    else:
        print("Invalid input.")
        promptContinue()
def coinFlip():
    print("[H]eads or [T]ails? H/T")
    guess = input()
    print("The coin is flipping...")
    time.sleep(1)
    coinSide = random.randint(1,2)
    if coinSide == 1:
        print("The coin landed on tails!")
    elif coinSide == 2:
        print("The coin landed on heads!")
    if (guess == ('H') or guess == ('h')) and coinSide == 2:
        print("You win!")
    elif (guess == ('T') or guess == ('t')) and coinSide == 1:
        print("You win!")
    else:
        print("You lose!")
    promptContinue()
        
def blackjack():
    print("test")
    

menu()
menuSelection()



