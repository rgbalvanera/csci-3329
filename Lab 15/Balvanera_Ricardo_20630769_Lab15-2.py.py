#define user data dictionary to store IDs and passwords
user_data = {}

#define the login/signup menu function
def login_signup_menu():
    flag = True
    while flag:
        print("Login/Signup Menu")
        print("1. Log in")
        print("2. Sign up")
        print("3. Exit")
        choice = input("Please input: ")

        if choice == '1':  
            login()
        elif choice == '2':  
            signup()
        elif choice == '3': 
            print("Thank you! Bye~")
            flag = False
        else:
            print("Invalid choice. Please select a valid option.")

#define the login function
def login():
    print("Log in")
    id_input = input("Please input your ID: ")
    password_input = input("Please input your password: ")
    if id_input in user_data and user_data[id_input] == password_input:
        print(f"Welcome back, {id_input}!")
        main_menu()
    else:
        print("ID or Password is incorrect!")

#define the signup function
def signup():
    print("Sign up")
    id_input = input("Please input an ID: ")
    password_input = input("Please input a password: ")
    user_data[id_input] = password_input
    print("Signup successful!")

#define the main menu function
def main_menu():
    flag = True
    while flag:
        print("Main Menu")
        print("1. Utility")
        print("2. Game")
        print("3. Multimedia")
        print("4. Log out")
        choice = input("Please input: ")

        if choice == '1': 
            utility()
        elif choice == '2':
            game()
        elif choice == '3':  
            multimedia()
        elif choice == '4':
            print("You are logged out!")
            flag = False
        else:
            print("Invalid choice. Please select a valid option.")

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

#start the program by calling the Login/Signup Menu function
login_signup_menu()
