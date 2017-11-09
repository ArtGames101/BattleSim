# (c) ArtGames 2017

import config
from data import ads
from data import bots as api
from data import version as v
import sys
import os
import random
import time
import subprocess

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"

def loading():
    clear_screen()
    d = ["Did you know that the first version of battle sim was released in 2 days!", "This game has been fully tested!", "Did you know this game was made by ArtGames101?"]
    print("10% {}".format(random.choice(d)))
    time.sleep(2)
    clear_screen()
    print("30% {}".format(random.choice(d)))
    time.sleep(2)
    clear_screen()
    print("40% {}".format(random.choice(d)))
    time.sleep(2)
    clear_screen()
    print("50% {}".format(random.choice(d)))
    time.sleep(2)
    clear_screen()
    print("70% {}".format(random.choice(d)))
    time.sleep(2)
    clear_screen()
    print("100% {}".format(random.choice(d)))
    time.sleep(2)
    clear_screen()
    print("Have Fun!")
    time.sleep(2)

    main()

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

def user_choice():
    return input("\n>>> ").lower().strip()

def main():
    # Starting screen
    clear_screen()
    print("Welcome to battle sim {} {}!".format(v.ver, v.e))
    input("\nPush Enter to continue!")
    menu()

def menu():
    clear_screen()
    print("|================|                                  {} {}\n"
          "|---Battle Sim---|                                  (c) 2017 ArtGames\n"
          "|================|                                  Logged in as:\n"
          "                                                    {}\n".format(v.ver, v.e, config.NAME))
    print("1. Battle List\n")
    print("2. Fun\n")
    print("3. Help\n")
    print("0. Exit")
    choice = user_choice()
    if choice == "1":
        battlelist()
    if choice == "2":
        fun()
    if choice == "3":
        hlist()
    if choice == "0":
        clear_screen()
        print("Stopped all scripts!")
        sys.exit(1)

def battlelist():
    clear_screen()
    print("|================|                                  {} {}\n"
          "|---Battle Sim---|                                  (c) 2017 ArtGames\n"
          "|================|                                  Logged in as:\n"
          "                                                    {}\n".format(v.ver, v.e, config.NAME))
    print("1. Battle")
    print("2. Multiplayer Battle")
    print("0. Back")
    choice = user_choice()
    if choice == "1":
        if config.gunselection == True:
            gun()
        else:
            battle()
    if choice == "2":
        if config.tgunselection == True:
            tgun()
        else:
            tbattle()
    if choice == "0":
        menu()

def fun():
    clear_screen()
    print("|================|                                  {} {}\n"
          "|---Battle Sim---|                                  (c) 2017 ArtGames\n"
          "|================|                                  Logged in as:\n"
          "                                                    {}\n".format(v.ver, v.e, config.NAME))
    print("1. Extras")
    print("2. Input Code")
    print("0. Back")
    choice = user_choice()
    if choice == "1":
        if config.extras == True:
            subprocess.call((sys.executable, "extras.py"))
        else:
            input("Extras is Disabled!")
            menu()
    if choice == "2":
        code()
    if choice == "0":
        menu()

def hlist():
    clear_screen()
    print("|================|                                  {} {}\n"
          "|---Battle Sim---|                                  (c) 2017 ArtGames\n"
          "|================|                                  Logged in as:\n"
          "                                                    {}\n".format(v.ver, v.e, config.NAME))
    print("1. Tutorial")
    print("2. Changelog")
    print("3. Settings")
    print("4. Help")
    print("0. Back")
    choice = user_choice()
    if choice == "1":
        tutorial()
    if choice == "2":
        changelog()
    if choice == "3":
        settings()
    if choice == "4":
        halp()
    if choice == "0":
        menu()
def msenu():
    # Main Menu
    clear_screen()
    print("|================|                                  {} {}\n"
          "|---Battle Sim---|                                  (c) 2017 ArtGames\n"
          "|================|                                  Logged in as:\n"
          "                                                    {}\n".format(v.ver, v.e, config.NAME))
    print("1. Battle")
    print("2. Multiplayer Battle")
    print("t. Tutorial")
    if config.extras == True:
        print("e. Extras")
    else:
        print("\a")
    print("r. Input Code")
    print("c. Changelog")
    print("!. Settings")
    print("?. Help")
    print("0. Exit\n")
    if config.ads == True:
        print(random.choice(ads.a))
    else:
        print("\a")
    choice = user_choice()
    if choice == "1":
        if config.gunselection == True:
            gun()
        else:
            battle()
    if choice == "2":
        if config.tgunselection == True:
            tgun()
        else:
            tbattle()
    if choice == "t":
        tutorial()
    if choice == "e":
        if config.extras == True:
            subprocess.call((sys.executable, "extras.py"))
        else:
            input("Extras is Disabled!")
            menu()
    if choice == "c":
        changelog()
    if choice == "r":
        code()
    if choice == "!":
        settings()
    if choice == "?":
        halp()
    if choice == "l":
        # Dont Tell O.O
        print("You found the secret (o.o)")
        input("Dont tell anyone...")
        menu()
    if choice == "0":
        clear_screen()
        print("Stopped all scripts!")
        sys.exit(1)
    else:
        menu()

