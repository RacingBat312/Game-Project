#------------------------------------------------------------------------

global_health = 10
global_stamina = 10
global_happiness = 10
global_maxhealth = 10
global_maxstamina = 10

# maximum on happiness?? no way!

#------------------------------------------------------------------------

# Start of the game!

import textwrap
import random

def menu_screen():
    global global_happiness , global_health , global_stamina , global_maxhealth , global_maxstamina , creategamename

    ascii_art = textwrap.dedent(r"""
 ______________ ______________  __      __________________       _____       .___                    __                           ________                       
 \__    ___/   |   \_   _____/ /  \    /  \_   _____/  _  \     /  _  \    __| _/__  __ ____   _____/  |_ __ _________   ____    /  _____/_____    _____   ____  
   |    | /    ~    \    __)_  \   \/\/   /|    __)/  /_\  \   /  /_\  \  / __ |\  \/ // __ \ /    \   __\  |  \_  __ \_/ __ \  /   \  ___\__  \  /     \_/ __ \ 
   |    | \    Y    /        \  \        / |     \/    |    \ /    |    \/ /_/ | \   /\  ___/|   |  \  | |  |  /|  | \/\  ___/  \    \_\  \/ __ \|  Y Y  \  ___/ 
   |____|  \___|_  /_______  /   \__/\  /  \___  /\____|__  / \____|__  /\____ |  \_/  \___  >___|  /__| |____/ |__|    \___  >  \______  (____  /__|_|  /\___  >
     \/        \/         \/       \/         \/          \/      \/           \/     \/                        \/          \/     \/      \/     \/ 
""")
    print(ascii_art, end="\n\n")

    tips = [
     textwrap.dedent("""\
    Tip: Dont get expelled plsss
    ⣏⠱⣌⠣⡈⠓⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⢾⢺⣤⡘⢦⡈⢢⡀⠱⣤⢶⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⢸⡿⡏⠻⡀⠳⡄⠹⡄⠹⡸⡇⠀⠀⠀⠀⠀⠀⠀⠀
    ⣸⠃⢳⡀⢳⠀⢹⡀⠱⡄⠳⣹⣄⠀⠀⠀⠀⠀⠀⠀
    ⢿⠀⢮⢇⠈⠣⠀⠓⠀⠈⠀⠀⠹⡆⠀⠀⠀⠀⠀⠀
    ⠈⢧⠈⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⣏⠀⠀⠀⠀⠀⠀
    ⠀⠀⡇⠈⢹⡄⠀⠀⠀⠀⠀⠀⠀⠹⡀⠀⠀⠀⠀⠀
    ⠀⠀⢳⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀
    ⠀⠀⠈⢧⠀⠈⣆⡀⠀⠀⠀⠀⠀⠀⢻⣤⣤⣤⣀⡀
    ⠀⠀⢀⣾⣦⠀⠈⠳⣄⠀⠀⠀⠀⢠⣾⣿⣿⣿⡟⠁
    ⠀⠀⣿⣿⣿⠀⠀⠀⠈⣳⣤⡀⣰⣿⣿⣿⣿⡟⠀⠀
    ⠀⠀⣿⣿⣿⣀⣀⣀⣴⣿⡗⠳⣿⣿⣿⣿⣿⠃⠀⠀
    ⠀⠀⠹⣿⣿⣿⣿⣿⣿⡿⠁⢰⣿⣿⣿⣿⡏⠀⠀⠀
    ⠀⠀⠀⠙⠻⠿⠿⠿⠛⠁⠀⠈⠛⠿⣿⣿⠁"""),
        "Tip: Try to avoid getting into trouble, it will only make your life harder and will make you less happy. (づᴗ _ᴗ)づ♡",
        "Tip: Talk to your teachers, they are there to help you and they can give you advice on how to succeed in school. (づ｡◕‿‿◕｡)づ",
        "Tip: Make sure you do your work proeprtly, whoops, I meant properly, or else... ",
    ]
    
    tip = random.choice(tips)
    print(tip)

    print("\n-----------------------------------------------------------------------------------------------------------------------------------\n")

    print("Now, how would would you like to start the game?")
    print("Type Load or Create")
    print("Remember, only one game can be saved at a time, for now")
    
    while True:
    
        choicemenu = input(">>>")
        if choicemenu in ["Load", "load"]:
            load_game()
        elif choicemenu in ["Create", "create"]:
            create_game()
        else:
            print("Erm, that won't work lil bro, try again")
        


def create_game():
    global global_happiness , global_health , global_stamina , global_maxhealth , global_maxstamina , creategamename
    global_happiness = 10
    global_health = 10
    global_stamina = 10
    global_maxhealth = 10
    global_maxstamina = 10
    creategamename = input("What would you like to name your save file? (Only one save file can be saved at a time, for now) ")
    import pickle
    global global_happiness , global_health , global_stamina , global_maxhealth , global_maxstamina , creategamename
    game_state = {
        'global_happiness': global_happiness,
        'global_health': global_health,
        'global_stamina': global_stamina,
        'global_maxhealth': global_maxhealth,
        'global_maxstamina': global_maxstamina
    }
    with open(f'{creategamename}.pkl', 'w') as f:
        pickle.dump(game_state, f)
        game_intro()

