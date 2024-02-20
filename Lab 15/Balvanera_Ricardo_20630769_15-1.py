#define the main menu function header
def main_menu():
    flag = True
    while flag:
        menu = '''Main Menu
1. Utility
2. Game
3. Multimedia
4. Exit
'''
        print(menu)
        ans = input("Please input:")
 #check if the input is a digit
        if ans.isdigit(): 
            ans = int(ans)
            if ans == 1:
                utility()
            elif ans == 2:
                game()
            elif ans == 3:
                multimedia()
            elif ans == 4:
                flag = False
            else:
                print("Invalid input. Please select a number from the menu.\n")
        else:
            print("Invalid input. Please enter a number.\n")

    print("Thank you! Bye~")

#define the utility menu
def utility():
    menu = '''Utility Menu
1. Calculator
2. Email
3. Note 
4. Main Menu''' 
    print(menu)
    ans = input("Please input:")
    if ans.isdigit():
        ans = int(ans)
        if ans == 1:
            calculator()
        elif ans == 2:
            email()
        elif ans == 3:
            note()
        elif ans == 4:
            return
        else:
            print("Invalid input. Please select a number from the menu.\n")
            utility()
    else:
        print("Invalid input. Please enter a number.\n")
        utility()

#define calculator
def calculator():
    print("I am sorry. It's not ready yet")

#define email
def email():
    print("I am sorry. It's not ready yet")

#define note
def note():
    print("I am sorry. It's not ready yet")

#define the game menu
def game():
    menu = '''Game Menu
1. Poker
2. Blackjack
3. Main menu
'''
    print(menu)
    ans = input("Input:")
    if ans.isdigit():
        ans = int(ans)
        if ans == 1:
            poker()
        elif ans == 2:
            blackjack()
        elif ans == 3:
            return
        else:
            print("Invalid input. Please select a number from the menu.\n")
            game()
    else:
        print("Invalid input. Please enter a number.\n")
        game()

#define poker
def poker():
    print("I am sorry. It's not ready yet")

#define blackjack
def blackjack():
    print("I am sorry. It's not ready yet")

#define the multimedia menu
def multimedia():
    menu = '''Multimedia Menu
1. Music player
2. Camera
3. Download Youtube
4. Main menu
'''
    print(menu)
    ans = input("Input:")
    if ans.isdigit():
        ans = int(ans)
        if ans == 1:
            music_player()
        elif ans == 2:
            camera()
        elif ans == 3:
            download_youtube()
        elif ans == 4:
            return
        else:
            print("Invalid input. Please select a number from the menu.\n")
            multimedia()
    else:
        print("Invalid input. Please enter a number.\n")
        multimedia()

#define music player
def music_player():
    print("I am sorry. It's not ready yet")

#define camera
def camera():
    print("I am sorry. It's not ready yet")

#define download youtube
def download_youtube():
    print("I am sorry. It's not ready yet")

main_menu()
