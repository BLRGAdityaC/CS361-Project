import random
totalLuck = 0
totalBalance = 100

def get_random(minimum, maximum):
    # TODO
    return minimum

def calc_luck(minimum, maximum, current, select):
    # TODO
    # different behavior if dice or no dice
    if (select != minimum - 1): behavior = 'TODO'
    return 0

def luck_Str(luckLevel):
    # TODO
    return "Unknown"

def calc_bet(bet, luck):
    # TODO
    # WILL BE CHANGED A LOT
    # PARAMETERS WILL CHANGE
    return 0

def help_menu():
    # TODO
    print("\n\n Hey there! This page will be dedicated to")
    print("providing information about what you can do.\n")
    print("Under Construction...\n")
    input("Press Enter to Exit...")
    return 0


def modify_values():
    # TODO
    global totalBalance, totalLuck
    print("Current Luck = " + str(totalLuck))
    print("Current Balance = " + str(totalBalance))
    inputLuck = input("\nSet Luck: ")
    if(inputLuck.isdigit() == True): totalLuck = int(inputLuck)
    
    inputBalance = input("Set Balance: ")
    if(inputBalance.isdigit() == True): totalBalance = int(inputBalance)
    return 0

def dice_mode():
    global totalLuck, totalBalance
    print("Roll a set of dice.")
    while True:
        # number of dice
        diceStr = input("Enter a number of dice: ")
        if(diceStr.isdigit() == False): 
            print("Error Invalid Entry. Please Pick Positive Integer\n")
            continue
        # number of faces
        faceStr = input("Enter number of faces:")
        if(faceStr.isdigit() == False or faceStr == '1'): 
            print("Error! Invalid Entry. Please Pick Integer Greater Than 1\n")
            continue
        diceNum = int(diceStr)
        faceNum = int(faceStr)
        break
    
    # amount to bet
    bet = input("Select amount to bet (skipped if non-positive integer): ")
    if(bet.isdigit() == False or int(bet) <= 0): betting = False
    else: betting = True

    # random num
    randomNum = get_random(diceNum, diceNum*faceNum)
    print("\nAfter Rolling " + diceStr + "d" + faceStr + " the combined value was " + str(randomNum))
    luck = calc_luck(diceNum, diceNum*faceNum, randomNum, diceNum-1)
    totalLuck = totalLuck + luck

    # betting results
    print("This result is considered " + luck_Str(luck))
    if(betting == True):
        earned = calc_bet(bet, luck)
        print("\nYou made/lost $" + str(earned))
        totalBalance = totalBalance +  earned

    input("\nPress Enter to continue...")



def range_mode():
    global totalLuck, totalBalance
    print("Select from a Range.")
    while True:
        # minimum
        minStr = input("Select first number: ")
        if(minStr.isdigit() == False): #on error
            print("Error! Invalid Entry. Please Pick Positive Integer.\n")
            continue
        # maximum 
        maxStr = input("Select last number: ")
        if(maxStr.isdigit() == False or int(maxStr) <= int(minStr)): #on error
            if(maxStr.isdigit()): print("Error! Make sure last number is less than first\n")
            else: print("Error! Invalid Entry. Please Pick Positive Integer.\n")
            continue
        minimum = int(minStr)
        maximum = int(maxStr)
        break
    # select value in range
    while True:
        selection = input("\nChoose a number in range: ")
        if(selection.isdigit() == True and int(selection) >= minimum and int(selection) <= maximum): break
        print("Error! Invalid Entry, pick a number within the range.")
    
    # amount to bet
    bet = input("Select amount to bet (skipped if non-positive integer): ")
    if(bet.isdigit() == False or int(bet) <= 0): betting = False
    else: betting = True

    # random num
    randomNum = get_random(minimum, maximum)
    print("\nThe random number between " + str(minStr) + " and " + str(maxStr) + " is: " + str(randomNum))
    luck = calc_luck(minimum, maximum, randomNum, int(selection))
    totalLuck = totalLuck + luck

    # betting results
    print("This result is considered " + luck_Str(luck))
    if(betting == True):
        earned = calc_bet(bet, luck)
        print("\nYou made/lost $" + str(earned))
        totalBalance = totalBalance +  earned


    input("\nPress Enter to continue...")

    


def main():
    while True:
        print("Select an option")
        print("1: Pick a number")
        print("2: Roll some dice")
        print("3: Modify Values")
        print("4: Help")
        print("5: Exit")
        print("\nCurrent Balance: " + str(totalBalance) + "\n")
        selected = input("Pick Option: ")
        match selected:
            case '1': range_mode()
            case '2': dice_mode()
            case '3': modify_values()
            case '4': help_menu()
            case '5': 
                if(input("Type 1 if sure: ") == '1'): exit()
            case _ : print("\nInvalid Entry! Try Again.")
main()