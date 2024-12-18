import sys

def level_one():
    print("You find yourself lost in a dense forest. You need to make decisions to find your way out.")
    print("You come across a fork in the path. Which way do you choose?")
    choice = input("A. LEFT\nB. RIGHT\nC. FORWARD\n").upper()
    
    if choice == "A":
        level_two_left()
    elif choice == "B":
        level_two_right()
    elif choice == "C":
        level_two_forward()
    else:
        print("Oops! An error has occurred please try again.")

    #I found that there was an infinite loop in my system so I looked up how to make max attempts and what I implemented is down below!
    
        max_attempts = 3
        attempts = 0
    
    while attempts < max_attempts:
        choice = input("A. LEFT\nB. RIGHT\nC. FORWARD\n").upper()
        
        if choice == "A":
            level_two_left()
            break
        elif choice == "B":
            level_two_right()
            break
        elif choice == "C":
            level_two_forward()
            break
        else:
            print("Invalid choice. Please choose A, B, or C.")
            attempts += 1
    
    if attempts == max_attempts:
        print("You failed to make a valid choice. Game over.")

    else:
        print("Invalid choice. Please choose A, B, or C.")
        level_one()

def level_two_left():
    print("You chose LEFT. You stumble upon a river. What do you do?")
    choice = input("A. FOLLOW THE RIVER\nB. CROSS THE RIVER\nC. BUILD A RAFT\n").upper()
    
    if choice == "A":
        level_three_bridge()
    elif choice == "B":
        level_three_rapids()
    elif choice == "C":
        level_three_raft()

    else:
        print("Invalid choice. Please choose A, B, or C.")
        level_two_left()

def level_two_right():
    print("You chose RIGHT. You encounter a group of people near the riverbank. They look at you hungrily. What do you do?")
    choice = input("A. TRY TO NEGOTIATE\nB. FLEE\nC. FIGHT\n").upper()
    
    if choice == "A":
        print("You attempt to negotiate with the cannibals, but they are not interested. You narrowly escape.")
        level_one()
    elif choice == "B":
        print("You flee from the cannibals and manage to evade them, continuing your journey through the forest.")
    elif choice == "C": 
        print("You engage in combat with the cannibals, but they overpower you. Game over.")
    else:
        print("Invalid choice. Please choose A, B, or C.")   

def level_two_forward():
    print("You chose FORWARD. You see a thicket with thorns. What do you do?")
    choice = input("A. POWER THROUGH THICKET\nB. GRAB STICK AND START WACKING THE THICKET\nC. START EATING THE THICKET\n").upper()

    if choice == "A":
        print("You chose POWER THOUGH THICKET. You power through the thicket and get deep scratches")
    elif choice == "B":
        print("You chose GRAB STICK AND START WACKING THE THICKET. You break though the thicket and see a village. Game over you winc!")
        end_function()
    elif choice == "C":
        print("You chose to START EATING THE THICKET. You choke and die Game Over.")

def level_three_bridge():
    print("You chose FOLLOW THE RIVER. You find a bridge. What's your next move?")
    choice = input("A. CROSS THE BRIDGE\nB. FOLLOW THE RIVER\nC. TURN BACK\n").upper()
    
    if choice == "A":
        print("Congratulations! You successfully crossed the bridge and found your way out of the forest.")
    elif choice == "B":
        level_two_left()
    elif choice == "C":
        print("You decided to turn back, but unfortunately, you got even more lost in the forest.")
    else:
        print("Invalid choice. Please choose A, B, or C.")
        level_three_bridge()

def level_three_rapids():
    print("You chose CROSS THE RIVER. You make it across safely. What now?")
    choice = input("A. CONTINUE EXPLORING\nB. REST AND RECUPERATE\nC. CALL FOR HELP\n").upper()
    
    if choice == "A":
        print("You continued exploring and eventually found your way out of the forest.")
    elif choice == "B":
        print("You rested and regained your strength, allowing you to find your way out of the forest more easily.")
    elif choice == "C":
        print("You called for help, and eventually, rescue arrived to guide you out of the forest. Game Over you win!")
        end_function()
    else:
        print("Invalid choice. Please choose A, B, or C.")
        level_three_rapids()

def level_three_raft():
    print("You chose BUILD A RAFT. It takes time, but you succeed. What's your next move?")
    choice = input("A. CROSS THE RIVER ON THE RAFT\nB. FOLLOW THE RIVER\nC. ABANDON THE RAFT AND EXPLORE ELSEWHERE\n").upper()
    
    if choice == "A":
        print("You successfully crossed the river on the raft and find a camp.")
    elif choice == "B":
        level_two_left()
    elif choice == "C":
        print("You abandoned the raft and explored elsewhere, eventually finding your way out of the forest.")
    else:
        print("Invalid choice. Please choose A, B, or C.")
        level_three_raft()

# Start the game
#I added an end function to my code because I found that the bottom function I added would continually repeat the game.
def end_function():
    sys.exit()


level_one()