def settings():
    clear_screen()
    print("Change Your Settings in Config!")
    print("==============\n"
          "---Settings---\n"
          "==============\n")
    print("Name : {}\n".format(config.NAME))
    if config.gunselection == True:
        print("Gun Selection : True\n")
    else:
        print("Gun Selection : False\n")
    if config.tgunselection == True:
        print("Team Gun Selection : True\n")
    else:
        print("Team Gun Selection : False\n")
    if config.extras == True:
        print("Extras : True\n")
    else:
        print("Extras : False")
    if config.ads == True:
        print("Ads : True")
    else:
        print("Ads : False")
    input(".")
    menu()
def code():
    clear_screen()
    print("Input a Secret Code (type back to go back!)\n")
    choice = user_choice()
    if choice == "1christmasxyz":
        clear_screen()
        print("Merry Christmas!")
        input(".")
        menu()
    if choice == "7hallowee1n98":
        clear_screen()
        print("Happy Halloween!")
        input(".")
        menu()
    if choice == "back":
        menu()
def changelog():
    clear_screen()
    print("|================|\n"
          "|---Battle Sim---|\n"
          "|   Changelog    |\n"
          "|================|\n")
    print("\n"
          "Whats New in Version {}?\n"
          "\n"
          "* Loading Screen\n"
          "* \n"
          "\n"
          "\n"
          "Whats Next?\n"
          "\n"
          "* Online Multiplayer?\n"
          "* Sounds?\n"
          "* Waiting to Fill!\n"
          "* Money?\n"
          "* Shop?\n"
          "* Waiting to Fill!\n".format(v.ver))
    input("\nPush Enter to go to Menu!")
    menu()

def gun():
    clear_screen()
    print("Select a weapon!\n"
          "\n"
          "1 - Shotgun\n"
          "2 - Minigun\n"
          "3 - Sniper Rifle\n"
          "4 - Pistol\n"
          "5 - Nerf Gun\n")
    choice = user_choice()
    if choice == "1":
        print("Shotgun Selected!")
        time.sleep(2)
        battle()
    if choice == "2":
        print("Minigun Selected!")
        time.sleep(2)
        battle()
    if choice == "3":
        print("Sniper Rifle Selected!")
        time.sleep(2)
        battle()
    if choice == "4":
        print("Pistol Selected!")
        time.sleep(2)
        battle()
    if choice == "5":
        print("Nerf Gun Selected!")
        time.sleep(2)
        battle()
    else:
        print("Fists Selected XD")
        time.sleep(2)
        battle()

def tgun():
    clear_screen()
    print("Select a team weapon!\n"
          "\n"
          "1 - Shotgun\n"
          "2 - Minigun\n"
          "3 - Sniper Rifle\n"
          "4 - Pistol\n"
          "5 - Nerf Gun\n")
    choice = user_choice()
    if choice == "1":
        print("Shotgun Selected!")
        time.sleep(2)
        tbattle()
    if choice == "2":
        print("Minigun Selected!")
        time.sleep(2)
        tbattle()
    if choice == "3":
        print("Sniper Rifle Selected!")
        time.sleep(2)
        tbattle()
    if choice == "4":
        print("Pistol Selected!")
        time.sleep(2)
        tbattle()
    if choice == "5":
        print("Nerf Gun Selected!")
        time.sleep(2)
        tbattle()
    else:
        print("Fists Selected XD")
        time.sleep(2)
        tbattle()

def battle():
    bt = ["{} Got Wounded".format(config.NAME), "Bot was spotted!", "Bot Was Shot!", "Bot Got Wounded", "{} Was Shot".format(config.NAME)]
    wintitle = ["{} Won!".format(config.NAME), "Bot Won!"]
    clear_screen()
    print("-------------------------------\n"
          "{}      -VS-      {}\n"
          "-------------------------------\n".format(config.NAME, random.choice(api.bname)))
    input("\nPush Enter to Battle!!!\n")
    clear_screen()
    print("Battling...")
    time.sleep(2)
    print("[0.0.1] {}".format(random.choice(bt)))
    time.sleep(2)
    print("[0.0.2] {}".format(random.choice(bt)))
    time.sleep(2)
    print("[0.0.3] {}".format(random.choice(bt)))
    time.sleep(2)
    print("[0.0.4] {}".format(random.choice(bt)))
    time.sleep(2)
    print("Ending Match...")
    time.sleep(3)
    clear_screen()
    print(random.choice(wintitle))
    input("\nPush Enter to continue!")
    menu()

