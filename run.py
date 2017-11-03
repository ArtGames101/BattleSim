# (c) ArtGames 2017

import config
from data import bots as api
from data import version as v
import sys
import os
import random
import time
import subprocess

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"

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
    # Main Menu
    clear_screen()
    print("|================|                                  {} {}\n"
          "|---Battle Sim---|                                  (c) 2017 ArtGames\n"
          "|================|                                  Logged in as:\n"
          "                                                    {}\n".format(v.ver, v.e, config.NAME))
    print("1. Battle")
    print("2. Multiplayer Battle")
    print("e. Extras")
    print("c. Changelog")
    print("?. Help")
    print("0. Exit\n")
    choice = user_choice()
    if choice == "1":
        gun()
    if choice == "2":
        tgun()
    if choice == "e":
        subprocess.call((sys.executable, "extras.py"))
    if choice == "c":
        changelog()
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

def changelog():
    clear_screen()
    print("|================|\n"
          "|---Battle Sim---|\n"
          "|   Changelog    |\n"
          "|================|\n")
    print("\n"
          "Whats New in Version {}?\n"
          "\n"
          "* Extras\n"
          "* More Secrets\n"
          "\n"
          "\n"
          "Whats Next?\n"
          "\n"
          "* Online Multiplayer?\n"
          "* Sounds?\n"
          "* Waiting to fill!\n"
          "* Money?\n"
          "* Shop?\n"
          "* Waiting to fill!\n".format(v.ver))
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


main()
