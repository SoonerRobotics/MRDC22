# This is the starting state, right after competition starts
# start state is defined as 0
state = 0

def choose_competition(state):
    choice = int(input("What would you like to do?\n1) Break into Treasury\n2)Stock Treasury\n3)Seek Wizard's Wisdom\n4)Brew Potions\n5)Steal Dragon Egg\n6)Slay Dragon\n7)Sabotage Stock Treasury\n> "))
    if choice == 1:
        #return "Break into Treasury" is 2
        return 2
    elif choice == 2:
        #return "Stock Treasury" is 3
        return 3
    elif choice == 3:
        #return "Seek Wizard's Wisdom" is 4
        return 4
    elif choice == 4:
        #return "Brew Potions" is 5
        return 5
    elif choice == 5:
        #return "Steal Dragon Egg" is 6
        return 6
    elif choice == 6:
        #return "Slay Dragon" is 7
        return 7
    elif choice == 7:
        #return "Sabotage Stock Treasury" is 8
        return 8
    else:
        #return "Error!" is -1
        return -1

a = choose_competition(state)
print(a)

def done(question):
    success = input(question)
    while success != 'y':
        success = input(question)

def stock_treasury():
    print("START stocking treasury")
    print("Heading to ball pit")
    done("At ball pit?\n> ")
    
    print("Picking up ball")
    done("Have ball in claw?\n> ")

    print("Determining color")
    success = input("Have right color?\n> ")
    while success == 'n':
        print("Dropping ball")
        done("Is ball dropped?\n> ")
        print("Picking up ball")
        done("Is ball picked up?\n> ")
        success = input("Have right color?")
    print("Keeping ball")
    done("Ball held?\n> ")
    print("Moving to treasury")
    done("In front of chest?\n> ")
    print("Dropping in chest")
    done("Dropped?\n> ")
    print("END")

def break_into_treasury():
    print("START breaking into treasury")
    print("Move to door")
    done("At door?\n> ")
    print("At door")
    done("In position?\n> ")
    print("Press button / Pull door")
    print("Waiting for five second")
    print("Opening door")
    done("Door opened?\n> ")
    print("END")

def seek_wizards_wisdom():
    print("START seeking wizards wisdom")
    print("locating tower")
    done("Know location?\n> ")
    print("Pointing IR at tower")
    done("Pointed at tower?\n> ")
    print("Sending signal")
    done("Signal sent\n> ")
    print("END")

def brew_potions():
    test_variable = 0
    print("STARTING brewing potions")
    success4 = 'n'
    while success4 == 'n':
        print("Moving to ball pit")
        done("Arrived at ball pit?\n> ")
        print("Picking up ball")
        done("Ball picked up?\n> ")
        print("Determining color")
        success = input("Sequence selected?\n> ")
        while success != "y":
            print("Picking sequence")
            success2 = input("Ball matches first color of sequence?\n> ")
            if success2 == 'n':
                print("Dropping ball")
                done("Ball dropped?\n> ")
                print("Picking up ball")
                done("Ball picked up?\n> ")
            elif success2 == 'y':
                test_variable = 1
                break
            success = input("Sequence selected?\n> ")
        if test_variable == 0:
            print("Checking sequence")
            success3 = input("Matches sequence?\n> ")
            while success3 != 'y':
                print("Dropping ball")
                done("Ball dropped?\n> ")
                print("Picking up ball")
                done("Ball picked up?\n> ")
                print("Determining color")
                success3 = input("Matches sequence?\n> ")
        test_variable = 0
    
        print("Moving to cauldron")
        done("At cauldron?\n> ")

        print("Dropping ball into cauldron")
        success4 = input("Sequence complete?\n> ")
    print("END")

def steal_the_dragon_egg():
    print("START steal the dragon egg.")
    print("Selecting dragon egg")
    done("Egg selected?\n> ")
    print("Moving to dragon egg")
    success = input("Egg present?\n> ")
    if success == 'n':
        print("fail")
        print("END")
        return("END")
    print("Picking up dragon egg")
    done("Egg picked up?\n> ")
    print("Moving to treasury")
    done("At treasury?\n> ")
    print("Drop egg GENTLY")
    done("egg dropped (gently)?\n> ")
    print("END")
steal_the_dragon_egg()
input()