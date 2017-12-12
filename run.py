# (c) ArtGames 2017

errormsg = "==========\nError 404\n==========\nOops! Looks like one of our servers failed!\n\nPlease try again later!"
import sys
try:
    import config
    import sys
    import os
    import random
    import time
    import subprocess
    from data import version as v
except Exception as ImportError

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

def user_choice():
    return input("\n0> ").lower().strip()

# Shorts
orig = "Electric Warrior (Common)\nFire Warrior (Common)\nWater Warrior (Common)"
name = config.warriorname
wtype = config.warriortype
pet = config.pet
weapon = config.weapon
exittext = ["See you later {}!".format(name), "Goodbye SpaceCowboy", "{} : hi\nGame : hi\nGame : JINX!".format(name), "Hello... Goodbye!"]

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"

def loading():
    try:
        unwarfile = open("unwar.txt", "w")
        unwarfile.write("Electric Warrior (Common)\n")
        unwarfile.write("Fire Warrior (Common)\n")
        unwarfile.write("Water Warrior (Common)\n")
        unwarfile.close()
    except Exception as ImportError:
        input(errormsg)
        sys.exit()
    
    clear_screen()
    d = ["Did you know that the first version of battle sim was released in 2 days!", "This game has been fully tested!", "Did you know this game was made by ArtGames101?", "This Game is made with Love!", "Collect Special Characters for Halloween & Christmas!", "(c) ArtGames101", "Friend us on XBOX ONE (artucuno)", "Battle-Sim is made in Python!"]
    print("=============\n"
          " Loading...  \n"
          "=============\n"
          "10% \n{}".format(random.choice(d)))
    time.sleep(2)
    clear_screen()
    print("=============\n"
          " Loading.  \n"
          "=============\n"
          "20% \n{}".format(random.choice(d)))
    time.sleep(2)
    clear_screen()
    print("=============\n"
          " Loading..  \n"
          "=============\n"
          "40% \n{}".format(random.choice(d)))
    time.sleep(2)
    clear_screen()
    print("=============\n"
          " Loading...  \n"
          "=============\n"
          "50% \n{}".format(random.choice(d)))
    time.sleep(2)
    clear_screen()
    print("=============\n"
          " Loading.  \n"
          "=============\n"
          "70% \n{}".format(random.choice(d)))
    time.sleep(2)
    clear_screen()
    print("=============\n"
          " Loading..  \n"
          "=============\n"
          "100% \n{}".format(random.choice(d)))
    time.sleep(2)
    clear_screen()
    print("Have Fun!")
    time.sleep(2)
    main()


def main():
    clear_screen()
    print("+ + + + + + + +\n"
          "   Battle Sim  \n"
          "+ + + + + + + +\n")
    print("++++{}++++\n".format(v.ver))
    print("\n"
          "1. Start Your Adventure")
    print("2. Changelog")
    print("0. Exit")
    choice = user_choice()
    if choice == "1":
        begin()
    if choice == "2":
        changelog()
    if choice == "0":
        clear_screen()
        print(random.choice(exittext))
        sys.exit(1)
    else:
        main()

def changelog():
    clear_screen()
    print("-------------\n"
          "+ Changelog +\n"
          "-------------\n")
    print("Whats New in Version {}?\n"
          "\n"
          "\n"
          "* Added Heaps Of New Things!\n"
          "\n"
          "\n"
          "\n"
          "Whats Next?\n"
          "* Team Battles (v 0.1.6)".format(v.ver))
    input("\nPush Enter to go back!")
    main()

def begin():
    clear_screen()
    print("===============\n"
          "    Welcome    \n"
          "===============\n"
          "Hello {} Welcome to Battle-Sim! {}".format(name, v.ver))
    input("\nEnter")
    clear_screen()
    print("======================\n"
          "Your Stats for battle:\n"
          "======================\n"
          "NAME = {}\n"
          "Type = {}\n"
          "Pet = {}\n"
          "Weapon = {}\n"
          "======================\n".format(name, wtype, pet, weapon))
    print("You can check this anytime in menu by pushing s!")
    input("\nEnter")
    lobby()

def lobby():
    clear_screen()
    print("==============\n"
          "     Menu     \n"
          "==============\n")
    print("1. Battle CPU")
    print("3. Quests (1)")
    print("4. Collect Christmas Warrior!")
    print("5. Unlocked Characters")
    print("0. Back to Main menu")
    print("\n"
          "(c) ArtGames101 2017")
    choice = user_choice()
    if choice == "1":
        cpubattle()
    if choice == "2":
        input("Comming Soon!")
        lobby()
    if choice == "3":
        quests()
    if choice == "4":
        last = open("lastcol.txt", "r")
        lastw = open("lastcol.txt", "w")
        unwarfile = open("unwar.txt", "w")
        unwarfile.write("{} \nChristmas Warrior (Rare)\n".format(orig))
        lastw.write("Christmas Warrior\n")
        unwarfile.close()
        clear_screen()
        input("Collected Christmas Warrior!")
        lobby()
    if choice == "5":
        clear_screen()
        unwarfile = open("unwar.txt", "r")
        print("=================\n"
              "Unlocked Warriors\n"
              "=================\n")
        print(unwarfile.read())
        print("\n Enter any of these in config!")
        input("\nEnter")
        unwarfile.close()
        lobby()
    if choice == "0":
        main()
    if choice == "s":
        stats()