def tbattle():
    bt = ["{} Got Wounded".format(config.NAME), "Bot was spotted!", "Bot Was Shot!", "Bot Got Wounded", "{} Was Shot".format(config.NAME), "Friend was shot!", "Friend was wounded!", "Friend was spotted!"]
    wintitle = ["{} & Your Friend Won!".format(config.NAME), "Bot & Bot's Friend Won!"]
    clear_screen()
    print("--------------------------------------------------\n"
          "{} & {}     -VS-      {} & {}\n"
          "--------------------------------------------------\n".format(config.NAME, random.choice(api.bname), random.choice(api.bname), random.choice(api.bname)))
    input("\nPush Enter to Team Battle!!!\n")
    clear_screen()
    print("Battling...")
    time.sleep(2)
    print("[0.0.1] {}".format(random.choice(bt)))
    time.sleep(2)
    print("[0.0.2] {}".format(random.choice(bt)))
    time.sleep(2)
    print("[0.0.3] {}".format(random.choice(bt)))
    time.sleep(2)
    print("[0.0.4] {}".format(random.choice(bt)))
    time.sleep(2)
    print("[0.0.5] {}".format(random.choice(bt)))
    time.sleep(2)
    print("[0.0.6] {}".format(random.choice(bt)))
    time.sleep(2)
    print("[0.0.7] {}".format(random.choice(bt)))
    time.sleep(2)
    print("[0.0.8] {}".format(random.choice(bt)))
    time.sleep(2)
    print("Ending Match...")
    time.sleep(3)
    clear_screen()
    print(random.choice(wintitle))
    input("\nPush Enter to continue!")
    menu()

def halp():
    clear_screen()
    print("What do you need help with?:\n"
          "\n"
          "1* Errors\n"
          "2* Game stopped working\n"
          "3* Other\n"
          "0 Back\n")
    choice = user_choice()
    if choice == "1":
        clear_screen()
        input("Try Restarting the game or restarting your computer if this does\n"
              "not work uninstall then reinstall this game!\n")
        halp()
    if choice == "2":
        clear_screen()
        input("if the game had stopped working you wouldnt be reading this\n"
              "\n"
              "Try reinstalling this game!\n")
        halp()
    if choice == "3":
        clear_screen()
        input("Report the bug/error on github! (Remember this is {}!)".format(v.e))
        halp()
    if choice == "0":
        menu()
    else:
        halp()

def tutorial():
    clear_screen()
    print("Welcome To The Tutorial!\n"
          "\n"
          "Here you will learn how to play this game!\n"
          "Type a number to learn how to use it!\n")
    print("1. Battle Option")
    print("2. Extras")
    print("3. Settings")
    print("0. Back")
    choice = user_choice()
    if choice == "1":
        bt()
    if choice == "2":
        et()
    if choice == "3":
        st()
    if choice == "0":
        menu()

def bt():
    # Battle Tutorial
    clear_screen()
    print("Welcome to the Battle Tutorial")
    input("\nPush Enter to continue!")
    clear_screen()
    print("Today i will teach you how to battle!\n"
          "First off in the menu you need to push 1 then enter\n")
    input("\nPush Enter to continue!")
    clear_screen()
    print("After it will show a screen which will show you your name and\n"
          "Who you are battling\n")
    input("\nPush Enter to continue!")
    clear_screen()
    print("After you have seen that screen you need to push enter to start the battle!")
    input("\nPush Enter to continue!")
    clear_screen()
    print("Once the battle has finished you will be taken back to the menu!")
    input("\nPush Enter to continue!")
    clear_screen()
    print("Now its your turn to battle!\n")
    input("\nPush Enter to continue!")
    gun()

def et():
    clear_screen()
    print("Welcome to the Extras Tutorial!")
    input("\nPush Enter to continue!")
    clear_screen()
    print("In Extras its a bunch of random games\n"
          "Which you can play (There will be more soon!)")
    input("\nPush Enter to continue!")
    clear_screen()
    print("In The Menu there is a bunch of game options\n"
          "EG : if you pick 1 it will take you to a dice!")
    input("\nPush Enter to continue!")
    clear_screen()
    print("Now its your turn to play some games!")
    input("\nPush Enter to continue!")
    # If Extras is disabled it wont work
    subprocess.call((sys.executable, "extras.py"))

def st():
    clear_screen()
    print("Welcome to the settings tutorial!")
    input("\nPush Enter to continue!")
    clear_screen()
    print("Well for one settings choose how your game play works or reacts\n"
          "EG : From Settings we can tell that your name is {}!".format(config.NAME))
    input("\nPush Enter to continue!")
    clear_screen()
    print("To Choose this games settings go to config.py!")
    input("\nPush Enter to continue!")
    clear_screen()
    print("See your settings!")
    input("\nPush Enter to continue!")
    settings()

loading()