def save_game():

    import pickle
    global global_happiness , global_health , global_stamina , global_maxhealth , global_maxstamina , creategamename
    game_state = {
        'global_happiness': global_happiness,
        'global_health': global_health,
        'global_stamina': global_stamina,
        'global_maxhealth': global_maxhealth,
        'global_maxstamina': global_maxstamina
    }
    with open(f'{creategamename}.pkl', 'w') as f:
        pickle.dump(game_state, f)

def load_game():

    global global_happiness , global_health , global_stamina , global_maxhealth , global_maxstamina , creategamename
    
    import pickle
    print("Which save file would you like to load? (Only one save file can be saved at a time, for now)")
    print("Type the name of your save file, or type 'back' to go back to the menu")
    while True:
        loadname = input(">>>")
        if loadname in ["back", "Back"]:
            menu_screen()
        try:
            with open(f'{loadname}.pkl', 'rb') as f:
                game_state = pickle.load(f)
                global_happiness = game_state['global_happiness']
                global_health = game_state['global_health']
                global_stamina = game_state['global_stamina']
                global_maxhealth = game_state['global_maxhealth']
                global_maxstamina = game_state['global_maxstamina']
                print("Game loaded successfully!")
        except FileNotFoundError:
            print("That save file does not exist, please try again.")

def game_intro():
    global global_happiness , global_health , global_stamina , global_maxhealth , global_maxstamina , creategamename
    
    from time import sleep
    print("The SUPER SCARY SCHOOL GAME is loading...")
    sleep(2)
    print("Just kidding! It's not scary at all...")
    sleep(0.5)
    print("...Maybe")
    sleep(1)
    print("But anyway, this is a game on how you can experience a day in the life of a WFA student!")
    sleep(1)
    print("Random guy: \"WFA is the best!\"")#
    sleep(1)
    print("Random girl: \"I love WFA!\"")
    sleep(1)
    print("Random guy 2: \"Go WFA!\"")
    sleep(1)
    print("Random girl 2: \"WFA is the best school in the world!\"")
    sleep(2)
    print("This game is here to teach you how to behave, how to make friends and how to have fun at WFA!")
    sleep(1)
    print("Let's get started!")
    sleep(1)
    day_morning_start()

#------------------------------------------------------------------------
def formspeech():
    global global_happiness , global_health , global_stamina , global_maxhealth , global_maxstamina , creategamename
    


def schoolgates():
    
    global global_happiness , global_health , global_stamina , global_maxhealth , global_maxstamina , creategamename

    print("You arrive at the school gates. What do you do?")
    print("1. Go to the reception area and go where the Student Buddies are waiting to greet you.")
    print("2. Go to the reception area and ask an SLT member about the school.")
    print("3. Go to the reception area and ask a random teacher about the school.")
    print("4. Wander around")
    choicesg = input("Enter the number of your choice: ")
    if choicesg in ["1"]:
        print("You go to the reception area and go where the Student Buddies are waiting to greet you. They take you to the wembley steps and you see your form waiting for you")
        global_happiness += 2
        if global_happiness > 10:
            global_happiness = 10
            formspeech()
    elif choicesg in ["2"]:
        print("You go to the reception area and ask an SLT member about the school. They are a busy but they take you to the wembley steps and you see your form waiting for you")
        global_happiness += 2
        if global_happiness > 10:
            global_happiness = 10
            formspeech()
    elif choicesg in ["3"]:
        print("You go to the reception area and ask a random teacher about the school. They are a busy but they take you to the wembley steps and you see your form waiting for you")
        global_happiness += 2
        if global_happiness > 10:
            global_happiness = 10
            formspeech()
    elif choicesg in ["4"]:
        print("You wander around the school gates, then a teacher takes you to the wembley steps and you see your form waiting for you")
        global_happiness -= 1
        if global_happiness < 0:
            global_happiness = 0
            formspeech()



def day_morning_start():
    global global_happiness , global_health , global_stamina , global_maxhealth , global_maxstamina , creategamename

    print("You wake up in the morning, this is your first day at WFA as a Year 7 student! What do you do?")
    print("1. Get dressed in your WFA uniform and eat breakfast.")
    print("2. Stay in bed and skip breakfast.")
    print("3. Get dressed in your WFA uniform but skip breakfast.")
    choice = input("Enter the number of your choice: ")
    if choice == "1":
        print("You get dressed in your WFA uniform and eat breakfast. You feel energized and ready for the day!")
        global_health += 2
        global_stamina += 2
        if global_health > global_maxhealth:
            global_health = global_maxhealth
        if global_stamina > global_maxstamina:
            global_stamina = global_maxstamina
        schoolgates()
    elif choice == "2":
        print("You stay in bed and skip breakfast. You feel tired and sluggish.")
        global_health -= 2
        global_stamina -= 2
        if global_health < 0:
            global_health = 0
        if global_stamina < 0:
            global_stamina = 0
        print("You should probably get ready for school now, or else you might be late and the SLT will be mad at you.")
        schoolgates()
    elif choice == "3":
        print("You get dressed in your WFA uniform but skip breakfast. You feel tired and sluggish.")
        global_health -= 2
        global_stamina -= 2
        if global_health < 0:
            global_health = 0
        if global_stamina < 0:
            global_stamina = 0
        print("You should probably eat something before you go to school, or your performance in lessons might be affected.")
        schoolgates()

#---Main Game Loop-------------------------------------------------------

#--Area where the game starts, and the player can choose to start the game or exit the game.

menu_screen()