def stats():
    clear_screen()
    print("======================\n"
          "Your Stats for battle:\n"
          "======================\n"
          "NAME = {}\n"
          "Type = {}\n"
          "Pet = {}\n"
          "Weapon = {}\n"
          "======================\n".format(name, wtype, pet, weapon))
    input("\nEnter")
    lobby()

# Battles
def cpubattle():
    bname = ["(@MOD) ArtGames101", "(@MOD) Nik", "jeff", "bob", "Abigail", "Samantha", "Sam", "Alyssa", "Luke", "Zane", "Philip", "Ben", "Byron", "Slayer", "Nikolas", "Peter", "Summer"]
    btype = ["Rainbow"]
    bpet = ["Omega Dragon", "GiantLizard", "BigBadWolf", "Lizard", "Dragon", "Wolf"]
    bweapon = ["Birthday Sword", "Halloween Sword", "Christmas Sword", "Sword", "Gun", "Sniper", "Fists", "Nerf Gun"]
    battacks = ["Water Strike", "Water Fall", "Fire Storm", "Fire Wheel", "Static Attack", "Electric Cyclone"]
    clear_screen()
    print("======================\n"
          "Your Stats for battle:\n"
          "======================\n"
          "NAME = {}\n"
          "Type = {}\n"
          "Pet = {}\n"
          "Weapon = {}\n"
          "======================\n\n".format(name, wtype, pet, weapon))
    print("Bots Stats for battle:\n"
          "======================\n"
          "NAME = {}\n"
          "Type = {}\n"
          "Pet = {}\n"
          "Weapon = {}\n"
          "======================\n".format(random.choice(bname), random.choice(btype), random.choice(bpet), random.choice(bweapon)))
    input("\nReady to battle!")
    clear_screen()
    print("------\n"
          "     |\n"
          "     |\n"
          "-----|\n"
          "     |\n"
          "     |\n"
          "------\n")
    time.sleep(1)
    clear_screen()
    2
    print("------\n"
          "    /\n"
          "   / \n"
          "  /  \n"
          " /   \n"
          "/    \n"
          "------\n")
    time.sleep(1)
    clear_screen()
    print("------\n"
          "     |\n"
          "     |\n"
          "     |\n"
          "     |\n"
          "     |\n"
          "---------\n")
    time.sleep(1)
    clear_screen()
    print("|----  (-)   ___   |   |   |     |\n"
          "|           |  |   |   |   |     |\n"
          "|       |   |  |   |   |   |     |\n"
          "|----   |   |__|   |---|  ---    |\n"
          "|       |      |   |   |   |     |\n"
          "|       |      |   |   |   |     \n"
          "|       |   ---|   |   |   |    (-)\n")
    clear_screen()
    attacks = ["Heal", "Static Attack", "Electric Cyclone", "Thunder", "ThunderBolt", "Heal", "Fire Storm", "Fire Wheel", "Heal", "Water Strike", "Water Fall"]
    clear_screen()
    used = ["Bot used {}".format(random.choice(battacks)), "{} used {}".format(name, random.choice(attacks))]
    print("[10] {}".format(random.choice(used)))
    time.sleep(1)
    print("[9] {}".format(random.choice(used)))
    time.sleep(1)
    print("[8] {}".format(random.choice(used)))
    time.sleep(1)
    print("[7] {}".format(random.choice(used)))
    time.sleep(1)
    print("[6] {}".format(random.choice(used)))
    time.sleep(1)
    print("[5] {}".format(random.choice(used)))
    time.sleep(1)
    print("[4] {}".format(random.choice(used)))
    time.sleep(1)
    print("[3] {}".format(random.choice(used)))
    time.sleep(1)
    print("[2] {}".format(random.choice(used)))
    time.sleep(1)
    print("[1] {}".format(random.choice(used)))
    time.sleep(1)
    clear_screen()
    print("Ending Match in 3")
    time.sleep(1)
    clear_screen()
    print("Ending Match in 2")
    time.sleep(1)
    clear_screen()
    print("Ending Match in 1")
    won()

def won():
    won = ["=+++Bot Won!+++=", "=+++{} Won!+++=".format(name)]
    clear_screen()
    print("Calculating...")
    time.sleep(5)
    clear_screen()
    print(random.choice(won))
    input("Push Enter to go to lobby!")
    lobby()

def quests():
    clear_screen()
    print("============\n"
          "   Quests   \n"
          "============\n")
    print("\n"
          "1. Play a game of CPU Battle")
    print("\n0. Back\n"
          "More Soon!")
    choice = user_choice()
    if choice == "1":
        cpubattle()
    if choice == "0":
        lobby()
    else:
        quests()

loading()
