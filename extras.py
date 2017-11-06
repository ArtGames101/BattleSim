import subprocess
import sys
import os
import time
import random
import config
from data import version as v
from data import bots as api
IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"
def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

def user_choice():
    return input("\n>>> ").lower().strip()

def menu():
    clear_screen()
    print("Loading...")
    time.sleep(2)
    clear_screen()
    print("=============\n"
          "Extras v{}\n"
          "=============\n".format(v.ever))
    print("1. Dice")
    print("2. Ring Toss")
    print("0. Back")
    choice = user_choice()
    if choice == "1":
        dice()
    if choice == "2":
        toss()
    if choice == "0":
        clear_screen()
        print("Loading...")
        time.sleep(2)
        subprocess.call((sys.executable, "run.py"))
    else:
        menu()

def dice():
    clear_screen()
    input("Push Enter to Roll the Dice!!!")
    n = ["1", "2", "3", "4", "5", "6"]
    print("Wow you got a {}!".format(random.choice(n)))
    input("\nPush Enter to go to Menu!")
    menu()

def toss():
    clear_screen()
    n = ["4", "3", "2", "1"]
    print("There are 4 bottles you need to toss rings over them to win!")
    input("\nPush Enter to continue!")
    print("Oh My Gawd you got {} rings on!".format(random.choice(n)))
    input("Press Enter to Go back to menu!")
    menu()

if config.extras == True:    
    menu()
else:
    clear_screen()
    print("Extras is Disabled!")
